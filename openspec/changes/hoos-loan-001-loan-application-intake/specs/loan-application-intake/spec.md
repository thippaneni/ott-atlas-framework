## ADDED Requirements

### Requirement: Borrower can start a draft loan application

HOOS SHALL allow a borrower to create a draft loan application with initial applicant and loan intent information.

#### Scenario: Draft application is created

- **WHEN** a borrower provides the minimum required intake information
- **THEN** the system SHALL create a draft loan application with a stable application ID

#### Scenario: Required information is missing

- **WHEN** a borrower attempts to create a draft without required information
- **THEN** the system SHALL reject the request with validation errors

### Requirement: Borrower can save and update draft intake information

HOOS SHALL allow a borrower to save and update draft loan application intake information before submission.

#### Scenario: Draft application is updated

- **WHEN** a borrower updates a draft application with valid information
- **THEN** the system SHALL persist the updated intake information

#### Scenario: Submitted application is edited

- **WHEN** a borrower attempts to update an application that is no longer in Draft state
- **THEN** the system SHALL reject the update

### Requirement: Intake captures applicant basics

HOOS SHALL capture applicant basics needed for initial home loan intake.

#### Scenario: Applicant details are entered

- **WHEN** a borrower enters applicant details
- **THEN** the system SHALL capture name, contact, date of birth or age indicator, employment type, monthly income, and existing monthly obligations where available

### Requirement: Intake captures property and loan intent basics

HOOS SHALL capture property and loan intent information needed for initial intake.

#### Scenario: Loan intent details are entered

- **WHEN** a borrower enters loan intent details
- **THEN** the system SHALL capture loan purpose, estimated property value, desired loan amount, property location, and expected purchase timeline where available

### Requirement: Intake supports optional co-applicant basics

HOOS SHALL allow a borrower to add optional co-applicant basics to a draft application.

#### Scenario: Co-applicant is added

- **WHEN** a borrower adds co-applicant information
- **THEN** the system SHALL associate the co-applicant with the draft loan application

#### Scenario: Co-applicant is omitted

- **WHEN** a borrower submits intake without a co-applicant
- **THEN** the system SHALL allow submission if all primary applicant requirements are satisfied

### Requirement: Borrower can review and submit intake

HOOS SHALL allow a borrower to review and submit the completed intake.

#### Scenario: Complete intake is submitted

- **WHEN** all required fields and consent are present
- **THEN** the system SHALL change the application state from Draft to Submitted

#### Scenario: Incomplete intake is submitted

- **WHEN** required fields or consent are missing
- **THEN** the system SHALL prevent submission and show actionable validation errors

### Requirement: Intake exposes repository-specific implementation responsibilities

Loan application intake implementation SHALL be split between backend and frontend repositories.

#### Scenario: Backend implementation is planned

- **WHEN** backend tasks are created
- **THEN** they SHALL target `hoos/HOOS-Backend`

#### Scenario: Frontend implementation is planned

- **WHEN** frontend tasks are created
- **THEN** they SHALL target `hoos/HOOS-Frontend`