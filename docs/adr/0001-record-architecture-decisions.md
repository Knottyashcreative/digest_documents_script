# ADR 0001: Record architecture decisions

Status: Accepted

## Context
We want a lightweight, durable way to capture *why* important decisions were made. Without a decision log, future changes risk breaking implicit constraints, redoing work, or re-arguing already-settled trade-offs.

## Decision
We will use Architecture Decision Records (ADRs) in `docs/adr/` to document significant decisions and their rationale.

We will:
- Write ADRs for impactful decisions (see `docs/adr/README.md`).
- Use `docs/adr/template.md` as the standard format.
- Link ADRs from relevant docs (architecture, contracts, security) when they influence behavior.

## Consequences
### Positive
- Shared context for humans and coding agents.
- Faster onboarding and fewer repeated debates.
- Better alignment between architecture, contracts, and operations.

### Negative / trade-offs
- Small ongoing cost to write and maintain ADRs.
- Requires discipline to keep ADRs current (supersede rather than silently drift).

## Alternatives considered
- **Rely on PR discussions only**
  - Pros: no extra artifact
  - Cons: context gets buried; hard to search; links rot
- **Central “architecture doc” only**
  - Pros: one place to read
  - Cons: becomes large and hard to keep coherent; loses decision-by-decision history

## Follow-ups
- TODO: Add ADRs as major decisions are made (contracts format, deployment model, auth model, etc.).

## Links
- `docs/adr/README.md`
- `docs/adr/template.md`

