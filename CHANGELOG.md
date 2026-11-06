# Changelog

All notable changes to this project are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The `v0.0.0` tag is a baseline, not a release: it marks where versioning starts so the first real release is `0.1.0` rather than `1.0.0`. The schema stays below 1.0.0 until its shape settles, so a breaking change is a minor release.

## [Unreleased]

### Changed

- **The bundle's schema files sit in `.lokf/schema/`**: `lokf.yaml` and the `lokf adapt` copy `iso29100.yaml`, as KTL v0.62.0 lays them out.

## [0.1.0] - 2026-11-05

### Added

- **ISO Open Data's records** of the edition and of the two it replaced, and **DPV's mapping** to the standard, with a weekly watch. It reads only https addresses on a list of hosts and caps what it reads.
- **`PfPrinciple`**, which holds the privacy principles by subclause number, with titles of this project's own, and **`PfPiiRecognition`**, the ways information turns out to be PII.
- **`.lokf/iso29100.yaml`, the schema's `lokf adapt` copy.** The knowledge release attaches it as `schema-<tag>-iso29100.yaml`.
- **The Knowledge Trust Ladder (KTL) sidecar**, from the KTL v0.61.0 templates with the lokf floor at 0.9.0, and a knowledge website that replaces the mkdocs site.
- **The governance files**: SECURITY.md, AI_COVENANT.md and the CONTRIBUTING checklist.
- **`scripts/check_overlap.py`**, for a licence holder to test this repository's words and numbers against their own copy.

### Changed

- **The schema is rewritten.** Classes and enums take the `Pf` prefix and slots the `pf_` prefix, every record has a `pf_id`, a reference holds one, and an actor states its kind. Every title and description is this project's own.
- **Mappings.** The only ones left are the five rows DPV publishes for this edition. `PfPiiItem` maps to `dpv:PersonalData` by `narrow_mappings`, the direction DPV's Turtle states.
- **The template settings** turn PyPI publishing and the docs preview off, linkml and linkml-runtime are locked at 1.12.1, the Python project is named `iso29100-linkml`, and the generators' settings move to `.linkml/generators.yaml`.

### Removed

- **The SSSOM set**, whose rows the schema now holds, and every mapping and clause number that no source supports.
- **The subsets, and the annotations that named a maintainer's address and repeated NOTICE.**
- **The mkdocs site**, with redirects from its addresses to the new site.
