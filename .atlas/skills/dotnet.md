# .NET Skill

## Metadata

- Version: 0.1.0
- Status: Draft
- Layer: Skills
- Depends on: standards/coding.md, standards/api.md, patterns/vertical-slice.md, patterns/result-pattern.md

## Purpose

Guide .NET backend implementation for Atlas projects.

## Scope

Use for ASP.NET Core APIs, application services, domain logic, validation, background work, and tests.

## Best Practices

- Implement from specifications and API contracts.
- Keep business logic testable and independent of infrastructure.
- Use explicit result handling for expected business failures.
- Validate inputs at API and application boundaries.
- Keep dependency injection registrations clear and minimal.
- Prefer integration tests for persistence and API behavior that depends on framework wiring.

## Anti-patterns

- Controllers or endpoints containing business logic.
- Generic abstractions that duplicate framework behavior.
- Exceptions for normal validation or domain failures.

## References

- patterns/result-pattern.md
- patterns/vertical-slice.md
- rules/api.yaml
- rules/errors.yaml
