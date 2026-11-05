"""Checks the upstream watch's decisions against stubbed answers.

scripts/check_upstream_release.py streams ISO Open Data's metadata file, reads ISO's
open data page and reads DPV's mapping file. These tests replace its two network
calls, `_lines` and `_get`, with canned answers built from the extract and the copy,
so they run offline. They show what the report says when ISO adds a supplement,
changes a stage, publishes a new edition, drops a record or changes the licence, when
DPV changes its file, and when the network fails.
"""

import importlib.util
import http.client
import json
import urllib.error
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "check_upstream_release.py"
EXTRACT = (
    ROOT
    / "src"
    / "iso29100"
    / "schema"
    / "iso-open-data"
    / "iso_deliverables_metadata.jsonl"
)

DPV_COPY = ROOT / "upstream" / "dpv-iso.ttl"

PAGE = """<html><body>
<section id="iso_technical_committees"><table>
<tr><td>License</td><td><a href="https://example.org/other">Other</a></td></tr>
</table></section>
<section id="iso_deliverables_metadata"><table>
<tr><td>Dataset identifier</td><td>iso_deliverables_metadata</td></tr>
<tr><td>License</td><td><a href="{url}" target="_blank">{name}</a></td></tr>
</table></section></body></html>"""


@pytest.fixture
def watch():
    """A fresh copy of the script, so no test sees another's stubs."""
    spec = importlib.util.spec_from_file_location("watch_under_test", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _records():
    """The pinned records as the dataset would serve them, scope and all."""
    records = []
    for line in EXTRACT.read_text(encoding="utf-8").splitlines():
        record = json.loads(line)
        record["scope"] = {"en": "<p>A summary in ISO's words.</p>"}
        records.append(record)
    return records


def _unrelated():
    return {
        "id": 1,
        "deliverableType": "IS",
        "supplementType": None,
        "reference": "ISO 9001:2015",
        "currentStage": 9093,
        "replaces": None,
        "replacedBy": None,
    }


def _stub(watch, records, page=None, lines_error=None, page_error=None, dpv_body=None):
    """Make the dataset serve `records`, the open data page serve `page`, and DPV's
    address serve `dpv_body`. iso.org refuses the script, so the page comes from the
    mirror."""

    def lines(url):
        assert url == watch.DATASET
        if lines_error:
            raise lines_error
        for record in [_unrelated(), *records]:
            yield json.dumps(record, ensure_ascii=False) + "\n"

    def get(url):
        if url == watch.DPV_MAPPING_URL:
            return url, dpv_body if dpv_body is not None else DPV_COPY.read_bytes()
        if url == watch.LICENCE_PAGE:
            raise urllib.error.HTTPError(url, 403, "Forbidden", None, None)
        assert url == watch.LICENCE_MIRROR
        if page_error:
            raise page_error
        text = page or PAGE.format(
            url=watch.PINNED_LICENCE_URL, name=watch.PINNED_LICENCE
        )
        return "https://web.archive.org/web/20261017044329id_/x", text.encode()

    watch._lines = lines
    watch._get = get


def _run(watch, tmp_path):
    report = tmp_path / "report.md"
    code = watch.main(["--report", str(report)])
    return code, report.read_text(encoding="utf-8")


def _by_id(records, rid):
    return next(r for r in records if r["id"] == rid)


def test_nothing_changed(watch, tmp_path):
    """With every record as pinned and the licence unchanged, the watch
    reports the extract current and exits 0."""
    _stub(watch, _records())
    code, text = _run(watch, tmp_path)
    assert code == 0, text
    assert "The extract holds the 3 pinned records, each line as pinned." in text
    assert "3 of 3 pinned records are unchanged." in text
    assert "DPV's mapping to the standard is unchanged since dpv-2.3." in text
    assert f"Licence: {watch.PINNED_LICENCE}" in text


def test_the_scope_is_left_out_of_the_comparison(watch, tmp_path):
    """A record whose scope alone changes is unchanged for the watch, since
    the extract holds no scope."""
    records = _records()
    _by_id(records, watch.EDITION_ID)["scope"] = {"en": "<p>Reworded.</p>"}
    _stub(watch, records)
    code, text = _run(watch, tmp_path)
    assert code == 0, text


def test_a_new_supplement(watch, tmp_path):
    """A supplement of the edition that is not pinned sets attention."""
    reference = "ISO/IEC 29100:2024/Amd 1:2027"
    records = _records()
    records.append(
        {
            **_by_id(records, watch.EDITION_ID),
            "id": 99999,
            "reference": reference,
            "supplementType": "Amd",
            "replaces": None,
            "currentStage": 6060,
        }
    )
    _stub(watch, records)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert (
        f"**ISO lists a supplement that is not pinned: {reference} (record 99999, "
        "stage 6060).**" in text
    )


def test_a_replaced_record_moving_on_is_reported(watch, tmp_path):
    """A change to a replaced edition's record is a change to a pinned record."""
    records = _records()
    _by_id(records, 73722)["currentStage"] = 9999
    _stub(watch, records)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "**ISO/IEC 29100:2011/Amd 1:2018 (record 73722) changed:**" in text
    assert "`currentStage` from 9599 to 9999" in text


def test_the_pinned_edition_replacing_its_predecessors_is_no_finding(watch, tmp_path):
    """The edition itself replaces the two pinned records before it, and that is what
    the pin says, so only an unpinned record that replaces one is reported."""
    _stub(watch, _records())
    code, text = _run(watch, tmp_path)
    assert code == 0, text
    assert "replaces record" not in text


def test_a_stage_change_and_a_replacement(watch, tmp_path):
    """A pinned record whose stage and replacedBy change is reported field by
    field, with what each means."""
    records = _records()
    edition = _by_id(records, watch.EDITION_ID)
    edition["currentStage"] = 9599
    edition["replacedBy"] = [99998]
    _stub(watch, records)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "**ISO/IEC 29100:2024 (record 85938) changed:**" in text
    assert "`currentStage` from 6060 to 9599" in text
    assert "`replacedBy` from null to [99998]" in text
    assert "Its stage is now 9599, not 6060 (published)" in text
    assert "ISO now lists it as replaced by [99998]" in text
    assert "2 of 3 pinned records are unchanged." in text


def test_a_new_edition(watch, tmp_path):
    """A record that replaces a pinned one is reported."""
    records = _records()
    records.append(
        {
            "id": 99997,
            "reference": "ISO/IEC DIS 29100",
            "currentStage": 4020,
            "replaces": [watch.EDITION_ID],
            "replacedBy": None,
        }
    )
    _stub(watch, records)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert (
        "**ISO/IEC DIS 29100 (record 99997, stage 4020) replaces record 85938.**"
        in text
    )


def test_a_dropped_record(watch, tmp_path):
    """A pinned record missing from the dataset sets attention."""
    records = [r for r in _records() if r["id"] != 45123]
    _stub(watch, records)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "**ISO/IEC 29100:2011 (record 45123) is no longer in the dataset.**" in text


def test_a_changed_licence(watch, tmp_path):
    """A licence other than the pinned one, by name or by link, sets
    attention."""
    page = PAGE.format(
        url="https://creativecommons.org/licenses/by-nc/4.0/", name="CC BY-NC 4.0"
    )
    _stub(watch, _records(), page=page)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "names the dataset's licence as CC BY-NC 4.0" in text


def test_a_page_without_the_licence_row(watch, tmp_path):
    """A page the check cannot read the licence from is reported, not taken
    as unchanged."""
    _stub(watch, _records(), page="<html><body>Moved.</body></html>")
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "no longer names the licence of iso_deliverables_metadata" in text


def test_a_network_failure_still_writes_a_report(watch, tmp_path):
    """A check that cannot reach the dataset is reported as unfinished, sets
    attention, and leaves the other checks to run."""
    _stub(watch, _records(), lines_error=urllib.error.URLError("Connection refused"))
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert (
        "**The records check could not finish: `<urlopen error Connection refused>`.**"
        in text
    )
    assert "The extract holds the 3 pinned records" in text
    assert f"Licence: {watch.PINNED_LICENCE}" in text


def test_a_cut_connection_or_short_page_could_not_finish(watch, tmp_path):
    """A dataset cut off mid-read and a gzipped page cut short are checks that
    could not finish, and the extract is still checked."""
    _stub(
        watch,
        _records(),
        lines_error=http.client.IncompleteRead(b"{"),
        page_error=EOFError("Compressed file ended before the end-of-stream marker"),
    )
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "**The records check could not finish: `IncompleteRead" in text
    assert "**The licence check could not finish: `Compressed file ended" in text
    assert "The extract holds the 3 pinned records" in text


def test_dpv_changing_its_mapping_is_reported(watch, tmp_path):
    """A DPV file that differs from the pin sets attention, naming what to do."""
    _stub(watch, _records(), dpv_body=b"changed\n")
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "**DPV's mapping to the standard" in text
    assert "changed since dpv-2.3.**" in text


def test_a_copy_of_dpvs_file_that_drifts_is_reported(watch, tmp_path):
    """A local copy that differs from the pin is reported, without reading DPV."""
    copy = tmp_path / "dpv-iso.ttl"
    copy.write_bytes(b"edited\n")
    watch.DPV_COPY = copy
    _stub(watch, _records())
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "**dpv-iso.ttl differs from the file pinned at dpv-2.3.**" in text


def test_a_gzipped_page_is_read(watch, tmp_path):
    """The Internet Archive serves the page gzipped; `_get` unpacks it."""
    import gzip

    body = gzip.compress(b"<p>ok</p>")

    class Response:
        def __enter__(self):
            return self

        def __exit__(self, *exc):
            return False

        def read(self, size=-1):
            return body

        def geturl(self):
            return "https://web.archive.org/x"

    watch._open = lambda url: Response()
    assert watch._get("https://web.archive.org/x") == (
        "https://web.archive.org/x",
        b"<p>ok</p>",
    )


def test_a_redirect_to_plain_http_is_refused(watch):
    """The watch follows a redirect only over https."""
    handler = watch._HttpsOnly()
    with pytest.raises(urllib.error.URLError, match="refused"):
        handler.redirect_request(
            None, None, 302, "Found", {}, "http://www.iso.org/open-data.html"
        )


def test_a_redirect_to_another_host_is_refused(watch):
    """The watch follows a redirect only to a host it reads from."""
    handler = watch._HttpsOnly()
    with pytest.raises(urllib.error.URLError, match="refused"):
        handler.redirect_request(None, None, 302, "Found", {}, "https://example.org/x")


@pytest.mark.parametrize(
    "url", ["http://www.iso.org/open-data.html", "https://example.org/x"]
)
def test_an_address_off_the_list_is_refused(watch, url):
    """The address the watch starts from is held to the same rule."""
    with pytest.raises(urllib.error.URLError, match="refused"):
        watch._open(url)


def test_an_oversized_page_is_refused(watch):
    """The watch reads no more of a page than its cap."""
    watch.MAX_PAGE_BYTES = 8

    class Response:
        def __enter__(self):
            return self

        def __exit__(self, *exc):
            return False

        def read(self, size=-1):
            return b"x" * size

        def geturl(self):
            return "https://web.archive.org/x"

    watch._open = lambda url: Response()
    with pytest.raises(ValueError, match="more than 8 bytes"):
        watch._get("https://web.archive.org/x")


def test_an_oversized_dataset_is_refused(watch):
    """The watch stops streaming the dataset at its cap."""
    watch.MAX_DATASET_BYTES = 8

    class Response(list):
        def __enter__(self):
            return self

        def __exit__(self, *exc):
            return False

    watch._open = lambda url: Response([b"{}\n"] * 9)
    with pytest.raises(ValueError, match="more than 8 bytes"):
        list(watch._lines(watch.DATASET))
