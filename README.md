<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# iso29100

ISO/IEC 29100:2024 privacy framework records (LinkML)

> **Only want to ask?** Install `ktl-docent` into any agent you use, by a route from [the install page](https://w3id.org/ktl/docs/install/), and ask it about this project. It answers from the bundle and says how far each answer has been checked.
>
> **Agents:** if `.lokf/knowledge/index.md` exists, read it first. `llms.txt` says how to weigh it.

## Documentation Website

[https://lmodel.github.io/iso29100](https://lmodel.github.io/iso29100)

## What it models

The schema models the records an organization keeps when it applies the privacy framework of [ISO/IEC 29100:2024](https://www.iso.org/standard/85938.html), second edition, to the systems that handle personally identifiable information (PII). The records cover who takes part, which PII is involved and how it moves, what must be safeguarded and how, and how the organization stands against each privacy principle. It holds no text of the standard, and a few classes go beyond it as an adopter's records, which [the about page](docs/about.md) names.

ISO's licence bars giving the text to AI tools, so [src/iso29100/schema/iso-open-data/](src/iso29100/schema/iso-open-data) pins ISO Open Data's records of the edition and of the two it replaced instead. A weekly workflow opens an issue when one of those records changes or ISO lists another supplement or edition.

## Mappings

* **[Data Privacy Vocabulary (DPV)](https://w3id.org/dpv)**: `exact_mappings` and `narrow_mappings` on five classes, which are the rows DPV publishes for this edition in [upstream/dpv-iso.ttl](upstream/dpv-iso.ttl). `tests/test_upstream.py` checks each against that file, and the weekly workflow reports a change to it.

The schema is the one home for mappings. The SSSOM set is gone: it repeated those rows, and hung DPV's row for consent on a record about consent. The other mappings in the old schema had no source, so they went too.

## Repository Structure

* [docs/](docs/): the website's own pages
* [project/](project/): generated project files (do not edit them)
* [scripts/](scripts/): the upstream watch and a licence holder's check for shared words
* [src/iso29100/schema/](src/iso29100/schema): the LinkML schema (edit it) and ISO Open Data's records
* [src/iso29100/datamodel/](src/iso29100/datamodel): the generated Python datamodel
* [tests/](tests/): Python tests, with example data in [data/](tests/data) and the neighbours' adapt copies in [neighbours/](tests/neighbours)
* [upstream/](upstream/): DPV's mapping and its licence, unchanged
* [website/](website/): the Astro Starlight site built from the README, `docs/`, the schema's pages and the knowledge bundle

## Developer Tools

Run `just` to list the project's [just](https://github.com/casey/just/) recipes.

## Knowledge Trust Ladder (KTL)

`.lokf/` holds this project's [KTL](https://w3id.org/ktl/) sidecar. Its domain schema, `.lokf/iso29100.yaml`, is the copy `just lokf-adapt` writes from `src/iso29100/schema/iso29100.yaml`, and `just lokf-adapt-check` says when it is stale. Edit the source, never the copy. A release carries the copy as its schema asset.

In Obsidian, add these to the *Known LOKF types* setting of the KTL Registrar and KTL Curator plugins:

```text
PfPiiPrincipal, PfPiiController, PfPiiProcessor, PfThirdParty, PfPiiItem, PfProcessingActivity, PfSafeguardingRequirement, PfPolicy, PfControl, PfPrincipleImplementation, PfRisk, PfImpactAssessment
```

The copy drops `pf_id` for LOKF's `id`, folds `title` and `description` into LOKF's, and demotes `pf_actor_type`, since a concept's `type` already names its class. Every other key starts with `pf_`, so it shares none with a neighbour's copy, and a host can import them together.

## License

The schema and the code are under the Apache License 2.0 ([LICENSE](LICENSE)), and a knowledge bundle in [.lokf/knowledge/](.lokf/knowledge) is under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

ISO/IEC 29100 is copyright ISO and IEC, and [NOTICE](NOTICE) states this project's position. This is not an ISO project, and its use implies no endorsement by ISO or IEC.

## Contributing and security

[CONTRIBUTING.md](CONTRIBUTING.md) is the checklist for pull requests and releases, [AI_COVENANT.md](AI_COVENANT.md) sets the rules for AI-assisted work, [SECURITY.md](SECURITY.md) says how to report a vulnerability, and [CHANGELOG.md](CHANGELOG.md) records the changes.

## Credits

Built from the [linkml-project-copier](https://github.com/linkml/linkml-project-copier) template ([doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584)).
