# API Contract: Loan Application Intake

## Metadata

- Feature ID: HOOS-LOAN-001
- Artifact: API Contract
- Target Repo: `hoos/HOOS-Backend`

## Authentication / Authorization

Authentication is expected but not implemented by this feature package. Backend implementation should integrate with the current-user identity mechanism once available.

## Endpoints

### Create Draft Application

`POST /api/loan-applications`

Purpose: Create a new draft loan application.

Request body:

```json
{
  "primaryBorrower": {
    "fullName": "string",
    "email": "string",
    "phone": "string",
    "employmentType": "string",
    "monthlyIncome": 0,
    "monthlyObligations": 0
  },
  "loanIntent": {
    "purpose": "purchase",
    "desiredLoanAmount": 0,
    "purchaseTimeline": "string"
  },
  "property": {
    "location": "string",
    "estimatedValue": 0,
    "propertyType": "string"
  }
}
```

Success: `201 Created`

### Get Application

`GET /api/loan-applications/{applicationId}`

Purpose: Retrieve a loan application for review or continuation.

Success: `200 OK`

### Update Draft Application

`PUT /api/loan-applications/{applicationId}`

Purpose: Update draft intake information.

Success: `200 OK`

Errors:

- `400 Bad Request`: Validation failure
- `404 Not Found`: Application not found
- `409 Conflict`: Application is not editable

### Submit Application Intake

`POST /api/loan-applications/{applicationId}/submit`

Purpose: Submit a complete intake to HOOS.

Request body:

```json
{
  "consentAccepted": true,
  "consentVersion": "string"
}
```

Success: `200 OK`

Errors:

- `400 Bad Request`: Missing required information or consent
- `404 Not Found`: Application not found
- `409 Conflict`: Application is not in Draft state

## Response Shape

```json
{
  "applicationId": "string",
  "status": "Draft",
  "primaryBorrower": {},
  "coApplicants": [],
  "loanIntent": {},
  "property": {},
  "consent": null,
  "createdAt": "datetime",
  "updatedAt": "datetime"
}
```

## Validation Rules

- Primary borrower full name is required.
- Primary borrower email or phone is required.
- Desired loan amount must be greater than zero when provided.
- Estimated property value must be greater than zero when provided.
- Consent is required for submission.

## Observability

- Log application creation, update, submit, validation failure, and conflict events.
- Do not log sensitive borrower details.
- Include correlation ID when available.