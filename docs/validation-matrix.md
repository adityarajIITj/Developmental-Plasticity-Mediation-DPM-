# Protocol validator test matrix

The automated tests in `tests/test_protocol_validator.py` cover these structural cases.

| Case | Expected outcome |
|---|---|
| Current draft configuration | Accept |
| Train/held-out context overlap | Reject |
| Non-positive episode count | Reject |
| Unknown top-level key | Reject |
| Malformed YAML | Reject |
| Boolean value used as seed | Reject |
| Duplicate metric name | Reject |
| Duplicate context ID within one split | Reject |
| Duplicate YAML mapping key | Reject |
| Null mediator intervention level | Reject |
| Misspelled nested episode key | Reject |
| Repeated mediator intervention level | Reject |
| Empty metric list | Reject |
| Non-string protocol note | Reject |

This matrix describes structural regression coverage, not a scientific validation checklist. It should be updated alongside tests when the protocol schema intentionally changes.
