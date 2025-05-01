---
title: "API Reference"
linkTitle: "API"
weight: 1
description: >
  Complete reference for VersionTwo API endpoints and usage
---

# API Reference

The VersionTwo API provides a RESTful interface for managing your VersionTwo deployments programmatically.

## Base URL

```
https://api.versiontwo.com/v1
```

## Authentication

All API requests require authentication using an API key. Include your API key in the `Authorization` header:

```bash
Authorization: Bearer YOUR_API_KEY
```

### API Key Management

- Generate API keys using the CLI: `version2 keys generate`
- List API keys: `version2 keys list`
- Revoke API keys: `version2 keys revoke <key-id>`

## Rate Limits

- 100 requests per minute per API key
- Rate limit headers included in responses:
  - `X-RateLimit-Limit`: Maximum requests per minute
  - `X-RateLimit-Remaining`: Remaining requests in current window
  - `X-RateLimit-Reset`: Time when rate limit resets

## Endpoints

### Projects

#### List Projects

```http
GET /projects
```

Response:
```json
{
  "projects": [
    {
      "id": "proj_123",
      "name": "My Project",
      "created_at": "2024-02-26T12:00:00Z",
      "updated_at": "2024-02-26T12:00:00Z"
    }
  ]
}
```

#### Get Project

```http
GET /projects/{project_id}
```

Response:
```json
{
  "id": "proj_123",
  "name": "My Project",
  "created_at": "2024-02-26T12:00:00Z",
  "updated_at": "2024-02-26T12:00:00Z",
  "config": {
    "environment": "production",
    "region": "us-west-2"
  }
}
```

#### Create Project

```http
POST /projects
```

Request:
```json
{
  "name": "New Project",
  "config": {
    "environment": "production",
    "region": "us-west-2"
  }
}
```

#### Update Project

```http
PATCH /projects/{project_id}
```

Request:
```json
{
  "name": "Updated Project",
  "config": {
    "environment": "staging"
  }
}
```

#### Delete Project

```http
DELETE /projects/{project_id}
```

### Workspaces

#### List Workspaces

```http
GET /workspaces
```

Response:
```json
{
  "workspaces": [
    {
      "id": "ws_123",
      "name": "Development",
      "created_at": "2024-02-26T12:00:00Z"
    }
  ]
}
```

#### Get Workspace

```http
GET /workspaces/{workspace_id}
```

#### Create Workspace

```http
POST /workspaces
```

Request:
```json
{
  "name": "New Workspace",
  "config": {
    "environment": "development"
  }
}
```

### Deployments

#### List Deployments

```http
GET /projects/{project_id}/deployments
```

Response:
```json
{
  "deployments": [
    {
      "id": "dep_123",
      "version": "v1.0.0",
      "status": "completed",
      "created_at": "2024-02-26T12:00:00Z"
    }
  ]
}
```

#### Get Deployment

```http
GET /projects/{project_id}/deployments/{deployment_id}
```

#### Create Deployment

```http
POST /projects/{project_id}/deployments
```

Request:
```json
{
  "version": "v1.0.0",
  "config": {
    "environment": "production"
  }
}
```

#### Rollback Deployment

```http
POST /projects/{project_id}/deployments/{deployment_id}/rollback
```

### Monitoring

#### Get Metrics

```http
GET /projects/{project_id}/metrics
```

Query Parameters:
- `start_time`: Start time for metrics (ISO 8601)
- `end_time`: End time for metrics (ISO 8601)
- `interval`: Metrics interval (1m, 5m, 1h)

Response:
```json
{
  "metrics": {
    "cpu": {
      "values": [
        {
          "timestamp": "2024-02-26T12:00:00Z",
          "value": 45.2
        }
      ]
    },
    "memory": {
      "values": [
        {
          "timestamp": "2024-02-26T12:00:00Z",
          "value": 1024
        }
      ]
    }
  }
}
```

#### Get Logs

```http
GET /projects/{project_id}/logs
```

Query Parameters:
- `start_time`: Start time for logs (ISO 8601)
- `end_time`: End time for logs (ISO 8601)
- `level`: Log level (debug, info, warn, error)
- `component`: Component name

Response:
```json
{
  "logs": [
    {
      "timestamp": "2024-02-26T12:00:00Z",
      "level": "info",
      "component": "api",
      "message": "Request processed"
    }
  ]
}
```

### Configuration

#### Get Configuration

```http
GET /projects/{project_id}/config
```

#### Update Configuration

```http
PATCH /projects/{project_id}/config
```

Request:
```json
{
  "environment": "production",
  "region": "us-west-2",
  "scaling": {
    "min_instances": 2,
    "max_instances": 10
  }
}
```

### Security

#### List API Keys

```http
GET /api-keys
```

#### Create API Key

```http
POST /api-keys
```

Request:
```json
{
  "name": "Production Key",
  "permissions": ["read", "write"]
}
```

#### Revoke API Key

```http
DELETE /api-keys/{key_id}
```

## Error Handling

### Error Response Format

```json
{
  "error": {
    "code": "invalid_request",
    "message": "Invalid request parameters",
    "details": {
      "field": "name",
      "reason": "required"
    }
  }
}
```

### Common Error Codes

| Code | Description |
|------|-------------|
| `invalid_request` | Invalid request parameters |
| `unauthorized` | Authentication required |
| `forbidden` | Insufficient permissions |
| `not_found` | Resource not found |
| `conflict` | Resource conflict |
| `rate_limited` | Rate limit exceeded |
| `internal_error` | Internal server error |

## Best Practices

1. Always use HTTPS
2. Implement proper error handling
3. Cache responses when appropriate
4. Use pagination for large datasets
5. Monitor rate limits
6. Keep API keys secure
7. Use appropriate HTTP methods
8. Validate request parameters
9. Handle timeouts gracefully
10. Implement retry logic

## SDKs

Official SDKs are available for:

- Python](/docs/reference/sdk/python/)
- JavaScript](/docs/reference/sdk/javascript/)
- Go](/docs/reference/sdk/go/)
- Java](/docs/reference/sdk/java/)

## Webhooks

Configure webhooks to receive real-time notifications for events:

```http
POST /projects/{project_id}/webhooks
```

Request:
```json
{
  "url": "https://example.com/webhook",
  "events": ["deployment.completed", "deployment.failed"]
}
```

## Versioning

The API is versioned using the URL path. The current version is v1.

- Current version: v1
- Deprecated versions will be announced 6 months in advance
- Breaking changes will only be introduced in new major versions 