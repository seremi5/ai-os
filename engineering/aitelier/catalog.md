# AItelier — module catalog

The menu `/aitelier-init` picks from. Each row is a module under [`modules/`](modules/) with a `module.yaml` manifest. "Installs" = what it drops into the target project's `.claude/` (or root). "Needs" = module dependencies.

## Spine — almost always on

| Module | Installs | Needs | Pick when |
|--------|----------|-------|-----------|
| **`workflow`** | `.claude/workflow.md` + selected `phases/*.md` | — | Always. The phase methodology: choose which phases apply. |
| **`project-profile`** | `aitelier.json` + `.claude/project-profile.md` | — | Always. The stack/commands/language/deploy config everything else reads. |

**Phases are data.** Default set: `prepare → architect → code → test`. Add `design` (front of line, UI work), add `ship` (end, deploys). Drop `architect` for ≤2-file changes. Configured in `aitelier.json → workflow.phases`.

## Agents — pick by stack

One file each under `modules/agents/`. Install only the roster a project needs.

| Module | Role | Pick when |
|--------|------|-----------|
| `agents:preparer` | Research docs/APIs before building | Unfamiliar surface area |
| `agents:architect` | System design across modules | Changes spanning >2 files |
| `agents:designer` | Figma wireframes + HIG/UX | User-facing UI |
| `agents:backend-coder` | Server/API/Core implementation | Any backend or shared-core code |
| `agents:frontend-coder` | UI implementation | Web/desktop UI |
| `agents:mobile-coder` | iOS/Android + extensions | Mobile targets |
| `agents:database-engineer` | Schema, migrations, queries | A database exists |
| `agents:test-engineer` | Test suite per phase | Always, if you test (you do) |
| `agents:reviewer` | Audit/critique a diff | Want an adversarial review pass |

> A CLI tool installs `preparer + backend-coder + test-engineer`. A SwiftUI app installs `designer + mobile-coder + test-engineer`. Skip the rest.

## Guardrails — your safety net

Toggle each hook and rule independently.

| Module | Installs | Pick when |
|--------|----------|-----------|
| `hooks:protect-secrets` | `.claude/hooks/protect-sensitive.sh` | Always |
| `hooks:lint-after-edit` | `.claude/hooks/post-edit.sh` | Project has a linter |
| `hooks:typecheck-on-done` | end-of-turn typecheck gate | Typed language |
| `rules:quality-gates` | per-phase pass/fail gates | Always |
| `rules:async-questions` | queue ambiguities, don't block | Always |
| `rules:context-management` | sub-agent return format, @-refs, compaction | Multi-agent or long sessions |
| `rules:full-stack-awareness` | cross-layer impact checklist | >1 layer (BE+FE, app+db) |
| `rules:conventions` | stack conventions (language, deps, style) | Always — rendered from `aitelier.json` |

## Power — the optional muscle

The optional muscle — file-based, take what you need.

| Module | Installs | Needs | Pick when |
|--------|----------|-------|-----------|
| **`memory`** | `.claude/memory/` (decisions, mistakes, project-facts, builder-preferences, workflows) | — | You want the project to learn across sessions. Approve-before-save. |
| **`worktrees`** | `.claude/scripts/` (new-task, sync) + worktree guide | — | You run more than one task at a time, or want isolation per task. |
| **`lifecycle`** | `.aitelier/backlog/ · tasks/ · releases/` markdown board | — | You want a tracked backlog→task→release flow without an app. |
| **`gates`** | approval-checkpoint + manual-test-checklist conventions | `lifecycle` (recommended) | You want a human sign-off at each phase. |
| **`design-system`** | `.claude/design-system.md` + Figma pointers | `agents:designer` | UI projects with a design system. |

## Presets

`/aitelier-init` offers shortcuts that pre-tick a module set:

- **`minimal`** — `workflow(code,test) + project-profile + backend-coder + test-engineer + hooks:protect-secrets + rules:quality-gates`. The weekend-CLI kit.
- **`standard`** — minimal + `architect + preparer + reviewer + all rules + lint/typecheck hooks + memory`.
- **`product`** — everything: full agent roster + all guardrails + all power modules. The serious-project kit.
- **`custom`** — tick modules yourself.
