# Project profile

> Generated at init, kept current as the codebase evolves. The first thing every agent reads. Human-readable; the machine-readable twin is `aitelier.json` at the root.

Two files describe the project:

- **`aitelier.json`** (root) — the manifest: stack, commands, language, deploy, installed modules. Machine-read by hooks, gates, and the orchestrator. Schema: AItelier `init/manifest.md`.
- **`.claude/project-profile.md`** (this file, per project) — the prose profile: what the project *is*, its conventions, and where things live. Read by humans and agents for orientation.

## What this file should contain

Keep it under ~400 words. Sections:

### Overview
One paragraph: what the product does, for whom, the one non-negotiable principle (e.g. "runs on-device, zero network on the default path").

### Stack & layers
Mirror `aitelier.json → project.stack` / `layers`, with the one-line "why" behind each major choice.

### Conventions (the load-bearing ones)
The rules an agent must not violate — the seams, the boundaries, the "always / never". Point to `.claude/rules/conventions.md` for the rendered detail; here, capture the project-specific invariants (e.g. "all transcript transforms are pipeline stages, never branches in the view model").

### Where things live
A short map: which folder holds what, which targets share source, where tests sit.

### What's locked
One-way doors. Decisions not to relitigate.

## Discipline

- Update this when an architectural fact changes — a stale profile misleads every agent.
- Facts that change often (status, open phases) belong in the `lifecycle` board or git, not here.
- If it passes ~400 words, move detail into `docs/` and link it.
