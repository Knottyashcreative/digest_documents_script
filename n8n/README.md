# n8n workflows (Phase 1 indexer)

Purpose: Document what the **Obsidian → Redis** synchronizer must do. Export committed workflows here when ready (e.g. `workflows/index-cache.json`).

## Required behavior

1. **Scope:** Only watch `00_LLM_Cache/**/*.md` (absolute path from vault root).
2. **Write-ahead:** After a file save event, confirm the file exists and mtime is stable (debounce 1–3 s optional) before embedding + Redis upsert.
3. **Validate first:** Run `python scripts/validate_llm_cache.py --root <vault> --folder 00_LLM_Cache` or equivalent in-node logic; on failure, alert and **skip** upsert (no silent bad rows).
4. **Upsert key:** Use `fingerprint` from frontmatter as idempotent key (plus `embedding_model` namespace).
5. **Metadata:** Store at minimum fields from [docs/contracts/redis-vector-metadata-v1.md](../docs/contracts/redis-vector-metadata-v1.md).
6. **Deletes:** On file delete, remove Redis row for that `fingerprint` / `uuid` or rely on periodic [reconcile](../docs/runbooks/reconcile-cache-index.md).

## Embedding

Use the model locked in [ADR 0002](../docs/adr/0002-embedding-model-phase1-lock.md). Changing model → new ADR + full reindex per [rebuild runbook](../docs/runbooks/rebuild-redis-index.md).
