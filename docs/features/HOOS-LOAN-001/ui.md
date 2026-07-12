# UI Contract: Loan Application Intake

## Metadata

- Feature ID: HOOS-LOAN-001
- Artifact: UI Contract
- Target Repo: `hoos/HOOS-Frontend`

## User Flow

The borrower completes a step-based intake flow.

## Steps

1. Start Application
2. Applicant Basics
3. Income and Obligations
4. Property Details
5. Loan Intent
6. Optional Co-applicant
7. Review
8. Consent and Submit

## Screen States

- Empty state: No draft application exists.
- Draft state: Application exists and can be continued.
- Saving state: User changes are being saved.
- Saved state: User changes are persisted.
- Validation error state: Required fields are missing or invalid.
- Submit blocked state: Review shows incomplete sections.
- Submitted state: Intake is complete and no longer editable as draft.

## Frontend Validation

- Required fields show inline validation.
- Numeric amounts must be positive where required.
- Email and phone formats should be validated where provided.
- Consent must be checked before submit.

## API Integration

- Create draft: `POST /api/loan-applications`
- Load draft: `GET /api/loan-applications/{applicationId}`
- Update draft: `PUT /api/loan-applications/{applicationId}`
- Submit: `POST /api/loan-applications/{applicationId}/submit`

## Accessibility

- Step navigation must be keyboard accessible.
- Validation errors must be associated with fields.
- Review page must be readable by assistive technologies.

## Open Questions

- Should the first UI autosave or require explicit save?
- Should users be able to skip optional sections?
- What design system will HOOS frontend use?