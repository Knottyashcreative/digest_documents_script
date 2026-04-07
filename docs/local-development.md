# Local development

Purpose: How to run and iterate on **this** repo locally, plus placeholders for broader Phase 1 ops (Docker, Redis, n8n).

## This repository (`digest_documents_script`)

### Prerequisites

- **Python 3.10+** (3.12 tested)
- **`pip`** / venv
- **Optional (OCR):** Tesseract on `PATH` (e.g. `apt install tesseract-ocr tesseract-ocr-eng`)

### Setup

```bash
git clone https://github.com/Knottyashcreative/digest_documents_script.git
cd digest_documents_script
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm   # optional
```

### Run ingestion (CLI)

```bash
python obsidian_pro_master.py --config config.json --input /path/to/documents --output /path/to/vault_out
# Optional: --recursive  --no-skip
python obsidian_pro_master.py --config config.json --gui
```

### Quick sanity check (compile)

```bash
python -m py_compile obsidian_pro_master.py
python scripts/validate_llm_cache.py --help
```

### Test (placeholder)

There is **no** `pytest` suite in-repo yet. See `gap-analysis-outstanding.md` (P1 backlog).

---

## Phase 1 ops (not in this repo yet)

When you add Redis, n8n, or Docker:

- Document **exact** compose paths, env files, and startup commands under `operations.md`.
- Add a **`.env.example`** at repo root (no secrets) listing `N8N_*`, Redis URLs, vault path, etc.

---

## Generic placeholders (other services)

- **Prefix / casing:** prefer `SCREAMING_SNAKE_CASE` for env vars; use a short prefix when multiple tools share a host.
- **Secrets:** never commit real keys; use `.env` (gitignored) + `.env.example` (committed patterns only).
