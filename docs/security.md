# Security

Purpose: Capture lightweight threat notes, trust boundaries, and security expectations. This is stack-agnostic by design.

## Threat model (lightweight)
- TODO: What are we protecting? (data, money, availability, reputation)
- TODO: Likely adversaries (curious users, malicious actors, insiders, bots)
- TODO: Top abuse cases (1–5 bullets)

## Trust boundaries
- TODO: Identify trust boundaries between actors and system components (see `architecture.md`).
- TODO: List the “entry points” (APIs, jobs, webhooks, CLIs, admin tools, etc.).

## Secrets management
- Example env template for local compose: **`.env.example`** at repo root (copy to `.env`, never commit secrets).
- TODO: Where secrets are stored (conceptually) and how they’re accessed locally vs in production.
- TODO: Rotation expectations and ownership.
- TODO: Rules: never commit secrets; how to handle leaked secrets.

## Authentication (placeholder)
- TODO: How identities are established (sessions, tokens, API keys, SSO, etc.).
- TODO: How we handle anonymous/guest access, if any.

## Authorization model (placeholder)
- TODO: What permissions model we use (RBAC/ABAC/custom).
- TODO: Where authorization is enforced (central gateway vs per-service).
- TODO: “Default deny” rule and audit expectations.

## Data protection
- TODO: Data classification (public/internal/confidential/regulated).
- TODO: Encryption at rest/in transit assumptions (leave vendor details TBD).
- TODO: Logging rules for sensitive fields (redaction/masking).

## Secure development checklist
- [ ] Inputs validated and bounded (size, type, rate).
- [ ] Least privilege for internal calls and data access.
- [ ] Safe error handling (no sensitive leaks).
- [ ] Dependency risks tracked (SCA approach TBD).
- [ ] Security-relevant events are logged (auth failures, permission denials, admin actions).

