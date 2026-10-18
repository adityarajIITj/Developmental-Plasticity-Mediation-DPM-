# Protocol configuration review

Before treating a configuration as executable or confirmatory, check:

- [ ] Every key is consumed by a versioned runner.
- [ ] Types, ranges, defaults, and units are defined.
- [ ] Train and held-out context sets are explicit and disjoint.
- [ ] Intervention values and timing are numeric or otherwise operationally defined.
- [ ] Seeds and replicate counts are specified.
- [ ] Metrics have precise estimators and aggregation rules.
- [ ] Model capacity and tuning budgets are documented.
- [ ] Configuration validation fails on unknown or missing required keys.
- [ ] The configuration is frozen before confirmatory evaluation.

The current `configs/protocol.yaml` is a draft planning file and does not yet satisfy all items.
