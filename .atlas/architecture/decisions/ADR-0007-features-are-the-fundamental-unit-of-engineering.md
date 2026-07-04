# ADR-0007: Features Are the Fundamental Unit of Engineering

## Status

Accepted

## Date

2026-07-04

## Context

Atlas is designed for specification-driven, AI-assisted software engineering. As projects grow, implementation work can become scattered across repositories, modules, tickets, prompts, and commits. This weakens traceability and makes it harder for AI assistants and developers to understand why code exists.

HOOS needs a consistent way to organize every feature from business intent through release.

## Decision

Atlas SHALL treat features as the fundamental unit of engineering.

Every Atlas-managed feature SHALL have a stable feature ID, lifecycle state, and self-contained artifact package. Feature work SHALL progress through explicit lifecycle gates before implementation and release.

A feature package SHOULD include business context, specifications, acceptance criteria, domain model, architecture review, API contract, database design, UI contract, tasks, implementation notes, tests, reviews, documentation updates, and release notes where applicable.

For HOOS:

- Backend implementation SHALL target `hoos/HOOS-Backend`.
- Frontend implementation SHALL target `hoos/HOOS-Frontend`.
- Atlas/OpenSpec SHALL remain the source of truth for feature intent, lifecycle, and traceability.

## Consequences

Positive consequences:

- Strong traceability from business need to implementation.
- Better AI context loading for long-lived feature work.
- Clearer backend/frontend task boundaries.
- Repeatable readiness gates before implementation and release.
- Easier maintenance months after a feature ships.

Negative consequences:

- More upfront artifact creation before coding.
- Feature package discipline must be maintained.
- Some information may overlap with OpenSpec change artifacts unless conventions remain clear.

## Alternatives Considered

- Organize primarily by repository. Rejected because business context and implementation traceability become fragmented.
- Organize primarily by service or module. Rejected because features often cross backend, frontend, database, and documentation boundaries.
- Organize only by tickets. Rejected because tickets are not durable engineering memory and may not carry enough context for AI-assisted work.

## Related ADRs

- ADR-0001
- ADR-0003
- ADR-0004
- ADR-0005
