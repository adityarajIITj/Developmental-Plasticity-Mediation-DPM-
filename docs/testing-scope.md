# Testing scope

Tests in this repository must state which layer they validate.

- **Build checks** establish that the code compiles with the tested toolchain.
- **Scaffold tests** validate the minimal project API.
- **Unit tests** will validate individual model operations once those operations exist.
- **Intervention tests** will check the semantics and isolation of controlled changes.
- **Scientific evaluations** will compare models under a declared experimental protocol.

These levels are not interchangeable. Passing build or unit tests does not establish that a theoretical framework is correct, that a model exhibits functional affect, or that subjective experience is present.
