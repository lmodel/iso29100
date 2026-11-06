---
lokf_version: "0.2"
okf_version: "0.2"
base_iri: https://w3id.org/lmodel/iso29100/knowledge/
context: https://w3id.org/lokf/context.jsonld
title: iso29100 Knowledge Bundle
description: ISO/IEC 29100:2024 privacy framework records (LinkML)
license: https://creativecommons.org/licenses/by/4.0/
publisher:
  type: Person
  id: https://w3id.org/lmodel/iso29100/knowledge/person/noel-mcloughlin
  name: Noel McLoughlin
---

# iso29100 Knowledge Bundle

A [LOKF](https://lokf.nolan-nichols.com) knowledge base for iso29100. Every Markdown file under `knowledge/` is one concept; together they form a queryable knowledge graph, derived from this repository's code and docs.

# Services

* [Documentation site](services/documentation-site.md) - The knowledge website in `website/`, an Astro Starlight site that the Knowledge website workflow publishes to GitHub Pages at `https://lmodel.github.io/iso29100`, built from the README, `docs/`, the schema's pages and the bundle. It replaces the mkdocs site.

# Glossary

* [Adapt copy](glossary/adapt-copy.md) - An adapt copy: the copy of a published LinkML schema that `lokf adapt` writes so that it can sit beside LOKF's `lokf.yaml` in a domain schema, with its chosen roots on `Concept`.

# Datasets

* [The generated artefacts](datasets/generated-artefacts.md) - What `just gen-project` and `just gen-doc` generate from the schema: the projections in `project/`, the Python models in `src/iso29100/datamodel/`, and the merged schema in `docs/schema/`. None is edited by hand.
* [The iso29100 LinkML schema](datasets/iso29100-linkml-schema.md) - `src/iso29100/schema/iso29100.yaml`: the records an organization keeps when it applies the privacy framework of ISO/IEC 29100:2024, with the `Pf` class prefix, the `pf_` slot prefix and `PfFramework` as its root.
* [The schema's adapt copy](datasets/adapt-copy.md) - `.lokf/schema/iso29100.yaml`, the copy `just lokf-adapt` writes from the schema so that it sits beside LOKF's `lokf.yaml`: nine classes rooted on `Concept`, `pf_id` dropped for LOKF's `id`, `title` and `description` folded into LOKF's, and the actor's designator demoted.
* [The example data](datasets/example-data.md) - `tests/data/`: a valid example per class and a counter-example per constraint, each counter-example naming on its first line where it must fail. `PfFramework-acme` is one whole framework.
* [A privacy notice as a concept](datasets/example-policy.md) - An example written as a concept of type `PfPolicy` in the adapt copy's keys. It shows that the domain schema admits a policy as a concept, naming its audience and the principle it bears on by number.
* [ISO Open Data's records](datasets/iso-open-data-records.md) - `src/iso29100/schema/iso-open-data/`: ISO's records of the edition and of the two it replaced as of 2026-11-05, under ODC-By v1.0, each without its scope and pinned by hash.
* [DPV's mapping to the standard](datasets/dpv-mapping.md) - `upstream/dpv-iso.ttl`: the five rows the Data Privacy Vocabulary (DPV) publishes between its terms and ISO/IEC 29100:2024, copied unchanged at DPV's tag `dpv-2.3` under the W3C Software and Document License, and pinned by git object hash.
* [The neighbours' adapt copies](datasets/neighbour-copies.md) - The adapt copies of 27 released lmodel repositories in `tests/neighbours/`, each pinned by its SHA-256, which a test holds this schema's names apart from.

# Playbooks

* [Regenerate and test](playbooks/regenerate-and-test.md) - How to change the schema: edit `src/iso29100/schema/iso29100.yaml`, run `just lint`, `just gen-project`, `just gen-doc`, `just lokf-adapt` and `just test`, and commit what they write.
* [Release](playbooks/release.md) - How a release happens: `semantic-release.yml` reads Conventional Commits on `main`, promotes the `## [Unreleased]` section, tags and publishes. The first release needs the `v0.0.0` baseline tag on `main`, and PyPI publishing stays off.
* [Check the wording against a copy of the standard](playbooks/check-against-a-copy.md) - How a person who holds a copy of ISO/IEC 29100 tests that the repository shares no run of four or more words with it and cites only numbers that start a line of it, using `scripts/check_overlap.py`, with the copy kept outside the repository.
* [Move to another edition or supplement](playbooks/update-upstream-pins.md) - What to do when the watch reports a change: read the record, decide what the schema changes, replace the extract from one day's dataset, and move the watch's pins and the schema header together. A change to DPV's file moves the mappings.
* [Knowledge sources map](playbooks/knowledge-sources.md) - The librarian's scrape map: every repository location this bundle derives concepts from, how to re-check each, and the tracked paths left out with their reasons.

# Workflows

* [Knowledge librarian (knowledge-librarian.yaml)](workflows/knowledge-librarian.md) - The sidecar's scheduled agent run that keeps the bundle in step with the repository and opens a pull request for a person to review. It is inert until `KNOWLEDGE_LIBRARIAN_ENABLED` is `true`.
* [Knowledge registrar (knowledge-registrar.yaml)](workflows/knowledge-registrar.md) - The gate on the bundle: it validates the bundle on each pull request that touches it and weekly, and checks that each new `human:` event in a pull request is backed by an approval or a signature. It never judges whether content is true.
* [Knowledge release (knowledge-release.yaml)](workflows/knowledge-release.md) - The workflow that attaches the bundle, a Copilot skill and the schema's adapt copy to a GitHub release, each with a checksum. It starts by hand or, once `KNOWLEDGE_RELEASE_ENABLED` is `true`, on each published release.
* [Knowledge sync (knowledge-sync.yaml)](workflows/knowledge-sync.md) - The weekly workflow that keeps the sidecar's copies and the skills pin at the newest release of Knowledge Trust Ladder, by one pull request that a person merges.
* [Knowledge website (knowledge-website.yaml)](workflows/knowledge-website.md) - The workflow that builds `website/` on each pull request that touches its inputs, and deploys the default branch's build to GitHub Pages once `KNOWLEDGE_WEBSITE_ENABLED` is `true`.
* [Lint and docs (lint-and-docs.yaml)](workflows/lint-and-docs.md) - The static checks on pull requests, on `main` and every Monday: ShellCheck, actionlint, the word budgets of CONTRIBUTING.md and SECURITY.md, markdownlint, lychee and codespell.
* [Build and test (main.yaml)](workflows/main.md) - The Build and test workflow: on every pull request and push to `main`, it runs `just test` on Python 3.10 to 3.14, and lints the schema and checks the adapt copy on 3.13.
* [Semantic release (semantic-release.yml)](workflows/semantic-release.md) - The workflow that computes the next version from Conventional Commits on `main`, promotes the changelog, tags and publishes a GitHub Release, and dispatches the knowledge release once `KNOWLEDGE_RELEASE_ENABLED` is `true`.
* [Upstream watch (upstream-watch.yaml)](workflows/upstream-watch.md) - The weekly check that `scripts/check_upstream_release.py` runs: a change to ISO's records of the edition or of the two it replaced, to the dataset's licence, or to DPV's mapping file fails the run and opens or updates an issue.

# References

* [ISO/IEC 29100:2024](references/iso-iec-29100.md) - The edition the schema models: ISO's record 85938, second edition, published 2024-02-16, which replaced ISO/IEC 29100:2011 and its Amendment 1:2018. This bundle holds none of the standard's text.

# Explanations

* [Mappings and the SSSOM set](explanations/mappings.md) - Where the schema crosses to another vocabulary: the five rows DPV publishes for this edition, each held to the pinned copy of DPV's file. The SSSOM set and the other mappings of the old schema are gone.
* [Modelling choices](explanations/modelling-choices.md) - Why the schema has these shapes: records that refer by identifier, an actor's kind told apart by a designator, principles held by subclause number, and fields that go beyond the framework named as an adopter's.
* [Scope](explanations/scope.md) - What the model leaves out: the text of the standard, a clause number for a term or a lower subclause, a fixed method of risk assessment, and the rules no validator checks.

# Policies

* [AI covenant](policies/ai-covenant.md) - The rules for AI-assisted work here: whoever submits owns the contribution, an element cites by number and never quotes, no ISO text goes anywhere in the repository, and ISO's metadata records are never edited.
* [Licence and attribution](policies/license-and-attribution.md) - Whose work each part is: the code and schema under Apache-2.0, the bundle under CC BY 4.0, ISO's metadata records under ODC-By, DPV's mapping under the W3C Software and Document License, and the standard's text, which the repository does not hold.
* [Security policy](policies/security-policy.md) - How to report a vulnerability in this repository, by GitHub's private reporting, what executes here and what holds each surface. A problem in the standard belongs with its committee.
