# Test Plan

## Metadata

- Feature ID: HOOS-LOAN-001
- Artifact: Test Plan

## Backend Test Coverage

- [ ] Create draft application successfully.
- [ ] Reject draft creation with missing required fields.
- [ ] Retrieve existing draft application.
- [ ] Update draft application successfully.
- [ ] Reject update when application is Submitted.
- [ ] Submit complete draft successfully.
- [ ] Reject submit when required fields are missing.
- [ ] Reject submit when consent is missing.
- [ ] Verify persistence of applicants, property, loan intent, and consent.

## Frontend Test Coverage

- [ ] User can start intake.
- [ ] User can progress through intake steps.
- [ ] Validation errors display clearly.
- [ ] User can save draft progress.
- [ ] Review screen summarizes entered data.
- [ ] Submit is blocked until required fields and consent are complete.
- [ ] Submitted state is displayed after successful submit.

## Integration Test Coverage

- [ ] Frontend can create draft through backend API.
- [ ] Frontend can update draft through backend API.
- [ ] Frontend can submit intake through backend API.

## Known Test Gaps

- Authentication behavior is out of scope until the identity feature is specified.
- Market-specific validation rules are pending confirmation.