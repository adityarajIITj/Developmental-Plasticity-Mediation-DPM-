# Continuous integration scope

The native workflow configures and compiles the CMake project and runs the registered CTest target. The repository-hygiene workflow checks that selected planning documents are present and non-empty.

These checks do not currently validate:

- the semantic correctness of a DPM update rule;
- the scientific validity of the planned metrics;
- the completeness of the YAML protocol;
- reproducibility of an experiment;
- any empirical or phenomenal claim.

Workflow success should be reported with the exact run link and commit SHA. A queued or skipped workflow is not a pass.
