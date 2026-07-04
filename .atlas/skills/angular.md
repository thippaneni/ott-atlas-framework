# Angular Skill

## Metadata

- Version: 0.1.0
- Status: Draft
- Layer: Skills
- Depends on: standards/coding.md, standards/testing.md, rules/validation.yaml

## Purpose

Guide Angular frontend implementation for Atlas projects.

## Scope

Use for Angular applications, feature modules, components, services, state, routing, forms, and UI tests.

## Best Practices

- Build from UI design, feature specifications, and API contracts.
- Keep components focused on presentation and interaction.
- Keep data access and business workflow orchestration in services or feature state.
- Validate forms close to user input and mirror backend validation where needed.
- Prefer accessible, responsive, and predictable UI behavior.
- Keep feature folders aligned with vertical slices where practical.

## Anti-patterns

- Components that mix UI, API calls, mapping, and business decisions without boundaries.
- Hardcoded API contracts not linked to specifications.
- UI behavior that only exists in code and not in acceptance criteria.

## References

- standards/testing.md
- rules/api.yaml
- rules/validation.yaml
