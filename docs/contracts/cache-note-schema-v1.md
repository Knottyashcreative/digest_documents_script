# Contract: `00_LLM_Cache` Obsidian note (schema v1)

Purpose: **Source of truth** for human-readable cache notes. Redis/indexer must be rebuildable from files matching this contract.

Version: **1** (`schema_version: 1` in frontmatter)

## Required YAML properties

Every note MUST have these keys (types as specified):

| Key | Type | Notes |
|-----|------|--------|
| `schema_version` | int | Must be `1` until this contract bumps |
| `uuid` | string | Stable note instance id (UUID v4 or ULID recommended) |
| `fingerprint` | string | Hash of canonicalized “solution” + keyed constraints (see `phase-1-shared-cache-mvp.md`) |
| `adversarial_status` | string | One of: `tentative`, `verified`, `deprecated` |
| `similarity_gate` | number | Threshold used when this note participates in retrieval (e.g. `0.94`) |
| `embedding_model` | string | Must match the active vector index model id (see [ADR 0002](../adr/0002-embedding-model-phase1-lock.md)) |
| `source` | string or mapping | At minimum: identify origin; if mapping, use `project` and `context` string fields |

Optional but recommended:

- `tags` (list of strings)
- `mtime_obsidian` or indexer-maintained `source_path` / `mtime` in Redis only (path may live in Redis metadata to avoid duplicating long paths in every note—your choice; if absent in note, indexer must still record path in Redis)

## Required markdown sections

Body MUST include these level-2 headings (order flexible):

- `## Problem`
- `## Solution`
- `## Why it works`
- `## Lessons learned`

Heading text is matched **case-insensitively** after normalizing whitespace.

## Validation

Run:

```bash
python scripts/validate_llm_cache.py --root /path/to/vault --folder 00_LLM_Cache
```

Non-zero exit = at least one invalid note (prints paths + reasons).

The validator parses **only the first YAML block** between line-delimited `---` markers (so horizontal rules `---` later in the body do not break parsing). Repo smoke fixture: `fixtures/vault/00_LLM_Cache/valid_cache_note.example.md`.

## Versioning

- Bump `schema_version` only when required keys or section names change.
- When bumping: add `cache-note-schema-v2.md`, new ADR if needed, and a migration note for n8n/indexer.
