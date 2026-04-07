# Engineering standards

Purpose: Set lightweight, enforceable standards for implementation quality and consistency (testing, logging, errors, reviews).

## Testing bar
- TODO: Define what “unit”, “integration”, and “e2e” mean in this repo.
- TODO: Minimum coverage expectations (if any) and what matters more than coverage.
- TODO: What must be tested at contract boundaries (see `contracts/`).

## Logging & errors
- TODO: Logging style (structured vs plain), required fields (request ID, user/account ID, etc.).
- TODO: Error taxonomy: expected vs unexpected errors, retryable vs non-retryable.
- TODO: Public error contract: what is safe to expose to clients (avoid stack traces, secrets).

## Code quality & review
- TODO: Lint/format conventions (tools TBD).
- TODO: Review expectations (size limits, required approvals, design review triggers).
- TODO: Performance considerations (where to measure, what to avoid).

## Repository layout pointers
- TODO: Once code exists, document the main directories and what belongs where.
- TODO: Where configs live, where generated artifacts go (if any).

## Definition of Done (checklist)
- [ ] Behavior matches a documented spec (feature spec or issue) and acceptance criteria.
- [ ] Contracts updated if interface behavior changed (`docs/contracts/`).
- [ ] Docs updated if user-facing behavior, data model, ops, or workflows changed.
- [ ] Tests added/updated (appropriate level).
- [ ] Observability updated (logs/metrics/traces) where meaningful.
- [ ] Security considerations reviewed (see `security.md` for checklist).
- [ ] Rollback considerations documented for risky changes.

