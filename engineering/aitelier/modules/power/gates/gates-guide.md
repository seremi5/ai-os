# Approval gates

The workflow runs human-in-the-loop. At every phase boundary the orchestrator **stops, reports, and waits** for the builder before starting the next phase. No silent progress past a gate.

## At each phase boundary, the orchestrator posts

1. **Phase** just finished and the one about to start.
2. **What changed** — files touched, in one short list.
3. **Manual-test checklist** — concrete steps the builder runs to verify (from the Test phase / `task.md`).
4. **Ask:** approve to proceed, or request changes.

Then it **waits**. It does not start the next phase until the builder approves.

## Builder actions

- **Approve** → the next phase starts.
- **Request changes** → the orchestrator addresses them and re-posts the gate.
- **A free-form nudge mid-gate** ("also rename X") counts as changes-requested: re-open the gate after applying it, don't treat silence as approval.

## Rules

- **The quality gate is automatic; the approval gate is human.** Code can't pass to the next phase unless `rules:quality-gates` passes *and* the builder approves.
- **Checklists are specific.** "Hold Right Cmd, speak, release, see pasted text" — not "test it works".
- **One gate, one round of work.** Re-arm after each approval.
- Approvals and checklists are logged in the task's `Log` (`lifecycle`), so the trail survives the session.
