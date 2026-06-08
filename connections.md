# L2 · Connections

> Reach beyond the workspace. The OS stops being a sandbox the moment one of these connects.
> **Discipline: 3 used beats 12 connected.** Disconnect anything unused in 30 days.

## What's connected now

| Type | Connection | Use it for | Last used |
|------|-----------|-----------|-----------|
| **MCP** | Gmail | Search threads, draft (never auto-send), label | 🟢 active |
| **MCP** | Google Calendar | Read schedule, morning briefing | 🟢 active |
| **MCP** | Google Drive | Pull docs into context | 🟡 occasional |
| **MCP** | Notion | Portfolio board, LinkedIn cards, Start-up hub | 🟢 active |
| **MCP** | Figma | Design ↔ code, mockups, design system | 🟡 project-only |
| **MCP** | browser-agent | DOM-aware web actions, forms, scraping | 🟡 `@browser` only |
| **CLI** | `git` / `gh` | Version control, PRs, issues | 🟢 active |
| **CLI** | shell | File ops, `curl`, local scripts | 🟢 active |
| **Local** | `~/GitHub/*`, `~/.claude/` | Filesystem as durable storage | 🟢 always |

## Rules that override defaults

- **Browser agent needs `@browser`** in the message. No `@browser` → reply "Add `@browser` to your message to use the browser agent." In an `@browser` session, act autonomously but **stop before** checkout/payment, entering personal data, or irreversible deletes. Never screenshot unless asked. (Full rule: `~/.claude/CLAUDE.md`.)
- **Gmail: draft, don't send.** Never send mail without explicit approval.
- **APIs over wrappers.** When a direct provider API exists (Anthropic, Gemini), prefer it to a SaaS middle layer — invoke from a skill or service, not ad hoc.

## Health check

| Working | Rotting |
|---------|---------|
| Composes across 2+ tools unprompted | I copy-paste between disconnected apps |
| One question hits the right places | Agent only knows what's in the repo |
| I stopped copy-pasting between apps | 12 connected, it picks the wrong one |

## Candidates (connect only when a real task needs it)

- A market/news API for the investing experiments (invoke from a service — see [`engineering/`](engineering/)).
- Slack — only if a workflow actually moves there. Not before.
