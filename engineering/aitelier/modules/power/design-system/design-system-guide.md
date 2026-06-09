# Design system

The source of truth for how this project looks. Designer and UI coders read it before drawing or building anything.

## Where it lives

- **Figma library:** `<url>` — components, variants, tokens. The canonical reference.
- **Tokens in code:** `<path>` — colour, type, spacing, radius. What the UI actually consumes.
- **Code components:** `<path>` — the reusable building blocks. Check here before writing a new one.

> Fill these three at init. If the project has no design system yet, this module seeds the intent and the designer establishes one in the Design phase.

## Rules

- **Reuse before custom.** A new component is a last resort — first look for an existing one to compose. The designer flags reuse-vs-custom in the Design phase.
- **Tokens, not literals.** No hard-coded hex/spacing in UI code — bind to the token. A value that isn't a token is a smell.
- **Design ↔ code stay in sync.** A token added in Figma lands in code (and vice versa) in the same change; don't let them drift.
- **One register.** User-facing text follows `aitelier.json → project.language`.

## Handoff

The designer produces a Figma URL (never ASCII art), names the components to reuse, and lists any new ones to add to the library before the frontend/mobile coder implements.
