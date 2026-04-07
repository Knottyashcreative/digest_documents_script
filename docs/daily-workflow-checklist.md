# Daily workflow checklist

Purpose: Provide a step-by-step daily routine that connects product intent, contracts, architecture, standards, and ops so work stays industry-grade.

## Start of day (10–15 minutes)
- [ ] **Sync on intent**: skim `product-brief.md` and any active feature spec(s) under `templates/` (or your issue tracker link).
- [ ] **Use the vocabulary**: open `glossary.md`; add/adjust terms for anything you expect to name today.
- [ ] **Scan decision context**: check `adr/` for any relevant decisions; if you expect to choose between alternatives, plan to write an ADR.
- [ ] **Identify contract touchpoints**: if you’ll change an interface, open `contracts/README.md` and decide where the source-of-truth artifact will live (still TBD is ok, but document the plan).
- [ ] **Confirm your “definition of done”**: re-check `engineering-standards.md` and the checklist you’ll need to satisfy.
- [ ] **Phase 1 cache health** (if working on memory): skim `phase-1-shared-cache-mvp.md` acceptance tests and confirm yesterday’s invariants still hold.

## Before writing code (5 minutes)
- [ ] **Choose the right spec artifact**:
  - If new behavior: draft a feature spec using `templates/feature-spec.md`.
  - If a decision between approaches: draft an ADR using `adr/template.md`.
- [ ] **Clarify boundaries**: update `architecture.md` with the container/ownership you’re about to touch (who owns what).
- [ ] **Data impact check**: if entities/relationships/IDs change, update `data.md` first (or in the same change).
- [ ] **Security sanity check**: if there’s any new trust boundary, secrets handling, authn/authz change, or sensitive data, update `security.md`.

## While coding (habits to enforce)

### Python (logic layer)
- [ ] **Style & clarity**: follow PEP 8 naming and formatting.
- [ ] **Type hints**: add/maintain type hints for public interfaces and complex logic.
- [ ] **Docstrings**: add docstrings for non-trivial modules/classes/functions (choose a style later; be consistent).
- [ ] **Testing**: add unit tests for logic and boundary tests for contract behavior (tooling TBD).
- [ ] **Logging > printing**: use structured or consistent logging; avoid `print` for anything that might ship.
- [ ] **Packaging/portability**: keep runtime assumptions explicit; plan for packaging as artifacts (wheel/container) once stack is chosen.

### Bash / scripting (automation layer)
- [ ] **Safety header**: `set -euo pipefail` (where compatible) and predictable error handling.
- [ ] **Portable shebang**: `#!/usr/bin/env bash` for bash scripts.
- [ ] **Quote variables**: use `"$VAR"` unless you explicitly want splitting/globbing.
- [ ] **Idempotency**: scripts should be safe to re-run (check before create/delete).
- [ ] **Clean exits**: use `trap` for cleanup when creating temp files or spawning subprocesses.
- [ ] **Self-documentation**: include `-h/--help` for non-trivial scripts.

### Infrastructure & systemic constraints (design posture)
- [ ] **Least privilege**: do not widen access “temporarily”; model access boundaries explicitly.
- [ ] **Resource awareness**: avoid unbounded memory growth; stream/iterate for large inputs.
- [ ] **Secrets discipline**: never commit secrets; prefer env vars; maintain `.env.example` (policy in `local-development.md`).
- [ ] **Fail fast, safely**: crash loudly on unsafe states to prevent silent corruption; document any recovery steps in `operations.md`.
- [ ] **Observability**: ensure the change is debuggable via logs/metrics/traces (placeholders allowed, but the intent must be documented).

## Before opening a PR / requesting review (10 minutes)
- [ ] **Update docs with the behavior**:
  - `glossary.md` for any new terms
  - `contracts/` for interface changes (and compatibility notes)
  - `architecture.md` for ownership/boundary changes
  - `data.md` for model/migration/identifier changes
  - `security.md` for trust boundary/auth/secret changes
  - `operations.md` for deploy/rollback/observability implications
- [ ] **Run tests**: TODO: add the exact commands once toolchain is chosen (see `local-development.md`).
- [ ] **Use the PR checklist**: `templates/change-request-checklist.md`.
- [ ] **Keep changes atomic**: split unrelated refactors from behavior changes.

## After merge (5 minutes)
- [ ] **Backfill documentation debt**: convert any “TODO after merge” into tracked tasks or finish the docs immediately.
- [ ] **Operational follow-up**: if the change needs new dashboards/alerts/runbooks, add them (or add TODOs in `operations.md` with an owner).
- [ ] **Index integrity check (Phase 1)**: ensure renames/moves/deletes didn’t create duplicates or stale entries; run reconcile/rebuild if needed.

## Weekly maintenance (30–60 minutes)
- [ ] **Review ADR drift**: are there decisions made in PRs/issues that aren’t captured in `adr/`?
- [ ] **Contract hygiene**: ensure deprecations have timelines; remove dead paths only when policy allows.
- [ ] **Docs refresh**: prune stale TODOs; ensure `docs/README.md` map remains accurate.

