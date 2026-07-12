# Database Design: Loan Application Intake

## Metadata

- Feature ID: HOOS-LOAN-001
- Artifact: Database Design
- Target Repo: `hoos/HOOS-Backend`

## Scope

Define initial persistence for draft and submitted loan application intake.

## Proposed Tables

### loan_applications

| Column | Type | Notes |
| ------ | ---- | ----- |
| id | uuid | Primary key |
| status | text | Draft, Submitted, Cancelled |
| primary_borrower_id | uuid | Required |
| loan_purpose | text | Nullable during draft |
| desired_loan_amount | numeric | Nullable during draft |
| purchase_timeline | text | Nullable |
| property_location | text | Nullable during draft |
| estimated_property_value | numeric | Nullable during draft |
| property_type | text | Nullable |
| consent_accepted | boolean | Required for submission |
| consent_version | text | Required for submission |
| consent_accepted_at | timestamp | Required for submission |
| created_at | timestamp | Required |
| updated_at | timestamp | Required |

### loan_application_applicants

| Column | Type | Notes |
| ------ | ---- | ----- |
| id | uuid | Primary key |
| loan_application_id | uuid | FK to loan_applications |
| applicant_type | text | PrimaryBorrower or CoApplicant |
| full_name | text | Required |
| email | text | Nullable if phone exists |
| phone | text | Nullable if email exists |
| employment_type | text | Nullable during draft |
| monthly_income | numeric | Nullable during draft |
| monthly_obligations | numeric | Nullable during draft |
| created_at | timestamp | Required |
| updated_at | timestamp | Required |

## Indexes

- `loan_applications(status)`
- `loan_applications(primary_borrower_id)`
- `loan_application_applicants(loan_application_id)`

## Constraints

- Application status must be one of Draft, Submitted, Cancelled.
- Applicant type must be one of PrimaryBorrower, CoApplicant.
- Desired loan amount must be positive when present.
- Estimated property value must be positive when present.
- Monthly income and obligations must be non-negative when present.

## Migration Notes

Implementation should add a migration in `hoos/HOOS-Backend` when backend code begins.

## Open Questions

- Should borrower profile be separate before loan application intake?
- Should contact details be normalized into a user/profile table?
- Which fields are mandatory in the first market?