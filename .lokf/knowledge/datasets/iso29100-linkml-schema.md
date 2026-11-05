---
type: Dataset
id: https://w3id.org/lmodel/iso29100/knowledge/datasets/iso29100-linkml-schema
genre: reference
title: The iso29100 LinkML schema
description: "`src/iso29100/schema/iso29100.yaml`: the records an organization keeps when it applies the privacy framework of ISO/IEC 29100:2024, with the `Pf` class prefix, the `pf_` slot prefix and `PfFramework` as its root."
resource: src/iso29100/schema/iso29100.yaml
about:
  - https://w3id.org/lmodel/iso29100/knowledge/references/iso-iec-29100
sources:
  - id: schema
    resource: src/iso29100/schema/iso29100.yaml
  - id: about.md
    resource: docs/about.md
    title: How the classes fit together
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:12:24Z"
status: draft
---

# The iso29100 LinkML schema

`PfFramework` is the tree root and holds each kind of record in a list of its own. Every record mixes in `PfRecordMixin`, which gives it a `pf_id`, a title and a description, and a reference holds the `pf_id` of the record it names.[^about.md]

An actor is a principal, a controller, a processor or a third party, told apart by the designator `pf_actor_type`.[^about.md]

An element cites what it models by number in the `iso29100_clause` annotation, where a third party's public outline of the edition gives that number, and its title and description are this project's own words. `PfPrinciple` holds the privacy principles by subclause number.[^schema]

[^schema]: src/iso29100/schema/iso29100.yaml
[^about.md]: docs/about.md, How the classes fit together
