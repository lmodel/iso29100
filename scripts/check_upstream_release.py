#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Check ISO's records of ISO/IEC 29100:2024 against ISO Open Data, and DPV's
mapping to the standard against DPV's repository.

ISO's licence bars giving the text of ISO/IEC 29100 to an AI tool, so this
repository pins what ISO publishes openly about it instead. Those are its records
in ISO Open Data's ``iso_deliverables_metadata`` dataset, which ISO updates daily
under the ODC Attribution License (ODC-By) v1.0. Three records matter here:

- ISO/IEC 29100:2024, the edition the schema models;
- ISO/IEC 29100:2011 and ISO/IEC 29100:2011/Amd 1:2018, the two it replaced.

``src/iso29100/schema/iso-open-data/iso_deliverables_metadata.jsonl`` holds
those records as ISO published them on the pinned date, each without its
``scope`` field: a scope is a summary of the standard in ISO's words, which this
repository does not reproduce. Each record is pinned below by the SHA-256 hash
of its line.

``upstream/dpv-iso.ttl`` is the Data Privacy Vocabulary's (DPV) own mapping to the
standard, copied at DPV's tag ``dpv-2.3`` and pinned below by its git object hash.
The schema's mappings to DPV come from it.

The script reports:

- a change to a pinned record, such as a stage or a publication date;
- a supplement of either standard that is not pinned;
- a record that replaces a pinned one, such as a new edition;
- a pinned record leaving the dataset, or ISO changing the dataset's licence;
- an extract that drifts from what was pinned;
- a change to DPV's mapping file, or a copy that differs from the pin.

The dataset is about 80 MB. The script streams it line by line and parses only
the lines that name a pinned record or edition. It reads the dataset's licence
from ISO's open data page, through the Internet Archive's latest capture when
iso.org refuses a script, as it usually does. It follows a redirect only over
https to a host below, sends no token, and prints a Markdown report. It exits 1
when any of the above is found or a check could not finish.

Usage::

    python scripts/check_upstream_release.py [--report FILE]
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import html
import http.client
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXTRACT = (
    ROOT
    / "src"
    / "iso29100"
    / "schema"
    / "iso-open-data"
    / "iso_deliverables_metadata.jsonl"
)
USER_AGENT = "lmodel-iso29100-upstream-check"

DATASET = (
    "https://isopublicstorageprod.blob.core.windows.net/opendata/_latest/"
    "iso_deliverables_metadata/json/iso_deliverables_metadata.jsonl"
)
LICENCE_PAGE = "https://www.iso.org/open-data.html"
# The Internet Archive's latest capture of the page, as it was served.
LICENCE_MIRROR = f"https://web.archive.org/web/3000id_/{LICENCE_PAGE}"

# The date the extract was taken from the dataset.
PINNED_DATE = "2026-11-05"

# The edition the schema models. The schema header's `version` and `source`
# carry the same values, and tests/test_upstream.py holds them equal.
PINNED_EDITION = "ISO/IEC 29100:2024"
PINNED_VERSION = "2024"
PINNED_SOURCE = "https://www.iso.org/standard/85938.html"
EDITION_ID = 85938

# Each extract line, by ISO's record id, and the SHA-256 hash of the line.
PINNED_RECORDS = {
    45123: "acb58e6b81aa48be652b487d76a437c25c2e9ce7368fd40a5cfb8361ea2c0d92",
    73722: "56db898fde23fe09a1fe26de44503ca0f641dd36774d1a52e49fd39fdfe357f2",
    85938: "26a604221ae2b41be123d376a730eec9d296432687a28921b3cc44106e151082",
}

# A record whose reference starts so is a supplement of the edition.
SUPPLEMENT_PREFIXES = (f"{PINNED_EDITION}/",)

# The field of a record that the extract leaves out, as the docstring says.
LEFT_OUT = ("scope",)

# What ISO's open data page names as the dataset's licence.
PINNED_LICENCE = "ODC Attribution License (ODC-By) v1.0"
PINNED_LICENCE_URL = "https://opendatacommons.org/licenses/by/1-0/"

