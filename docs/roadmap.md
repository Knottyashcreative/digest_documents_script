# Roadmap (docs-driven)

Purpose: Keep the project focused. This file defines the MVP (Phase 1) and explicitly parks future aspirations so they don’t distort implementation quality.

## Milestone M1 (repository / GitHub)

**Shipped in repo:** docs skeleton (`docs/README.md` and linked pages), `docs/AGENTS.md`, ADR folder + template, ingestion engine `obsidian_pro_master.py` + `config.json` + `requirements.txt`, runbook `docs/document-ingestion-engine.md`, sample input `fixtures/in/`.

**Branching:** work on `main`; tag releases optionally as `m1-docs-ingestion` after CI or manual smoke test.

**Implicit goals satisfied by M1:**

- Humans and agents share one doc index (`docs/README.md`).
- Phase 1 “cold storage” path is supported: consistent Obsidian-ready markdown + YAML (`document-ingestion-engine.md` + engine output contract).
- Programming/coding memory loop remains specified in `phase-1-shared-cache-mvp.md` (capture → verify → distill → index); ingestion is the **import** side for non-chat sources into the same vault shape.

**Still TODO after M1 (Phase 1 ops):** wire `00_LLM_Cache` schema to your vault, Redis/n8n sync, MCP scope, and rebuild/reconcile checks per `phase-1-shared-cache-mvp.md` acceptance tests.

## Phase 1 (MVP): Shared Cache Module (Memory foundation)
Goal: A reliable, rebuildable “shared cache” that learns from programming/coding queries by turning verified answers into reusable assets.

- Source of truth and scope: `phase-1-shared-cache-mvp.md`
- Daily operating routine: `daily-workflow-checklist.md`

### Phase 1 deliverables (MVP-complete when true)
- Obsidian `00_LLM_Cache` note schema is defined and used consistently.
- Retrieval works (Cursor can read/search notes scoped to `00_LLM_Cache`).
- Indexing works (notes become searchable via vector metadata store) OR a clearly documented manual reindex exists.
- Redis is explicitly treated as rebuildable (volatile) and can be recreated from Obsidian alone.
- Critical flaw mitigations documented (model lock, write-ahead, namespace isolation, dual-stream truth).
- Rename/move/delete behaviors are handled (or reconciled) so the index does not rot over time.
- Minimal schema validation exists (malformed notes fail visibly rather than silently degrading recall).

## Parked (future aspirations — do not implement in Phase 1)
These are intentionally deferred. If you start them, you’ll likely break the MVP focus.
- Adversarial evaluation and automated “red-team” checks
- Multi-model embeddings and automatic model switching
- Cross-machine or team-shared memory with access controls
- Full production ops (HA, multi-node, backups for volatile stores, disaster recovery)
- Tool-specific integrations beyond the minimum retrieval/indexing loop

## Phase 2+ (placeholders only)
- TODO: Define Phase 2 objective (one sentence)
- TODO: Define gating criteria (what must be stable in Phase 1 before starting)
- TODO: Add ADRs as each new phase introduces non-trivial decisions

