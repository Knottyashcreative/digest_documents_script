# Crosswalk: ingestion engine YAML ↔ `00_LLM_Cache` schema

Purpose: Make explicit how [`obsidian_pro_master.py`](../obsidian_pro_master.py) output relates to the Phase 1 **cache note** contract in [`phase-1-shared-cache-mvp.md`](phase-1-shared-cache-mvp.md). The engine **does not** yet emit the full cache schema; merge manually or extend the script.

## Engine emits today (per note)

Typical frontmatter from the designer pipeline includes (non-exhaustive):

- `source`, `sha256`, `chapter`, `chapter_title`, `tags`, `concepts`, `content_source`, `processed_at`, `status` (from `yaml_template`), optional `warnings`, index note adds `role: index`.

## Cache requires (Phase 1 minimum)

From `phase-1-shared-cache-mvp.md`:

| Field | In engine today? | Action |
|-------|------------------|--------|
| `uuid` | No | Add (ULID/UUID v4) per note instance |
| `fingerprint` | No | Hash canonical **Solution** body + key constraints (document rule in note) |
| `adversarial_status` | No | Default `tentative`; set to `verified` after human/review gate |
| `similarity_gate` | No | Set default (e.g. `0.94`) in template or per-asset |
| `embedding_model` | No | Set when Redis index is wired; must match index |
| `schema_version` | No | Set `1` |
| `source.project` / `source.context` | Partial (`source` is filename string) | Split into structured fields or map filename → project |
| Sections: Problem, Solution, Why it works, Lessons learned | No (ingestion is generic markdown) | **Restructure** imported content or use ingestion only for **non-cache** paths |

## Recommended workflows

1. **General vault import** — output to e.g. `Ingest/`; no change to cache schema required.
2. **Programming cache (`00_LLM_Cache`)** — either:
   - **Manual:** paste engine output into the required section layout and fill cache frontmatter; or  
   - **Future:** add `--profile cache` (or separate script) that wraps body in the four sections and computes `fingerprint` from the Solution block.

## Integrity overlap

- Engine **`sha256`** = hash of **input file bytes** (provenance).  
- Cache **`fingerprint`** = hash of **logical solution** (dedupe across projects).  
Keep **both**; they answer different questions.

## Validation before indexing

Notes destined for `00_LLM_Cache` should pass:

```bash
python scripts/validate_llm_cache.py --root /path/to/Vault --folder 00_LLM_Cache
```

See [cache-note-schema-v1.md](contracts/cache-note-schema-v1.md).
