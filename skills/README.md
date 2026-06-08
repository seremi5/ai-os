# L3 · Skills

> Prompts I reuse, not retype. Named, reusable patterns saved as files and invoked by trigger word.
> **Discipline: write the skill the *third* time you type the same prompt.** Prune anything unused in 30 days.

## The five types

| Type | Purpose | Mine / examples |
|------|---------|-----------------|
| **Creators** | Make something new | `prd-writer`, `board-deck`, the startup `/monday-ideas` |
| **Reviewers** | Audit and critique | `/code-review`, `/security-review`, the startup Challenger |
| **Formatters** | Transform what exists | `linkedin-formatter`, `/linkedin-daily` |
| **Monitors** | Watch and alert | `page-watcher`, competitor/pricing diffs |
| **Wizards** | Guide a setup | `/linkedin-onboard`, `find-skills` |

## Where my skills actually live

- **Global** — `~/.claude/skills/` (`find-skills`) and `~/.claude/commands/`.
- **Domain (startup)** — `~/GitHub/startup/.claude/commands/` holds the weekly cycle and portfolio/LinkedIn flows: `/weekly-cycle`, `/monday-ideas` … `/friday-decide`, `/portfolio-execute`, `/linkedin-daily`, `/execution-pipeline`.
- **Installed plugins** — Figma suite, `/code-review`, `/verify`, `/run`, `/schedule`, `/loop`, etc.
- **Engineering** — pipeline-building isn't a slash skill but a reusable pattern: [`../engineering/`](../engineering/).

This folder holds **personal, cross-project** skills that don't belong to one domain. Drop a `SKILL.md` here when a prompt earns it.

## A skill is just a file

```markdown
---
name: my-skill
description: One line — when should this fire?
---
Trigger words: <the phrases that should invoke it>
The reusable prompt body.
```

## Health check

| Working | Rotting |
|---------|---------|
| Trigger by name, useful output one-shot | Skills accumulate, never fire |
| Auto-fires when conditions match | I retyped the same prompt this week |
| I stopped retyping the same prompt | I forgot what skills I have |

## Backlog — prompts typed 3+ times, not yet skills

_(The Weekly OS Audit scans recent chats and proposes additions here.)_

- ⚠️ _TODO — fill from the next audit._
