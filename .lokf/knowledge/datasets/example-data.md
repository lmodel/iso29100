---
type: Dataset
id: https://w3id.org/lmodel/iso29100/knowledge/datasets/example-data
genre: reference
title: The example data
description: "`tests/data/`: a valid example per class and a counter-example per constraint, each counter-example naming on its first line where it must fail. `PfFramework-acme` is one whole framework."
resource: tests/data
references:
  - https://w3id.org/lmodel/iso29100/knowledge/datasets/iso29100-linkml-schema
sources:
  - id: test_data.py
    resource: tests/test_data.py
  - id: readme
    resource: tests/data/README.md
  - id: index.md
    resource: docs/index.md
    title: Validating data
  - resource: examples/README.md
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:12:24Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-11-05T14:23:23Z"
---

# The example data

File names follow `classname-###.yaml`.[^readme] A counter-example's first line, `# Fails at: <pointer>`, names where it must fail, so a file that starts failing for another reason fails the test. Every class that is neither abstract nor a mixin has a valid example.[^test_data.py]

The same test file checks the rules no validator checks, and shows that each is caught when it is broken. Within a whole framework no two records share a `pf_id`, and each reference names a record the framework holds, of the class it ranges over. The other rules cover flows, risk levels, impact assessments, the order of dates and transfer safeguards.[^test_data.py] The overview lists those rules for a reader.[^index.md]

[^readme]: tests/data/README.md
[^test_data.py]: tests/test_data.py
[^index.md]: docs/index.md, Validating data
