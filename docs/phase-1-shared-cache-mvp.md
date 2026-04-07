# Phase 1 MVP: Shared Cache Module (Memory foundation)

Purpose: Define the smallest complete “shared cache” that reliably stores and retrieves validated programming/coding solutions across projects, and learns from queries by turning answers into reusable assets.

**Implementation status:** This file is the **spec**. What is shipped vs still open in the repo is tracked in [`gap-analysis-outstanding.md`](gap-analysis-outstanding.md). Ingestion output vs this note schema: [`crosswalk-ingestion-to-cache.md`](crosswalk-ingestion-to-cache.md).

## MVP scope (do now)
- **SSoT**: The Obsidian folder `00_LLM_Cache` is the *master record*.
- **Volatile accelerator**: Redis is a cache that can be rebuilt from Obsidian at any time.
- **Sync**: A synchronizer (e.g., n8n) watches `00_LLM_Cache` and upserts metadata + vectors into Redis.
- **Retrieval**: Cursor can retrieve from `00_LLM_Cache` via MCP (path-scoped to the folder) and/or via Redis-backed search (if wired later).
- **Learning loop**: For each resolved query, we create/update a cache note capturing: problem, verified solution, lessons learned, and tags.

## Phase 1 “plan of record” (what we will implement first)
- **Truth contract**: Obsidian frontmatter + sections are the canonical record for each asset.
- **Index contract**: Redis stores only derived/indexable data and must be rebuildable from Obsidian alone.
- **Keying strategy**:
  - **Primary key**: `fingerprint` (dedupe by “same logic” across projects).
  - **Secondary key**: `uuid` (note instance identity).
  - TODO: If you prefer the reverse (uuid-primary), document it here and update all tooling accordingly.
- **Lifecycle gate**: Retrieval should prefer `adversarial_status=verified` over `tentative`.

## Explicitly out of scope (park for later)
- “Adversarial specialist” audits and automated challenge suites
- Multi-embedding model support / model switching without reindex
- Cross-machine sync and multi-user access control
- Production-grade HA, backups for Redis, and distributed orchestration
- Vendor-specific optimizations beyond basic correctness and rebuildability

## Data model (Obsidian note = truth)

### Required frontmatter (minimum)
- `uuid`: TODO: stable unique ID for the note
- `fingerprint`: TODO: hash of canonicalized solution (used for dedupe)
- `adversarial_status`: `tentative` | `verified` | `deprecated`
- `similarity_gate`: TODO: default threshold for retrieval acceptance
- `embedding_model`: must match [ADR 0002](adr/0002-embedding-model-phase1-lock.md) and your indexer config
- `schema_version`: `1` (increment only when the note schema changes)
- `source`:
  - `project`: TODO
  - `context`: TODO: “error log”, “question”, “incident”, etc.

### Required sections (minimum)
- **Problem**: paste the error/log/question and constraints
- **Solution**: verified code or steps (copy/paste safe)
- **Why it works**: short explanation; key assumptions
- **Lessons learned**: pitfalls, gotchas, what to watch next time
- **Tags**: TODO: language, framework, topic

## Learning-from-queries workflow (SSoT-first)
1. **Capture** the query context (error log, stack trace, expected behavior).
2. **Answer** with a proposed solution.
3. **Verify** (at least one): reproduces fix; test passes; lint passes; command output; before/after evidence.
4. **Distill** into a note in `00_LLM_Cache` with the required structure.
5. **Index**: synchronizer upserts to Redis (vector + metadata).
6. **Reuse**: future queries should retrieve the note before generating new solutions.

## Critical flaws (MVP-breaking) and amended resolutions

### 1) Embedding vector drift (mixed models in one index)
- **Risk**: similarity search becomes unreliable; old vectors become incomparable.
- **MVP amendment**:
  - Store `embedding_model` in every note and in Redis metadata.
  - Enforce “one model per index namespace”; changing the model requires a full rebuild job.
  - **Locked for Phase 1:** see [ADR 0002](adr/0002-embedding-model-phase1-lock.md) (`nomic-embed-text-v1.5` or superseding ADR if you swap runtime).

