# Domain-Driven Design Pattern

## Metadata

- Version: 0.1.0
- Status: Draft
- Layer: Patterns
- Depends on: standards/coding.md, rules/naming.yaml

## Purpose

Keep software aligned with the business domain and use business language in models, rules, and conversations.

## Scope

Use this pattern for domain modeling, business rules, aggregates, value objects, and service boundaries.

## Guidance

- Model the domain using ubiquitous language from specifications.
- Keep domain rules close to the model they protect.
- Use value objects for meaningful concepts with validation rules.
- Keep infrastructure concerns out of core business logic.

## Example

For home loans, concepts such as applicant, income, obligation, property, eligibility, lender policy, and repayment capacity should be explicit domain terms.

## Best Practices

- Validate domain language with product and domain stakeholders.
- Prefer clear business names over technical shortcuts.
- Capture ambiguous rules in specifications before coding.

## Anti-patterns

- Anemic models that only hold data while rules live elsewhere.
- Generic names that hide business meaning.
- Infrastructure-first design.

## References

- ADR-0001
- standards/coding.md
