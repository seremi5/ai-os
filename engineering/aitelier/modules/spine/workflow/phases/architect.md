# Phase · Architect

**Intent:** design the change before code — data model, interfaces, cross-layer impact, migration plan.

**Owner:** `architect`.

**Entry:** any change spanning more than two files or touching a module boundary. Skip for trivial edits.

**Do:**
- Write the architecture doc in `docs/architecture/` (or an ADR for significant calls).
- Define the public API surface, the data model, and every affected layer (`full-stack-awareness` if installed).
- Note whether this adds a pipeline stage / new seam, and the migration steps.

**Gate (exit):** architecture doc saved; all cross-layer impacts named; consistent with existing patterns.
