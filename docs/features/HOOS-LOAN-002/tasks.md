# Tasks

## Metadata

- Feature ID: HOOS-LOAN-002
- Artifact: Tasks

## Backend Tasks - `hoos/HOOS-Backend`

- [ ] Create Loan domain model.
- [ ] Add Loan status handling: Active, Archived.
- [ ] Add create loan API endpoint.
- [ ] Add list loans API endpoint with includeArchived option.
- [ ] Add get loan API endpoint.
- [ ] Add update loan API endpoint.
- [ ] Add archive loan API endpoint.
- [ ] Add restore loan API endpoint.
- [ ] Add request/response models and validation.
- [ ] Add database migration for `loans` table.
- [ ] Add backend tests for create, list, get, update, archive, restore, validation, and conflict paths.

## Frontend Tasks - `hoos/HOOS-Frontend`

- [ ] Create Loan Workspace route.
- [ ] Add active loan list view.
- [ ] Add empty state for no loans.
- [ ] Add create loan form.
- [ ] Add edit loan form.
- [ ] Add loan details view.
- [ ] Add archive confirmation.
- [ ] Add archived loans view or filter.
- [ ] Integrate create, list, get, update, archive, and restore API calls.
- [ ] Add frontend tests for core workspace flows and validation states.

## Atlas/OpenSpec Tasks

- [x] Create OpenSpec proposal, design, spec, and tasks.
- [x] Create feature package.
- [x] Validate Atlas.
- [x] Validate OpenSpec.

## Implementation Gate

Implementation may begin after human review of this package.