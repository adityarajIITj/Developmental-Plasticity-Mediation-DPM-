# Results and reporting policy

The `results/` directory is reserved for generated outputs from executed experiments.

Every reported run should record:

- source commit;
- configuration file and its version;
- compiler/runtime versions where relevant;
- random seed;
- baseline and task identifiers;
- evaluation split;
- metrics and uncertainty across runs;
- failed, interrupted, or excluded runs with reasons.

Never hand-enter expected values into a result file and present them as measurements. Smoke tests, unit tests, and scientific experiments must be labelled separately. A passing scaffold test is not evidence for DPM's explanatory claims.