# The stage code of a published standard. Any other is reported.
PUBLISHED = 6060

# DPV's mapping to the standard, the tag it was copied at, its git object hash,
# and where DPV keeps the current file.
DPV_COPY = ROOT / "upstream" / "dpv-iso.ttl"
DPV_LICENCE_COPY = ROOT / "upstream" / "DPV-LICENSE.md"
DPV_TAG = "dpv-2.3"
DPV_MAPPING_BLOB = "84ba5815880d6f431220175563b6113ddfa97c01"
DPV_LICENCE_BLOB = "58ec5edeb28e92f73397833a93d8218562046dde"
DPV_MAPPING_URL = (
    "https://raw.githubusercontent.com/w3c-cg/dpv/master/mappings/iso/dpv-iso.ttl"
)


# The hosts the script may reach, and the most it reads from each answer.
ALLOWED_HOSTS = {
    "isopublicstorageprod.blob.core.windows.net",
    "raw.githubusercontent.com",
    "web.archive.org",
    "www.iso.org",
}
MAX_DATASET_BYTES = 300 * 1024 * 1024
MAX_PAGE_BYTES = 20 * 1024 * 1024


class _HttpsOnly(urllib.request.HTTPRedirectHandler):
    """Follow a redirect only over https, and only to a host the script reads from."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        parts = urllib.parse.urlsplit(newurl)
        if parts.scheme != "https" or parts.hostname not in ALLOWED_HOSTS:
            raise urllib.error.URLError(f"refused a redirect to {newurl}")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def _open(url: str):
    """A public address, held to the same rule as a redirect. It carries no token."""
    parts = urllib.parse.urlsplit(url)
    if parts.scheme != "https" or parts.hostname not in ALLOWED_HOSTS:
        raise urllib.error.URLError(f"refused to read {url}")
    opener = urllib.request.build_opener(_HttpsOnly)
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    return opener.open(req, timeout=120)


def _get(url: str) -> tuple[str, bytes]:
    """The address a request ended at and the body, gunzipped if need be."""
    with _open(url) as resp:
        body = resp.read(MAX_PAGE_BYTES + 1)
        final = resp.geturl()
    if len(body) > MAX_PAGE_BYTES:
        raise ValueError(f"{url} answered with more than {MAX_PAGE_BYTES} bytes")
    if body[:2] == b"\x1f\x8b":
        body = gzip.decompress(body)
    return final, body


def _lines(url: str):
    """The dataset's lines, read one at a time from the response."""
    read = 0
    with _open(url) as resp:
        for raw in resp:
            read += len(raw)
            if read > MAX_DATASET_BYTES:
                raise ValueError(
                    f"{url} answered with more than {MAX_DATASET_BYTES} bytes"
                )
            yield raw.decode("utf-8")


def _code(text: object) -> str:
    """Text a site chose, such as an address it redirected to or a record's
    fields, as a code span, so it cannot mention a person or add a link in the
    issue the watch opens."""
    return "`" + str(text).replace("`", "'") + "`"


def line_of(record: dict) -> str:
    """A record as the extract writes it: the dataset's compact JSON, without
    the fields the extract leaves out."""
    kept = {k: v for k, v in record.items() if k not in LEFT_OUT}
    return json.dumps(kept, ensure_ascii=False, separators=(",", ":"))


def digest(line: str) -> str:
    return hashlib.sha256(line.encode("utf-8")).hexdigest()


def git_blob(body: bytes) -> str:
    """The git object hash of a file's bytes, as ``git hash-object`` gives it."""
    return hashlib.sha1(
        b"blob %d\0" % len(body) + body, usedforsecurity=False
    ).hexdigest()


def _extract() -> dict[int, dict]:
    """The extract's records, by id."""
    records = {}
    for line in EXTRACT.read_text(encoding="utf-8").splitlines():
        record = json.loads(line)
        records[record["id"]] = record
    return records


