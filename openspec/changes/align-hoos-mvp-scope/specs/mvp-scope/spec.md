## ADDED Requirements

### Requirement: MVP scope is limited to five launch features

HOOS SHALL limit immediate MVP feature work to Loan Workspace, EMI Calculator, Part Payment Simulator, Balance Transfer Analyzer, and Loan Dashboard.

#### Scenario: New feature is proposed

- **WHEN** a new feature is proposed before MVP completion
- **THEN** the feature SHALL map directly to one of the five launch features or be deferred

### Requirement: Deferred modules are not implemented during MVP

HOOS SHALL defer non-MVP modules until the five launch features are specified and implementation has started.

#### Scenario: Deferred module is requested

- **WHEN** a feature belongs to identity, document intelligence, AI advisor, property intelligence, marketplace, or loan origination
- **THEN** it SHALL be marked deferred unless it is a technical prerequisite for the five launch features

### Requirement: Loan application intake is not the next implementation target

HOOS SHALL not treat loan application intake/origination as the next MVP implementation feature.

#### Scenario: Implementation planning begins

- **WHEN** the team chooses the next implementation target
- **THEN** the team SHALL choose from Loan Workspace, EMI Calculator, Part Payment Simulator, Balance Transfer Analyzer, or Loan Dashboard

### Requirement: Product docs preserve future roadmap

HOOS SHALL preserve future module ideas while keeping MVP scope explicit.

#### Scenario: Future module is documented

- **WHEN** a future module is recorded
- **THEN** it SHALL be assigned to a later phase instead of entering MVP scope automatically