# Domain Model: Loan Workspace

## Metadata

- Feature ID: HOOS-LOAN-002
- Artifact: Domain Model

## Ubiquitous Language

| Term | Meaning |
| ---- | ------- |
| Loan Workspace | The user's operating area for managing one or more home loans. |
| Loan Record | A user-entered representation of a home loan. |
| Active Loan | A loan visible in the default workspace. |
| Archived Loan | A loan hidden from the default view but retained for history. |
| Outstanding Principal | Remaining principal balance for the loan. |
| EMI | Equated monthly installment paid by the borrower. |
| Interest Rate Type | Whether the loan uses floating or fixed interest rate behavior. |

## Aggregate: Loan Record

- Identity: Loan ID
- Root: Loan Record
- State: Active, Archived
- Owns: loan details needed by MVP calculators and dashboard

## Fields

- Loan ID
- Owner/User ID, or placeholder owner until identity is implemented
- Loan nickname
- Lender name
- Loan amount
- Interest rate
- Interest rate type: Floating, Fixed
- Tenure months
- EMI
- Outstanding principal
- Loan start date
- Status: Active, Archived
- Created at
- Updated at
- Archived at

## State Transitions

| From | To | Trigger |
| ---- | -- | ------- |
| None | Active | User creates loan |
| Active | Active | User edits loan |
| Active | Archived | User archives loan |
| Archived | Active | User restores loan |

## Domain Events

- LoanRecordCreated
- LoanRecordUpdated
- LoanRecordArchived
- LoanRecordRestored

## Invariants

- Loan amount must be positive.
- Interest rate must be positive.
- Tenure months must be positive.
- EMI must be positive.
- Outstanding principal must be non-negative.
- Archived loans cannot be edited unless restored.