### 2) Sync collision / partial writes
- **Risk**: Redis contains entries that don’t exist (or don’t match) on disk; retrieval returns ghosts.
- **MVP amendment**:
  - Implement write-ahead behavior: only upsert after file exists on disk and is stable (mtime/size check).
  - Use idempotent upserts keyed by `fingerprint` (preferred) or `uuid`.
  - Record `source_path` + `mtime` in Redis metadata.

### 3) Namespace pollution (retrieval returns noise)
- **Risk**: system retrieves irrelevant notes (daily logs, brainstorming) instead of verified fixes.
- **MVP amendment**:
  - Hard-scope MCP indexing to `00_LLM_Cache` only.
  - Add `adversarial_status` gating: default retrieval should prefer `verified`, then `tentative`.

### 4) Metadata siloing (truth split across Redis/Obsidian)
- **Risk**: backups restore notes but not essential metadata; cache becomes unrebuildable.
- **MVP amendment**:
  - Obsidian frontmatter must contain everything needed to rebuild Redis (model id, fingerprint, tags, status).
  - Redis stores only derived/index fields and can be wiped at any time.

### 5) Compose resource limits placebo
- **Risk**: “memory limits” aren’t actually applied; the system OOMs unpredictably.
- **MVP amendment**:
  - Treat memory limits as operational configuration; verify actual limits in your runtime (Compose vs Swarm differ).
  - Document the verified enforcement method in `docs/operations.md` once chosen.

### 6) Fingerprint instability (can’t dedupe or trust reuse)
- **Risk**: the same “solution” hashes differently due to whitespace, timestamps, ordering.
- **MVP amendment**:
  - Define a canonicalization rule for hashing (e.g., normalize line endings, strip trailing spaces).
  - Include what was hashed in the note (inputs: code block + constraints).

### 7) Deletes/renames not propagated (index rot)
- **Risk**: Obsidian notes get renamed/moved/deleted; Redis continues to return stale entries.
- **MVP amendment**:
  - Index must store `source_path` + `mtime`, and a stable identity (`uuid` + `fingerprint`).
  - Synchronizer must handle: create, update, rename/move, delete (or a periodic “reconcile” job).
  - If delete handling is hard initially: run a scheduled full reconcile (Obsidian directory is truth).

### 8) Schema drift (notes stop being parseable)
- **Risk**: frontmatter fields become optional/inconsistent; automation breaks silently.
- **MVP amendment**:
  - Add `schema_version: 1` now.
  - Enforce a minimal schema validator in the sync path (fail fast + log the note path).
  - Keep the schema intentionally small for Phase 1.

### 9) Secret/key hygiene (local keys treated as “just config”)
- **Risk**: committed encryption keys or tokens compromise the system; also makes restores brittle.
- **MVP amendment**:
  - Treat sync/orchestrator keys as secrets (do not hardcode in committed files).
  - Store secret-handling rules in `docs/security.md` and reference `.env.example` policy in `docs/local-development.md`.

### 10) Non-deterministic retrieval (no ranking/tie-break rules)
- **Risk**: similar queries return inconsistent notes; humans stop trusting the cache.
- **MVP amendment**:
  - Retrieval rule: prefer `verified`, then highest similarity, then newest `mtime`.
  - Require “why chosen” metadata in the retrieval response (at least: similarity score + status + fingerprint).

## MVP acceptance tests (must pass)

**Repo support today:** schema contract + validator CLI + runbooks + MCP doc + example compose + ADR embedding lock.  
**You still execute** MCP/Redis/n8n in your environment and tick these when true.

- [ ] Cursor can read a known test note from `00_LLM_Cache` via MCP — [setup](mcp-setup-cursor.md).
- [ ] Saving a new note triggers a Redis upsert (or documented manual reindex) — [n8n expectations](../n8n/README.md).
- [ ] Redis entries include `uuid`, `fingerprint`, `embedding_model`, `source_path`, `mtime`, and a vector — [contract](contracts/redis-vector-metadata-v1.md).
- [ ] Deleting Redis data and re-running indexing fully rebuilds the cache — [runbook](runbooks/rebuild-redis-index.md).
- [ ] Renaming/moving/deleting is handled — [reconcile runbook](runbooks/reconcile-cache-index.md).
- [ ] A malformed note is rejected visibly — `python scripts/validate_llm_cache.py` + indexer must skip/alert on failure — [note contract](contracts/cache-note-schema-v1.md).

