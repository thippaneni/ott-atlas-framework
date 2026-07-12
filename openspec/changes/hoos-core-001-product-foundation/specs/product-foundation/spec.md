## ADDED Requirements

### Requirement: Product vision is defined

HOOS SHALL define a product vision for a Home Ownership Operating System focused initially on home loan intelligence.

#### Scenario: Product foundation is loaded

- **WHEN** a developer or AI assistant loads the HOOS product foundation
- **THEN** the product purpose, initial scope, and non-goals SHALL be available

### Requirement: Core domain language is defined

HOOS SHALL define initial domain terms for home loan and home ownership workflows.

#### Scenario: Feature specifications are written

- **WHEN** future HOOS feature specifications are created
- **THEN** they SHALL use the product foundation domain language where applicable

### Requirement: Initial user roles are defined

HOOS SHALL define the initial user and stakeholder roles that future features may target.

#### Scenario: A feature identifies an actor

- **WHEN** a feature references a user or actor
- **THEN** the actor SHOULD map to a role defined by the product foundation or explicitly introduce a new role

### Requirement: Initial module map is defined

HOOS SHALL define an initial conceptual module map for product planning and architecture.

#### Scenario: Backend or frontend implementation is planned

- **WHEN** implementation tasks are created
- **THEN** each task SHOULD identify the conceptual HOOS module it affects

### Requirement: Repository responsibility is explicit

HOOS SHALL keep product foundation and specifications in the Atlas/OpenSpec repository while implementation code lives in the backend and frontend repositories.

#### Scenario: Backend implementation is needed

- **WHEN** a future feature requires backend code
- **THEN** implementation tasks SHALL target `hoos/HOOS-Backend`

#### Scenario: Frontend implementation is needed

- **WHEN** a future feature requires frontend code
- **THEN** implementation tasks SHALL target `hoos/HOOS-Frontend`