# Testing Skill

## Metadata

- Version: 0.1.0
- Status: Draft
- Layer: Skills
- Depends on: standards/testing.md, rules/validation.yaml, patterns/vertical-slice.md

## Purpose

Guide test strategy and verification across Atlas projects.

## Scope

Use for unit tests, integration tests, API tests, frontend tests, end-to-end tests, regression review, and acceptance validation.

## Best Practices

- Trace tests to specifications, acceptance criteria, and known risks.
- Cover success paths, important edge cases, and expected failure paths.
- Prefer integration tests where framework, database, or API wiring matters.
- Keep tests deterministic and readable.
- Document test gaps when risk remains.

## Anti-patterns

- Testing implementation details instead of behavior.
- Skipping failure paths for validation, authorization, and domain rules.
- Treating manual checks as permanent substitutes for automated tests.

## References

- standards/testing.md
- rules/errors.yaml
- rules/validation.yaml
