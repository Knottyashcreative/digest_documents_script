# Document ingestion engine (Phase output)

Purpose: This repository’s **deliverable script** converts arbitrary supported documents into **preformatted Obsidian Markdown** with YAML frontmatter, optional chapter splitting, spindle navigation, and integrity metadata.

## Artifact locations

| Artifact | Path |
|---------|------|
| Engine | [`obsidian_pro_master.py`](../obsidian_pro_master.py) (repo root) |
| Configuration | [`config.json`](../config.json) |
| Dependencies | [`requirements.txt`](../requirements.txt) |

## Quick start

```bash
cd /path/to/digest_documents_script
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm   # optional; entity tags skipped if missing

python obsidian_pro_master.py --config config.json --input /path/to/input_dir --output /path/to/vault_folder
```

Optional GUI:

```bash
python obsidian_pro_master.py --config config.json --gui
```

CLI flags:

- `--no-skip` — reprocess every file even if `process_log.json` has a success entry for that SHA-256
- `--recursive` — include supported files in subfolders (`rglob`)

## Outputs per source file

- One or more `.md` notes: `{sanitized_stem}_{NN}_{slug}.md`
- One index note: `{sanitized_stem}_Index.md` linking all parts
- Each note includes YAML (source, `sha256`, chapter info, tags, concepts, `processed_at`, optional `warnings`)
- Footer **Navigation**: previous | index | next (wikilinks match actual basenames)

## Operational files

- `process_log.json` — keyed by **SHA-256** of input bytes; skip successful hashes on reruns unless `--no-skip`
- `error_log.csv` — append-only failures

Paths are relative to the **current working directory** unless you override in config (see `system_settings.log_file` / `error_log`).

## Critical limitations (honest)

- **MarkItDown**: optional for **`.md` / `.txt` / `.markdown`** (read as UTF-8); required for PDF/DOCX/PPTX/etc. If absent, YAML `warnings` will include `markitdown_unavailable` for plain-text inputs.
- **Image-only PDFs**: extraction may be near-empty; `warnings` will include `low_content` when below `low_content_threshold_chars`. OCR is not enabled unless you add a separate pipeline (`pkm_settings.ocr_enabled` is reserved).
- **spaCy**: optional; missing model → no entity tags, `user_tags` still apply.
- **Chapter regex**: invalid patterns raise a clear error; patterns with inner `(...)` capturing groups are safe (splitting uses `finditer`, not `re.split`).

## Design guarantees implemented in code

- **SHA-256** for dedupe and logging (not MD5)
- **Atomic writes** (temp file + replace) per note
- **Partial failure rollback**: if writing a multi-chapter document fails mid-way, already-written outputs for that source are removed
- **Basename collision avoidance** (suffix append when two chapters would share the same filename)
- **Worker fault isolation**: a crash in one parallel worker returns a failed result instead of killing the whole pool

For the broader “shared cache / vault” architecture, see `phase-1-shared-cache-mvp.md` and `roadmap.md`.
