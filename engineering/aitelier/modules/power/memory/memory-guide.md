# Project memory

> What this project has learned, kept across sessions. Read every file here at the start of a task. Append as you work — but **propose, get approval, then save**. Never accumulate silently.

## The five files

| File | Holds | Append when |
|------|-------|-------------|
| `decisions.md` | Choices made and the trade-off behind each | A real fork is settled (a one-way door, a library pick, a pattern) |
| `mistakes.md` | What went wrong and the lesson | A bug or wrong turn that future-you would repeat |
| `project-facts.md` | Durable facts about the codebase | A fact not obvious from the code that orients future work |
| `builder-preferences.md` | How the builder likes things done | A correction given twice, or a stated preference |
| `workflows.md` | How this project builds/tests/ships in practice | A repeatable procedure worth not re-deriving |

## Discipline (the SR-OS rule)

- **Type every entry** — put it in the right file, not a catch-all.
- **Write the WHY** — an entry without a reason rots into noise.
- **Approve before save** — propose the entry to the builder; don't write it unasked.
- **Prune contradictions** — when a new fact overrides an old one, edit or delete the old; don't stack both.
- **Date entries** (absolute dates). Stale-past-90-days is a smell to review.

## Entry format

```md
### <short title> — <YYYY-MM-DD>
<the fact / decision / lesson, one short paragraph>
**Why:** <the reason it's worth remembering>
```

This memory is project-scoped. Cross-project facts about *you* live in SR-OS's own memory (`~/.claude/.../memory/`), not here.
