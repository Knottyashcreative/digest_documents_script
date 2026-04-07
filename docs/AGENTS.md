# Rules for coding agents

Purpose: Provide enforceable rules for AI coding agents so code changes stay aligned with project intent, vocabulary, architecture, and contracts.

## Hard rules (follow every time)
- **Start at `docs/README.md`** to find the correct doc(s) before changing code.
- **Use the vocabulary in `docs/glossary.md`**. If you need a new term, add it before implementing.
- **Read relevant ADRs in `docs/adr/`** before making decisions that touch architecture, contracts, data, security, or operations.
- **Treat `docs/contracts/` as the interface source of truth**. Do not implement “silent” contract changes.
- **Update docs when behavior changes**: if code behavior, data shape, error semantics, or operational behavior changes, update the corresponding doc(s) in the same change.
- **No stack/vendor assumptions** unless explicitly provided by the project docs or the user.
- **Prefer smallest coherent change**: keep PRs atomic; separate refactors from behavior changes.
- **Testing is part of the feature**: add/update tests appropriate to the change (exact tooling may be TBD; document what you did).
- **Logging over printing**: avoid `print` in code paths that might ship; follow the repo’s logging conventions once defined.
- **Secrets never in git**: do not add credentials, tokens, or real secrets to the repo; use `.env.example` patterns.
- **Be explicit about breaking changes**: if a change could break consumers, document it and follow the contract breaking-change rules.
- **Operational readiness**: if the change affects deploy/rollback/observability, update `docs/operations.md`.

## Working routine (use this checklist)
- Follow `docs/daily-workflow-checklist.md` for step-by-step execution and review.
- Before changing or indexing `00_LLM_Cache` notes, run `python scripts/validate_llm_cache.py --root <vault> --folder 00_LLM_Cache` and fix failures.

## If information is missing
- Add `TODO:` prompts in the most relevant doc rather than guessing.
- If multiple implementations are valid, record the trade-off in an ADR draft.

