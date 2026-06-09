#!/usr/bin/env bash
#
# Pull the base branch into the current task worktree, safely.
#   .claude/scripts/sync.sh [base-branch]
#
set -euo pipefail

BASE="${1:-$(git symbolic-ref --quiet --short refs/remotes/origin/HEAD 2>/dev/null | sed 's#origin/##' || echo main)}"
CURRENT="$(git rev-parse --abbrev-ref HEAD)"

if [ "$CURRENT" = "$BASE" ]; then echo "on $BASE — nothing to sync into"; exit 0; fi

STASHED=0
if ! git diff --quiet || ! git diff --cached --quiet; then
  git stash push -u -m "aitelier-sync $(date +%s)" >/dev/null
  STASHED=1
  echo "• stashed work-in-progress"
fi

git fetch --quiet origin "$BASE"
echo "• rebasing $CURRENT onto origin/$BASE"
if git rebase "origin/$BASE"; then
  [ "$STASHED" = 1 ] && git stash pop && echo "• restored work-in-progress"
  echo "✓ synced with origin/$BASE"
else
  echo "✗ rebase hit conflicts — resolve, then: git rebase --continue"
  [ "$STASHED" = 1 ] && echo "  (your WIP is stashed — git stash pop after the rebase finishes)"
  exit 1
fi
