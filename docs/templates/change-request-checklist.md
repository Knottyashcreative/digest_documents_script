# Change request checklist (PR)

Purpose: Ensure each change is reviewable, safe, and keeps docs/contracts aligned with behavior.

## Summary
- TODO: What changed and why? (1–3 bullets)

## Scope & risk
- [ ] This PR is small and focused (or split into smaller PRs).
- [ ] Risk level: TODO: low / medium / high (and why)
- [ ] Rollback plan exists (or not needed): TODO

## Docs & decisions
- [ ] `docs/glossary.md` updated for new/renamed terms.
- [ ] `docs/architecture.md` updated if boundaries/ownership changed.
- [ ] ADR added/updated if a meaningful decision was made (`docs/adr/`).
- [ ] `docs/daily-workflow-checklist.md` followed (or consciously deviated with reason): TODO

## Contracts (if applicable)
- [ ] Contract source of truth updated (`docs/contracts/`).
- [ ] Compatibility assessed and documented (breaking vs additive).
- [ ] Examples included (requests/responses/events) and error semantics documented.

## Data (if applicable)
- [ ] `docs/data.md` updated for entity/relationship/identifier changes.
- [ ] Migration/backfill plan documented (and rollback considered).

## Security (if applicable)
- [ ] `docs/security.md` updated for trust boundary/authn/authz/secrets changes.
- [ ] Sensitive data handling verified (redaction/masking; no secrets in logs).

## Tests
- [ ] Unit tests added/updated.
- [ ] Integration tests added/updated (if needed).
- [ ] E2E tests added/updated (if applicable).
- TODO: Paste the commands and results once defined in `docs/local-development.md`.

## Operations & observability
- [ ] `docs/operations.md` updated if deploy/rollback/monitoring behavior changed.
- [ ] Logging/metrics/traces added or updated to support debugging.

