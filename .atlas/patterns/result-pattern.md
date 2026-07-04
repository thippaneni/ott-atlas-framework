# Result Pattern

## Metadata

- Version: 0.1.0
- Status: Draft
- Layer: Patterns
- Depends on: rules/errors.yaml, rules/api.yaml, standards/testing.md

## Purpose

Represent expected success and failure outcomes explicitly instead of relying on exceptions for normal business flow.

## Scope

Use this pattern for .NET services, domain operations, API handlers, validation, and integration boundaries.

## Guidance

- Use result objects for expected validation, domain, conflict, authorization, and not-found outcomes.
- Reserve exceptions for unexpected system failures.
- Map result failures to documented API error contracts.
- Ensure tests cover both success and failure outcomes.

## Example

A loan affordability calculation can return success with computed eligibility or failure with a domain error explaining missing income data.

## Best Practices

- Keep error codes stable and documented.
- Avoid leaking internal details through result messages.
- Make failures easy for callers to handle.

## Anti-patterns

- Returning null for failed business operations.
- Throwing exceptions for expected validation failures.
- Creating one generic failure for every error mode.

## References

- rules/errors.yaml
- rules/validation.yaml
