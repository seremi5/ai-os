# Phase · Test

**Intent:** prove the change works and broke nothing.

**Owner:** `test-engineer`.

**Do:**
- Run the full suite (`project.commands.test`). Zero regressions.
- New tests cover happy path, error path, and realistic edge cases.
- Use the project's test framework and isolation style (fakes over loose stubs).
- Write the manual-test steps for the builder (feeds `gates` if installed).

**Gate (exit):** all tests pass; new coverage in place; manual-test checklist written. Never mark complete with a failing test.
