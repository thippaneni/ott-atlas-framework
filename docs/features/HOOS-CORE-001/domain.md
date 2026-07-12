# Domain Model: Product Foundation

## Metadata

- Feature ID: HOOS-CORE-001
- Artifact: Domain Language

## Ubiquitous Language

| Term | Meaning |
| ---- | ------- |
| Borrower | A person seeking a home loan or home ownership guidance. |
| Co-applicant | A person who joins a borrower on a loan application. |
| Advisor | A person who helps borrowers understand readiness, options, or next steps. |
| Loan Application | A structured request for home loan evaluation or processing. |
| Eligibility | Assessment of whether a borrower may qualify for loan options based on available information. |
| Affordability | Estimate of repayment capacity based on income, obligations, and assumptions. |
| Property | Home, apartment, plot, or other real estate involved in the loan journey. |
| Document | Evidence or supporting file required for loan readiness or application processing. |
| Lender | Bank, financial institution, or partner that may provide loan offers. |
| Offer | A loan option or quote from a lender or simulated lender policy. |
| Workflow | A sequence of steps that moves a borrower from intent to readiness or application progress. |

## Initial Entities

### Borrower

- Identity: Borrower ID
- Responsibilities: Holds profile, income, obligations, preferences, and application relationship.
- Invariants: Must have enough identity/contact information before application submission.

### Loan Application

- Identity: Application ID
- Responsibilities: Captures application intent, applicant details, property details, and status.
- Invariants: Must reference at least one borrower before progression beyond draft.

### Property

- Identity: Property ID or application-local property reference
- Responsibilities: Captures purchase/property information relevant to loan evaluation.
- Invariants: Required fields depend on the loan journey stage.

### Document

- Identity: Document ID
- Responsibilities: Stores metadata and readiness status for required files.
- Invariants: Must have owner, type, and status.

## Initial Domain Events

- BorrowerProfileCreated
- LoanApplicationStarted
- EligibilityCalculated
- DocumentUploaded
- OfferReceived

## Open Questions

- Which country or market defines the first loan rules?
- Are lender offers simulated first or integrated with real lenders?
- What document types are mandatory for the first release?