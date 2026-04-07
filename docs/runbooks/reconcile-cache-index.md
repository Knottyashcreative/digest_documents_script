# Runbook: Reconcile Redis index with Obsidian filesystem

Purpose: Fix **index rot** after renames, moves, or deletes without requiring a full rebuild (or use as cheaper periodic hygiene).

## When to run

- After bulk renames in `00_LLM_Cache`.
- On a schedule (e.g. daily) if event-driven delete handling is not implemented yet.

## Procedure

1. **List filesystem truth**: all `*.md` under `00_LLM_Cache` with `(fingerprint or uuid, resolved_path, mtime_ms)`.
2. **List Redis truth**: all indexed docs with `source_path` / `fingerprint` / `mtime_ms` (whatever you stored).
3. **Diff**:
   - **Orphan Redis rows**: path not on disk → **delete** key / vector entry.
   - **Missing Redis rows**: file on disk but not indexed → **enqueue upsert** (same as incremental indexer).
   - **Stale mtime**: path matches but `mtime_ms` older on Redis than on disk → **re-read file and re-embed** (content changed).

## Implementation options

- **n8n** scheduled workflow: HTTP to small service, or Redis + filesystem script.
- **One-shot script** (future in repo): `scripts/reconcile_index.py` — placeholder for your environment.

## Invariants

- Never delete Obsidian files from this job—only index rows.
- Prefer `fingerprint` as stable identity; `source_path` may change on rename (update row, don’t duplicate).
