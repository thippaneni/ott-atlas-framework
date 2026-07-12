# Domain Model: Loan Application Intake

## Metadata

- Feature ID: HOOS-LOAN-001
- Artifact: Domain Model

## Ubiquitous Language

| Term | Meaning |
| ---- | ------- |
| Loan Application | A structured request for home loan evaluation or processing. |
| Draft Application | A loan application that has been started but not submitted. |
| Submitted Intake | A completed intake submitted to HOOS, not to a lender. |
| Applicant | Borrower or co-applicant represented in the application. |
| Primary Borrower | Main borrower who owns the application. |
| Co-applicant | Optional applicant associated with the loan application. |
| Loan Intent | Desired loan amount, purpose, and purchase timeline. |
| Consent | Borrower permission to process provided intake information. |

## Aggregate: Loan Application

- Identity: Application ID
- Root: Loan Application
- State: Draft, Submitted, Cancelled
- Owns: Applicants, property summary, loan intent, consent record

## Value Objects

### Applicant Basics

- Full name
- Contact email
- Contact phone
- Date of birth or age indicator
- Employment type
- Monthly income
- Existing monthly obligations

### Property Summary

- Property location
- Estimated property value
- Property type, if known

### Loan Intent

- Loan purpose
- Desired loan amount
- Purchase timeline

### Consent Record

- Consent accepted
- Consent timestamp
- Consent text/version

## State Transitions

| From | To | Trigger |
| ---- | -- | ------- |
| None | Draft | Borrower starts application |
| Draft | Draft | Borrower updates application |
| Draft | Submitted | Borrower submits complete intake |
| Draft | Cancelled | Borrower cancels draft |

## Domain Events

- LoanApplicationStarted
- LoanApplicationUpdated
- LoanApplicationSubmitted
- LoanApplicationCancelled

## Invariants

- A loan application must have one primary borrower.
- A submitted application must have required applicant, property, loan intent, and consent information.
- Submitted applications cannot be modified through draft update behavior.
- Consent must be recorded before submission.