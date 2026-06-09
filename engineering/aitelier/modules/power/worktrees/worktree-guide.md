# Worktrees

Each task gets its own git worktree and branch, so parallel work never collides and the base branch stays clean.

## Layout

```
<repo>/
├── .aitelier-worktrees/
│   ├── add-filler-list/      ← worktree, branch feature/add-filler-list
│   └── fix-paste-race/       ← worktree, branch feature/fix-paste-race
└── … (base branch checkout)
```

## Commands

```bash
# start a task (creates worktree + branch off the base)
.claude/scripts/new-task.sh add-filler-list
cd .aitelier-worktrees/add-filler-list && claude

# pull base in while you work (safe: stashes, rebases, restores)
.claude/scripts/sync.sh
```

## Rules

- **One task, one worktree.** Don't develop two tasks in one checkout.
- **Sync before you finish**, not after a long divergence — small rebases beat big merges.
- **Carry only what's needed.** `aitelier.json → project.worktree_assets` lists gitignored files (e.g. `.env`) copied into a new worktree.
- **Finish = merge to base** (or open a PR), then `git worktree remove .aitelier-worktrees/<task>`.
- The base branch comes from `origin/HEAD`, overridable as the second arg to either script.
