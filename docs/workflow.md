# Workflow

This repository is designed to support an agent-first delivery loop from issue definition through review and retrospective.

## Work Intake

Prefer opening a GitHub issue before substantial work starts.

Issue templates currently cover:

- bug
- feature
- workflow or process change

Each issue should define acceptance criteria and validation expectations clearly enough that an agent can execute without guessing.

## Pull Request Flow

1. Start from an issue or written task definition.
2. Read `AGENTS.md` and the relevant docs.
3. Make the smallest complete change that satisfies the task.
4. Validate the change.
5. Open a pull request using the repository template.
6. Let automated review run.
7. Address findings or clarify why they do not apply.

## Review Routing

The repository currently distinguishes between two review classes:

- **Code review** for future `src/**` or `build.ps1` changes, routed to `cpp-pr-review`
- **Process review** for docs, workflow, template, and agent changes, routed to `process-pr-review`

Both review agents are expected to produce structured JSON with:

- `event`
- `body`
- `blocking`
- `comments`

The workflow converts that into a pull request review summary. This keeps review parsing deterministic and independently testable.

## Review Guardrails

- automated review rounds are capped
- process-only pull requests are reviewed with process criteria instead of C++ criteria
- parsing failures fall back to a blocking review rather than silently passing

## Retrospective Loop

The retrospective workflow exists to study repeated review churn and propose improvements to prompts, templates, workflows, and docs instead of treating every mistake as isolated.

Its goal is to improve the system, not just critique a single pull request.

## Current Runner Strategy

- Use standard GitHub-hosted Ubuntu runners for agent and workflow automation now.
- Add Windows build and test automation later, when the game code and `build.ps1` exist.
