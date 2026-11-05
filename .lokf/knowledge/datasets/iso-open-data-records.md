---
type: Dataset
id: https://w3id.org/lmodel/iso29100/knowledge/datasets/iso-open-data-records
genre: reference
title: ISO Open Data's records
description: "`src/iso29100/schema/iso-open-data/`: ISO's records of the edition and of the two it replaced as of 2026-11-05, under ODC-By v1.0, each without its scope and pinned by hash."
resource: src/iso29100/schema/iso-open-data/iso_deliverables_metadata.jsonl
about:
  - https://w3id.org/lmodel/iso29100/knowledge/references/iso-iec-29100
sources:
  - id: notice
    resource: NOTICE
    title: ISO Open Data
  - id: watch
    resource: scripts/check_upstream_release.py
    title: the pins
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: the docstring
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:12:24Z"
status: draft
---

# ISO Open Data's records

Each line is ISO's record as published, without its scope. The records were taken on 2026-11-05 and are used under the ODC Attribution License v1.0.[^notice]

The watch pins each line by its SHA-256, and leaves out the scope because it is a summary of the standard in ISO's words.[^watch] `tests/test_upstream.py` holds the schema header to the extract and the pins.[^test_upstream.py]

[^notice]: NOTICE, ISO Open Data
[^watch]: scripts/check_upstream_release.py, the pins
[^test_upstream.py]: tests/test_upstream.py, the docstring
