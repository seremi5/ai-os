# `aitelier.json` — the project manifest

One file at the project root. It is the single source of truth: which modules are installed, and the stack values every module reads. Generated `.claude/` files are derived from it — edit this and re-render, don't hand-edit the outputs.

## Schema

```jsonc
{
  "aitelier": {
    "version": "1.0",
    "rendered_at": "ISO8601"        // last time .claude/ was rendered from this file
  },

  "project": {
    "name": "string",
    "stack": "string",              // human label, e.g. "Swift 6 / SwiftUI"
    "layers": ["core","macos","ios","backend","frontend","database"],  // subset present
    "commands": {                    // empty string = gate skipped
      "build": "string",
      "test": "string",
      "lint": "string",
      "typecheck": "string"
    },
    "language": "en-GB",             // user-facing text register
    "deploy": null                   // or { "branch_strategy": "staging→main", "host": "…" }
  },

  "workflow": {
    "phases": ["prepare","design","architect","code","test","ship"]  // the active subset, in order
  },

  "modules": [
    "workflow",
    "project-profile",
    "agents:architect", "agents:backend-coder", "agents:test-engineer",
    "hooks:protect-secrets", "hooks:lint-after-edit", "hooks:typecheck-on-done",
    "rules:quality-gates", "rules:async-questions", "rules:conventions",
    "memory", "worktrees", "lifecycle", "gates", "design-system"
  ]
}
```

## Rules

- **Module ids** match folder/manifest ids in [`../catalog.md`](../catalog.md). Grouped modules use `group:id` (`agents:architect`, `hooks:lint-after-edit`, `rules:quality-gates`). Standalone modules use the bare id (`workflow`, `memory`, `worktrees`).
- **`requires`** in a module's `module.yaml` are auto-resolved at render: listing `gates` implies `lifecycle`.
- **`commands`** drive both the guardrail hooks and the quality-gate rule. An empty string skips that gate (e.g. no `lint` → no lint gate).
- **`language`** flows into `rules:conventions` and every agent's user-facing-text instruction.
- **`workflow.phases`** is the spine's contract: the orchestrator and gates iterate exactly this list, in this order.

## Minimal valid example

```json
{
  "aitelier": { "version": "1.0", "rendered_at": "2026-06-09T00:00:00Z" },
  "project": {
    "name": "my-cli", "stack": "Python 3.12", "layers": ["backend"],
    "commands": { "build": "", "test": "pytest", "lint": "ruff check", "typecheck": "mypy ." },
    "language": "en-GB", "deploy": null
  },
  "workflow": { "phases": ["code", "test"] },
  "modules": ["workflow","project-profile","agents:backend-coder","agents:test-engineer","hooks:protect-secrets","rules:quality-gates"]
}
```
