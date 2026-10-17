# Intervention design notes

The proposed mediator clamp is intended to test whether changing the mediator changes the effect of later evidence on learned significance.

Before implementation, define:

1. The mediator variable and its allowed values.
2. The time at which the clamp is applied and released.
3. Which state transitions are directly modified by the intervention.
4. Which other variables are held fixed or measured.
5. How evidence sequences and initial states are paired across conditions.
6. Checks for unintended paths from the intervention to the outcome.

A difference between two trajectories alone is insufficient to establish the intended causal claim if the intervention also changes unrelated state or information access.
