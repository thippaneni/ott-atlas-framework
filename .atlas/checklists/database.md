# Database Checklist

## Metadata

- Version: 0.1.0
- Status: Draft
- Layer: Checklists
- Depends on: standards/database.md, rules/database.yaml, skills/postgres.md

## Purpose

Verify database changes for integrity, traceability, and performance risk.

## Checklist

- [ ] Schema changes trace to a domain model, feature specification, or ADR.
- [ ] Migrations are ordered, reviewable, and reproducible.
- [ ] Required constraints protect important invariants.
- [ ] Indexes map to documented access patterns or measured needs.
- [ ] Sensitive data handling is documented where relevant.
- [ ] Query behavior is reviewed for critical paths.
- [ ] Data ownership boundaries between modules are respected.
- [ ] Rollback or recovery expectations are documented where practical.

## Completion Criteria

The database change is ready when integrity, migration safety, and performance risks are reviewed.
