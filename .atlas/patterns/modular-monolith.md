# Modular Monolith Pattern

## Metadata

- Version: 0.1.0
- Status: Draft
- Layer: Patterns
- Depends on: standards/coding.md, standards/database.md

## Purpose

Build a deployable monolith with strong internal module boundaries so the system can evolve without premature distributed complexity.

## Scope

Use this pattern for early and mid-stage SaaS products where domain boundaries are known but independent services are not yet justified.

## Guidance

- Organize code by business modules and bounded contexts.
- Keep module dependencies explicit and directional.
- Avoid direct data ownership violations across modules.
- Extract services only when operational, scaling, or ownership needs justify the cost.

## Example

A home loan platform may start with modules for identity, borrower profile, loan eligibility, lender offers, documents, and notifications in one deployable application.

## Best Practices

- Keep public module contracts small.
- Use architecture tests or review checklists to protect boundaries.
- Document module dependencies in architecture decisions.

## Anti-patterns

- Creating microservices before module boundaries are stable.
- Sharing database tables freely across modules.
- Letting all modules depend on all other modules.

## References

- ADR-0004
- standards/database.md
