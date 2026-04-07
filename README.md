# digest_documents_script

Single source of truth for **documentation** and the **Obsidian document-ingestion** tool that feeds structured notes into a vault (aligned with Phase 1 cache / PKM goals).

## Start here

- **Doc map**: [docs/README.md](docs/README.md)
- **Ingestion engine (code + runbook)**: [docs/document-ingestion-engine.md](docs/document-ingestion-engine.md)
- **Phase 1 scope (shared cache / learning loop)**: [docs/phase-1-shared-cache-mvp.md](docs/phase-1-shared-cache-mvp.md)
- **Roadmap & milestones**: [docs/roadmap.md](docs/roadmap.md)
- **Gaps / what’s left**: [docs/gap-analysis-outstanding.md](docs/gap-analysis-outstanding.md)

## Ingestion (quick)

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
# Optional: sudo apt install tesseract-ocr tesseract-ocr-eng  (for OCR on scans / images)
python obsidian_pro_master.py --config config.json --input /path/to/docs --output /path/to/vault
```

Details, PDF dual-path + cross-check, and OCR flags: [docs/document-ingestion-engine.md](docs/document-ingestion-engine.md).

**Phase 1 cache:** validate notes → [scripts/validate_llm_cache.py](scripts/validate_llm_cache.py); contracts → [docs/contracts/](docs/contracts/); ops → [docs/operations.md](docs/operations.md).

## Goals (explicit from project start)

| Area | Where it lives |
|------|----------------|
| Product intent | `docs/product-brief.md` |
| Vocabulary | `docs/glossary.md` |
| Architecture | `docs/architecture.md` |
| Contracts | `docs/contracts/` |
| Dev workflow | `docs/local-development.md`, `docs/daily-workflow-checklist.md` |
| Ops | `docs/operations.md` |
| Security | `docs/security.md` |
| ADRs | `docs/adr/` |
| Agent rules | `docs/AGENTS.md` |
