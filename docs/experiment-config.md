# Experiment configuration conventions

The draft configuration lives at `configs/protocol.yaml`.

## Rules

- Treat values as proposals until the model equations and matching protocol are fixed.
- Record the random seed and all task, model, intervention, and evaluation parameters.
- Keep training contexts separate from held-out evaluation contexts.
- Do not tune on held-out outcomes.
- Replace symbolic intervention labels with explicitly defined values and units before execution.
- Version configuration changes alongside the code that consumes them.

The current YAML file is a planning document; no experiment runner consumes it yet. The listed episode counts and metrics are not preregistered or scientifically justified by their presence in the file.
