# API Pattern

## Metadata

- Version: 0.1.0
- Status: Draft
- Layer: Patterns
- Depends on: standards/api.md, rules/api.yaml, rules/security.yaml

## Purpose

Create APIs that are specification-driven, predictable, secure, and testable.

## Scope

Use this pattern for HTTP APIs, API contracts, request and response models, and integration endpoints.

## Guidance

- Define the API contract before implementation.
- Validate requests at the boundary.
- Use consistent response and error envelopes where the project adopts them.
- Keep authorization explicit and testable.
- Keep API behavior traceable to the feature specification.

## Example

A mortgage comparison endpoint should document required inputs, returned offers, validation errors, authorization behavior, and expected status codes before implementation.

## Best Practices

- Keep endpoint names resource-oriented.
- Keep request and response models stable.
- Version public contracts intentionally.

## Anti-patterns

- Adding undocumented endpoints.
- Returning inconsistent error shapes.
- Exposing internal exception details.

## References

- standards/api.md
- rules/api.yaml
