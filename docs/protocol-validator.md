# Draft protocol validator

Run the structural validator from the repository root:

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate_protocol.py configs/protocol.yaml
python -m unittest discover -s tests -p 'test_protocol_validator.py' -v
```

The validator checks that the YAML is parseable, required keys and expected sections are present, numeric counts are positive integers, context identifiers are valid and non-overlapping, and metric names are non-empty and unique. Unknown top-level and nested keys are rejected where the protocol structure is currently fixed.

This tool deliberately does not decide whether episode counts, mediator levels, metrics, or context selections are scientifically appropriate. It does not execute experiments and does not replace a formal protocol review. Because the configuration remains a draft, an empty train/held-out context list is accepted; populate and freeze these lists before confirmatory evaluation.
