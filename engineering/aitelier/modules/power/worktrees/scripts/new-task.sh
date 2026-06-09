#!/usr/bin/env bash
#
# Start a task in its own git worktree + branch.
#   .claude/scripts/new-task.sh <task-slug> [base-branch]
#
set -euo pipefail

SLUG="${1:?usage: new-task.sh <task-slug> [base-branch]}"
BASE="${2:-$(git symbolic-ref --quiet --short refs/remotes/origin/HEAD 2>/dev/null | sed 's#origin/##' || echo main)}"
SLUG="$(echo "$SLUG" | tr '[:upper:] ' '[:lower:]-' | tr -cd '[:alnum:]-')"
BRANCH="feature/${SLUG}"
DIR=".aitelier-worktrees/${SLUG}"

ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"

if [ -d "$DIR" ]; then echo "worktree already exists: $DIR"; exit 0; fi

git fetch --quiet origin "$BASE" 2>/dev/null || true
git worktree add -b "$BRANCH" "$DIR" "$BASE"

# carry across un-tracked, gitignored assets a task needs (e.g. .env), per aitelier.json
if [ -f aitelier.json ] && command -v jq >/dev/null 2>&1; then
  for asset in $(jq -r '.project.worktree_assets[]? // empty' aitelier.json 2>/dev/null); do
    [ -e "$asset" ] && cp -R "$asset" "$DIR/$asset" 2>/dev/null || true
  done
fi

echo "✓ worktree ready: $DIR  (branch $BRANCH off $BASE)"
echo "  cd $DIR  &&  claude"
