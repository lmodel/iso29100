"""Checks the script that tests the repository's words against a copy of the
standard. The copy itself stays outside the repository, so these tests give the
script text of their own."""

import importlib.util
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).parent.parent


@pytest.fixture(scope="module")
def overlap():
    spec = importlib.util.spec_from_file_location(
        "check_overlap", ROOT / "scripts" / "check_overlap.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _theirs(overlap, source):
    return overlap.shingles(overlap.source_words(source))


def test_a_shared_run_of_four_words_is_found(overlap):
    """Four words in a row are found, whatever their case and punctuation, and
    the whole shared run is reported once."""
    theirs = _theirs(overlap, "The quick brown fox, jumps over the lazy dog.")
    found = overlap.overlaps("a QUICK brown FOX jumps over it", theirs, {})
    assert found == ["quick brown fox jumps over"]


def test_three_shared_words_are_not_a_run(overlap):
    """Three words in a row pass."""
    theirs = _theirs(overlap, "The quick brown fox jumps.")
    assert not overlap.overlaps("a quick brown cat", theirs, {})


def test_an_allowed_run_passes(overlap):
    """A run on the allow-list is not reported, however it is cased."""
    theirs = _theirs(overlap, "The quick brown fox jumps.")
    allowed = {("quick", "brown", "fox", "jumps"): "A test."}
    assert not overlap.overlaps("Quick brown fox jumps.", theirs, allowed)


def test_every_allowed_run_gives_a_reason(overlap):
    """The committed allow-list loads, and every entry says why."""
    allowed = overlap.allowed_runs()
    assert allowed
    assert all(allowed.values())
    assert ("personally", "identifiable", "information", "pii") in allowed


def test_an_entry_without_a_reason_is_refused(overlap, tmp_path):
    """An allow-list entry must say why."""
    path = tmp_path / "allowed.yaml"
    path.write_text("- run: a b c d\n  reason: ''\n", encoding="utf-8")
    with pytest.raises(ValueError, match="gives no reason"):
        overlap.allowed_runs(path)


def test_a_dotted_number_is_one_word(overlap):
    """A clause number stays one word, and a word a line break split in the source
    is joined again."""
    assert overlap.words("Subclause 6.12 and clause 5.2") == [
        "subclause",
        "612",
        "and",
        "clause",
        "52",
    ]
    assert overlap.source_words("manage-\nment system") == ["management", "system"]


def test_the_script_reads_the_schema_text_and_the_prose(overlap):
    """Its texts cover a class description, a value's title, and the README."""
    places = {where for where, _ in overlap.repository_texts()}
    assert "schema/classes/PfPolicy/description" in places
    assert "schema/enums/PfPrinciple/permissible_values/principle_6_2/title" in places
    assert "README.md" in places
    assert "NOTICE" in places


def test_every_cited_number_is_checked(overlap):
    """The schema's numbers come from every annotation that cites the standard."""
    schema = yaml.safe_load(overlap.SCHEMA.read_text(encoding="utf-8"))
    numbers = set(overlap.schema_numbers(schema))
    assert {"5.2", "5.7", "6.1", "6.2", "6.12"} <= numbers
    assert all(" " not in number for number in numbers)


def _source_with_every_number(overlap):
    schema = yaml.safe_load(overlap.SCHEMA.read_text(encoding="utf-8"))
    numbers = sorted(set(overlap.schema_numbers(schema)))
    return numbers, "\n".join(f"{number} zzz yyy" for number in numbers) + "\n"


def test_a_cited_number_missing_from_the_source_is_reported(overlap):
    """A number the source starts no line with is named."""
    numbers, text = _source_with_every_number(overlap)
    text = text.replace("6.2 zzz yyy\n", "")
    assert overlap.missing_numbers(numbers, text) == ["6.2"]


def test_a_copy_inside_the_repository_is_refused(overlap, capsys):
    """The copy of the standard must stay outside the repository."""
    inside = ROOT / "tests" / "data" / "README.md"
    assert overlap.main(["--source", str(inside)]) == 2
    assert "inside the repository" in capsys.readouterr().out


def test_a_clean_run_exits_zero(overlap, tmp_path, capsys):
    """A source that shares no run and starts a line with every cited number
    passes."""
    _numbers, text = _source_with_every_number(overlap)
    source = tmp_path / "source.txt"
    source.write_text(text, encoding="utf-8")
    assert overlap.main(["--source", str(source)]) == 0
    assert "OK" in capsys.readouterr().out


def test_a_shared_run_fails_the_run(overlap, tmp_path, capsys):
    """A source that holds four words of a description fails, naming the place."""
    _numbers, text = _source_with_every_number(overlap)
    schema = yaml.safe_load(overlap.SCHEMA.read_text(encoding="utf-8"))
    description = schema["classes"]["PfPolicy"]["description"]
    source = tmp_path / "source.txt"
    source.write_text(text + description, encoding="utf-8")
    assert overlap.main(["--source", str(source)]) == 1
    assert "schema/classes/PfPolicy/description:" in capsys.readouterr().out
