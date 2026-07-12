# Implementation Notes

## Metadata

- Feature ID: HOOS-LOAN-001
- Artifact: Implementation Notes

## Summary

No backend or frontend implementation code is included in this specification change.

Implementation should be completed in later turns using the repository boundaries below.

## Backend Repository

Path: `hoos/HOOS-Backend`

Expected implementation:

- .NET API endpoints
- Domain model and validation
- PostgreSQL persistence
- Migration scripts
- Backend tests

## Frontend Repository

Path: `hoos/HOOS-Frontend`

Expected implementation:

- Angular route and screens
- Step-based intake flow
- Forms and validation
- API integration
- Frontend tests

## Implementation Order Recommendation

1. Backend domain model and persistence.
2. Backend API contracts and validation.
3. Backend tests.
4. Frontend route and step shell.
5. Frontend forms and API integration.
6. End-to-end happy path validation.

## Dependencies

- Authentication/current-user identity is expected but not specified here.
- Market-specific required fields need confirmation.