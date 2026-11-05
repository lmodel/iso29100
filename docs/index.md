# iso29100

This project is a LinkML model of the records an organization keeps when it applies the privacy framework of ISO/IEC 29100:2024. It holds no text of the standard.

- [Schema documentation](elements/index.md), generated from the schema
- [About](about.md): how the classes fit together and what the model leaves out
- [`iso29100.yaml`](schema/iso29100.yaml): the schema

## Validating data

```bash
uv run linkml-validate -s src/iso29100/schema/iso29100.yaml -C PfPolicy policy.yaml
```

This checks a file against the JSON Schema generated from the schema. Write dates as quoted strings, as JSON carries them. Validate a file before loading it into a model in `src/iso29100/datamodel/`, since LinkML 1.12.1 generates models that check less.

No validator checks these rules:

- that a reference names a record the framework holds, of the class the reference ranges over;
- that a list never repeats an identifier;
- that a flow goes from one actor to another, and that a processor never decides what happens to PII afterwards;
- that a risk's level after controls is not above its level before;
- that an impact assessment treats or accepts only risks it found, and that the next one falls after it;
- that a breach's times run in order, and a consent is withdrawn after it was given;
- that a transfer safeguard belongs to an activity that crosses a border.

`tests/test_data.py` checks the first two within the whole example, and the rest over every example.
