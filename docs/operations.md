# Operations

Purpose: Deploy, run, and recover the **Phase 1 shared cache** stack and related tooling.

## Phase 1 stack (reference)

Typical components:

- **Obsidian vault** with folder `00_LLM_Cache/` (SSoT for cache notes).
- **Redis Stack** (vector + metadata “hot” store).
- **n8n** (or other worker) for validate → embed → upsert.
- **Cursor MCP** scoped to `00_LLM_Cache` only.

### Example Docker Compose

Copy and customize:

- [`docker-compose.example.yml`](../docker-compose.example.yml) at repo root  
- [`../.env.example`](../.env.example) → local `.env` (never commit secrets)

Start (after copy/rename):

```bash
docker compose -f docker-compose.yml up -d
```

**Resource limits:** `deploy.resources` in Compose is **ignored** by default Docker Compose v2; use `mem_limit` / `cpus` at service level if you need caps.

### Persistent paths (document yours)

| Data | Example path |
|------|----------------|
| Obsidian vault | *your machine* |
| Redis volume | `./data/redis` (example compose) |
| n8n state | `./data/n8n` (example compose) |

## Validation (before index / in CI)

```bash
python scripts/validate_llm_cache.py --root "$VAULT" --folder 00_LLM_Cache
```

Non-zero exit = fix notes before relying on search.

## Runbooks

- [Rebuild Redis from vault](runbooks/rebuild-redis-index.md)
- [Reconcile index vs filesystem](runbooks/reconcile-cache-index.md)

## MCP (Cursor)

- [mcp-setup-cursor.md](mcp-setup-cursor.md)

## n8n workflow expectations

- [n8n/README.md](../n8n/README.md)

## Phase 1 invariants (checklist)

- [ ] “Wipe Redis → rebuild” executed once successfully (see rebuild runbook).
- [ ] Malformed notes fail validation (script above), not silent skip in indexer design.
- [ ] Reconcile strategy chosen: event-driven deletes and/or periodic job.

## Environments

For a single-machine Phase 1, **local** may be sufficient. Add staging/prod rows when you promote beyond one box.

## Deploy / rollback (generic)

- **Deploy:** pull config, validate notes, restart indexer, rolling Redis updates if clustered later.
- **Rollback:** Redis is disposable — rebuild from vault; n8n rollback via export/version control.

## Observability (grow as needed)

- RedisInsight (`:8001` in example) for key counts / slow queries.
- n8n execution logs for failed validations or upserts.
- Optional: export metrics when you outgrow manual checks.

## Operational policies

Define locally: who may change `embedding_model`, who runs rebuilds, backup of **vault** (Redis optional if rebuild SLA is acceptable).
