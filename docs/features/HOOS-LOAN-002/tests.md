# Test Plan

## Metadata

- Feature ID: HOOS-LOAN-002
- Artifact: Test Plan

## Backend Test Coverage

- [ ] Create loan successfully.
- [ ] Reject create with missing required fields.
- [ ] Reject create with invalid numeric values.
- [ ] List active loans by default.
- [ ] List loans including archived loans.
- [ ] Retrieve loan details by ID.
- [ ] Update active loan successfully.
- [ ] Reject update for archived loan.
- [ ] Archive active loan successfully.
- [ ] Restore archived loan successfully.
- [ ] Return not found for unknown loan ID.

## Frontend Test Coverage

- [ ] Empty state displays when no loans exist.
- [ ] User can open create loan form.
- [ ] User sees validation errors for invalid form values.
- [ ] User can create loan and see it in workspace.
- [ ] User can view loan details.
- [ ] User can edit active loan.
- [ ] User can archive loan after confirmation.
- [ ] Archived loan is hidden from active list.
- [ ] User can show archived loans.

## Integration Test Coverage

- [ ] Frontend can create loan through backend API.
- [ ] Frontend can list and view created loan.
- [ ] Frontend can update and archive loan.

## Known Test Gaps

- Authentication and real user ownership are deferred.
- Calculator integration is deferred to later features.