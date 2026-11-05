"""Checks that the schema models the edition ISO's records name, and maps to DPV
as DPV's own file does.

ISO's licence bars giving the text of ISO/IEC 29100 to an AI tool, so
src/iso29100/schema/iso-open-data/ holds ISO Open Data's records of the edition and
of the two it replaced instead, which scripts/check_upstream_release.py pins and
watches. These tests read that extract with the standard library, and hold the
schema header to it and to the watch's pins. They also hold the principles and the
clause citations to their numbering, and every mapping to the pinned copy of DPV's
mapping file.
"""

import importlib.util
import json
import re
from functools import cache
from pathlib import Path

import yaml
from rdflib import Graph, Namespace

ROOT = Path(__file__).parent.parent
SCHEMA = ROOT / "src" / "iso29100" / "schema" / "iso29100.yaml"
EXTRACT = (
    ROOT
    / "src"
    / "iso29100"
    / "schema"
    / "iso-open-data"
    / "iso_deliverables_metadata.jsonl"
)
DPV_MAPPING = ROOT / "upstream" / "dpv-iso.ttl"
DPV_ISO = Namespace("https://w3id.org/dpv/mappings/iso#")
SKOS = "http://www.w3.org/2004/02/skos/core#"

# The stage code ISO gives an edition or a supplement that a later one replaced.
WITHDRAWN = 9599

# The subclause numbers OneClickComply's public outline gives for this edition,
# read on 2026-11-05 at https://oneclickcomply.com/standards/iso-29100-2024/. Only an
# outline this repository can read names them, so a citation stays inside this list.
# Its wording is that site's and is not carried here. A licence holder compares the
# numbers with a copy through scripts/check_overlap.py.
OUTLINE = [f"5.{n}" for n in range(1, 8)] + [f"6.{n}" for n in range(1, 13)]
PRINCIPLES = [f"6.{n}" for n in range(2, 13)]

# Each row of DPV's file, as the concept it names, the predicate it states, the term
# it names, and the class that models the concept with the mapping key that says so.
DPV_ROWS = {
    ("PII", "narrower", "PersonalData"): ("PfPiiItem", "narrow_mappings"),
    ("PIIController", "exactMatch", "DataController"): (
        "PfPiiController",
        "exact_mappings",
    ),
    ("PIIPrincipal", "exactMatch", "DataSubject"): (
        "PfPiiPrincipal",
        "exact_mappings",
    ),
    ("PIIProcessor", "exactMatch", "DataProcessor"): (
        "PfPiiProcessor",
        "exact_mappings",
    ),
    ("Consent", "exactMatch", "InformedConsent"): ("PfConsent", "exact_mappings"),
}
MAPPING_KEYS = (
    "mappings",
    "exact_mappings",
    "close_mappings",
    "related_mappings",
    "narrow_mappings",
    "broad_mappings",
)


