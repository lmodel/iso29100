# About iso29100

This page says how the [LinkML](https://linkml.io) schema's classes fit together and what the model leaves out. [NOTICE](https://github.com/lmodel/iso29100/blob/main/NOTICE) says what rights it rests on.

## How the classes fit together

`PfFramework` is the tree root and holds each kind of record in a list of its own. Every record mixes in `PfRecordMixin`, which gives it a `pf_id`, a title and a description, and a reference holds the `pf_id` of the record it names.

An actor is a principal, a controller, a processor or a third party, told apart by the designator `pf_actor_type`. A flow names the actor PII comes from and the one it goes to. A processing activity joins the controller, the processors, the PII and the flows.

`PfSafeguardingRequirement` says what must be done and where the duty comes from. `PfControl` says what is done, and the two refer to each other. `PfPrincipleImplementation` says how the organization stands against one principle of `PfPrinciple`, which holds the principles by subclause number.

## What goes beyond the framework

The framework gives terms, roles and principles, and leaves the records to whoever applies it. So the fields of `PfRisk`, `PfImpactAssessment`, `PfBreach`, `PfConsent`, `PfPreference` and `PfProcessingActivity` are what an adopter keeps. `PfRiskLevel` is offered for an organization that adopts it.

## What the model leaves out

- The text of the standard.
- A clause number for a term or a lower subclause, since no source this repository can read gives one.
- A fixed method of risk assessment.
- The rules no validator checks, which the [overview](index.md) lists.
