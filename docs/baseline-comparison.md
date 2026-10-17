# Baseline comparison requirements

The proposed study names four model families: persistent-state adaptive control, evaluative decoupling, a DPM-style mediator, and generic meta-learning. They are research targets, not implemented classes in the current codebase.

Before comparison, document for every baseline:

- state variables and update equations;
- trainable and fixed parameters;
- how each parameter is selected;
- information available at each time step;
- intervention access and off-target effects;
- compute, data, and tuning budgets.

A comparison is not fair merely because models share a task. Capacity and tuning differences must be reported, and the generic meta-learning baseline must be strong enough to make the test meaningful.