def _relevant(line: str) -> bool:
    """Whether a raw line may hold a record the checks need, decided without
    parsing it: a pinned id anywhere in it, or a supplement's reference. A line
    that matches by chance costs one parse and no more."""
    if any(prefix in line for prefix in SUPPLEMENT_PREFIXES):
        return True
    return any(str(i) in line for i in PINNED_RECORDS)


def check_extract() -> tuple[list[str], bool]:
    """Report whether the extract is the lines pinned, offline."""
    report = [
        f"- Pinned edition: {PINNED_EDITION}, {PINNED_SOURCE}; "
        f"ISO Open Data as of {PINNED_DATE}."
    ]
    problems = []
    if not EXTRACT.is_file():
        problems.append("the extract is missing")
    else:
        lines = EXTRACT.read_text(encoding="utf-8").splitlines()
        seen = {}
        for line in lines:
            seen[json.loads(line)["id"]] = digest(line)
        for rid, pinned in sorted(PINNED_RECORDS.items()):
            if rid not in seen:
                problems.append(f"record {rid} is missing from the extract")
            elif seen[rid] != pinned:
                problems.append(f"record {rid} differs from the pinned line")
        problems += [
            f"record {rid} is in the extract but not pinned"
            for rid in sorted(seen.keys() - PINNED_RECORDS.keys())
        ]
    if problems:
        report.append(f"- **{len(problems)} problem(s) with the extract:**")
        report += [f"  - {p}" for p in problems]
        return report, True
    report.append(
        f"- The extract holds the {len(PINNED_RECORDS)} pinned records, each line as pinned."
    )
    return report, False


def check_records() -> tuple[list[str], bool]:
    """Stream the live dataset and report what changed since the pin."""
    pinned = _extract()
    live: dict[int, dict] = {}
    supplements: dict[int, dict] = {}
    replacements: dict[int, dict] = {}
    for line in _lines(DATASET):
        if not _relevant(line):
            continue
        record = json.loads(line)
        rid = record["id"]
        if rid in PINNED_RECORDS:
            live[rid] = record
        if record.get("reference", "").startswith(SUPPLEMENT_PREFIXES):
            supplements[rid] = record
        if rid not in PINNED_RECORDS and (
            set(record.get("replaces") or []) & set(PINNED_RECORDS)
        ):
            replacements[rid] = record

    report, attention = [], False
    unchanged = 0
    for rid in sorted(PINNED_RECORDS):
        old = pinned.get(rid, {})
        name = old.get("reference", str(rid))
        if rid not in live:
            attention = True
            report.append(
                f"- **{name} (record {rid}) is no longer in the dataset.** Find out "
                "whether ISO withdrew it or renumbered it."
            )
            continue
        new = live[rid]
        if digest(line_of(new)) == PINNED_RECORDS[rid]:
            unchanged += 1
            continue
        attention = True
        changed = sorted(
            k
            for k in (new.keys() | old.keys()) - set(LEFT_OUT)
            if new.get(k) != old.get(k)
        )
        details = "; ".join(
            f"`{k}` from {_code(json.dumps(old.get(k), ensure_ascii=False))} to "
            f"{_code(json.dumps(new.get(k), ensure_ascii=False))}"
            for k in changed
        )
        report.append(f"- **{name} (record {rid}) changed:** {details}.")
        if new.get("currentStage") != PUBLISHED:
            report.append(
                f"  - Its stage is now {_code(new.get('currentStage'))}, not {PUBLISHED} "
                "(published); read ISO's stage codes to see what that means."
            )
        if new.get("replacedBy"):
            report.append(
                f"  - ISO now lists it as replaced by {_code(new['replacedBy'])}. Decide "
                "whether the schema moves to the successor."
            )
    report.append(
        f"- {unchanged} of {len(PINNED_RECORDS)} pinned records are unchanged."
    )
    for rid, record in sorted(supplements.items()):
        if rid not in PINNED_RECORDS:
            attention = True
            report.append(
                f"- **ISO lists a supplement that is not pinned: "
                f"{_code(record.get('reference'))} (record {_code(rid)}, stage "
                f"{_code(record.get('currentStage'))}).** Read it, decide what the schema "
                "changes, and add it to the extract and the watch's pins."
            )
    for rid, record in sorted(replacements.items()):
        attention = True
        replaced = sorted(set(record.get("replaces") or []) & set(PINNED_RECORDS))
        report.append(
            f"- **{_code(record.get('reference'))} (record {_code(rid)}, stage "
            f"{_code(record.get('currentStage'))}) replaces record "
            f"{', '.join(map(str, replaced))}.** Decide whether the schema follows it."
        )
    return report, attention


