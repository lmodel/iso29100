---
type: Playbook
id: https://w3id.org/lmodel/iso29100/knowledge/playbooks/knowledge-sources
genre: reference
title: Knowledge sources map
description: "The librarian's scrape map: every repository location this bundle derives concepts from, how to re-check each, and the tracked paths left out with their reasons."
resource: .
references:
  - https://w3id.org/lmodel/iso29100/knowledge/datasets/iso29100-linkml-schema
  - https://w3id.org/lmodel/iso29100/knowledge/references/iso-iec-29100
sources:
  - resource: src/iso29100/schema
  - resource: src/iso29100/datamodel
  - resource: scripts
  - resource: tests
  - resource: docs
  - resource: upstream
  - resource: website
  - resource: .github/workflows
  - resource: .github/scripts
  - resource: .github/release
  - resource: .linkml
  - resource: .lokf/justfile
  - resource: .lokf/pyproject.toml
  - resource: .lokf/schema/iso29100.yaml
  - resource: project
  - resource: project.justfile
  - resource: justfile
  - resource: README.md
  - resource: CHANGELOG.md
  - resource: CONTRIBUTING.md
  - resource: SECURITY.md
  - resource: AI_COVENANT.md
  - resource: NOTICE
  - resource: LICENSE
  - resource: .releaserc.json
  - resource: examples/README.md
exclusions:
  - resource: .github/dependabot.yml
    reason: "Tooling: when Dependabot opens version bumps."
  - resource: .github/ISSUE_TEMPLATE
    reason: Issue forms, which are governance text and state nothing about the schema.
  - resource: .github/pull_request_template.md
    reason: The pull request checklist, which repeats CONTRIBUTING.md.
  - resource: .github/PULL_REQUEST_TEMPLATE
    reason: The sync pull request template, which the KTL sidecar owns.
  - resource: CODE_OF_CONDUCT.md
    reason: The Contributor Covenant, governance text with nothing about the schema.
  - resource: uv.lock
    reason: The package's lock file, tooling that pins versions.
  - resource: pyproject.toml
    reason: Package metadata and the spell checkers' settings; the changelog states the Python project's name.
  - resource: .gitignore
    reason: "Tooling: the files git ignores."
  - resource: .editorconfig
    reason: "Tooling: editor settings."
  - resource: .yamllint.yaml
    reason: "Tooling: the YAML linter's settings."
  - resource: .pre-commit-config.yaml
    reason: "Tooling: the hooks and the files they leave alone."
  - resource: .markdownlint-cli2.jsonc
    reason: "Tooling: the Markdown linter's settings."
  - resource: .linkmllint.yaml
    reason: "Tooling: the schema linter's settings."
  - resource: lychee.toml
    reason: "Tooling: the link checker's settings."
  - resource: llms.txt
    reason: A pointer for agents, which the KTL sidecar writes.
  - resource: .copier-answers.yml
    reason: The template's answers.
  - resource: config.public.mk
    reason: The template's variables.
  - resource: knowledge_bundle
    reason: The link to the bundle itself.
  - resource: src/README.md
    reason: The template's folder note.
  - resource: src/iso29100/__init__.py
    reason: An empty package file.
  - resource: src/iso29100/_version.py
    reason: The package version, which the build writes.
  - resource: .lokf/README.md
    reason: The sidecar page, from the KTL template.
  - resource: .lokf/.gitattributes
    reason: "Tooling: from the KTL template."
  - resource: .lokf/.gitignore
    reason: "Tooling: from the KTL template."
  - resource: .lokf/ingest.yaml.sample
    reason: A sample from the KTL template, not used here.
  - resource: .lokf/queries.http
    reason: Sample queries from the KTL template.
  - resource: .lokf/uv.lock
    reason: The sidecar's lock file.
  - resource: .lokf/schema/lokf.yaml
    reason: LOKF's schema, pinned by the sidecar.
  - resource: .lokf/scripts
    reason: Copies of the KTL templates, which the sync keeps current.
  - resource: .lokf/m365
    reason: Copies of the KTL templates, which the sync keeps current.
generated:
  by: process:ktl-librarian
  at: "2026-11-06T21:21:36Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-11-05T14:23:23Z"
---

# Knowledge sources map

Re-derive a concept from the paths under `sources`, and treat each exclusion's reason as the check for it. The bundle cites the standard by number and record only, so a re-check reads ISO's records and no text of the standard.
