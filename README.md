# CopilotCheckers

CopilotCheckers is a Windows-only checkers project being built with an **agent-first workflow**. This repository is intentionally bootstrapped with process, review, and retrospective automation before gameplay code exists so the delivery system is in place before the codebase grows.

## Product Direction

- Native Windows application
- 2D software rendering via the Windows API
- Local two-player mouse interaction on one machine
- Click-and-drag piece movement
- Game restart after a winner is decided

## Engineering Constraints

- C++
- Prefer C-style module boundaries and plain structs
- No object-oriented architecture as the primary structure
- No third-party libraries
- Avoid the C standard library where practical
- No runtime dynamic allocation; reserve memory up front and split it into system arenas
- Testing lives inside the application through a dedicated test mode

## Agent-First Workflow

Start with these files:

1. `AGENTS.md`
2. `.github/copilot-instructions.md`
3. `docs/requirements.md`
4. `docs/architecture.md`
5. `docs/testing.md`
6. `docs/workflow.md`
7. `docs/build-and-runner.md`

The repository is organized so agents can discover constraints mechanically:

- issue templates define the task shapes
- docs define the contract
- pull request review automation checks changes against those contracts
- retrospective automation analyzes churn and proposes system improvements

## Current State

- Workflow bootstrap complete
- Documentation baseline complete
- Issue and pull request templates complete
- Copilot-driven review and retrospective workflows scaffolded
- No gameplay or platform code yet
