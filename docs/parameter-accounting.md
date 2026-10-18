# Parameter accounting requirements

A parameter-count comparison is meaningful only if counting conventions are consistent.

For each model, report:

- trainable scalar parameters;
- fixed but model-specific constants;
- shared parameters and whether they are counted once or per component;
- state dimensions that are not trainable parameters;
- hyperparameters selected through tuning;
- any external learned components or pretrained models.

Parameter count alone is not a complete measure of complexity. Report tuning budget, compute, and information access alongside it, and explain the chosen complexity measure before evaluation.
