---
type: Dataset
id: https://w3id.org/lmodel/iso29100/knowledge/datasets/neighbour-copies
genre: reference
title: The neighbours' adapt copies
description: The adapt copies of 27 released lmodel repositories in `tests/neighbours/`, each pinned by its SHA-256, which a test holds this schema's names apart from.
resource: tests/neighbours
references:
  - https://w3id.org/lmodel/iso29100/knowledge/datasets/adapt-copy
sources:
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:12:24Z"
status: draft
---

# The neighbours' adapt copies

Each copy is the schema asset of a release, pinned by its checksum. The tests hold this schema's copy apart from them: no class, enum, type or subset name is shared, and the copy's keys share none with theirs.[^test_schema_rules.py]

[^test_schema_rules.py]: tests/test_schema_rules.py
