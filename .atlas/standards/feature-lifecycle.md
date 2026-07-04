# Feature Lifecycle Standard

## Metadata

- Version: 1.0.0
- Status: Active
- Layer: Standards
- Depends on: ADR-0001, ADR-0007, principles.md, checklists/feature-gates.md

## Purpose

Define the mandatory Atlas Feature Lifecycle (AFL) for every Atlas-managed feature.

A feature is the fundamental unit of engineering. It is not just code; it is a complete engineering artifact with business context, specifications, design, implementation, tests, reviews, documentation, and release history.

## Scope

This standard applies to all Atlas-managed projects and is immediately applicable to HOOS backend and frontend implementation work.

## Lifecycle

Every feature SHALL move through the following lifecycle:

1. Business Need
2. Vision
3. Epic
4. Feature Specification
5. Acceptance Criteria
6. Domain Modeling
7. Architecture Review
8. API Contract
9. Database Design
10. UI Contract
11. Task Breakdown
12. Implementation
13. Unit Tests
14. Integration Tests
15. AI Review
16. Human Review
17. Documentation Update
18. Release

Implementation SHALL NOT begin before specification and design readiness gates are satisfied.

## Feature ID

Every feature SHALL have a stable feature ID using this format:

```text
HOOS-AREA-NNN
```

Examples:

- `HOOS-LOAN-001`
- `HOOS-AUTH-001`
- `HOOS-DOC-001`

The same feature ID SHALL appear in feature artifacts, implementation tasks, review notes, and release notes where practical.

## Feature Package

Every feature SHOULD be organized as a self-contained package:

```text
HOOS-AREA-NNN/
  README.md
  feature.md
  acceptance.md
  domain.md
  api.md
  database.md
  ui.md
  tasks.md
  implementation.md
  tests.md
  review.md
  release.md
```

If an artifact does not apply, the file SHOULD state that it is not applicable and explain why.

## Feature Gates

### Gate 1: Specification Complete

Required evidence:

- Business need
- Vision or epic link
- Feature specification
- Acceptance criteria
- Non-goals
- Open questions resolved or explicitly tracked

### Gate 2: Design Complete

Required evidence where applicable:

- Domain model
- Architecture review
- API contract
- Database design
- UI contract
- Task breakdown

### Gate 3: Implementation Complete

Required evidence where applicable:

- Backend implementation in `hoos/HOOS-Backend`
- Frontend implementation in `hoos/HOOS-Frontend`
- Unit tests
- Integration tests
- Implementation notes

### Gate 4: Quality Complete

Required evidence:

- AI review
- Human review
- Security review where relevant
- Performance review where relevant
- Documentation update
- Known risks and test gaps documented

### Gate 5: Release Ready

Required evidence:

- Version or release scope
- Changelog or release notes
- Migration notes where relevant
- Rollback or recovery notes where relevant
- Final validation results

## Feature State Machine

Every feature SHALL declare one current state:

1. Draft
2. Proposed
3. Approved
4. Design
5. Ready
6. In Development
7. Code Review
8. QA
9. Released
10. Maintained
11. Deprecated
12. Archived

State changes SHOULD be supported by gate evidence.

## Repository Boundaries

Atlas and OpenSpec own feature intent, specifications, governance, templates, and lifecycle state.

HOOS implementation repositories own application code:

- Backend source code goes in `hoos/HOOS-Backend`.
- Frontend source code goes in `hoos/HOOS-Frontend`.

HOOS application source code SHALL NOT be added directly to the Atlas framework repository root.

## Completion Criteria

A feature is complete when its release gate is satisfied, implementation is traceable to specifications, tests and reviews are complete, and documentation reflects the delivered behavior.
