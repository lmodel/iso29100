---
type: Explanation
id: https://w3id.org/lmodel/iso29100/knowledge/explanations/mappings
genre: explanation
title: Mappings and the SSSOM set
description: "Where the schema crosses to another vocabulary: the five rows DPV publishes for this edition, each held to the pinned copy of DPV's file. The SSSOM set and the other mappings of the old schema are gone."
references:
  - https://w3id.org/lmodel/iso29100/knowledge/datasets/dpv-mapping
sources:
  - id: readme.md
    resource: README.md
    title: Mappings
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: the DPV tests
  - id: schema
    resource: src/iso29100/schema/iso29100.yaml
    title: the comment on PfPiiItem
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:12:24Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-11-05T14:23:23Z"
---

# Mappings and the SSSOM set

The schema is the one home for mappings. The SSSOM set is gone: it repeated DPV's rows, and hung DPV's row for consent on a record about consent. The other mappings in the old schema had no source, so they went too.[^readme.md]

`tests/test_upstream.py` holds each mapping to a row of DPV's file and fails on any other.[^test_upstream.py] `PfPiiItem` maps to `dpv:PersonalData` by `narrow_mappings`, because DPV's file states that term as narrower than the standard's PII.[^schema]

[^readme.md]: README.md, Mappings
[^test_upstream.py]: tests/test_upstream.py, the DPV tests
[^schema]: src/iso29100/schema/iso29100.yaml, the comment on PfPiiItem
