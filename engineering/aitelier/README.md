# AItelier

> The workshop where AI builds software — with the AI built into the name. SR-OS's engineering layer.

A composable, file-based framework for AI-assisted software development. You don't install a fixed bundle — you **pick the modules a project needs** at setup, and AItelier assembles a project-local `.claude/` from them, parametrised by one `aitelier.json`.

It grew out of [PACT](../pact/) (the Prepare→Architect→Code→Test methodology) and adds the capabilities a serious build wants — typed project memory, per-task worktrees, a backlog→release lifecycle, approval gates — while staying **yours**: plain markdown and shell, no desktop app, no vendor, no telemetry, no network. Same ethos as SR-OS and Shoutit.

## The idea in one line

> PACT was all-or-nothing. AItelier is à la carte, file-based, and yours — pick only the parts a project needs.

---

## Use it on a **brand-new** project

```bash
# 1. create the project and a git repo
mkdir my-app && cd my-app && git init

# 2. open Claude Code and run the setup
claude
```
Then tell Claude:
> **Set up AItelier in this project. Follow `~/GitHub/sr-os/engineering/aitelier/init/aitelier-init.md`.**

The wizard asks five things (with sensible defaults):

1. **Preset** — `minimal` (weekend CLI) · `standard` · `product` (everything) · `custom`.
2. **Phases** — confirm `prepare→architect→code→test`; add `design` (UI) or `ship` (deploys).
3. **Agents** — the roster for your stack (a SwiftUI app picks designer + mobile-coder + test-engineer).
4. **Power modules** — memory · worktrees · lifecycle · gates · design-system.
5. **Language** (default `en-GB`) and **deploy** target, if any.

It writes **`aitelier.json`** (your profile + chosen modules) and renders **`.claude/`** (the orchestrator + only what you picked) — plus **`.aitelier/`** if you took `lifecycle`. **Restart Claude Code** so hooks register, then describe your first task.

## Use it on an **existing** project

```bash
# 1. open the existing repo in Claude Code
cd ~/code/my-existing-app && claude
```
Then tell Claude:
> **Set up AItelier in this project. Follow `~/GitHub/sr-os/engineering/aitelier/init/aitelier-init.md`.**

The wizard **auto-detects** your stack and your build/test/lint/typecheck commands from `package.json` / `pyproject.toml` / `Package.swift` / `go.mod`, proposes a fitting module set, and you confirm or adjust. It then writes `aitelier.json` and renders `.claude/` **without touching your code**. If the repo already has a `.claude/`, it backs that up first and merges. **Restart Claude Code**, then carry on — now with the agents, gates, and memory you chose.

> Prefer typing `/aitelier-init` instead of pasting the runbook path? Wire it once as a command — see [Make it a command](#make-it-a-command).

---

## What setup actually does

`init` is a runbook ([`init/aitelier-init.md`](init/aitelier-init.md)) Claude follows:

1. **Detect** the stack and commands (existing projects) or ask (new ones).
2. **Write `aitelier.json`** — the one source of truth ([schema](init/manifest.md)): project profile + the module list.
3. **Render `.claude/`** — copy each chosen module's files to their targets, wire hooks in `settings.json`, and render `CLAUDE.md` (the orchestrator) and `conventions.md` from your `aitelier.json` values.

Nothing is hidden in a binary; every output is readable markdown/shell you can inspect and edit.

## The module groups

| Group | Modules | Almost always on? |
|-------|---------|-------------------|
| **Spine** | `workflow` (phases as data), `project-profile` | Yes |
| **Agents** | preparer, architect, designer, backend/frontend/mobile coder, test-engineer, reviewer, db | Pick by stack |
| **Guardrails** | hooks (secrets, lint, typecheck) · rules (quality-gates, conventions, …) | Pick your safety net |
| **Power** | `memory`, `worktrees`, `lifecycle`, `gates`, `design-system` | Optional |

Full menu with what each installs: [`catalog.md`](catalog.md). Each module is a folder under [`modules/`](modules/) with a `module.yaml` manifest declaring its files and dependencies.

## Change your setup later

`aitelier.json` is the source of truth — edit it and re-render, never hand-edit generated files a module owns.

- **Add a module:** append it to `aitelier.json → modules`, re-run the render for that module.
- **Change a command** (test/lint/build): edit `aitelier.json → project.commands`, re-render hooks + `CLAUDE.md`.
- **Add/drop a phase:** edit `aitelier.json → workflow.phases`.

## What AItelier deliberately is *not*

- **Not an app.** No UI, no runtime, no background process. Files Claude Code reads.
- **Not a vendor.** No account, no analytics, no feature flags, no phone-home.
- **Not all-or-nothing.** Every module is optional except the spine.
- **Not stack-locked.** Stack details live in `aitelier.json`; agents say "follow the conventions in CLAUDE.md", not "write Express".

## Make it a command

To type `/aitelier-init` in any project instead of pasting the runbook path, add a thin command that points at the runbook:

```bash
# one-time, global
mkdir -p ~/.claude/commands
printf '%s\n' 'Follow the AItelier setup runbook at ~/GitHub/sr-os/engineering/aitelier/init/aitelier-init.md for the current project.' \
  > ~/.claude/commands/aitelier-init.md
```

Then `/aitelier-init` works anywhere.

## Layout

```
aitelier/
├── README.md            # this file — how to use it
├── catalog.md           # the full module menu
├── init/
│   ├── aitelier-init.md # the setup runbook
│   └── manifest.md      # the aitelier.json schema
├── templates/
│   └── CLAUDE.md.template   # orchestrator, rendered at setup from your choices
└── modules/
    ├── spine/        workflow/ · project-profile/
    ├── agents/       architect.md · *-coder.md · test-engineer.md · reviewer.md · …
    ├── guardrails/   hooks/ · rules/
    └── power/        memory/ · worktrees/ · lifecycle/ · gates/ · design-system/
```

## Status

v1 — full module catalog. Opinionated, not authoritative; bend it per project through `aitelier.json`. Set up on any repo with the runbook above.
