# L4 · Automations

> Work that runs while I sleep. Scheduled prompts that run without me.
> **Discipline: every automation has a tight output constraint** — or it becomes noise I stop reading. "5 bullets, 8 words each" beats "a summary of the week."

## The five types

Digests · Monitors · Audits · Briefings · Reminders.

## What's scheduled now

| When (Madrid) | Type | Job | Owner | Constraint |
|---------------|------|-----|-------|-----------|
| Daily 23:07 | Digest | Startup ideation cycle drops ideas | `startup` routine | 5 ideas/day |
| Daily 23:30 | Audit | Project Steward syncs `portfolio/<project>.md` + Notion | Steward (per project) | State diff only |
| Weekday | Creator | LinkedIn — 3 post candidates in my voice | `/linkedin-daily` | 3 cards, sources verified |
| Sunday 09:00 | Briefing | Portfolio Coordinator writes the week's decision | Coordinator | 1 decision page |
| Monday (manual) | — | `/weekly-cycle` Mon→Fri | CEO (operator-run) | Not unattended |
| **Weekly (set this)** | **Audit** | **Weekly OS Audit** of all 5 layers | me + [`audit.md`](audit.md) | **max 5 proposals/layer, 1 line each** |

> The OS audit is the keystone. It isn't scheduled yet — see "Wiring" below.

## Limits to remember

- An agent team can't run unattended from cron — the lead must be a live session. The weekly cycle is operator-triggered.
- Posting (LinkedIn, email) is **always manual**. Automations draft and propose; they never publish.

## Health check

| Working | Rotting |
|---------|---------|
| Monday digest lands, actually read | Digest = wall of text, ignored |
| Output is tight, every line earns it | I can't remember what's scheduled |
| Downstream work runs without me triggering | I trigger work the automation should do |

## Wiring the OS Audit

Run it manually each Monday by pasting the prompt in [`audit.md`](audit.md), **or** schedule it:

- `/schedule` — a remote agent on a weekly cron (e.g. Monday 08:00 Madrid). Best for hands-off.
- `/loop` — self-paced reminder loop within a live session.

⚠️ _TODO — pick one and set the day/time._
