# Build And Runner Notes

## Intended Product Build

The future application build entry point should be a simple `build.ps1` script that invokes `cl.exe` over the project source files.

That build script does not exist yet because this bootstrap commit intentionally contains no gameplay or platform code.

## Current Automation

The repository currently includes:

- `copilot-setup-steps.yml` to prepare the Copilot cloud-agent environment
- `assign-next-issue.yml` to assign the next eligible open issue to Copilot when no pull request is open
- `pr-review.yml` to run automated pull request review
- `retrospective.yml` to analyze high-churn pull requests
- `validate-pr-review.yml` to test PR review parsing and routing logic offline

## Runner Strategy

For the bootstrap phase:

- review and process automation run on standard GitHub-hosted Ubuntu runners
- no Windows build workflow is present yet

This split is intentional. The repository needs live automation now, but the game-specific Windows build and test path should only be added once there is actual source code and a real `build.ps1` entry point to validate.

## Future Windows Build Expectations

When code exists, the Windows build path should:

- run on a Windows runner
- configure the MSVC toolchain
- invoke `build.ps1`
- run the application's test mode

## Secrets And Auth

The review and retrospective workflows expect a fine-grained personal access token stored as either:

- `COPILOT_REVIEW_TOKEN`
- `PERSONAL_ACCESS_TOKEN`

That token must belong to a GitHub user with Copilot access and include the **Copilot Requests** permission.

The issue-assignment workflow expects a user token stored as either:

- `COPILOT_ASSIGN_TOKEN`
- `PERSONAL_ACCESS_TOKEN`

For a fine-grained personal access token, GitHub's documented minimum is:

- metadata: read
- actions: read/write
- contents: read/write
- issues: read/write
- pull requests: read/write

The assignment workflow is currently intended for manual dispatch. The cron trigger is scaffolded but intentionally disabled.
