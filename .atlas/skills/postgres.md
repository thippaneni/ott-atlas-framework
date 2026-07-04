# PostgreSQL Skill

## Metadata

- Version: 0.1.0
- Status: Draft
- Layer: Skills
- Depends on: standards/database.md, rules/database.yaml, patterns/repository.md

## Purpose

Guide PostgreSQL schema, query, migration, and performance work.

## Scope

Use for database design, migrations, indexing, constraints, query review, and persistence behavior.

## Best Practices

- Model tables and constraints from domain and feature specifications.
- Use migrations for repeatable schema evolution.
- Add indexes for documented access patterns and measured needs.
- Prefer constraints for invariants the database must protect.
- Review query plans for performance-sensitive paths.
- Avoid cross-module table ownership confusion.

## Anti-patterns

- Schema changes without a corresponding specification or decision.
- Indexes added speculatively with no access pattern.
- Business-critical integrity enforced only in application code.

## References

- standards/database.md
- rules/database.yaml
- patterns/modular-monolith.md
