# Feature Specification: Loan Application Intake

## Metadata

- Feature ID: HOOS-LOAN-001
- Status: Draft
- State: Deferred
- Owner: Product / Architecture

## MVP Scope Notice

This feature is deferred from immediate MVP implementation. The clarified MVP scope is limited to Loan Workspace, EMI Calculator, Part Payment Simulator, Balance Transfer Analyzer, and Loan Dashboard. See docs/product/hoos-mvp-scope.md.

## Summary

Loan Application Intake lets a borrower create a draft home loan application, save and update intake information, review it, and submit the initial intake for later eligibility, document, and lender workflows.

## Source Requirements

- HOOS-CORE-001: Product Foundation
- OpenSpec change: `hoos-loan-001-loan-application-intake`
- ADR-0007: Features Are the Fundamental Unit of Engineering

## Actors

- Borrower: Primary user starting the application.
- Co-applicant: Optional participant in the application.
- Advisor: Future role that may help review or complete applications.
- Operations User: Future role that may review submitted intake.

## Scope

- Create a draft loan application.
- Save and update draft intake information.
- Capture primary applicant basics.
- Capture optional co-applicant basics.
- Capture property and loan intent basics.
- Capture consent for processing intake information.
- Review and submit intake.

## Non-goals

- Authentication implementation.
- Eligibility calculation.
- Document upload.
- Lender integration.
- Underwriting.
- Offer comparison.
- Advisor or operations workflows.

## Business Rules

- A draft application must have a primary borrower.
- A submitted application cannot be edited through draft update endpoints.
- Intake submission requires required applicant, loan intent, property, and consent fields.
- Co-applicant details are optional for the first version.
- Submitting intake does not submit to a lender.

## Open Questions

- Which country/market defines required fields?
- Should the first version require date of birth or only age range?
- Should draft applications expire?
- Should consent be captured as a timestamped audit event?