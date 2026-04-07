# Project Documentation (Start Here)

Purpose: This is the single entry point and navigation map for all project docs. If you’re not sure where to look, start here.

## How to use these docs
- **If you’re building/changing behavior**: read `glossary.md`, then the relevant section in `architecture.md`, then check `contracts/` and `adr/`.
- **If you’re making a decision**: record it as an ADR in `adr/` (use the template).
- **If you’re changing an interface** (API/event/schema): treat `contracts/` as the source of truth and follow the breaking-change rules.

## Documentation map
- `product-brief.md`: what we’re building and why (goals, non-goals, success metrics)
- `glossary.md`: project vocabulary (terms used in code, APIs, UX)
- `architecture.md`: boundaries/ownership and system context (stack-agnostic)
- `adr/`: Architecture Decision Records (why we decided things)
- `contracts/`: interface contracts (API/event/schema) and versioning rules
- `data.md`: entities, relationships, identifiers, migrations (vendor-agnostic)
- `security.md`: trust boundaries, secrets handling, authn/authz placeholders
- `local-development.md`: how to run locally, env var conventions, test commands
- `engineering-standards.md`: testing bar, logging/error conventions, definition of done
- `daily-workflow-checklist.md`: step-by-step routine for day-to-day engineering work
- `phase-1-shared-cache-mvp.md`: Phase 1 scope, critical flaws, MVP acceptance tests
- `roadmap.md`: MVP focus and parked future aspirations
- `ux-product-behavior.md`: user journeys and acceptance criteria (if UI exists)
- `operations.md`: deploy/rollback/observability placeholders
- `templates/`: reusable templates (feature spec, ADR, change request checklist)
- `AGENTS.md`: rules for coding agents working in this repo
- `document-ingestion-engine.md`: **Phase deliverable** — Obsidian ingestion script (`obsidian_pro_master.py`), config, runbook
- `gap-analysis-outstanding.md`: **critical / missing / outstanding** checklist (Phase 1 vs M1)
- `crosswalk-ingestion-to-cache.md`: ingestion YAML vs `00_LLM_Cache` schema alignment
- `mcp-setup-cursor.md`: scope Cursor MCP to `00_LLM_Cache` only
- `runbooks/rebuild-redis-index.md`: wipe Redis and rebuild from vault
- `runbooks/reconcile-cache-index.md`: fix index drift after renames/deletes

## Defaults & open questions (replace these TODOs)
- TODO: Define the product’s primary users and top 1–3 workflows (see `product-brief.md`).
- TODO: Decide contract format(s) used as “source of truth” (OpenAPI vs GraphQL vs events vs JSON schemas) (see `contracts/README.md`).
- TODO: Confirm whether the system includes a UI (if yes, maintain `ux-product-behavior.md`).
- TODO: Define the initial high-level system boundaries/containers (see `architecture.md`).
- TODO: Define identifier strategy (UUID/ULID/etc.) and time semantics (UTC, monotonic needs) (see `data.md` / `glossary.md`).

## Update policy (docs ↔ code)
- **Docs must be updated when behavior changes**: any change that affects user-facing behavior, data shape, contracts, error semantics, or operational behavior requires a doc update in the same change.
- **Docs lead for interfaces**: update `contracts/` first (or in the same change) before implementing consumers/providers.
- **ADRs capture decisions**: if you decide between alternatives (build vs buy, sync vs async, auth model, consistency rules), write an ADR.

