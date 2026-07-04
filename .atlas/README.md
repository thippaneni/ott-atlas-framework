# Atlas Framework

Atlas is an AI-native engineering framework for Specification-Driven Software Development (SDSD).

It standardizes how AI assistants, developers, and engineering teams collaborate across the software development lifecycle while keeping specifications, engineering standards, and architectural decisions as the source of truth.

## Purpose

Atlas ensures implementation follows documented intent, architecture, standards, and validation rules.

## Current Release

Atlas v0.2.0 establishes the Engineering Knowledge System.

This release turns Atlas from a core folder structure into a usable framework for AI-assisted engineering. It adds registered standards, rules, patterns, skills, instructions, agents, checklists, templates, and validation support.

## Core Responsibilities

- Specification management
- Context management
- AI agent orchestration
- Engineering standards
- Development patterns
- Knowledge management
- Prompt templates
- Validation rules
- Project governance

## Root Files

- `manifest.yaml`: Atlas and project identity, architecture, version, and AI configuration.
- `index.yaml`: Knowledge graph, module discovery, dependency graph, load order, and context resolution.
- `capabilities.yaml`: Capability-first map of what Atlas can do and which agents can perform each capability.
- `contexts.yaml`: Reusable context-loading profiles for focused work.
- `principles.md`: Immutable engineering principles that apply to every Atlas project.
- `ATS.md`: Atlas Technical Specification.

## Knowledge System

Atlas organizes engineering knowledge into reusable modules:

- `standards/`: Engineering standards for coding, documentation, APIs, databases, security, testing, performance, and Git.
- `rules/`: Machine-readable validation and governance rules.
- `patterns/`: Reusable engineering patterns such as vertical slice, result pattern, DDD, modular monolith, repository, specification, factory, and domain events.
- `skills/`: Stack-aware implementation skills for .NET, Angular, PostgreSQL, AWS, OpenAI, Python, and testing.
- `instructions/`: Role-specific operating instructions for architects, backend engineers, frontend engineers, database engineers, AI engineers, DevOps, testers, reviewers, and product managers.
- `agents/`: Machine-readable agent configurations that compose standards, rules, patterns, skills, and instructions.
- `checklists/`: Verification checklists for API, security, testing, review, release, specification, database, and frontend work.
- `templates/`: Artifact templates for vision, PRD, SRS, ADR, feature specs, API contracts, test plans, domain models, and architecture.

## Logical Layers

1. Project Metadata
2. Engineering Governance
3. AI Context Management
4. Knowledge System
5. Specifications

Every layer depends only on lower layers.

## Boot Sequence

Atlas should be loaded in this order:

1. `manifest.yaml`
2. `ATS.md`
3. `principles.md`
4. `index.yaml`
5. `contexts.yaml`
6. `capabilities.yaml`
7. Requested task context
8. Relevant specifications
9. Implementation or review workflow

## Validation

Atlas includes a dependency-free validator:

```bash
python tools/validate-atlas.py
```

The validator checks required files, JSON schemas, references, agent configs, rule configs, context structure, and obvious secret-like values.

The v0.2.0 release validates successfully with `0 errors` and `0 warnings`.

## Release Notes

### v0.2.0 - Engineering Knowledge System

- Added standards, rules, patterns, skills, instructions, agents, checklists, and templates.
- Added capability-first `capabilities.yaml` design with separate agent mappings.
- Added selective context-loading profiles in `contexts.yaml`.
- Added complete registry entries in `index.yaml`.
- Added validation schemas and `tools/validate-atlas.py`.
- Added Atlas ADR-0001 through ADR-0006.

### v0.1.0 - Atlas Core

- Added Atlas root structure and core files.
- Added Atlas Technical Specification, principles, manifest, index, capabilities, contexts, and initial schemas.
