# L5 · Memory

> What survives every conversation. The layer that decays fastest and compounds most when audited.
> **Discipline: approve every save. Type every memory. Write the WHY. Audit weekly.**

## Where it lives — don't duplicate it here

The real memory store is the global, file-based memory at:

```
~/.claude/projects/-Users-sergireina-GitHub/memory/
├── MEMORY.md          # the index — one line per memory, loaded every session
├── user_profile.md
└── …                  # one fact per file, with frontmatter
```

This file is a **pointer and a discipline reminder**, not a second copy. Edits happen in `~/.claude/.../memory/`. (The OS profile in [`context/profile.md`](context/profile.md) is the curated, stable identity; the memory store is the living, append-as-you-learn record. Keep them consistent — when profile changes, check memory, and vice-versa.)

## The four kinds

| Kind | Purpose | Example | Frontmatter `type` |
|------|---------|---------|--------------------|
| **User** | Who I am | "AI PM, OakNorth. ex-Monite." | `user` |
| **Feedback** | A correction given twice | "Lead with the conclusion." | `feedback` |
| **Project** | State with an expiry | "Portfolio launched 25 May 2026; Shoutit is project #1." | `project` |
| **Reference** | Where to look | "Portfolio rules live in `startup/portfolio/README.md`." | `reference` |

Each file = one fact. `feedback`/`project` entries carry **Why:** and **How to apply:** lines. Link related memories with `[[slug]]`. Convert relative dates to absolute before saving.

## The trap & the rule

Default-on memory with no audit → 40 entries in 30 days, six of them contradicting. The agent then picks one at random.

→ **Approve every save.** When proposing one, name the WHY. The Weekly OS Audit ([`audit.md`](audit.md)) flags contradictions and entries stale past 90 days.

## Health check

| Working | Rotting |
|---------|---------|
| Applies corrections I forgot I gave | Contradictory memories accumulate |
| Output I didn't have to nudge | Rules applied that no longer hold |
| I can explain WHY each memory exists | I override memories instead of editing |
