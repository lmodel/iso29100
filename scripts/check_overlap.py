#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml"]
# ///
"""Check this repository's words against a licence holder's copy of the standard.

The schema, the docs and the knowledge bundle are this project's own words, and
NOTICE says so. This script tests that: it fails on any run of four or more
consecutive words shared with the standard. It also fails when the schema cites
a clause whose number starts no line of the standard.

Give it the standard as plain text, for example from ``pdftotext`` run on your
own licensed copy. Keep that file outside the repository: it must never be
committed or published. The script is not part of CI, since CI has no copy, and
ISO's licence bars giving the text to an AI tool, so a person runs it.

Usage::

    python scripts/check_overlap.py --source /path/outside/the/repository/iso29100.txt

A run may be listed in tests/overlap_allowed.yaml with the reason it is allowed.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SCHEMA = ROOT / "src" / "iso29100" / "schema" / "iso29100.yaml"
ALLOWED = ROOT / "tests" / "overlap_allowed.yaml"
RUN = 4
WORD = re.compile(r"[a-z0-9]+")

# What holds text a person reads, and what the schema's cross-references cite.
TEXT_KEYS = {"description", "title", "comments", "notes"}
NUMBER_KEYS = {"iso29100_clause"}

# The Markdown this project writes, and its NOTICE.
PROSE = (
    "README.md",
    "NOTICE",
    "docs/*.md",
    "src/iso29100/schema/*.md",
    ".lokf/knowledge/**/*.md",
)


def words(text: str) -> list[str]:
    """The text's words in lower case, with a dotted number such as 6.2 as one."""
    text = re.sub(r"(?<=\w)\.(?=\d)", "", text.lower())
    return WORD.findall(text.replace("’", "").replace("'", ""))


def source_words(text: str) -> list[str]:
    """The source's words, with a word that a line break split put back together."""
    return words(re.sub(r"(\w)-\s*\n\s*(\w)", r"\1\2", text))


def shingles(tokens: list[str], size: int = RUN) -> set[tuple[str, ...]]:
    """Every run of `size` consecutive words."""
    return {tuple(tokens[i : i + size]) for i in range(len(tokens) - size + 1)}


def schema_texts(node, path: str = "schema"):
    """Each string a person reads in the schema, with where it sits."""
    if isinstance(node, dict):
        for key, value in node.items():
            here = f"{path}/{key}"
            # A slot may be named description too; its entry is a mapping.
            if key in TEXT_KEYS and isinstance(value, str):
                yield here, value
            elif key in TEXT_KEYS and isinstance(value, list):
                for item in value:
                    yield here, str(item)
            else:
                yield from schema_texts(value, here)
    elif isinstance(node, list):
        for item in node:
            yield from schema_texts(item, path)


def schema_numbers(node):
    """Each clause number the schema cites."""
    if isinstance(node, dict):
        for key, value in node.items():
            if key in NUMBER_KEYS and isinstance(value, str):
                yield from value.split(", ")
            else:
                yield from schema_numbers(value)
    elif isinstance(node, list):
        for item in node:
            yield from schema_numbers(item)


def repository_texts(root: Path = ROOT):
    """Each (where, text) this repository writes in its own words."""
    schema = root / SCHEMA.relative_to(ROOT)
    yield from schema_texts(yaml.safe_load(schema.read_text(encoding="utf-8")))
    for pattern in PROSE:
        for path in sorted(root.glob(pattern)):
            yield str(path.relative_to(root)), path.read_text(encoding="utf-8")


def allowed_runs(path: Path = ALLOWED) -> dict[tuple[str, ...], str]:
    """Each allowed run, normalized as words() leaves it, with its reason. Every
    entry must give a reason."""
    entries = yaml.safe_load(path.read_text(encoding="utf-8")) or []
    allowed = {}
    for entry in entries:
        if not str(entry.get("reason", "")).strip():
            raise ValueError(f"{entry.get('run')!r} gives no reason")
        allowed[tuple(words(str(entry["run"])))] = entry["reason"]
    return allowed


def overlaps(text: str, theirs: set[tuple[str, ...]], allowed) -> list[str]:
    """Each maximal run of the text's words that the source also holds, with the
    allowed runs taken out first."""
    tokens = words(text)
    for phrase in allowed:
        size = len(phrase)
        for start in range(len(tokens) - size + 1):
            if tuple(tokens[start : start + size]) == phrase:
                tokens[start : start + size] = [""] * size
    found, start = [], None
    for i in range(len(tokens) - RUN + 2):
        hit = tuple(tokens[i : i + RUN]) in theirs
        if hit and start is None:
            start = i
        elif not hit and start is not None:
            found.append(" ".join(tokens[start : i + RUN - 1]))
            start = None
    return found


def missing_numbers(numbers, raw: str) -> list[str]:
    """Each cited number that starts no line of the source."""
    return [
        number
        for number in sorted(set(numbers))
        if not re.search(rf"^\s*{re.escape(number)}\s", raw, flags=re.M)
    ]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--source", type=Path, required=True, help="The standard as plain text"
    )
    args = parser.parse_args(argv)
    if ROOT in args.source.resolve().parents:
        print(f"{args.source} sits inside the repository. Move it out.")
        return 2
    raw = args.source.read_text(encoding="utf-8", errors="replace")
    theirs = shingles(source_words(raw))
    allowed = allowed_runs()

    problems = []
    for where, text in repository_texts():
        problems += [f"{where}: {run}" for run in overlaps(text, theirs, allowed)]
    schema = yaml.safe_load(SCHEMA.read_text(encoding="utf-8"))
    problems += [
        f"schema cites {number}, which starts no line of the source"
        for number in missing_numbers(schema_numbers(schema), raw)
    ]

    print("\n".join(problems) if problems else "OK: nothing shared, every number found")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
