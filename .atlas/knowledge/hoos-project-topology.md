# HOOS Project Topology

## Metadata

- Version: 0.1.0
- Status: Active
- Layer: Knowledge
- Scope: Home Ownership Operating System implementation repositories

## Purpose

Record how Atlas, OpenSpec, and the HOOS implementation repositories relate to each other.

## Repository Layout

Atlas framework repository:

- Path: `D:\Projects\SAAS\ott-atlas-framework`
- Responsibility: Atlas framework, OpenSpec specifications, governance, templates, standards, rules, patterns, skills, instructions, agents, checklists, validation, and project-level specification workflow.

HOOS backend repository:

- Path: `D:\Projects\SAAS\ott-atlas-framework\hoos\HOOS-Backend`
- Responsibility: Home Ownership Operating System backend implementation.
- Expected stack: .NET backend, PostgreSQL integration, API implementation, backend tests.

HOOS frontend repository:

- Path: `D:\Projects\SAAS\ott-atlas-framework\hoos\HOOS-Frontend`
- Responsibility: Home Ownership Operating System frontend implementation.
- Expected stack: Angular frontend, UI workflows, API integration, frontend tests.

## Operating Rule

Atlas and OpenSpec define the project intent, specifications, architecture, and engineering governance.

HOOS implementation code belongs in the HOOS implementation repositories:

- Backend code goes into `hoos/HOOS-Backend`.
- Frontend code goes into `hoos/HOOS-Frontend`.

Do not place HOOS application source code directly in the Atlas framework repository root.

## Specification Flow

1. Define or update intent and requirements through OpenSpec in the Atlas framework repository.
2. Use Atlas contexts, standards, rules, patterns, skills, instructions, agents, templates, and checklists to guide implementation.
3. Apply backend implementation changes in `hoos/HOOS-Backend`.
4. Apply frontend implementation changes in `hoos/HOOS-Frontend`.
5. Keep implementation traceable to OpenSpec changes and Atlas specifications.

## Git Boundary

The `hoos/` folder contains separately cloned implementation repositories and is ignored by the Atlas framework repository.

Each HOOS implementation repository should manage its own commits, branches, tags, and releases.
