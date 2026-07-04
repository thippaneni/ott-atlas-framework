# AI Engineer Instruction

## Metadata

- Version: 0.1.0
- Status: Draft
- Layer: Instructions
- Depends on: skills/openai.md, skills/python.md, ADR-0005, ADR-0006

## Purpose

Guide AI workflow, prompt, context, and validation work while preserving Atlas provider agnosticism.

## Scope

Use for AI-assisted workflows, prompt templates, context loading, structured outputs, evaluations, and AI integration helpers.

## Instruction

- Keep persistent engineering knowledge in Atlas files, not prompts.
- Use prompts to orchestrate work against selected Atlas context.
- Keep provider-specific assumptions outside core Atlas knowledge.
- Validate AI outputs against schemas, specifications, and acceptance criteria.
- Treat AI output as a draft until verified.
- Keep secrets out of prompts, logs, documentation, and source control.

## Inputs

- Prompts, contexts, specifications, schemas, evaluation criteria.

## Outputs

- AI workflow guidance, prompt patterns, context profiles, validation notes.

## Definition of Done

- Context is scoped to the task.
- Outputs are validated.
- Provider-specific choices are isolated.
