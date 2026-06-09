# Workflow — phases as data

The spine of AItelier. A cycle moves through an ordered list of phases. The list is **not fixed** — it's `aitelier.json → workflow.phases`. Each phase is a file in `phases/` defining its intent, who runs it, and the gate it must pass.

## The phase library

| Phase | Intent | Default agent | In default set? |
|-------|--------|---------------|-----------------|
| `prepare` | Research the surface area before building | preparer | optional |
| `design` | Wireframes + UX before architecture | designer | UI only |
| `architect` | System design across modules | architect | yes (drop for ≤2 files) |
| `code` | Implement | the relevant coder(s) | yes |
| `test` | Cover happy/error/edge; no regressions | test-engineer | yes |
| `ship` | Stage → verify → release | reviewer + deploy | deploys only |

Default set: `prepare → architect → code → test`. Add `design` at the front for UI; add `ship` at the end for anything you deploy.

## Rules of the spine

- **Phases run in `aitelier.json` order.** The orchestrator iterates exactly that list.
- **A phase is done only when its gate passes** (`rules:quality-gates`). If `gates` is installed, the builder approves before the next phase starts.
- **Skip work, not gates.** Dropping `architect` is fine; skipping the test gate is not.
- **One phase, one owner.** The orchestrator delegates to the phase's agent and never writes application code itself.
- **Output lives in files**, not the conversation — `docs/` for research/architecture, the codebase for code, the repo for everything.

## Starting a cycle

Non-trivial work runs a full cycle (`prepare`…`test`). A ≤2-file change with no module-boundary impact skips the ceremony — just code + test. When in doubt, run the cycle.

Phase detail: [`phases/`](phases/). PRD scaffold for `design`/`architect`: [`prd-template.md`](prd-template.md).
