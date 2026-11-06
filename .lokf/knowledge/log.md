# Change Log

## 2026-11-06

* **Changed**: `lokf.yaml` and `iso29100.yaml` moved into `.lokf/schema/`, where KTL v0.62.0 keeps a sidecar's schema files, and the concepts that name them follow.

## 2026-11-05

* **Prose**: reworded 3 concept bodies in plain English. No fact, link, number or frontmatter changed.
* **Added**: Adapt copy, from project.justfile.
* **Added**: The generated artefacts, from CONTRIBUTING.md and docs/index.md.
* **Added**: Regenerate and test, from CONTRIBUTING.md, main.yaml and the justfile.
* **Added**: Release, from CONTRIBUTING.md and SECURITY.md.
* **Added**: Documentation site, from website/README.md and site.config.mjs.
* **Added**: Knowledge librarian (knowledge-librarian.yaml), from its workflow.
* **Added**: Knowledge registrar (knowledge-registrar.yaml), from its workflow.
* **Added**: Knowledge release (knowledge-release.yaml), from its workflow.
* **Added**: Knowledge sync (knowledge-sync.yaml), from its workflow.
* **Added**: Knowledge website (knowledge-website.yaml), from its workflow.
* **Added**: Lint and docs (lint-and-docs.yaml), from its workflow.
* **Added**: Build and test (main.yaml), from its workflow.
* **Added**: Semantic release (semantic-release.yml), from its workflow.
* **Added**: ISO/IEC 29100:2024, from ISO Open Data's records and NOTICE.
* **Added**: The iso29100 LinkML schema, from the schema and docs/about.md.
* **Added**: The schema's adapt copy, from project.justfile and the README.
* **Added**: The example data, from tests/test_data.py and tests/data/README.md.
* **Added**: A privacy notice as a concept, from the example in tests/data/valid/.
* **Added**: ISO Open Data's records, from NOTICE, the watch and its test.
* **Added**: DPV's mapping to the standard, from the copy, NOTICE and the watch.
* **Added**: The neighbours' adapt copies, from tests/test_schema_rules.py.
* **Added**: Mappings and the SSSOM set, from the README, the tests and the schema.
* **Added**: Modelling choices, from docs/about.md and the changelog.
* **Added**: Scope, from docs/about.md and docs/index.md.
* **Added**: Check the wording against a copy of the standard, from the script and its test.
* **Added**: Move to another edition or supplement, from the watch, CONTRIBUTING.md and NOTICE.
* **Added**: Knowledge sources map, the sweep of this repository.
* **Added**: AI covenant, from AI_COVENANT.md.
* **Added**: Licence and attribution, from NOTICE and the README.
* **Added**: Security policy, from SECURITY.md.
* **Added**: Upstream watch (upstream-watch.yaml), from its workflow, the script and the test.
* **Initialization**: Scaffolded the LOKF bundle for iso29100. Real concepts to follow.
