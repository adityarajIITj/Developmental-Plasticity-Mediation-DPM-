# Reproducibility checklist

For each future experimental result, retain:

- the source commit hash;
- the exact configuration;
- compiler and toolchain versions;
- seed and task/environment version;
- baseline version and hyperparameter selection procedure;
- commands used to run the experiment;
- raw outputs and analysis scripts;
- summary statistics and uncertainty;
- all exclusions and failed runs.

Re-running the same configuration should reproduce deterministic outputs where determinism is expected. Where hardware or parallel execution introduces variation, document the source and report variation rather than promising bitwise identity.
