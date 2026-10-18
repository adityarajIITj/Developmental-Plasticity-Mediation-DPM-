# Experiment data management

No empirical dataset is currently included in this repository.

For future runs:

- Keep raw run output separate from derived summaries.
- Record the source commit, configuration digest, seed, model identifier, and task identifier with each run.
- Do not commit large generated artifacts by default; document how to regenerate them and where they are archived.
- Preserve failed and interrupted runs with status labels rather than silently deleting inconvenient outcomes.
- Keep held-out evaluation labels and outcomes out of tuning workflows.
- Do not include private, licensed, or otherwise restricted data without documented authorization.
- Make analysis scripts consume saved outputs instead of manually transcribing values into tables.

A result should be traceable from a reported summary back to the configuration and raw output that produced it.
