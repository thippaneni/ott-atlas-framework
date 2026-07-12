# Database Design: Loan Workspace

## Metadata

- Feature ID: HOOS-LOAN-002
- Artifact: Database Design
- Target Repo: `hoos/HOOS-Backend`

## Scope

Persist user-entered home loan records for the MVP Loan Workspace.

## Proposed Table: loans

| Column | Type | Notes |
| ------ | ---- | ----- |
| id | uuid | Primary key |
| owner_id | text | Placeholder owner/current-user boundary until identity exists |
| nickname | text | Required |
| lender_name | text | Required |
| loan_amount | numeric | Required, positive |
| interest_rate | numeric | Required, positive annual percentage |
| interest_rate_type | text | Floating or Fixed |
| tenure_months | integer | Required, positive |
| emi | numeric | Required, positive |
| outstanding_principal | numeric | Required, non-negative |
| loan_start_date | date | Required |
| status | text | Active or Archived |
| created_at | timestamp | Required |
| updated_at | timestamp | Required |
| archived_at | timestamp | Nullable |

## Indexes

- `loans(owner_id, status)` for workspace list queries.
- `loans(owner_id, id)` for ownership-scoped lookup.
- `loans(created_at)` if sorting by creation date is needed.

## Constraints

- `loan_amount > 0`
- `interest_rate > 0`
- `tenure_months > 0`
- `emi > 0`
- `outstanding_principal >= 0`
- `outstanding_principal <= loan_amount` for MVP
- `interest_rate_type IN ('Floating', 'Fixed')`
- `status IN ('Active', 'Archived')`

## Migration Notes

Implementation should add the first Loan Workspace migration in `hoos/HOOS-Backend`.

## Open Questions

- Should owner_id be UUID now or text placeholder until identity is defined?
- Should interest_rate use decimal precision `(5,2)` or a more flexible scale?
- Should loan archive be reversible in the first implementation?