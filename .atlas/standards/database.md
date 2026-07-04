# Database Standard

## Purpose

Guide database design, integrity, and maintainability.

## Standard

- Schema changes must trace to the domain model or feature specification.
- Use constraints to protect data integrity.
- Design indexes intentionally and measure performance where needed.
- Keep migrations reviewable and reproducible.
- Avoid storing secrets or sensitive credentials in Atlas files.

## Verification

- Data structures reflect domain language.
- Migrations are documented and reversible where practical.
- Integrity and performance risks are reviewed.

