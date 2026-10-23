# Draft protocol validator

Run the structural validator from the repository root:

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate_protocol.py configs/protocol.yaml
python -m unittest discover -s tests -p 'test_protocol_validator.py' -v
```

The validator checks that the YAML is parseable, required keys and expected sections are present, numeric counts are positive integers, context identifiers are valid and non-overlapping, and metric names are non-empty and unique. Unknown top-level and nested keys are rejected where the protocol structure is currently fixed.

This tool deliberately does not decide whether episode counts, mediator levels, metrics, or context selections are scientifically appropriate. It does not execute experiments and does not replace a formal protocol review. Because the configuration remains a draft, an empty train/held-out context list is accepted; populate and freeze these lists before confirmatory evaluation.


## Additional safeguards

The validator also rejects duplicate YAML mapping keys, unknown top-level keys, unexpected keys in fixed protocol sections, duplicate context IDs within a split, null/non-scalar mediator levels, and repeated mediator values. These checks help catch common authoring mistakes that permissive YAML parsing can otherwise hide.

The regression suite exercises both accepted and rejected inputs. A rejection test passing means the validator correctly rejected that particular invalid fixture; it does not show that the entire protocol is ready for confirmatory use.
