# MCP setup: Cursor ↔ Obsidian `00_LLM_Cache` only

Purpose: Satisfy Phase 1 **namespace isolation** — retrieval must not ingest your entire vault as noise.

## Goal

- Cursor (via **Model Context Protocol**) can search/read **only** the folder `00_LLM_Cache` inside your vault.

## Steps (conceptual)

MCP servers vary by implementation (official Obsidian MCP, community vault servers, etc.). Common pattern:

1. Install or enable the **Obsidian / vault** MCP server in Cursor (**Settings → MCP** or project MCP config).
2. In the server configuration, set the **vault root** to your Obsidian vault path.
3. Set **allowed paths**, **include globs**, or **root subdirectory** so tools only see:

   `.../Vault/00_LLM_Cache/**`

4. **Verify:** create `00_LLM_Cache/_mcp_probe.md` with a unique string; in Cursor, use the MCP resource/search tool to open it. A note **outside** that folder should **not** appear in scoped search.

## Acceptance checklist

- [ ] MCP can read `_mcp_probe.md` from `00_LLM_Cache`.
- [ ] A file in e.g. `Daily Notes/` is **not** returned by scoped cache search.
- [ ] After rename of a cache note, MCP still resolves the new path (or you accept reindex delay until sync runs).

## References

- Phase 1 scope: `docs/phase-1-shared-cache-mvp.md`
- Note schema: `docs/contracts/cache-note-schema-v1.md`
