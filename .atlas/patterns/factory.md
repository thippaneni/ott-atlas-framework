# Factory Pattern

## Metadata

- Version: 0.1.0
- Status: Draft
- Layer: Patterns
- Depends on: standards/coding.md, rules/validation.yaml

## Purpose

Centralize creation logic when objects require invariants, validation, or multi-step construction.

## Scope

Use this pattern for domain entities, value objects, integration clients, and complex configuration-backed objects.

## Guidance

- Use factories when constructors would become unclear or invalid states must be prevented.
- Keep factory methods intention-revealing.
- Validate required inputs before returning created objects.
- Keep factories close to the domain concept they create.

## Example

A loan application factory can ensure applicant identity, declared income, selected property, and consent data are present before creating an application.

## Best Practices

- Prefer simple constructors for simple objects.
- Return explicit results when creation can fail for expected business reasons.
- Test invariant enforcement.

## Anti-patterns

- Factory classes that only call constructors without adding meaning.
- Hidden side effects during object creation.
- Factories that bypass domain validation.

## References

- result-pattern.md
- standards/coding.md
