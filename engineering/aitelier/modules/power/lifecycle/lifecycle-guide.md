# Lifecycle board

The project's work, as plain markdown. Readable on GitHub, no app needed.

```
.aitelier/
├── backlog/    bli-*.md     ← ideas/requests, not yet started
├── tasks/      <task>/      ← active work: task.md (+ state)
└── releases/   YYYY-MM-DD-*.md  ← shipped, with what changed
```

## The flow

1. **Backlog item** (`backlog/bli-<slug>.md`) — a one-screen description of a want. Cheap to add, cheap to drop.
2. **Promote to task** — when picked up, copy the item into `tasks/<slug>/task.md`, fill the plan, and (if `worktrees` is installed) `new-task.sh <slug>`.
3. **Work the phases** — the task moves through `aitelier.json → workflow.phases`. If `gates` is installed, each phase boundary needs the builder's approval.
4. **Release** — when it ships, write `releases/YYYY-MM-DD-<slug>.md`: what changed, what to test, any migration. Remove the worktree.

## Rules

- **One active task per worktree.** The backlog can be long; in-flight should be short.
- **The task file is the source of truth for *this* task** — not the conversation. Update it as you go.
- **Done means released.** A task isn't done at "code complete"; it's done when there's a release note and it's on the base branch.
- Templates live in `.aitelier/.templates/` (`backlog-item.md`, `task.md`, `release.md`).
