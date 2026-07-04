# Tester Instruction

## Metadata

- Version: 0.1.0
- Status: Draft
- Layer: Instructions
- Depends on: skills/testing.md, standards/testing.md, rules/validation.yaml

## Purpose

Guide verification and test planning for Atlas projects.

## Scope

Use for unit, integration, API, frontend, end-to-end, regression, and acceptance testing.

## Instruction

- Start from acceptance criteria and specifications.
- Identify critical paths, edge cases, failure paths, and security-sensitive behavior.
- Prefer automated tests where behavior is stable and repeatable.
- Use integration tests for database, API, and framework wiring risks.
- Document test gaps and manual verification requirements.

## Inputs

- Specifications, acceptance criteria, implementation, risks, standards, rules.

## Outputs

- Test plan, test cases, validation notes, test gap report.

## Definition of Done

- Acceptance criteria are covered or gaps are documented.
- Important failures are tested.
- Results are reproducible.
