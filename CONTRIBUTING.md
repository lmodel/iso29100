# Contributing to iso29100

*This file is a checklist, not a design log. Each rule is a line or two that links to where its reasoning lives: a code comment, a workflow header, or a linked page. `lint-and-docs.yaml` holds the file to a word budget so it stays that way.*

## What this project is

A LinkML schema of the records an organization keeps when it applies the privacy framework of ISO/IEC 29100:2024. It holds no text of the standard, which is ISO's copyright.

| Path | Holds |
| --- | --- |
| `src/iso29100/schema/iso29100.yaml` | The LinkML schema. Edit this. |
| `src/iso29100/schema/iso-open-data/` | ISO Open Data's records of the standard. Never edit. |
| `upstream/` | DPV's mapping to the standard and its licence, as published. Never edit. |
| `src/iso29100/datamodel/`, `project/`, `docs/schema/` | Artefacts generated from the schema. |
| `scripts/` | The weekly watch and a licence holder's check for shared words. |
| `docs/` | The website's own pages. |
| `tests/` | Python tests, valid and invalid example data, and the neighbours' released copies. |
| `.lokf/knowledge/` | This repository's knowledge bundle. |

## Development setup

You need Python 3.10+, [uv](https://docs.astral.sh/uv/) and [just](https://github.com/casey/just).

```bash
git clone https://github.com/lmodel/iso29100.git
cd iso29100
uv sync --group dev
just --list
```

### Agent skills (optional, only for this repo's `.lokf/` bundle)

The bundle is maintained with the Knowledge Trust Ladder (KTL) skills, **installed, never committed**. Continuous integration (CI) installs the librarian skill at run time, pinned to a release. Nothing in the schema depends on them. [The install page](https://w3id.org/ktl/docs/install/) lists every route. With npm:

```bash
npx skills add noelmcloughlin/knowledge-trust-ladder --skill ktl-librarian --yes   # derive concepts
npx skills add noelmcloughlin/knowledge-trust-ladder --skill ktl-curator --yes     # confirm them as a person
```

## Before opening a pull request

- **Quote nothing from the standard.** Name the clause by number, in your own words, everywhere. [AI_COVENANT.md](AI_COVENANT.md) says why.
- **Edit the schema, then regenerate.** Edit `src/iso29100/schema/iso29100.yaml`, run `just gen-project`, `just gen-doc` and `just lokf-adapt`, and commit the output. `project/`, `src/iso29100/datamodel/`, `docs/schema/` and `.lokf/schema/iso29100.yaml` are generated.
- **Leave `src/iso29100/schema/iso-open-data/` as ISO published it.** Replace it whole from one day's dataset, and move the pins in `scripts/check_upstream_release.py` and the schema header.
- **Map only what a source states, and keep names apart.** A mapping rests on a file this repository pins, such as DPV's in `upstream/dpv-iso.ttl`, with that file's predicate. A term with no sure match stays unmapped. A host imports the adapt copy beside the Linked Open Knowledge Format (LOKF) schema and those copies, so it shares no name with them. `tests/test_upstream.py` and `tests/test_schema_rules.py` check them.
- **Run the tests**: `just test`. Example data goes in `tests/data/valid/` and `tests/data/invalid/`, named `ClassName-suffix.yaml`, with an invalid example per constraint whose first line names where it fails.
- **Follow the schema's conventions**: classes and enums with the `Pf` prefix, snake_case slots with the `pf_` prefix and snake_case values, attributes unless two classes share a field, references by `pf_id`. `just lint` checks, under `.linkmllint.yaml`.
- **Run the pre-commit hooks** on what you staged (`uvx pre-commit run`): ruff, yamllint, codespell, typos and the `uv.lock` check.
- **Commit lock files with the change**, because CI installs with `uv sync --locked`.
- **Knowledge-bundle changes**: `cd .lokf && just lokf-validate` must pass.
- **`lint-and-docs.yaml` is easy to trip locally**: ShellCheck, actionlint, markdownlint against `.markdownlint-cli2.jsonc`, link-checking against `lychee.toml`, and codespell over every `*.md`.
- **Actions are pinned to commit hashes**, the version in a trailing comment, and bumped by Dependabot, never by hand to a tag.
- **The skills pin moves with the sidecar copies.** When moving `TRUST_LADDER_SKILLS_REF` in `.github/workflows/knowledge-librarian.yaml`, copy the other `knowledge-*.yaml` workflows and `.lokf/scripts/` and `.lokf/m365/` from that release's `skills/ktl-sidecar/templates/` in the same pull request.
- **If your change alters behaviour**, add an entry under `## [Unreleased]` in [CHANGELOG.md](CHANGELOG.md).

## Code of conduct

Participation here is covered by the [Contributor Covenant](CODE_OF_CONDUCT.md).

## Using AI tools

Artificial intelligence (AI) assistance is welcome, and [AI_COVENANT.md](AI_COVENANT.md) sets the rules, for people and the scheduled `knowledge-librarian` agent alike. You are the author of what you submit.

## Reporting issues

Use the [issue tracker](https://github.com/lmodel/iso29100/issues) for problems with the schema and requests for new elements. A problem in the standard itself belongs with ISO/IEC JTC 1/SC 27, through your national standards body.

## Releasing (maintainers)

- Write `## [Unreleased]` in [CHANGELOG.md](CHANGELOG.md) as you go. The release job refuses an empty one (`.github/scripts/changelog-release.mjs check`).
- Type the commit ([Conventional Commits](https://www.conventionalcommits.org/)) for what the change *is*. Only `feat:`, `fix:`, `security:` and a breaking `!` start a release. Other types leave their entries for the next release that does. A pull request that would release must carry a releasing type in its title too, since a squash merge takes its subject from it.
- On merge, [`semantic-release.yml`](.github/workflows/semantic-release.yml) retitles the section to `## [X.Y.Z] - YYYY-MM-DD`, commits `CHANGELOG.md`, tags `vX.Y.Z` and publishes the GitHub Release. No file is bumped. Once `KNOWLEDGE_RELEASE_ENABLED` is `true`, it dispatches `.github/workflows/knowledge-release.yaml`, which attaches the schema copy and the bundle when the bundle or the schema changed.
- That step runs behind the `release` GitHub Environment. Configure required reviewers on it in Settings → Environments, or every qualifying merge is released unattended.
- Below 1.0.0: push the `v0.0.0` baseline tag on `main` before the first releasing merge, which then releases 0.1.0. Both release jobs refuse to run without a `v*` tag. `.releaserc.json` maps `breaking: true` to `minor`, and reaching 1.0.0 means removing that rule in a pull request of its own.
- A branch rule requiring pull requests, status checks or signed commits would reject the release job's own push to `main`, so leave them off. [SECURITY.md](SECURITY.md) says what holds `main` instead, and the shared design is on [KTL's releasing page](https://github.com/noelmcloughlin/knowledge-trust-ladder/blob/main/docs/releasing.md).

## License

By contributing, you agree that your contributions are licensed under the [Apache License 2.0](LICENSE). ISO Open Data's records are under their own terms. [NOTICE](NOTICE) lists them: update it when you add something new from elsewhere.
