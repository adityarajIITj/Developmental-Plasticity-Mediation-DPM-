# Native core API contract

The current public header is `src/dpm/core.hpp`.

## Current contract

`dpm::CoreScaffold::project_name()` returns a stable, compile-time string identifying the project. It is a scaffold marker, not a model interface.

## Deliberately not specified yet

The API does not define:

- a DPM state representation;
- belief or significance update rules;
- mediator update or intervention semantics;
- environment transitions or action selection;
- serialization, experiment logging, or random-number policy.

These omissions are intentional. The interface should expand only after the model semantics and experiment protocol are specified, so the API does not silently commit the research to arbitrary dynamics.
