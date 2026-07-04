# Repository Pattern

## Metadata

- Version: 0.1.0
- Status: Draft
- Layer: Patterns
- Depends on: standards/database.md, rules/database.yaml

## Purpose

Encapsulate persistence access where it improves testability, domain clarity, or boundary control.

## Scope

Use this pattern for aggregate persistence, complex queries, and persistence boundaries in .NET and PostgreSQL-backed systems.

## Guidance

- Prefer repositories around meaningful aggregates or query boundaries.
- Avoid generic repositories that only duplicate ORM APIs.
- Keep persistence details out of domain logic.
- Use direct ORM/query access when a repository adds no clarity.

## Example

A lender policy repository may load active policy rules for eligibility evaluation while hiding table structure from the domain service.

## Best Practices

- Keep repository methods intention-revealing.
- Separate read models from write aggregates where useful.
- Test persistence behavior at the integration boundary.

## Anti-patterns

- One generic repository for every entity.
- Repositories that expose IQueryable or leak persistence internals.
- Mock-heavy tests that do not verify real database behavior where it matters.

## References

- rules/database.yaml
- standards/testing.md
