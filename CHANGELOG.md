# Changelog

All notable changes to this project will be documented in this file.

## [0.2.0] - 2026-07-04

### Added

- Added Atlas Engineering Knowledge System modules:
  - `standards/`
  - `rules/`
  - `patterns/`
  - `skills/`
  - `instructions/`
  - `agents/`
  - `checklists/`
  - `templates/`
- Added Atlas architecture decisions ADR-0001 through ADR-0006.
- Added stack-aware knowledge for .NET, Angular, PostgreSQL, AWS, OpenAI, Python, and multi-layer testing.
- Added machine-readable agent configurations for architect, backend, frontend, database, AI, DevOps, tester, reviewer, and product roles.
- Added validation schemas for agents, rules, contexts, manifest, index, and capabilities.
- Added `tools/validate-atlas.py` for dependency-free Atlas framework validation.
- Added artifact templates for vision, PRD, SRS, ADR, feature specs, API contracts, test plans, domain models, and architecture documents.
- Added review, release, API, security, testing, database, frontend, and specification checklists.

### Changed

- Updated `index.yaml` to register all current Atlas knowledge modules and file references.
- Updated `capabilities.yaml` to use a capability-first model with separate agent mappings.
- Updated `contexts.yaml` with selective context-loading profiles for architecture, specification, backend, frontend, database, testing, review, security, deployment, and AI engineering.
- Updated `.atlas/manifest.yaml` to register expanded validation coverage.
- Updated `.atlas/schemas/capabilities.schema.json` to match the capability-first design.

### Validation

- Atlas validation passes with `0 errors` and `0 warnings` using `tools/validate-atlas.py`.

## [0.1.0] - 2026-06-28

### Added

- Added Atlas Core project structure.
- Added root project files: `README.md`, `LICENSE`, `CONTRIBUTING.md`, `CHANGELOG.md`, `.editorconfig`, `.gitignore`, and `manifest.yaml`.
- Added `.atlas/` root structure for instructions, skills, agents, patterns, prompts, templates, checklists, standards, rules, architecture, and knowledge.
- Added Atlas core files: `.atlas/README.md`, `.atlas/manifest.yaml`, `.atlas/index.yaml`, `.atlas/capabilities.yaml`, `.atlas/contexts.yaml`, `.atlas/principles.md`, and `.atlas/ATS.md`.
- Added initial JSON schemas for manifest, index, and capabilities.
