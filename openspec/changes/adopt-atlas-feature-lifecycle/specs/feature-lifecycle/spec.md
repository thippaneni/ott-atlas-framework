## ADDED Requirements

### Requirement: Feature lifecycle is mandatory

Atlas-managed HOOS features SHALL follow the Atlas Feature Lifecycle before implementation begins.

#### Scenario: New feature starts from business need

- **WHEN** a new HOOS feature is proposed
- **THEN** the feature SHALL be documented through the Atlas Feature Lifecycle before backend or frontend implementation starts

#### Scenario: Implementation is requested too early

- **WHEN** a feature has not passed specification and design gates
- **THEN** implementation SHALL be blocked until required feature artifacts are completed

### Requirement: Feature IDs are stable

Every Atlas-managed HOOS feature SHALL have a stable feature ID using the format `HOOS-AREA-NNN`.

#### Scenario: Feature artifacts are created

- **WHEN** a feature artifact package is created
- **THEN** all artifacts SHALL reference the same stable feature ID

#### Scenario: Backend or frontend work is planned

- **WHEN** implementation tasks are created for a feature
- **THEN** each task SHALL reference the feature ID and target repository

### Requirement: Feature artifact packages are self-contained

Every feature SHALL keep related engineering artifacts together so AI assistants and developers can load complete feature context.

#### Scenario: Complete feature package is needed

- **WHEN** a feature reaches design complete status
- **THEN** its package SHALL include feature, acceptance, domain, API, database, UI, tasks, tests, review, and release artifacts where applicable

#### Scenario: Artifact does not apply

- **WHEN** an artifact is not applicable to a feature
- **THEN** the feature package SHALL state that the artifact is not applicable and explain why

### Requirement: Feature gates control progression

A feature SHALL pass explicit gates before moving to the next lifecycle stage.

#### Scenario: Specification gate is evaluated

- **WHEN** a feature moves from proposed to design
- **THEN** business need, requirements, acceptance criteria, and non-goals SHALL be complete

#### Scenario: Design gate is evaluated

- **WHEN** a feature moves from design to ready
- **THEN** domain, API, database, UI, architecture, and task breakdown artifacts SHALL be complete where applicable

#### Scenario: Quality gate is evaluated

- **WHEN** a feature moves from implementation to release readiness
- **THEN** tests, AI review, human review, security, performance, documentation, and release notes SHALL be complete where applicable

### Requirement: Implementation targets are repository-specific

Feature implementation SHALL be applied to the correct HOOS implementation repository.

#### Scenario: Backend work is required

- **WHEN** a feature includes backend API, domain, database, or backend test work
- **THEN** implementation tasks SHALL target `hoos/HOOS-Backend`

#### Scenario: Frontend work is required

- **WHEN** a feature includes UI, routing, frontend state, API integration, or frontend test work
- **THEN** implementation tasks SHALL target `hoos/HOOS-Frontend`

### Requirement: Feature state is explicit

Every feature SHALL declare its current lifecycle state.

#### Scenario: Feature status changes

- **WHEN** a feature progresses through the lifecycle
- **THEN** its state SHALL be updated to one of Draft, Proposed, Approved, Design, Ready, In Development, Code Review, QA, Released, Maintained, Deprecated, or Archived
