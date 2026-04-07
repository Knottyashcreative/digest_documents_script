# Gap analysis: critical elements, missing pieces, outstanding work

Purpose: Track what the **repository** supplies vs what **you** must run in your environment for Phase 1 complete.

## Executive summary

| Layer | Status |
|-------|--------|
| **Contracts + runbooks + validator** | **In repo:** `cache-note-schema-v1`, `redis-vector-metadata-v1`, MCP doc, rebuild/reconcile runbooks, ADR 0002 embedding lock, `scripts/validate_llm_cache.py`, `docker-compose.example.yml`, `.env.example`, `n8n/README.md` |
| **Live MCP / Redis / n8n instances** | **Your machine/host:** you start compose, import workflow, scope MCP, and execute acceptance tests |
| **Ingestion ↔ strict cache shape** | **Partial by design:** `obsidian_pro_master.py` is generic import; map to cache schema per [crosswalk-ingestion-to-cache.md](crosswalk-ingestion-to-cache.md) |

---

## Critical elements — resolution status

| Element | Resolved in repo | You still do |
|---------|------------------|--------------|
| **Embedding model lock** | [ADR 0002](adr/0002-embedding-model-phase1-lock.md) | Wire same id into actual embedder |
| **Note YAML + sections contract** | [cache-note-schema-v1.md](contracts/cache-note-schema-v1.md) | Author notes / migrate old files |
| **Redis metadata contract** | [redis-vector-metadata-v1.md](contracts/redis-vector-metadata-v1.md) | Implement in indexer code |
| **Malformed notes visible failure** | [validate_llm_cache.py](../scripts/validate_llm_cache.py) | Run in n8n/CI before upsert |
| **Rebuild from vault** | [rebuild-redis-index.md](runbooks/rebuild-redis-index.md) | Run once to prove |
| **Reconcile rename/delete** | [reconcile-cache-index.md](runbooks/reconcile-cache-index.md) | Schedule or implement deletes |
| **MCP folder isolation** | [mcp-setup-cursor.md](mcp-setup-cursor.md) | Configure Cursor + verify probe file |
| **Example stack** | [docker-compose.example.yml](../docker-compose.example.yml), [.env.example](../.env.example) | Copy, fill secrets, start |

---

## Missing / deferred (unchanged intent)

- **Filled product docs:** `product-brief.md`, `architecture.md` (beyond Phase 1 ops), `glossary.md`, etc. — still placeholders where not Phase-1-specific.
- **Committed n8n JSON export** — folder `n8n/` documents behavior; commit workflow when stable.
- **pytest CI** for `obsidian_pro_master.py` — backlog.
- **Automated `reconcile_index.py`** — runbook describes algorithm; script optional.

---

## P0 checklist (environment)

- [ ] `validate_llm_cache.py` clean on real vault.
- [ ] MCP probe passes (`mcp-setup-cursor.md`).
- [ ] Redis rebuild runbook executed once.
- [ ] Indexer enforces validate-before-upsert (`n8n/README.md`).

---

## Related

- [phase-1-shared-cache-mvp.md](phase-1-shared-cache-mvp.md)  
- [operations.md](operations.md)  
- [roadmap.md](roadmap.md)  
