"""Data test."""

import glob
import os
from pathlib import Path

import pytest
import yaml
from linkml.validator import validate
from linkml_runtime.loaders import yaml_loader
from linkml_runtime.utils.schemaview import SchemaView

import iso29100.datamodel.iso29100

DATA_DIR = Path(__file__).parent / "data"
DATA_DIR_VALID = DATA_DIR / "valid"
DATA_DIR_INVALID = DATA_DIR / "invalid"

VALID_EXAMPLE_FILES = sorted(glob.glob(os.path.join(DATA_DIR_VALID, "*.yaml")))
INVALID_EXAMPLE_FILES = sorted(glob.glob(os.path.join(DATA_DIR_INVALID, "*.yaml")))

SCHEMA = Path(__file__).parent.parent / "src" / "iso29100" / "schema" / "iso29100.yaml"


def _class_of(filepath):
    return Path(filepath).stem.split("-")[0]


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
def test_valid_data_files(filepath):
    """Each valid example loads into the generated dataclass of its class."""
    tgt_class = getattr(iso29100.datamodel.iso29100, _class_of(filepath))
    obj = yaml_loader.load(filepath, target_class=tgt_class)
    assert obj


# The JSON Schema the validator generates is the one check that applies every
# constraint (docs/index.md says what the generated models leave out), so each
# example is held to it: a valid one must pass, and a counter-example must fail.
# The examples quote their dates, as JSON carries them, because the validator
# reads a date as text.
@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
def test_valid_data_files_validate(filepath):
    """Every valid example passes the validator."""
    report = validate(
        yaml.safe_load(Path(filepath).read_text(encoding="utf-8")),
        str(SCHEMA),
        _class_of(filepath),
    )
    assert not report.results, [r.message for r in report.results]


@pytest.mark.parametrize("filepath", INVALID_EXAMPLE_FILES)
def test_invalid_data_files_fail(filepath):
    """Every counter-example fails the validator at the place its first line
    names, as `# Fails at: <JSON pointer>`, so a file that starts failing for
    another reason fails this test."""
    text = Path(filepath).read_text(encoding="utf-8")
    first = text.splitlines()[0]
    assert first.startswith("# Fails at: "), (
        f"{filepath}: the first line names where it fails, as # Fails at: /key"
    )
    pointer = first.removeprefix("# Fails at: ").strip()
    report = validate(yaml.safe_load(text), str(SCHEMA), _class_of(filepath))
    messages = [r.message for r in report.results]
    assert any(m.endswith(f" in {pointer}") for m in messages), messages


def test_every_class_has_an_example():
    """Each class that data can be written in has a valid example: every class
    but the mixins and the abstract ones."""
    classes = {
        name
        for name, cls in yaml.safe_load(SCHEMA.read_text())["classes"].items()
        if not cls.get("abstract") and not cls.get("mixin")
    }
    examples = {_class_of(f) for f in VALID_EXAMPLE_FILES}
    assert classes <= examples, sorted(classes - examples)


# The rules the validator cannot check, held over the examples. docs/index.md
# lists them.
VIEW = SchemaView(str(SCHEMA))
CLASSES = set(VIEW.all_classes())
DESIGNATORS = {
    name: slot.name
    for name in CLASSES
    for slot in VIEW.class_induced_slots(name)
    if slot.designates_type
}
RISK_LEVELS = list(VIEW.get_enum("PfRiskLevel").permissible_values)
FRAMEWORKS = [f for f in VALID_EXAMPLE_FILES if _class_of(f) == "PfFramework"]


def _records(node, cls, found):
    """Collect every record a document holds, as (class, data), with each inlined
    record under the class its slot ranges over, or the class its designator
    names."""
    if isinstance(node, list):
        for item in node:
            _records(item, cls, found)
        return
    if not isinstance(node, dict):
        return
    cls = node.get(DESIGNATORS.get(cls, ""), cls)
    found.append((cls, node))
    slots = {s.name: s for s in VIEW.class_induced_slots(cls)}
    for key, value in node.items():
        slot = slots.get(key)
        if slot and slot.range in CLASSES and (slot.inlined or slot.inlined_as_list):
            _records(value, slot.range, found)


def _all_records(filepath):
    found = []
    _records(
        yaml.safe_load(Path(filepath).read_text(encoding="utf-8")),
        _class_of(filepath),
        found,
    )
    return found


def _broken_references(records):
    """Each reference that names no record, or a record of the wrong class."""
    classes = {data["pf_id"]: cls for cls, data in records if "pf_id" in data}
    broken = []
    for cls, data in records:
        for slot in VIEW.class_induced_slots(cls):
            if slot.range not in CLASSES or slot.inlined or slot.inlined_as_list:
                continue
            value = data.get(slot.name)
            targets = value if isinstance(value, list) else [value]
            for target in (t for t in targets if t is not None):
                if target not in classes or slot.range not in VIEW.class_ancestors(
                    classes[target]
                ):
                    broken.append((slot.name, target))
    return broken


@pytest.mark.parametrize("filepath", FRAMEWORKS)
def test_a_framework_names_each_record_once_and_resolves_its_references(filepath):
    """Within a whole framework, no two records share a pf_id, and each reference
    names a record the framework holds, of the class it ranges over."""
    records = _all_records(filepath)
    ids = [data["pf_id"] for _, data in records if "pf_id" in data]
    assert not sorted({i for i in ids if ids.count(i) > 1})
    assert not _broken_references(records)


