# Implementation Notes

## Metadata

- Feature ID: HOOS-LOAN-002
- Artifact: Implementation Notes

## Summary

No backend or frontend implementation code is included in this specification change.

Implementation should be completed in later turns using the repository boundaries below.

## Backend Repository

Path: `hoos/HOOS-Backend`

Expected implementation:

- .NET API endpoints
- Loan domain model and validation
- PostgreSQL persistence
- Migration scripts
- Backend tests

## Frontend Repository

Path: `hoos/HOOS-Frontend`

Expected implementation:

- Angular Loan Workspace route
- Active loan list
- Create/edit loan form
- Loan details view
- Archive/restore interactions
- API integration
- Frontend tests

## Implementation Order Recommendation

1. Backend domain model and validation.
2. Backend persistence and migration.
3. Backend API endpoints and tests.
4. Frontend route and workspace shell.
5. Frontend create/edit/details/archive flows.
6. End-to-end happy path validation.

## Dependencies

- Authentication is deferred. Implementation must document temporary ownership/current-user strategy.
- EMI Calculator will later reuse Loan Workspace fields.