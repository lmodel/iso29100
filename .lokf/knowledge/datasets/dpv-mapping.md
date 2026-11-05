---
type: Dataset
id: https://w3id.org/lmodel/iso29100/knowledge/datasets/dpv-mapping
genre: reference
title: DPV's mapping to the standard
description: "`upstream/dpv-iso.ttl`: the five rows the Data Privacy Vocabulary (DPV) publishes between its terms and ISO/IEC 29100:2024, copied unchanged at DPV's tag `dpv-2.3` under the W3C Software and Document License, and pinned by git object hash."
resource: upstream/dpv-iso.ttl
about:
  - https://w3id.org/lmodel/iso29100/knowledge/references/iso-iec-29100
sources:
  - id: dpv-iso.ttl
    resource: upstream/dpv-iso.ttl
  - id: notice
    resource: NOTICE
    title: Data Privacy Vocabulary (DPV)
  - id: watch
    resource: scripts/check_upstream_release.py
    title: the DPV pins
  - resource: upstream/DPV-LICENSE.md
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:12:24Z"
status: draft
---

# DPV's mapping to the standard

The file names five concepts of the standard: PII, PII controller, PII principal, PII processor and consent. It states `dpv:PersonalData` as narrower than PII, and each of the other four as an exact match of one DPV term.[^dpv-iso.ttl]

NOTICE carries the attribution, and `upstream/DPV-LICENSE.md` the licence in full.[^notice] The watch compares the copy with the pin, and DPV's current file with the copy.[^watch]

[^dpv-iso.ttl]: upstream/dpv-iso.ttl
[^notice]: NOTICE, Data Privacy Vocabulary (DPV)
[^watch]: scripts/check_upstream_release.py, the DPV pins
