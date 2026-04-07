# Data

Purpose: Define the conceptual data model (entities, relationships, identifiers) and migration strategy without assuming any specific datastore vendor.

## Entities (inventory)
List each entity the system cares about. Keep this vendor-agnostic and focused on invariants.

Use this per-entity template:
- **Entity**: TODO: Name
  - **Purpose**: TODO
  - **Owner (source of truth)**: TODO: which container owns it (see `architecture.md`)
  - **Identifier**: TODO: type + generation strategy
  - **Key fields**: TODO: (names + meaning)
  - **Invariants**: TODO: rules that must always hold
  - **Lifecycle/status**: TODO: states + transitions
  - **PII/sensitivity**: TODO: classification + retention needs

## Relationships
- TODO: List the important relationships (1:1, 1:many, many:many) and constraints.
- TODO: Consistency expectations (strong vs eventual) per relationship.

## Identifiers & time
- TODO: ID format (UUID/ULID/etc.) and whether IDs are guessable.
- TODO: Timestamp format (UTC?), and which timestamps are authoritative.
- TODO: Ordering needs (monotonic IDs? event ordering?)

## Migrations & backwards compatibility
- TODO: Migration strategy (expand/contract, dual-write, backfills).
- TODO: How we roll back safely when a migration is involved.
- TODO: Data retention, deletion, and archival rules (including “right to delete” if applicable).

## Data access boundaries
- TODO: Which components may read/write which entities.
- TODO: Whether other components can cache/replicate derived views (and invalidation rules).

