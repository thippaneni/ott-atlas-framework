# Architecture Notes: Product Foundation

## Metadata

- Feature ID: HOOS-CORE-001
- Artifact: Architecture Notes

## Context

This foundation defines conceptual architecture only. Code-level architecture will be refined through future features and ADRs.

## Repository Boundaries

| Repository | Responsibility |
| ---------- | -------------- |
| Atlas/OpenSpec | Product specs, feature lifecycle, governance, templates, validation, and traceability. |
| hoos/HOOS-Backend | .NET APIs, domain logic, PostgreSQL persistence, migrations, backend tests. |
| hoos/HOOS-Frontend | Angular UI, routing, forms, state, API integration, frontend tests. |

## Initial Conceptual Modules

| Module | Responsibility | Expected Repo Impact |
| ------ | -------------- | -------------------- |
| Identity and Access | Users, roles, sessions, authorization | Backend + Frontend |
| Borrower Profile | Borrower personal, income, and obligation profile | Backend + Frontend |
| Loan Application | Application lifecycle and status | Backend + Frontend |
| Eligibility Intelligence | Loan readiness and eligibility calculations | Backend primarily |
| Property and Purchase Details | Property data and purchase context | Backend + Frontend |
| Document Management | Document metadata, upload flow, readiness | Backend + Frontend |
| Lender Offers | Loan options, comparisons, offer status | Backend + Frontend |
| Notifications | User and workflow notifications | Backend + Frontend |
| Administration | Internal configuration and management | Backend + Frontend |
| Audit and Compliance | Traceability, audit history, compliance evidence | Backend primarily |

## Architecture Principles

- Start as a modular monolith unless a future ADR justifies service extraction.
- Keep product specs and implementation traceable by feature ID.
- Keep backend and frontend implementation separated by repo.
- Do not introduce app source code in the Atlas framework repository root.

## Open Architecture Questions

- What authentication provider will HOOS use?
- What cloud deployment shape is expected for the first release?
- Which audit and compliance needs are mandatory for launch?