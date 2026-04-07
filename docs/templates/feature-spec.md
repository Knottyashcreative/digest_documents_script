# Feature spec template

Purpose: Describe user-facing behavior and engineering approach before implementation. Keep it short and testable.

## Summary
- TODO: One paragraph describing the feature and why it matters.

## Problem
- TODO: What user/system problem does this solve?
- TODO: Who is impacted?

## Goals / non-goals
- **Goals**: TODO
- **Non-goals**: TODO

## Proposed behavior
- TODO: Describe the behavior in terms of inputs → outputs, user actions → outcomes.
- TODO: Include examples (happy path + 1–2 edge cases).

## Acceptance criteria
- TODO: Use Given/When/Then bullets (copy from `ux-product-behavior.md` if helpful).

## Contracts (if applicable)
- TODO: What interfaces change? (API endpoints, events, schemas)
- TODO: Compatibility notes and versioning plan (see `docs/contracts/README.md`)

## Data (if applicable)
- TODO: Entities/relationships affected (see `docs/data.md`)
- TODO: Migration/backfill approach (if any)

## Security & privacy (if applicable)
- TODO: New trust boundaries, authn/authz impact (see `docs/security.md`)
- TODO: Sensitive data handling (redaction/logging)

## Observability & operations
- TODO: Logs/metrics/traces needed to support this feature
- TODO: Rollout plan (gradual release, feature flags) and rollback considerations (see `docs/operations.md`)

## Testing plan
- TODO: Unit tests
- TODO: Integration tests
- TODO: E2E tests (if applicable)

## Rollout / launch checklist
- [ ] Docs updated (glossary, contracts, architecture, ops)
- [ ] Tests added/updated
- [ ] Observability in place (or TODOs with owner)
- [ ] Rollback path documented

