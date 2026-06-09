# Phase · Ship

**Intent:** get the change out safely. Stage first, verify, then release.

**Owner:** `reviewer` + the deploy flow in `aitelier.json → project.deploy`.

**Entry:** the project deploys (`deploy` is set). Skip for libraries and local tools.

**Do:**
- Final review pass on the diff (`reviewer`).
- Follow the staging-first flow: feature → staging → verify (logs, smoke test) → main. Never straight to production.
- Run any migrations manually and record the commands in the release note.
- If `lifecycle` is installed, write the release to `.aitelier/releases/`.

**Gate (exit):** staging verified; release note written; production smoke-tested. No direct-to-main without staging.
