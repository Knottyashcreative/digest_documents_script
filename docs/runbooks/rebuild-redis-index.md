# Runbook: Rebuild Redis vector index from `00_LLM_Cache`

Purpose: Prove **Obsidian is SSoT** — Redis can be discarded and recreated from notes.

## Preconditions

- Vault path known (e.g. `/path/to/Vault/00_LLM_Cache`).
- Schema validation passes:

  ```bash
  python scripts/validate_llm_cache.py --root /path/to/Vault --folder 00_LLM_Cache
  ```

- `embedding_model` in notes matches indexer config (see [ADR 0002](../adr/0002-embedding-model-phase1-lock.md)).

## Procedure (generic)

Commands vary by stack (Redis Stack CLI, custom worker, n8n). Conceptual steps:

1. **Stop writers** (optional but avoids racing during wipe): pause n8n workflow or indexer cron.
2. **Wipe volatile index** (example keys—adjust to your key pattern):
   - Delete all keys under your index prefix, **or** flush the logical DB if isolated.
3. **Full scan**: walk every `*.md` in `00_LLM_Cache`.
4. For each file:
   - Parse frontmatter; confirm `embedding_model` and `fingerprint`.
   - Compute embedding with the **locked** model.
   - Upsert Redis: vector + metadata per [redis-vector-metadata-v1.md](../contracts/redis-vector-metadata-v1.md).
5. **Smoke test**: run a known query in RedisInsight or your client; expect the same top hit as before rebuild (given same model and data).

## Success criteria

- Document count in index == `.md` count in folder (minus non-cache files if any).
- Random sample: note `uuid` resolves to correct `source_path` in Redis.

## Rollback

Re-run rebuild from vault; there is no “old Redis state” worth keeping if Obsidian is canonical.
