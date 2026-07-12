# UI Contract: Loan Workspace

## Metadata

- Feature ID: HOOS-LOAN-002
- Artifact: UI Contract
- Target Repo: `hoos/HOOS-Frontend`

## Primary Screens

1. Loan Workspace List
2. Create Loan
3. Edit Loan
4. Loan Details
5. Archived Loans View

## Workspace List

Default view shows active loans.

Displayed fields:

- Loan nickname
- Lender name
- Outstanding principal
- EMI
- Interest rate
- Rate type
- Tenure
- Status

Actions:

- Create loan
- View details
- Edit loan
- Archive loan
- Show archived loans

## Create/Edit Loan Form

Fields:

- Loan nickname
- Lender name
- Loan amount
- Interest rate
- Interest rate type: Floating or Fixed
- Tenure months
- EMI
- Outstanding principal
- Loan start date

Validation:

- Required fields show inline validation.
- Numeric values must be positive where required.
- Outstanding principal cannot exceed loan amount in MVP.
- Rate type must be selected.

## Loan Details

Shows all loan fields and future extension points for calculators and dashboard links.

Future actions:

- Calculate EMI
- Simulate part payment
- Analyze balance transfer
- View dashboard

## Screen States

- Empty state: No loans yet, prompt to create first loan.
- Loading state: Workspace is fetching loans.
- Error state: Could not load or save loan.
- Active list state: Shows active loans.
- Archived list state: Shows archived loans separately or with clear labels.
- Confirm archive state: User confirms before archiving.

## API Integration

- Create: `POST /api/loans`
- List: `GET /api/loans?includeArchived=false`
- Details: `GET /api/loans/{loanId}`
- Update: `PUT /api/loans/{loanId}`
- Archive: `POST /api/loans/{loanId}/archive`
- Restore: `POST /api/loans/{loanId}/restore`

## Accessibility

- Forms must be keyboard navigable.
- Validation errors must be associated with fields.
- Archive confirmation must be accessible.
- Tables/cards must preserve readable labels for assistive technologies.