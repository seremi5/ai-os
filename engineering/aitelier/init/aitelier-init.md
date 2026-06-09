---
description: Set up AItelier in this project — pick modules, write aitelier.json, render .claude/
---

# /aitelier-init — the setup wizard

You are installing **AItelier** into the current project. AItelier lives at
`~/GitHub/sr-os/engineering/aitelier` (the source of truth for modules). Follow this runbook.

## 1. Detect

Read what you can without asking:
- Stack: from `package.json`, `pyproject.toml`, `Package.swift`, `go.mod`, `Cargo.toml`, etc.
- Test / lint / typecheck / build commands: from scripts in those files.
- Layers present: backend? frontend? database? mobile?
- Whether a `.git` repo exists and the base branch.

Summarise what you detected in one short block.

## 2. Ask (one round, queue nothing critical)

Ask the builder, defaulting to your detection:

1. **Preset?** `minimal` / `standard` / `product` / `custom` (see [`../catalog.md`](../catalog.md)).
2. **Phases?** confirm `prepare→architect→code→test`; offer `+design` (UI) and `+ship` (deploys); offer to drop `architect`.
3. **Agents?** confirm the roster implied by the stack (e.g. SwiftUI → designer + mobile-coder + test-engineer).
4. **Power modules?** memory / worktrees / lifecycle / gates / design-system — which apply.
5. **Language** for user-facing text (default `en-GB`), and **deploy** target if any.

If they chose a preset, only ask about deviations.

## 3. Write `aitelier.json`

At the project root, write the manifest (schema in [`manifest.md`](manifest.md)). Example:

```json
{
  "aitelier": { "version": "1.0", "rendered_at": "<ISO8601>" },
  "project": {
    "name": "shoutit",
    "stack": "Swift 6 / SwiftUI",
    "layers": ["core", "macos", "ios"],
    "commands": { "build": "swift build", "test": "./run-tests.sh", "lint": "", "typecheck": "swift build" },
    "language": "en-GB",
    "deploy": null
  },
  "workflow": { "phases": ["prepare", "design", "architect", "code", "test"] },
  "modules": [
    "workflow", "project-profile",
    "agents:preparer", "agents:designer", "agents:architect", "agents:mobile-coder", "agents:test-engineer",
    "hooks:protect-secrets", "hooks:lint-after-edit",
    "rules:quality-gates", "rules:async-questions", "rules:context-management", "rules:conventions",
    "memory", "worktrees", "lifecycle", "gates"
  ]
}
```

## 4. Render `.claude/`

For each selected module, copy its files from `aitelier/modules/<…>` into the project's `.claude/` per the module's `module.yaml → installs`. Specifically:

- **Agents** → `.claude/agents/<name>.md` (only the chosen roster).
- **Hooks** → `.claude/hooks/*.sh` (+ wire them in `.claude/settings.json` from `aitelier.json → project.commands`).
- **Rules** → `.claude/rules/*.md`. Render `conventions.md` from `aitelier.json` (language, deps policy, style).
- **Power modules** → their target paths (memory → `.claude/memory/`, lifecycle → `.aitelier/`, scripts → `.claude/scripts/`).
- **CLAUDE.md** → render [`../templates/CLAUDE.md.template`](../templates/CLAUDE.md.template), filling `{{project.*}}`, the active phases, the installed agents, and the active rules. This is the project's orchestrator.

Resolve `module.yaml → requires` first (e.g. `gates` pulls `lifecycle`); warn on any missing dependency and offer to add it.

## 5. Verify + report

- Confirm `aitelier.json` is valid and `.claude/` contains only the selected modules.
- Print: the chosen preset, the module list, and the next command (usually `/<workflow>-start` or just "describe the first task").
- Tell the builder to **restart Claude Code** so hooks register.

## Updating later

- Add a module: append to `aitelier.json → modules`, re-run the render step for that module only.
- Change a command (test/lint): edit `aitelier.json → project.commands`, re-render hooks + CLAUDE.md.
- Never hand-edit generated `.claude/` files that a module owns; edit `aitelier.json` and re-render.
