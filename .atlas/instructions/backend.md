# Backend Instruction

## Metadata

- Version: 0.1.0
- Status: Draft
- Layer: Instructions
- Depends on: skills/dotnet.md, skills/postgres.md, patterns/vertical-slice.md, patterns/result-pattern.md

## Purpose

Guide backend implementation for .NET, PostgreSQL, and API work.

## Scope

Use for API endpoints, application services, domain logic, validation, persistence, migrations, and backend tests.

## Instruction

- Load the feature specification, API contract, relevant standards, rules, and patterns before coding.
- Implement behavior as vertical slices where possible.
- Use result handling for expected validation and domain failures.
- Keep business rules independent of framework and infrastructure details.
- Validate inputs at the API boundary and domain invariants in the domain layer.
- Keep database changes traceable to domain or feature specifications.
- Add tests for success paths, failure paths, and important edge cases.

## Inputs

- Feature specification, API contract, domain model, database design, standards, rules.

## Outputs

- Backend implementation, tests, migration notes, implementation notes.

## Definition of Done

- Behavior matches specifications.
- API and database changes are documented.
- Tests cover business rules and important failures.
