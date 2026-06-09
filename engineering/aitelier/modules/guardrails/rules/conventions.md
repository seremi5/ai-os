# Conventions

> **Rendered at init from `aitelier.json`.** The `{{…}}` placeholders are filled per project. This is the single rule that carries stack-specific law; agents read it on every task.

## Language & register

- All user-facing text is **{{project.language}}** (default `en-GB` — "recognise", "colour").
- Error messages shown to people are human-readable, never internal codes.

## Stack

- This is a **{{project.stack}}** project. Layers present: {{project.layers}}.
- Match the idioms already in the codebase — the surrounding file's style wins over any general preference.

## Commands (run after non-trivial changes)

| Gate | Command |
|------|---------|
| Build | `{{project.commands.build}}` |
| Test | `{{project.commands.test}}` |
| Lint | `{{project.commands.lint}}` |
| Typecheck | `{{project.commands.typecheck}}` |

An empty command means that gate is skipped for this project.

## Dependencies

- **In-house preference.** No new dependency without a one-line rationale and the builder's nod.
- Before adding one, ask: "Can this be ~50 lines of our own code?"
- Forbidden without explicit approval: anything that widens network/permission scope, unclear-licence packages, or a dependency that breaks an established boundary.

## Code style

- Comments explain *why* (hidden constraints, workarounds), not *what* — names carry the *what*.
- Keep new behaviour in the project's established seam, not a one-off branch.
- Never commit secrets, `.env`, or keys.

## Project invariants

> Filled at init / maintained in `.claude/project-profile.md`. The "always / never" specific to this codebase — the boundaries an agent must not cross.

- _e.g. "all transcript transforms are pipeline stages, never branches in the view model"._
