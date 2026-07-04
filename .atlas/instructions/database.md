# Database Instruction

## Metadata

- Version: 0.1.0
- Status: Draft
- Layer: Instructions
- Depends on: skills/postgres.md, standards/database.md, rules/database.yaml

## Purpose

Guide PostgreSQL database design, migration, integrity, and performance work.

## Scope

Use for schema design, migrations, indexing, query review, data constraints, and persistence verification.

## Instruction

- Start from the domain model, feature specification, or ADR.
- Protect business invariants with appropriate constraints.
- Keep migrations ordered, reviewable, and reproducible.
- Add indexes for documented access patterns or measured performance needs.
- Review sensitive data handling and access boundaries.
- Document tradeoffs for data ownership, module boundaries, and performance-sensitive paths.

## Inputs

- Domain model, database design, feature specification, access patterns, performance requirements.

## Outputs

- Schema guidance, migration notes, indexing guidance, query review notes.

## Definition of Done

- Database changes trace to documented requirements.
- Integrity constraints are explicit.
- Performance and data exposure risks are reviewed.
