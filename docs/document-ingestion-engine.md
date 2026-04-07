# Document ingestion engine (Phase output)

Purpose: Convert **multiple document and image formats** into **Obsidian-ready Markdown** with YAML frontmatter, optional chapter splitting, spindle navigation, integrity metadata, **PDF cross-checking**, and **optional OCR**.

## Artifact locations

| Artifact | Path |
|---------|------|
| Engine | [`obsidian_pro_master.py`](../obsidian_pro_master.py) |
| Configuration | [`config.json`](../config.json) |
| Dependencies | [`requirements.txt`](../requirements.txt) |

## Quick start

```bash
cd /path/to/digest_documents_script
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm   # optional

# Linux: OCR needs Tesseract on PATH (example Debian/Ubuntu)
# sudo apt install tesseract-ocr tesseract-ocr-eng

python obsidian_pro_master.py --config config.json --input /path/to/input_dir --output /path/to/vault_folder
```

Optional GUI: `python obsidian_pro_master.py --config config.json --gui`

CLI: `--no-skip`, `--recursive`, `--doctor`

Preflight check (recommended):

```bash
python obsidian_pro_master.py --config config.json --doctor
```

## Extraction pipeline (by type)

| Input | Primary path | Fallback / cross-check |
|--------|----------------|-------------------------|
| `.md`, `.txt`, `.markdown` | UTF-8 read | If MarkItDown missing → still works; warning in YAML |
| `.pdf` | Microsoft **MarkItDown** | **PyMuPDF** full-document text; if both yield substantial text, **length-ratio cross-check** (configurable); if still **low text** and `ocr_enabled` → **per-page OCR** (capped pages, DPI configurable) |
| `.png`, `.jpg`, `.jpeg`, `.webp`, `.gif`, `.tif`, `.bmp` | **OCR** (if `ocr_enabled` + `images_ocr`) | Else `![[filename]]` embed + note to enable OCR |
| `.docx` | **MarkItDown** | Fallback: **python-docx** if MarkItDown missing |
| `.json`, `.csv`, `.xml` | stdlib parse → markdown | No MarkItDown required |
| `.html`, `.htm` | stdlib tag-strip → text | Readability fallback (not full HTML→MD) |
| `.pptx` | **MarkItDown** | Fallback: **python-pptx** if MarkItDown missing |
| `.xlsx` | **MarkItDown** | Fallback: **openpyxl** if MarkItDown missing |
| `.doc` | **MarkItDown** | No fallback provided (legacy format) |

YAML field **`content_source`** records the winning path, e.g. `markitdown`, `pymupdf`, `markitdown+pymupdf`, `ocr_pdf`, `ocr_image`, `utf8_plain`, `image_embed`.

## `pkm_settings` (OCR / PDF)

| Key | Meaning |
|-----|---------|
| `ocr_enabled` | Master switch for OCR on **images** and **low-text PDFs** |
| `images_ocr` | When true and `ocr_enabled`, raster images become OCR’d markdown sections |
| `ocr_langs` | Tesseract language string (e.g. `eng`, `fra+eng`) |
| `ocr_max_pdf_pages` | Max PDF pages to rasterize for OCR (cost control) |
| `ocr_dpi` | Render DPI for PDF→image before OCR |
| `pdf_pymupdf_text_fallback` | Extract text with PyMuPDF when MarkItDown alone is thin |
| `pdf_cross_check_markitdown_vs_pymupdf` | Emit **warning** if both extracts are long but **length ratio** &lt; threshold |
| `ocr_comparison_threshold` | Ratio in \((0,1]\); below → `cross_check:` warning (not auto-failure) |
| `prefer_longer_text_on_divergence` | When choosing between MarkItDown vs PyMuPDF text, prefer the longer |
| `require_markitdown_for_office_formats` | If true, `.docx` and other office formats hard-require MarkItDown |
| `fail_if_ocr_enabled_but_unavailable` | If true, treat missing OCR deps as a hard error (fail fast) |

## System dependencies (OCR)

Python packages alone are **not** enough: **Tesseract** must be installed and on `PATH` (so `pytesseract` can invoke it). Without it, OCR steps produce warnings and fall back to embeds or native PDF text only.

If you want OCR to be “required” (rather than best-effort), set `fail_if_ocr_enabled_but_unavailable=true` and use `--doctor` in your wrapper/CI.

## Outputs per source file

- Notes: `{sanitized_stem}_{NN}_{slug}.md` + `{stem}_Index.md`
- Front matter: `content_source`, `sha256`, tags, concepts, optional `warnings` (pipeline + cross-check + low-content notices)
- Footer spindle: previous | index | next

## Operational files

- `process_log.json`, `error_log.csv` (paths from `system_settings`)

## Step-by-step: convert an entire folder (including subfolders)

1) Create venv and install deps (once):

```bash
cd /path/to/digest_documents_script
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2) (Optional but recommended) Preflight your environment:

```bash
python obsidian_pro_master.py --config config.json --doctor
```

3) Convert everything under a folder recursively:

```bash
python obsidian_pro_master.py \
  --config config.json \
  --input "/path/to/source_folder" \
  --output "/path/to/obsidian_output_folder" \
  --recursive
```

4) Re-run to only process new/changed files (default behavior uses SHA-256 log):

```bash
python obsidian_pro_master.py --config config.json --input "/path/to/source_folder" --output "/path/to/obsidian_output_folder" --recursive
```

5) Force reprocess everything (ignores `process_log.json`):

```bash
python obsidian_pro_master.py --config config.json --input "/path/to/source_folder" --output "/path/to/obsidian_output_folder" --recursive --no-skip
```

## Honest limitations (“no flaws” is not guaranteed)

OCR and format conversion are **heuristic**. The design minimizes silent failure:

- **Garbage in / garbage out**: poor scans, skew, handwriting, or exotic fonts reduce OCR quality.
- **Dual PDF extracts** can disagree; we **warn** (`cross_check:`) rather than pretending certainty.
- **Chapters** still depend on your regexes; bad patterns → odd splits (but no regex split corruption from capturing groups).
- **Large PDFs**: CPU/time grows with `ocr_max_pdf_pages` × `ocr_dpi`; tune for your machine.
- **Security**: this tool reads user-chosen files and writes markdown; do not point it at untrusted paths without review.

## Design guarantees (engineering)

- SHA-256 for batch skip logic; atomic writes; rollback on partial multi-note failure
- Optional multiprocessing with worker recycling; isolated worker errors
- Invalid chapter regex → clear `ValueError` message

For shared-cache / vault architecture, see `phase-1-shared-cache-mvp.md` and `roadmap.md`.

**Schema alignment:** engine YAML is not the full `00_LLM_Cache` contract — see [`crosswalk-ingestion-to-cache.md`](crosswalk-ingestion-to-cache.md) and [`gap-analysis-outstanding.md`](gap-analysis-outstanding.md).
