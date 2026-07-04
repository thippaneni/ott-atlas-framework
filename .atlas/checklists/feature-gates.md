# Feature Gates Checklist

## Metadata

- Version: 0.1.0
- Status: Draft
- Layer: Checklists
- Depends on: standards/feature-lifecycle.md, ADR-0007

## Purpose

Verify that an Atlas-managed feature is ready to move through each lifecycle gate.

## Gate 1: Specification Complete

- [ ] Feature ID is assigned.
- [ ] Business need is documented.
- [ ] Vision or epic reference is documented.
- [ ] Feature specification is complete.
- [ ] Acceptance criteria are testable.
- [ ] Non-goals are explicit.
- [ ] Open questions are resolved or tracked.

## Gate 2: Design Complete

- [ ] Domain model is documented or marked not applicable.
- [ ] Architecture review is complete or marked not applicable.
- [ ] API contract is documented or marked not applicable.
- [ ] Database design is documented or marked not applicable.
- [ ] UI contract is documented or marked not applicable.
- [ ] Backend tasks target `hoos/HOOS-Backend` where applicable.
- [ ] Frontend tasks target `hoos/HOOS-Frontend` where applicable.

## Gate 3: Implementation Complete

- [ ] Backend implementation is complete where applicable.
- [ ] Frontend implementation is complete where applicable.
- [ ] Unit tests are complete where applicable.
- [ ] Integration tests are complete where applicable.
- [ ] Implementation notes are documented.

## Gate 4: Quality Complete

- [ ] AI review is complete.
- [ ] Human review is complete.
- [ ] Security review is complete where applicable.
- [ ] Performance review is complete where applicable.
- [ ] Documentation is updated.
- [ ] Known risks and test gaps are documented.

## Gate 5: Release Ready

- [ ] Release scope is defined.
- [ ] Changelog or release notes are updated.
- [ ] Migration notes are documented where applicable.
- [ ] Rollback or recovery notes are documented where applicable.
- [ ] Final validation results are recorded.

## Completion Criteria

A feature is release ready when all applicable gates are complete and any non-applicable artifacts explain why they are not required.
