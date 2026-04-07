# Operations

Purpose: Capture how the system is deployed, operated, observed, and recovered. Keep this stack/hosting agnostic until specified.

## Phase 1 (Shared Cache) operational notes
- TODO: Document how the sync stack is started/stopped (Docker Compose or other).
- TODO: Document how you verify any declared resource limits are *actually enforced* in your runtime.
- TODO: Document where persistent state lives (Obsidian vault path, Redis volume path, n8n state path).

## Environments
- TODO: List environments (local/dev/staging/prod) and what each is for.
- TODO: Promotion policy (what moves between environments and how).

## Deploy
- TODO: Deployment mechanism (CI/CD, manual steps) — describe at a high level.
- TODO: Pre-deploy checks (migrations, canaries, smoke tests).
- TODO: Post-deploy validation steps.

## Rollback / recovery
- TODO: Rollback strategy (artifact rollback, config rollback, feature flags).
- TODO: Data migration rollback considerations (expand/contract, backfills).
- TODO: Incident recovery playbook link (create later if needed).

## Rebuild & recovery (Phase 1 invariants)
These must remain true for the Shared Cache MVP:
- **Obsidian is recoverable**: `00_LLM_Cache` can be restored from backups/version control.
- **Redis is disposable**: Redis can be wiped and rebuilt from Obsidian notes.
- **Reconcile exists**: there is a way to remove stale index entries caused by note renames/moves/deletes (event-driven or periodic).

Checklist:
- [ ] “Wipe Redis → rebuild” is documented and has been executed successfully at least once.
- [ ] Malformed notes cause visible errors (alerts/logs), not silent skipping.
- [ ] Index reconciliation strategy is documented (how often, what it checks).

## Observability

### Dashboards (placeholders)
- TODO: List key dashboards and what questions they answer.

### Alerts (placeholders)
- TODO: List key alerts (symptoms), thresholds, and runbooks.

### Signals to standardize
- TODO: Request/operation latency
- TODO: Error rates (by category)
- TODO: Saturation/capacity (queue depth, workers, etc.)
- TODO: Business KPIs (ties back to `product-brief.md`)

## Operational policies
- TODO: On-call expectations (if any)
- TODO: Access controls for production
- TODO: Change windows and emergency change process

