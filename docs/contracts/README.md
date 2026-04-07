# Contracts (Source of truth)

Purpose: Define and version the interfaces this project exposes and consumes (APIs, events, schemas). The exact format is TBD until chosen.

## What counts as a contract
- **API contracts**: TODO: REST/OpenAPI? GraphQL? gRPC? (pick one or more)
- **Event contracts**: TODO: event types, payload schemas, ordering/delivery semantics
- **Data schemas**: TODO: JSON schema / protobuf / Avro / other

## Where the source of truth lives
- TODO: Decide the authoritative contract artifact(s) and commit them under this folder.
- Suggested future structure (choose what applies):
  - `openapi/` (OpenAPI specs)
  - `graphql/` (schema files)
  - `events/` (event catalogs + payload schemas)
  - `schemas/` (shared JSON schemas or similar)

## Compatibility & versioning policy (checklist)

### General rules
- [ ] **Every contract change is reviewed as a product + engineering change** (not “just refactor”).
- [ ] **Consumers/providers must agree on ownership**: who defines and who implements.
- [ ] **Additive changes preferred**: add new fields/endpoints/event types without breaking old ones.
- [ ] **Explicit default behavior** for unknown fields/enum values (forward compatibility).

### Breaking change rules
- [ ] **Define what is breaking** for each contract type (API/event/schema) in this section.
- [ ] **Deprecation window**: TODO: how long old behavior remains supported.
- [ ] **Migration plan required**: docs + steps + rollback path.
- [ ] **Communication**: TODO: who needs to be notified, where announcements live.

### Versioning scheme
- TODO: Choose a versioning scheme for contracts (SemVer? date-based?).
- TODO: Define version bump rules (major/minor/patch semantics).
- TODO: Define how versions are negotiated (URL path, header, schema registry, topic, etc.).

## Contract review requirements (checklist)
- [ ] Contract change includes examples (requests/responses/events) and edge cases.
- [ ] Error semantics documented (status codes, error codes, retryability).
- [ ] Backwards compatibility assessed and documented.
- [ ] Tests added/updated for the contract boundary.
- [ ] Observability updates: logs/metrics for new paths or events.

