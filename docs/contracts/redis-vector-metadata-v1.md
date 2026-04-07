# Contract: Redis vector index metadata (mirror of note v1)

Purpose: Define **index-side** fields stored with each vector so the cache can be **rebuilt**, **reconciled**, and **deduped** without Obsidian losing truth.

Obsidian note remains **SSoT** for semantic content and most identity; Redis holds **derived** data plus operational fields.

## Required fields (per indexed document)

| Field | Type | Notes |
|-------|------|--------|
| `fingerprint` | string | Primary idempotent upsert key (same as note frontmatter) |
| `uuid` | string | Note instance id (same as note) |
| `embedding_model` | string | Must equal note’s `embedding_model`; index namespace is per model |
| `source_path` | string | Absolute or vault-relative path to the `.md` file |
| `mtime_ms` | int (optional) | File mtime in ms for reconcile (write-ahead checks) |
| vector | binary/float array | Product of `embedding_model`; dimension fixed per index |

## Upsert rules

1. **Write-ahead:** Upsert only after the `.md` exists on disk and passes schema validation (or after strict mtime/size stability window—implement in n8n/worker).
2. **Idempotency:** Same `fingerprint` replaces the prior row (no duplicate logic rows for the same fix).
3. **Delete/rename:** On note delete or path change, remove stale key or run **reconcile** job (compare Redis paths to filesystem).

## Rebuild procedure

See [runbook: rebuild Redis from vault](../runbooks/rebuild-redis-index.md).

## Out of scope v1

- Multi-tenant ACLs
- Cross-region replication
