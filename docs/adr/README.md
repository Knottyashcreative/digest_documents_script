# ADRs (Architecture Decision Records)

Purpose: ADRs capture *why* we made significant engineering/product decisions so future contributors can understand context and avoid re-litigating old choices.

## When to write an ADR
Write an ADR when you:
- Choose between meaningful alternatives (e.g., sync vs async, library A vs B, consistency rules).
- Introduce a new system boundary/container or materially change ownership.
- Define or change a contract approach (API style, eventing semantics, versioning rules).
- Make decisions with long-term operational/security implications.

## What an ADR should include
- **Context**: what problem/constraint drove the decision
- **Decision**: what we chose
- **Consequences**: what gets better/worse, risks, follow-ups
- **Alternatives considered**: what we didn’t choose and why

## Lifecycle
- **Proposed**: drafted and under discussion
- **Accepted**: decision is made and should be treated as current guidance
- **Superseded**: replaced by a newer ADR (link both ways)

## Naming & numbering
- File names are `NNNN-short-title.md` (e.g., `0002-event-contract-format.md`).
- Keep titles short and scannable; use kebab-case.
- Do not renumber existing ADRs once merged.

## Template
Use `template.md`. Copy it to a new `NNNN-...` file and fill it in.

## Index
- [0001-record-architecture-decisions.md](0001-record-architecture-decisions.md) — use ADRs
- [0002-embedding-model-phase1-lock.md](0002-embedding-model-phase1-lock.md) — Phase 1 embedding model lock

