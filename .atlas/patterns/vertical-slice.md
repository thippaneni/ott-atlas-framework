# Vertical Slice Pattern

## Metadata

- Version: 0.1.0
- Status: Draft
- Layer: Patterns
- Depends on: standards/coding.md, standards/api.md, rules/naming.yaml, rules/validation.yaml

## Purpose

Organize feature work around complete user or business capabilities instead of horizontal technical layers.

## Scope

Use this pattern for backend APIs, frontend features, and end-to-end feature implementation in Atlas projects.

## Guidance

- Start from a feature specification or story.
- Keep request handling, validation, business behavior, persistence, and tests close to the feature boundary.
- Avoid scattering a single feature across unrelated folders without a clear reason.
- Keep shared abstractions small and proven by multiple slices.

## Example

A home loan eligibility feature may include the API endpoint, request validator, domain service, persistence query, response model, and tests in one feature slice.

## Best Practices

- Let specifications define the slice boundary.
- Keep each slice independently reviewable.
- Prefer explicit dependencies over global shared helpers.

## Anti-patterns

- Creating generic service layers before behavior is known.
- Sharing code between slices before duplication proves the need.
- Implementing slices without acceptance criteria.

## References

- ADR-0001
- ADR-0004
