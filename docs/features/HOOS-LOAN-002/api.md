# API Contract: Loan Workspace

## Metadata

- Feature ID: HOOS-LOAN-002
- Artifact: API Contract
- Target Repo: `hoos/HOOS-Backend`

## Authentication / Authorization

Authentication is deferred in MVP scope. Backend implementation should still isolate loan records by an owner/current-user boundary. Until identity exists, implementation may use a placeholder owner strategy documented in implementation notes.

## Endpoints

### Create Loan

`POST /api/loans`

Purpose: Create an active loan record.

Request body:

```json
{
  "nickname": "string",
  "lenderName": "string",
  "loanAmount": 5000000,
  "interestRate": 8.5,
  "interestRateType": "Floating",
  "tenureMonths": 240,
  "emi": 43391,
  "outstandingPrincipal": 4800000,
  "loanStartDate": "2026-01-01"
}
```

Success: `201 Created`

### List Loans

`GET /api/loans?includeArchived=false`

Purpose: List active loans by default, optionally including archived loans.

Success: `200 OK`

### Get Loan

`GET /api/loans/{loanId}`

Purpose: Retrieve a loan record by ID.

Success: `200 OK`

### Update Loan

`PUT /api/loans/{loanId}`

Purpose: Update an active loan record.

Success: `200 OK`

Errors:

- `400 Bad Request`: Validation failure
- `404 Not Found`: Loan not found
- `409 Conflict`: Loan is archived and cannot be edited

### Archive Loan

`POST /api/loans/{loanId}/archive`

Purpose: Archive an active loan.

Success: `200 OK`

### Restore Loan

`POST /api/loans/{loanId}/restore`

Purpose: Restore an archived loan to active status.

Success: `200 OK`

## Response Shape

```json
{
  "loanId": "string",
  "nickname": "string",
  "lenderName": "string",
  "loanAmount": 5000000,
  "interestRate": 8.5,
  "interestRateType": "Floating",
  "tenureMonths": 240,
  "emi": 43391,
  "outstandingPrincipal": 4800000,
  "loanStartDate": "2026-01-01",
  "status": "Active",
  "createdAt": "datetime",
  "updatedAt": "datetime",
  "archivedAt": null
}
```

## Validation Rules

- Loan amount must be greater than zero.
- Interest rate must be greater than zero.
- Interest rate type must be Floating or Fixed.
- Tenure months must be greater than zero.
- EMI must be greater than zero.
- Outstanding principal must be zero or greater.
- Outstanding principal should not exceed loan amount in MVP.
- Loan start date must be a valid date.

## Observability

- Log create, update, archive, restore, validation failure, and not-found events.
- Do not log sensitive user identifiers beyond safe correlation IDs.