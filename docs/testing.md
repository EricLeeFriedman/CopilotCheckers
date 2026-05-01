# Testing

Testing is a first-class part of the application rather than a separate harness executable.

## Testing Model

- The future executable must support a dedicated test mode.
- Tests run inside the application process.
- Subsystems should own their own tests in dedicated `*_tests.cpp` files once code exists.
- A central `RunTests()` entry point should orchestrate subsystem test execution.

## Test Expectations

- Each new behavior should have a named test that proves that behavior.
- Tests should be deterministic and avoid hidden external dependencies.
- Failure paths matter: init failure, shutdown behavior, and memory exhaustion paths should be considered part of coverage.
- When gameplay branches by player or color, tests should explicitly cover both sides.

## Validation Layers

- in-application automated test mode
- manual interaction checks for mouse behavior and restart flow
- repository automation for workflow validation and review routing

## Current State

There is no game code yet, so current automated validation focuses on repository workflow logic instead of application behavior.
