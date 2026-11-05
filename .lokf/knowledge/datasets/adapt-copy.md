---
type: Dataset
id: https://w3id.org/lmodel/iso29100/knowledge/datasets/adapt-copy
genre: reference
title: The schema's adapt copy
description: "`.lokf/iso29100.yaml`, the copy `just lokf-adapt` writes from the schema so that it sits beside LOKF's `lokf.yaml`: nine classes rooted on `Concept`, `pf_id` dropped for LOKF's `id`, `title` and `description` folded into LOKF's, and the actor's designator demoted."
resource: .lokf/iso29100.yaml
derivedFrom:
  - https://w3id.org/lmodel/iso29100/knowledge/datasets/iso29100-linkml-schema
about:
  - https://w3id.org/lmodel/iso29100/knowledge/glossary/adapt-copy
sources:
  - id: project.justfile
    resource: project.justfile
    title: the comment above the recipes
  - id: readme.md
    resource: README.md
    title: the Knowledge Trust Ladder (KTL) section
  - resource: .lokf/iso29100.yaml
  - resource: .lokf/justfile
    title: the schema line
  - resource: .lokf/pyproject.toml
    title: the schema setting
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:12:24Z"
status: draft
---

# The schema's adapt copy

`just lokf-adapt` writes `.lokf/iso29100.yaml` from the schema, and `just lokf-adapt-check` fails when it is stale. The roots are the classes a knowledge concept may use as its `type`: the actors, a PII item, a processing activity, a requirement, a policy, a control, a principle's implementation, a risk and an impact assessment.[^project.justfile]

The README lists the concept types for the *Known LOKF types* setting. Every other key starts with `pf_`, so the copy shares none with a neighbour's copy, and a host can import them together. A release carries the copy as its schema asset.[^readme.md]

[^project.justfile]: project.justfile, the comment above the recipes
[^readme.md]: README.md, the Knowledge Trust Ladder (KTL) section
