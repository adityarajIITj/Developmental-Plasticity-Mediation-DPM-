# Model specification: TEMPLATE

Copy this document for each model variant and replace every prompt before implementation. This template is not itself a model specification.

## Purpose and claim

What restricted hypothesis does this variant represent?

## State and observations

List each state variable, its domain, initialization, observability, and update timing.

## Transition and update rules

Give complete equations, parameter domains, update order, and any stochasticity.

## Actions and environment

Specify action space, policy, environment feedback, and what information is available to the model.

## Intervention semantics

Define the intervention target, timing, allowed values, direct effects, and checks for off-target paths.

## Parameters and matching

List trainable parameters, initialization, tuning procedure, capacity measure, and compute/data budget.

## Predictions and failure criteria

State discriminating predictions, expected failure cases, and what result would weaken the model's claim.

## Verification

List unit tests, invariants, and reproducibility checks required before evaluation.
