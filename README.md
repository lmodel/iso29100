<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# iso29100

ISO 29100 / Privacy LinkML Schema

## License And Standards Rights

This repository's original code, schema structure, and documentation are licensed under Apache-2.0.

ISO/IEC standards text is owned by ISO. This repository does not grant rights to reproduce or redistribute ISO text through the project license. If your workflow needs normative ISO/IEC text in distributed artifacts, obtain the appropriate license from ISO.

## Documentation Website

[https://lmodel.github.io/iso29100](https://lmodel.github.io/iso29100)

## Repository Structure

* [docs/](docs/) - mkdocs-managed documentation
  * [elements/](docs/elements/) - generated schema documentation
* [examples/](examples/) - Examples of using the schema
* [project/](project/) - project files (these files are auto-generated, do not edit)
* [src/](src/) - source files (edit these)
  * [iso29100](src/iso29100)
    * [schema/](src/iso29100/schema) -- LinkML schema
      (edit this)
    * [datamodel/](src/iso29100/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests
  * [data/](tests/data) - Example data

## Developer Tools

There are several pre-defined command-recipes available.
They are written for the command runner [just](https://github.com/casey/just/). To list all pre-defined commands, run `just` or `just --list`.

## Credits

This project uses the template [linkml-project-copier](https://github.com/linkml/linkml-project-copier).