@cache
def _watch():
    """The upstream watch script, loaded once as a module."""
    spec = importlib.util.spec_from_file_location(
        "watch", ROOT / "scripts" / "check_upstream_release.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@cache
def _schema():
    return yaml.safe_load(SCHEMA.read_text(encoding="utf-8"))


def _records():
    lines = EXTRACT.read_text(encoding="utf-8").splitlines()
    return {r["id"]: r for r in map(json.loads, lines)}


def _annotated(node, key):
    """Every value of an annotation anywhere in the schema."""
    if isinstance(node, dict):
        for name, value in node.items():
            if name == "annotations" and isinstance(value, dict) and key in value:
                yield from str(value[key]).split(", ")
            yield from _annotated(value, key)
    elif isinstance(node, list):
        for item in node:
            yield from _annotated(item, key)


def _schema_mappings(schema):
    """Each mapping a class of the schema declares, as (class, key, target)."""
    for name, cls in schema["classes"].items():
        for key in MAPPING_KEYS:
            for target in cls.get(key) or []:
                yield name, key, target


def _dpv_rows():
    """Each statement in DPV's file between one of its concepts and a DPV term."""
    graph = Graph().parse(DPV_MAPPING, format="turtle")
    rows = set()
    for subject, predicate, value in graph:
        if str(predicate).startswith(SKOS) and str(value).startswith(
            "https://w3id.org/dpv#"
        ):
            rows.add(
                (
                    str(subject).removeprefix(str(DPV_ISO)),
                    str(predicate).removeprefix(SKOS),
                    str(value).removeprefix("https://w3id.org/dpv#"),
                )
            )
    return rows


def test_extract_matches_the_pinned_lines():
    """Each line of the extract hashes to the watch's pin, and the extract holds
    no scope, the field that summarizes the standard in ISO's words."""
    watch = _watch()
    lines = EXTRACT.read_text(encoding="utf-8").splitlines()
    hashes = {json.loads(line)["id"]: watch.digest(line) for line in lines}
    assert hashes == watch.PINNED_RECORDS
    for record in _records().values():
        assert not set(watch.LEFT_OUT) & record.keys(), record["id"]
        assert watch.line_of(record) in lines


def test_header_pins_match_the_watch():
    """The header's version, source and dates are the ones the watch pins and the
    extract records."""
    watch = _watch()
    header = _schema()
    notes = header["annotations"]
    edition = _records()[watch.EDITION_ID]
    assert header["version"] == watch.PINNED_VERSION
    assert header["source"] == watch.PINNED_SOURCE
    assert header["source"].endswith(f"/{watch.EDITION_ID}.html")
    assert notes["standard"] == edition["reference"] == watch.PINNED_EDITION
    assert notes["edition"] == str(edition["edition"])
    assert notes["publication_date"] == edition["publicationDate"]
    assert notes["iso_open_data_date"] == watch.PINNED_DATE


def test_the_edition_is_published_and_replaced_the_two_before_it():
    """ISO's records say the edition is in force and that it replaced the first
    edition and its amendment, as the header says."""
    watch = _watch()
    records = _records()
    edition = records.pop(watch.EDITION_ID)
    assert edition["currentStage"] == watch.PUBLISHED
    assert not edition["replacedBy"]
    assert set(edition["replaces"]) == set(records)
    assert _schema()["annotations"]["replaces"] == ", ".join(
        record["reference"] for record in records.values()
    )
    for record in records.values():
        assert record["currentStage"] == WITHDRAWN, record["reference"]
        assert record["replacedBy"] == [watch.EDITION_ID], record["reference"]


def test_header_does_not_describe_a_supplement():
    """The edition has no supplement yet, so the version is the year alone."""
    watch = _watch()
    assert not [
        r
        for r in _records().values()
        if r["reference"].startswith(f"{watch.PINNED_EDITION}/")
    ]


def test_the_principles_are_numbered_6_2_to_6_12():
    """The enum holds eleven principles by number, in order. Each title starts with
    its number and goes on to a name of this project's own, and each value cites the
    same number."""
    enum = _schema()["enums"]["PfPrinciple"]["permissible_values"]
    assert list(enum) == ["principle_" + n.replace(".", "_") for n in PRINCIPLES]
    for number, value in zip(PRINCIPLES, enum.values()):
        assert re.fullmatch(rf"{re.escape(number)} \S.*", value["title"]), number
        assert value["annotations"]["iso29100_clause"] == number
        assert value["description"].strip(), number


def test_each_citation_is_a_number_the_outline_gives():
    """A clause annotation names a subclause of the outline. A term's number or a
    lower subclause's is not there, so neither is cited."""
    cited = set(_annotated(_schema(), "iso29100_clause"))
    assert cited
    assert cited <= set(OUTLINE), sorted(cited - set(OUTLINE))


def test_the_clause_annotation_is_the_one_citation_key():
    """The script a licence holder runs checks this key, so no number hides under
    another one."""
    overlap = importlib.util.spec_from_file_location(
        "check_overlap", ROOT / "scripts" / "check_overlap.py"
    )
    module = importlib.util.module_from_spec(overlap)
    overlap.loader.exec_module(module)
    assert module.NUMBER_KEYS == {"iso29100_clause"}


def test_the_copy_of_dpvs_file_is_the_one_pinned():
    """The copy of DPV's mapping and of its licence hash to the watch's pins."""
    watch = _watch()
    assert watch.git_blob(DPV_MAPPING.read_bytes()) == watch.DPV_MAPPING_BLOB
    assert watch.git_blob(watch.DPV_LICENCE_COPY.read_bytes()) == watch.DPV_LICENCE_BLOB


def test_the_rows_are_dpvs_with_the_direction_its_turtle_states():
    """The table above is DPV's file, row for row. skos:narrower on PII says that
    dpv:PersonalData is the narrower of the two, so the class maps by narrow_mappings."""
    assert _dpv_rows() == set(DPV_ROWS)


def test_every_mapping_of_the_schema_is_a_row_of_dpvs_file():
    """Each class declares the mapping its row says and nothing else, so no guessed
    mapping can sit beside them, and no value or slot holds one."""
    expected = {
        (cls, key, f"dpv:{term}") for (_, _, term), (cls, key) in DPV_ROWS.items()
    }
    schema = _schema()
    assert set(_schema_mappings(schema)) == expected
    for section in ("slots", "enums"):
        text = yaml.safe_dump(schema[section])
        assert "mappings:" not in text
        assert "meaning:" not in text, section
    assert schema["prefixes"]["dpv"] == "https://w3id.org/dpv#"
