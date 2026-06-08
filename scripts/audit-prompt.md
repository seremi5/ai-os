You are running the Weekly OS Audit on Sergi's AI OS. Your current directory is the repo root (`~/GitHub/sr-os`).

Read and assess each layer:

- **L1 Context** — `CLAUDE.md` and `context/*.md`. Flag any file older than 30 days, longer than 500 words, or the router if over 80 lines. Note unfilled `⚠️ TODO`s (e.g. the quarter's outcome metric in `context/strategy.md`).
- **L2 Connections** — `connections.md`. Flag any connection marked unused/occasional that looks stale.
- **L3 Skills** — `skills/README.md`. Flag skills unused 30 days; note if the backlog is empty.
- **L4 Automations** — `automations.md`. Flag any job whose output exceeds its stated constraint or that looks unread.
- **L5 Memory** — `~/.claude/projects/-Users-sergireina-GitHub/memory/MEMORY.md` and the files it indexes. Flag contradictions and entries older than 90 days.

You may read file modification times to judge staleness.

Output **only** the audit as markdown — no preamble, no closing chatter — in exactly this shape:

```
# Weekly OS Audit — <ISO week>

> Run: <today's date>.

**L1 CONTEXT**
- [ ] DISCUSS — <one line, ≤20 words>

**L2 CONNECTIONS**
- [ ] APPROVE — <one line, ≤20 words>

**L3 SKILLS**
- [ ] REJECT — <one line, ≤20 words>

**L4 AUTOMATIONS**
- [ ] DISCUSS — <one line, ≤20 words>

**L5 MEMORY**
- [ ] APPROVE — <one line, ≤20 words>

---

**So what:** <one line on OS health>
```

Rules: max 5 proposals per layer; one line each, ≤20 words; tag every proposal `[ ] APPROVE`, `[ ] REJECT`, or `[ ] DISCUSS`. Do **not** write any files — just print the markdown.
