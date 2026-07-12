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

| Module | MVP Status | Responsibility | Expected Repo Impact |
| ------ | ---------- | -------------- | -------------------- |
| Loan Management Core | MVP | Loan workspace, loan details, part payments, balance transfer inputs | Backend + Frontend |
| Calculator Engine | MVP | EMI, part payment, balance transfer, comparison calculations | Backend and/or Frontend |
| Dashboard and Reporting | MVP | Loan summary, outstanding, EMI, savings, basic reporting | Backend + Frontend |
| Identity and User Management | Deferred | Registration, login, profile, subscription | Backend + Frontend |
| Property Management | Deferred | Property profile, builder details, possession, construction tracking | Backend + Frontend |
| Document Intelligence | Deferred | OCR, document summary, risk detection | Backend + AI + Frontend |
| AI Financial Intelligence | Deferred | Loan health score, advisor, recommendations | Backend + AI + Frontend |
| Notifications and Automation | Deferred | EMI due, demand letter, refinance alerts | Backend + Frontend |
| Property Intelligence | Deferred | Builder ratings, RERA, price trends, locality score | Backend + Frontend |
| Marketplace | Deferred | Lenders, advisors, professional services, SaaS plans | Backend + Frontend |

## Architecture Principles

- Start as a modular monolith unless a future ADR justifies service extraction.
- Keep product specs and implementation traceable by feature ID.
- Keep backend and frontend implementation separated by repo.
- Do not introduce app source code in the Atlas framework repository root.

## Open Architecture Questions

- What authentication provider will HOOS use?
- What cloud deployment shape is expected for the first release?
- Which audit and compliance needs are mandatory for launch?