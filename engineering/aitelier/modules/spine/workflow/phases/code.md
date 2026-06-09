# Phase · Code

**Intent:** implement the design, one layer at a time, behind the project's conventions.

**Owner:** the relevant coder(s) — `backend-coder`, `frontend-coder`, `mobile-coder`, `database-engineer`. Dispatch in parallel when their work is independent.

**Do:**
- Follow `.claude/rules/conventions.md` (rendered from `aitelier.json`) — language, deps policy, style.
- Read architecture/design docs by `@`-reference; don't re-derive them in chat.
- Keep new behaviour in the project's established seam, not one-off branches.
- Run `build` and `test` commands from `aitelier.json` as you go.

**Gate (exit):** `build` clean (zero errors/warnings); no secrets committed; user-facing text in `project.language`; assumptions logged (`async-questions`).
