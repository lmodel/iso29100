---
type: Explanation
id: https://w3id.org/lmodel/iso29100/knowledge/explanations/modelling-choices
genre: explanation
title: Modelling choices
description: "Why the schema has these shapes: records that refer by identifier, an actor's kind told apart by a designator, principles held by subclause number, and fields that go beyond the framework named as an adopter's."
references:
  - https://w3id.org/lmodel/iso29100/knowledge/datasets/iso29100-linkml-schema
sources:
  - id: about.md
    resource: docs/about.md
  - id: changelog.md
    resource: CHANGELOG.md
    title: Unreleased
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:12:24Z"
status: draft
---

# Modelling choices

The schema was rewritten with the `Pf` prefix on classes and enums and the `pf_` prefix on slots. Every record has a `pf_id`, a reference holds one, and an actor states its kind. Every title and description is this project's own.[^changelog.md]

The framework gives terms, roles and principles, and leaves the records to whoever applies it. So the fields of `PfRisk`, `PfImpactAssessment`, `PfBreach`, `PfConsent`, `PfPreference` and `PfProcessingActivity` are what an adopter keeps, and `PfRiskLevel` is offered for an organization that adopts it.[^about.md]

[^about.md]: docs/about.md
[^changelog.md]: CHANGELOG.md, Unreleased
