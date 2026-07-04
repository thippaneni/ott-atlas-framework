# Testing Checklist

## Metadata

- Version: 0.1.0
- Status: Draft
- Layer: Checklists
- Depends on: standards/testing.md, skills/testing.md, rules/validation.yaml

## Purpose

Verify that implementation behavior is covered by meaningful tests and acceptance checks.

## Checklist

- [ ] Tests trace to specifications or acceptance criteria.
- [ ] Success paths are covered.
- [ ] Important edge cases are covered.
- [ ] Expected validation, authorization, conflict, not-found, and domain failure paths are covered where relevant.
- [ ] Integration tests cover database, API, or framework wiring risks where needed.
- [ ] Tests are deterministic and repeatable.
- [ ] Manual verification steps are documented when automation is not practical.
- [ ] Known test gaps and residual risks are documented.

## Completion Criteria

The change is ready when critical behavior is verified and remaining gaps are explicit.
