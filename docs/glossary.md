# Glossary

Purpose: Define the terms we use in code, APIs/contracts, and UX. This file prevents ambiguity and inconsistent naming.

## Rules
- **One term = one meaning**. If a word is overloaded, split it into distinct terms (e.g., `Account` vs `BillingAccount`).
- **Prefer project terms over synonyms**. Use the canonical term below in code, docs, and UI.
- **If it’s used in a contract** (API/event/schema), it must be defined here or in a linked contract glossary.

## Canonical terms

Use this format for each entry:
- **Term**: TODO: `CanonicalName`
  - **Definition**: TODO
  - **Where used**: TODO: (code, API, UI, ops, data)
  - **Related terms**: TODO
  - **Forbidden synonyms / don’t say**: TODO: list ambiguous alternatives
  - **Notes**: TODO: edge cases, time semantics, units, constraints

### Seed entries (edit/replace)
- **User**
  - **Definition**: TODO: Who/what counts as a “user” in this system?
  - **Where used**: TODO
  - **Related terms**: TODO: Account, Admin, Identity
  - **Forbidden synonyms / don’t say**: TODO: “customer”, “member”, etc. (pick one)

- **Account**
  - **Definition**: TODO
  - **Where used**: TODO
  - **Related terms**: TODO
  - **Forbidden synonyms / don’t say**: TODO

## Naming & formatting conventions
- **Identifiers**: TODO: (UUID/ULID/etc.), case (lower_snake vs camel), exposure rules (public vs internal)
- **Timestamps**: TODO: timezone (UTC?), format (RFC3339?), precision
- **Money/units**: TODO: currency representation, unit fields, rounding rules
- **Statuses/enums**: TODO: naming, unknown/unspecified rules, forward compatibility

