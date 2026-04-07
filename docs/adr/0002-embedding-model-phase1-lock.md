# ADR 0002: Lock embedding model for Phase 1 vector index

Status: Accepted

## Context

Embedding vectors are not comparable across different models or dimensions. Switching models without a full reindex corrupts similarity search and erodes trust in the shared cache.

## Decision

For **Phase 1**, we standardize on this **embedding model identifier** for all new index entries and `00_LLM_Cache` notes:

- **`nomic-embed-text-v1.5`** (record the exact provider/runtime string you deploy, e.g. Ollama tag or API id, in your indexer config).

If your runtime only supports a different **single** model (e.g. `bge-m3`), adopt it **once** and treat this ADR as superseded by a new ADR that documents the swap + **mandatory full reindex**.

## Consequences

### Positive

- One namespace per index; comparable scores; simpler ops.

### Negative

- Changing model later requires an explicit ADR, **full reindex**, and possible downtime for search.

## Alternatives considered

- **Per-note mixed models** — rejected: breaks global retrieval quality.
- **No documented default** — rejected: guarantees silent drift.

## Follow-ups

- Ensure every note’s `embedding_model` field matches the indexer configuration.
- n8n or batch job: reject upsert if `embedding_model` mismatches index policy.

## Links

- `docs/phase-1-shared-cache-mvp.md`
- `docs/contracts/cache-note-schema-v1.md`
- `docs/contracts/redis-vector-metadata-v1.md`
