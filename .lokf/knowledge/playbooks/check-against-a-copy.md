---
type: Playbook
id: https://w3id.org/lmodel/iso29100/knowledge/playbooks/check-against-a-copy
genre: how-to
title: Check the wording against a copy of the standard
description: How a person who holds a copy of ISO/IEC 29100 tests that the repository shares no run of four or more words with it and cites only numbers that start a line of it, using `scripts/check_overlap.py`, with the copy kept outside the repository.
references:
  - https://w3id.org/lmodel/iso29100/knowledge/references/iso-iec-29100
sources:
  - id: overlap
    resource: scripts/check_overlap.py
    title: the docstring
  - id: allowed
    resource: tests/overlap_allowed.yaml
  - id: test_overlap.py
    resource: tests/test_overlap.py
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:12:24Z"
status: draft
---

# Check the wording against a copy of the standard

The script's docstring gives the commands. It reads the copy's plain text, refuses a copy inside the repository, and also reports a clause number the schema cites that starts no line of the copy.[^overlap]

A run may be allowed only with a reason, in `tests/overlap_allowed.yaml`.[^allowed] Run it by hand: CI has no copy, and `tests/test_overlap.py` tests the script on text of its own.[^test_overlap.py]

[^overlap]: scripts/check_overlap.py, the docstring
[^allowed]: tests/overlap_allowed.yaml
[^test_overlap.py]: tests/test_overlap.py
