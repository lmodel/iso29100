---
type: PfPolicy
id: https://w3id.org/lmodel/iso29100/knowledge/datasets/example-policy
genre: reference
title: A privacy notice as a concept
description: An example written as a concept of type `PfPolicy` in the adapt copy's keys. It shows that the domain schema admits a policy as a concept, naming its audience and the principle it bears on by number.
resource: tests/data/valid/PfPolicy-notice.yaml
references:
  - https://w3id.org/lmodel/iso29100/knowledge/datasets/adapt-copy
sources:
  - id: readme.md
    resource: README.md
    title: the Knowledge Trust Ladder (KTL) section
  - id: example
    resource: tests/data/valid/PfPolicy-notice.yaml
pf_policy_audience: public_notice
pf_policy_version: "3.1"
pf_principles:
  - principle_6_8
pf_stated_rights:
  - See the PII held about you
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:12:24Z"
status: draft
---

# A privacy notice as a concept

This concept carries the audience, version, principle and stated right of the example in `tests/data/valid/`, written in the keys the adapt copy gives a concept.[^example] The README lists the classes a concept may name as its type.[^readme.md]

[^example]: tests/data/valid/PfPolicy-notice.yaml
[^readme.md]: README.md, the Knowledge Trust Ladder (KTL) section
