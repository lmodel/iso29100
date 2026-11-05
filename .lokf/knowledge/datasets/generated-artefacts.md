---
type: Dataset
id: https://w3id.org/lmodel/iso29100/knowledge/datasets/generated-artefacts
genre: reference
title: The generated artefacts
description: "What `just gen-project` and `just gen-doc` generate from the schema: the projections in `project/`, the Python models in `src/iso29100/datamodel/`, and the merged schema in `docs/schema/`. None is edited by hand."
resource: project
references:
  - https://w3id.org/lmodel/iso29100/knowledge/datasets/iso29100-linkml-schema
sources:
  - id: contributing.md
    resource: CONTRIBUTING.md
    title: Before opening a pull request
  - id: index.md
    resource: docs/index.md
    title: Validating data
  - resource: src/iso29100/datamodel
  - resource: docs/schema
  - resource: .linkml/generators.yaml
  - resource: config.public.mk
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:12:24Z"
status: draft
---

# The generated artefacts

`just gen-project` writes the projections in `project/` and the Python models in `src/iso29100/datamodel/`, and `just gen-doc` writes the merged schema to `docs/schema/`. They are committed and never edited by hand.[^contributing.md]

`linkml-validate` checks a file against the JSON Schema generated from the schema, which applies every constraint. Validate a file before loading it into a model in `src/iso29100/datamodel/`, since LinkML 1.12.1 generates models that check less, and write dates as quoted strings.[^index.md]

[^contributing.md]: CONTRIBUTING.md, Before opening a pull request
[^index.md]: docs/index.md, Validating data
