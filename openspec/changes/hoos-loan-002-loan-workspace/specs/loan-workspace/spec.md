## ADDED Requirements

### Requirement: User can create a loan record

HOOS SHALL allow a user to create a loan record with required loan details.

#### Scenario: Loan is created with valid details

- **WHEN** a user submits valid loan workspace details
- **THEN** the system SHALL create an active loan record with a stable loan ID

#### Scenario: Loan creation has invalid details

- **WHEN** a user submits missing or invalid required loan details
- **THEN** the system SHALL reject the request with actionable validation errors

### Requirement: User can view multiple loans

HOOS SHALL allow a user to view all active and archived loan records available to them.

#### Scenario: User opens loan workspace

- **WHEN** the user opens Loan Workspace
- **THEN** the system SHALL show active loan records by default

#### Scenario: User includes archived loans

- **WHEN** the user chooses to include archived loans
- **THEN** the system SHALL show archived loan records separately or clearly marked as archived

### Requirement: User can view loan details

HOOS SHALL allow a user to view details for a selected loan record.

#### Scenario: Existing loan is selected

- **WHEN** the user selects an existing loan
- **THEN** the system SHALL show loan amount, interest rate, rate type, tenure, EMI, outstanding principal, lender name, start date, and loan status

### Requirement: User can edit an active loan

HOOS SHALL allow a user to edit an active loan record.

#### Scenario: Active loan is updated

- **WHEN** the user submits valid updates for an active loan
- **THEN** the system SHALL persist the updated loan details

#### Scenario: Archived loan is edited

- **WHEN** the user attempts to edit an archived loan
- **THEN** the system SHALL reject the update unless the loan is restored first

### Requirement: User can archive a loan

HOOS SHALL allow a user to archive a loan record without deleting it.

#### Scenario: Loan is archived

- **WHEN** the user archives an active loan
- **THEN** the system SHALL set the loan status to Archived and hide it from the default active workspace view

### Requirement: Loan details support MVP calculations

HOOS loan records SHALL capture enough information to support EMI, part payment, balance transfer, and dashboard features.

#### Scenario: Loan record is used by calculators

- **WHEN** future calculator or dashboard features load a loan record
- **THEN** loan amount, interest rate, rate type, tenure, EMI, outstanding principal, and lender name SHALL be available

### Requirement: Implementation targets are repository-specific

Loan Workspace implementation SHALL be split between backend and frontend repositories.

#### Scenario: Backend implementation is planned

- **WHEN** backend tasks are created
- **THEN** they SHALL target `hoos/HOOS-Backend`

#### Scenario: Frontend implementation is planned

- **WHEN** frontend tasks are created
- **THEN** they SHALL target `hoos/HOOS-Frontend`