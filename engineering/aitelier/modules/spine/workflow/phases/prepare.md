# Phase · Prepare

**Intent:** understand the surface area before anyone designs or codes. Research APIs, docs, constraints, prior art.

**Owner:** `preparer`.

**Entry:** an unfamiliar area, or a task that touches APIs/SDKs the team hasn't used.

**Do:**
- Read the real documentation (not just the first hit), and the relevant existing code.
- Capture findings in `docs/preparation/<topic>.md`.
- List blocking unknowns (API availability, version constraints) explicitly.

**Don't:** recommend an implementation — that's Architect's call.

**Gate (exit):** research saved to `docs/preparation/`; no ambiguity left that would block design.