def _broken_rules(records):
    """Each rule no validator checks that a list of records breaks, as a sentence."""
    classes = {data["pf_id"]: cls for cls, data in records if "pf_id" in data}
    broken = []
    for _, data in records:
        name = data.get("pf_id")
        if data.get("pf_provider") and data.get("pf_provider") == data.get(
            "pf_recipient"
        ):
            broken.append(f"{name}: a flow goes from one actor to another")
        if classes.get(data.get("pf_decides_afterwards")) == "PfPiiProcessor":
            broken.append(f"{name}: a processor never decides what happens to PII")
        before, after = (
            data.get("pf_risk_inherent_level"),
            data.get("pf_risk_residual_level"),
        )
        if before and after and RISK_LEVELS.index(after) > RISK_LEVELS.index(before):
            broken.append(f"{name}: controls never raise a risk's level")
        found = set(data.get("pf_risks_found") or [])
        for key in ("pf_risks_treated", "pf_risks_accepted"):
            if set(data.get(key) or []) - found:
                broken.append(f"{name}: {key} names a risk the assessment did not find")
        for earlier, later in (
            ("pf_assessment_date", "pf_next_assessment"),
            ("pf_breach_occurred", "pf_breach_discovered"),
            ("pf_breach_discovered", "pf_breach_closed"),
            ("pf_consent_given", "pf_consent_withdrawn"),
        ):
            first, second = data.get(earlier), data.get(later)
            if first and second and str(second) < str(first):
                broken.append(f"{name}: {later} comes before {earlier}")
        if data.get("pf_transfer_safeguards") and not data.get("pf_crosses_borders"):
            broken.append(f"{name}: transfer safeguards need a border crossed")
    return broken


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
def test_examples_keep_the_rules_no_validator_checks(filepath):
    """Every valid example keeps the rules the validator cannot state."""
    assert not _broken_rules(_all_records(filepath))


@pytest.mark.parametrize(
    "records, fragment",
    [
        (
            [("PfPiiFlow", {"pf_provider": "a:x", "pf_recipient": "a:x"})],
            "from one actor to another",
        ),
        (
            [
                ("PfPiiProcessor", {"pf_id": "a:p"}),
                ("PfPiiFlow", {"pf_decides_afterwards": "a:p"}),
            ],
            "a processor never decides",
        ),
        (
            [
                (
                    "PfRisk",
                    {"pf_risk_inherent_level": "low", "pf_risk_residual_level": "high"},
                )
            ],
            "never raise",
        ),
        (
            [
                (
                    "PfImpactAssessment",
                    {"pf_risks_found": ["a:r"], "pf_risks_treated": ["a:s"]},
                )
            ],
            "did not find",
        ),
        (
            [
                (
                    "PfImpactAssessment",
                    {"pf_risks_found": ["a:r"], "pf_risks_accepted": ["a:s"]},
                )
            ],
            "did not find",
        ),
        (
            [
                (
                    "PfImpactAssessment",
                    {
                        "pf_assessment_date": "2026-03-02",
                        "pf_next_assessment": "2025-03-02",
                    },
                )
            ],
            "pf_next_assessment comes before",
        ),
        (
            [
                (
                    "PfBreach",
                    {
                        "pf_breach_occurred": "2026-04-02T00:00:00Z",
                        "pf_breach_discovered": "2026-04-01T00:00:00Z",
                    },
                )
            ],
            "pf_breach_discovered comes before",
        ),
        (
            [
                (
                    "PfBreach",
                    {
                        "pf_breach_discovered": "2026-04-02T00:00:00Z",
                        "pf_breach_closed": "2026-04-01T00:00:00Z",
                    },
                )
            ],
            "pf_breach_closed comes before",
        ),
        (
            [
                (
                    "PfConsent",
                    {
                        "pf_consent_given": "2026-04-02T00:00:00Z",
                        "pf_consent_withdrawn": "2026-04-01T00:00:00Z",
                    },
                )
            ],
            "pf_consent_withdrawn comes before",
        ),
        (
            [
                (
                    "PfProcessingActivity",
                    {
                        "pf_transfer_safeguards": ["Clauses"],
                        "pf_crosses_borders": False,
                    },
                )
            ],
            "need a border crossed",
        ),
    ],
)
def test_a_broken_rule_is_named(records, fragment):
    """Each rule is caught when it is broken, so an example cannot pass it by
    accident."""
    assert any(fragment in sentence for sentence in _broken_rules(records))


def test_a_broken_reference_is_named():
    """A reference to no record, and one to a record of the wrong class, are both
    caught."""
    actor = ("PfPiiController", {"pf_id": "a:c"})
    flow = {"pf_id": "a:f", "pf_provider": "a:c", "pf_recipient": "a:nobody"}
    assert _broken_references([actor, ("PfPiiFlow", flow)]) == [
        ("pf_recipient", "a:nobody")
    ]
    principal_ref = {"pf_id": "a:k", "pf_principal": "a:c"}
    assert _broken_references([actor, ("PfConsent", principal_ref)]) == [
        ("pf_principal", "a:c")
    ]