def check_dpv() -> tuple[list[str], bool]:
    """Report whether the copy of DPV's mapping is the one pinned, and whether DPV
    has changed the file since."""
    for path, pinned in (
        (DPV_COPY, DPV_MAPPING_BLOB),
        (DPV_LICENCE_COPY, DPV_LICENCE_BLOB),
    ):
        if not path.is_file() or git_blob(path.read_bytes()) != pinned:
            return [
                f"- **{path.name} differs from the file pinned at {DPV_TAG}.** Copy "
                "it again from that tag."
            ], True
    where, body = _get(DPV_MAPPING_URL)
    if git_blob(body) == DPV_MAPPING_BLOB:
        return [f"- DPV's mapping to the standard is unchanged since {DPV_TAG}."], False
    return [
        f"- **DPV's mapping to the standard ({_code(where)}) changed since {DPV_TAG}.** "
        "Read it, change the schema's mappings to match, and pin the new file."
    ], True


def check_licence() -> tuple[list[str], bool]:
    """Report the dataset's licence as ISO's open data page names it."""
    try:
        where, body = _get(LICENCE_PAGE)
    except urllib.error.HTTPError as err:
        if err.code not in (401, 403, 429):
            raise
        where, body = _get(LICENCE_MIRROR)
    page = body.decode("utf-8", errors="replace")
    section = page.partition('id="iso_deliverables_metadata"')[2]
    row = re.search(
        r"<td>\s*License\s*</td>\s*<td>(.*?)</td>", section, flags=re.S | re.I
    )
    if not row:
        return [
            f"- **ISO's open data page ({_code(where)}) no longer names the licence of "
            "iso_deliverables_metadata where the check looks.** Read the page."
        ], True
    href = re.search(r'href="([^"]+)"', row.group(1))
    name = html.unescape(re.sub(r"<[^>]+>", "", row.group(1))).strip()
    url = href.group(1) if href else ""
    if name != PINNED_LICENCE or url.rstrip("/") != PINNED_LICENCE_URL.rstrip("/"):
        return [
            f"- **ISO's open data page ({_code(where)}) names the dataset's licence as "
            f"{name} ({url or 'no link'}), not {PINNED_LICENCE}.** Check that the "
            "extract and NOTICE still meet its terms."
        ], True
    return [f"- Licence: {PINNED_LICENCE}, as read at {_code(where)}."], False


# Each check, by the name the report gives it when it cannot finish.
CHECKS = (
    ("extract", check_extract),
    ("records", check_records),
    ("DPV mapping", check_dpv),
    ("licence", check_licence),
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--report", type=Path, help="Also write the Markdown report to this file"
    )
    args = parser.parse_args(argv)
    lines, attention = [], False
    for label, check in CHECKS:
        try:
            found, needs = check()
        # OSError covers a refused or failed fetch and a timeout,
        # HTTPException a connection cut off mid-dataset, EOFError a gzipped
        # page cut short, and ValueError a line that is not JSON or UTF-8.
        except (OSError, http.client.HTTPException, EOFError, ValueError) as err:
            found = [f"- **The {label} check could not finish: {_code(err)}.**"]
            needs = True
        lines += found
        attention = attention or needs
    text = "\n".join(lines) + "\n"
    print(text, end="")
    if args.report:
        args.report.write_text(text, encoding="utf-8")
    return 1 if attention else 0


if __name__ == "__main__":
    sys.exit(main())
