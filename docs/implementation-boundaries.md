# Implementation boundaries

The current native library exposes only a project-identification scaffold. The repository does not yet implement model state, learning, action selection, mediator interventions, or an experiment runner.

Future additions should be classified explicitly:

- **Infrastructure:** build, configuration, logging, reproducibility, and testing utilities.
- **Model implementation:** executable state transitions and update rules derived from a written specification.
- **Evaluation:** task execution, intervention procedures, metrics, and comparison logic.
- **Analysis:** aggregation, uncertainty estimation, plots, and reporting.

Infrastructure can improve research quality, but it must not be described as evidence that the model or its theory has been validated.
