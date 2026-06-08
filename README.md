# Sergi's AI OS

> Formerly `ai-forge` / `sr-pipeline`. The engineering standards didn't disappear — they're now one layer (`engineering/`) inside a larger system.

A personal operating model for working with AI. Not a better model — a better setup. Five layers the agent reads so it knows who I am, what it can reach, what to reuse, what runs without me, and what to remember. One loop keeps it from rotting.

Built once. Portable across tools (Claude, Codex, Cursor, whatever's next). The system decays the moment the loop stops running.

> **This is not an AI problem. It's an operating-model problem.** — adapted from the CraftMatters AI-OS masterclass (Ines Lourenço, 2026).

---

## The five layers + one loop

| Layer | Purpose | File |
|-------|---------|------|
| **L1 · Context** | What the agent reads first | [`CLAUDE.md`](CLAUDE.md) (router) + [`context/`](context/) |
| **L2 · Connections** | Reach beyond the workspace | [`connections.md`](connections.md) |
| **L3 · Skills** | Prompts I reuse, not retype | [`skills/`](skills/) |
| **L4 · Automations** | Work that runs while I sleep | [`automations.md`](automations.md) |
| **L5 · Memory** | What survives every conversation | [`memory.md`](memory.md) → `~/.claude/.../memory/` |
| **The loop** | Weekly OS Audit — the keystone | [`audit.md`](audit.md) |

Plus the engineering layer this repo grew out of:

| | | |
|---|---|---|
| **Engineering** | How I build AI pipelines (the old ai-forge) | [`engineering/`](engineering/) |

---

## How to use it

**Working *in* the OS** — open this repo in Claude Code. `CLAUDE.md` loads first and routes the agent to the right context file before it answers anything.

```bash
cd ~/GitHub/ai-os
claude
```

**Making the OS govern *every* session** — add one routing line to the global `~/.claude/CLAUDE.md` so it points here for product/startup/writing work. Then the voice and domain apply everywhere, not only in this repo. (Editing the global config needs your explicit OK — see Status.)

**Running the loop** — once a week, paste the audit from [`audit.md`](audit.md). Ten minutes. Approve 2–3 changes, reject 1–2, move on. Skip it and the OS rots.

---

## Folder map

```
ai-os/                       # the repo (was sr-pipeline / ai-forge)
├── README.md                # this file
├── CLAUDE.md                # L1 router — read first, ≤80 lines
├── context/                 # L1 Context
│   ├── profile.md           #   identity: voice, principles, role, banned phrases
│   ├── strategy.md          #   this quarter's priorities (≤200 words)
│   ├── domain.md            #   the area I own: fintech / AP·AR / e-invoicing
│   └── terminology.md       #   guardrails: banned vocabulary
├── connections.md           # L2 Connections inventory
├── skills/                  # L3 Skills catalog
│   └── README.md
├── automations.md           # L4 Automations registry
├── memory.md                # L5 — pointer to ~/.claude memory (not duplicated)
├── audit.md                 # the Weekly OS Audit (the loop)
└── engineering/             # how I build pipelines (the folded-in ai-forge)
    ├── README.md
    ├── standards/
    ├── patterns/
    └── template/
```

---

## Status

- ✅ Renamed `sr-pipeline → ai-os` (folder + GitHub `seremi5/ai-os`; old name redirects).
- ✅ Weekly OS Audit scheduled — see [`automations.md`](automations.md). Outputs land in [`audits/`](audits/).
- ⏳ Route the global `~/.claude/CLAUDE.md` into this OS — **needs your explicit OK** (it's the agent's own startup config).
- ⚠️ Set the quarter's outcome metric in [`context/strategy.md`](context/strategy.md) — only you can.
