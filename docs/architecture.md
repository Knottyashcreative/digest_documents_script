# Architecture

Purpose: Describe system boundaries, ownership, and how parts interact. Keep external dependencies as black boxes until named.

## Context (what this system is)
- TODO: 2–5 sentences describing what the system does.
- TODO: What the system is *not* responsible for.

## Key principles
- TODO: e.g., “contracts-first”, “backwards compatible changes”, “auditable changes”, “least privilege”

## System boundaries & ownership

List “containers” (services, apps, libraries, jobs, etc.) and what each owns.

Use this template per container:
- **Container**: TODO: Name
  - **Responsibilities (owns)**: TODO
  - **Does not own**: TODO
  - **Primary inputs**: TODO: requests/events/files
  - **Primary outputs**: TODO: responses/events/files
  - **Persistence**: TODO: data it owns (conceptually; vendor TBD)
  - **Dependencies (black boxes)**: TODO: external systems (treat as opaque)

## External dependencies (black boxes for now)
- TODO: List external systems with a one-line purpose each (no vendor assumptions).

## Runtime flows (optional)
- TODO: Add a sequence diagram for the top 1–2 flows once known.

```mermaid
sequenceDiagram
  participant Actor as Actor
  participant System as System
  participant External as ExternalDependency
  Actor->>System: TODO: Request / trigger
  System->>External: TODO: Call / publish
  External-->>System: TODO: Response / event
  System-->>Actor: TODO: Result
```

## Cross-cutting concerns
- **Configuration**: TODO: how configuration is loaded and validated
- **Errors**: TODO: error taxonomy + what is safe to expose externally
- **Authn/Authz**: TODO: where identity is established; where permissions enforced
- **Observability**: TODO: logs/metrics/traces conventions and key signals
- **Data ownership**: TODO: which container is the source of truth per entity

## Non-functional requirements (placeholders)
- TODO: latency/throughput targets
- TODO: availability/reliability targets
- TODO: cost constraints
- TODO: privacy/compliance constraints

