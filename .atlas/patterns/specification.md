# Specification Pattern

## Metadata

- Version: 0.1.0
- Status: Draft
- Layer: Patterns
- Depends on: ADR-0001, rules/validation.yaml

## Purpose

Represent business criteria as reusable, testable, and composable specifications.

## Scope

Use this pattern for eligibility rules, filtering, validation, and policy decisions.

## Guidance

- Use specifications for business rules that need names, reuse, composition, or testing.
- Keep specification names aligned with domain language.
- Avoid hiding complex behavior in anonymous predicates.
- Document how each specification traces to product or domain requirements.

## Example

A borrower eligibility specification can combine income sufficiency, credit score range, existing obligation limits, and property constraints.

## Best Practices

- Keep specifications small and composable.
- Test positive and negative cases.
- Link specifications to source requirements.

## Anti-patterns

- Turning every simple if statement into a specification.
- Combining unrelated rules into one large opaque specification.
- Implementing specifications without documented business meaning.

## References

- ADR-0001
- standards/testing.md
