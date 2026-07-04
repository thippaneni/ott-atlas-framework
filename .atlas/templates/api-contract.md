# API Contract Template

## Metadata

- Version: 0.1.0
- Status: Draft
- Layer: Templates
- Artifact Type: API Contract

## Endpoint

`METHOD /path`

## Purpose

<!-- What capability does this endpoint provide? -->

## Source Specification

- <!-- Feature spec, story, or task reference -->

## Authentication / Authorization

<!-- Required authentication and authorization behavior. -->

## Request

### Path Parameters

| Name | Type | Required | Description |
| ---- | ---- | -------- | ----------- |
|      |      |          |             |

### Query Parameters

| Name | Type | Required | Description |
| ---- | ---- | -------- | ----------- |
|      |      |          |             |

### Body

```json
{}
```

## Response

### Success

Status: `200 OK`

```json
{}
```

### Errors

| Status | Code | Description |
| ------ | ---- | ----------- |
| 400    |      |             |
| 401    |      |             |
| 403    |      |             |
| 404    |      |             |
| 409    |      |             |
| 500    |      |             |

## Validation Rules

- <!-- Input or business validation rule -->

## Observability

- <!-- Logging, metrics, audit, correlation ID expectations -->

## Test Coverage

- [ ] Success path
- [ ] Validation failure
- [ ] Authorization failure
- [ ] Domain failure
