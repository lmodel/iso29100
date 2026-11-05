---
type: Playbook
id: https://w3id.org/lmodel/iso29100/knowledge/playbooks/update-upstream-pins
genre: how-to
title: Move to another edition or supplement
description: "What to do when the watch reports a change: read the record, decide what the schema changes, replace the extract from one day's dataset, and move the watch's pins and the schema header together. A change to DPV's file moves the mappings."
references:
  - https://w3id.org/lmodel/iso29100/knowledge/datasets/iso-open-data-records
  - https://w3id.org/lmodel/iso29100/knowledge/datasets/dpv-mapping
  - https://w3id.org/lmodel/iso29100/knowledge/workflows/upstream-watch
sources:
  - id: watch
    resource: scripts/check_upstream_release.py
    title: the report it writes
  - id: contributing.md
    resource: CONTRIBUTING.md
    title: Before opening a pull request
  - id: test_upstream.py
    resource: tests/test_upstream.py
  - id: notice
    resource: NOTICE
    title: ISO/IEC 29100
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:12:24Z"
status: draft
---

# Move to another edition or supplement

1. Read the watch's report, which names the record and the fields that changed.[^watch]
2. Replace the extract whole from one day's dataset, never by editing it.[^contributing.md]
3. Move the pins in the watch, and the header's `version` and annotations if the edition moved. `tests/test_upstream.py` holds them equal.[^test_upstream.py]
4. A person who holds the new text reads it and decides what the schema changes. ISO's agreement restricts use of the text with AI tools, so none of it goes to one.[^notice]
5. When the report names DPV's file, read it, change the schema's mappings to match, copy the file again and pin it.[^watch]

[^watch]: scripts/check_upstream_release.py, the report it writes
[^contributing.md]: CONTRIBUTING.md, Before opening a pull request
[^test_upstream.py]: tests/test_upstream.py
[^notice]: NOTICE, ISO/IEC 29100
