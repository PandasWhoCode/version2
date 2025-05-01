---
title: "Referência da API"
linkTitle: "API"
weight: 1
description: >
  Referência completa para endpoints e uso da API do VersionTwo
---

# Referência da API

A API do VersionTwo fornece uma interface RESTful para gerenciar suas implantações do VersionTwo programaticamente.

## URL Base

```
https://api.versiontwo.com/v1
```

## Autenticação

Todas as requisições à API requerem autenticação usando uma chave API. Inclua sua chave API no cabeçalho `Authorization`:

```bash
Authorization: Bearer SUA_CHAVE_API
```

### Gerenciamento de Chaves API

- Gerar chaves API usando a CLI: `version2 keys generate`
- Listar chaves API: `version2 keys list`
- Revogar chaves API: `version2 keys revoke <id-da-chave>`

## Limites de Taxa

- 100 requisições por minuto por chave API
- Cabeçalhos de limite de taxa incluídos nas respostas:
  - `X-RateLimit-Limit`: Máximo de requisições por minuto
  - `X-RateLimit-Remaining`: Requisições restantes na janela atual
  - `X-RateLimit-Reset`: Tempo quando o limite de taxa é redefinido

## Endpoints

### Projetos

#### Listar Projetos

```http
GET /projects
```

Resposta:
```json
{
  "projects": [
    {
      "id": "proj_123",
      "name": "Meu Projeto",
      "created_at": "2024-02-26T12:00:00Z",
      "updated_at": "2024-02-26T12:00:00Z"
    }
  ]
}
```

#### Obter Projeto

```http
GET /projects/{project_id}
```

Resposta:
```json
{
  "id": "proj_123",
  "name": "Meu Projeto",
  "created_at": "2024-02-26T12:00:00Z",
  "updated_at": "2024-02-26T12:00:00Z",
  "config": {
    "environment": "production",
    "region": "us-west-2"
  }
}
```

#### Criar Projeto

```http
POST /projects
```

Requisição:
```json
{
  "name": "Novo Projeto",
  "config": {
    "environment": "production",
    "region": "us-west-2"
  }
}
```

#### Atualizar Projeto

```http
PATCH /projects/{project_id}
```

Requisição:
```json
{
  "name": "Projeto Atualizado",
  "config": {
    "environment": "staging"
  }
}
```

#### Excluir Projeto

```http
DELETE /projects/{project_id}
```

### Workspaces

#### Listar Workspaces

```http
GET /workspaces
```

Resposta:
```json
{
  "workspaces": [
    {
      "id": "ws_123",
      "name": "Desenvolvimento",
      "created_at": "2024-02-26T12:00:00Z"
    }
  ]
}
```

#### Obter Workspace

```http
GET /workspaces/{workspace_id}
```

#### Criar Workspace

```http
POST /workspaces
```

Requisição:
```json
{
  "name": "Novo Workspace",
  "config": {
    "environment": "development"
  }
}
```

### Implantações

#### Listar Implantações

```http
GET /projects/{project_id}/deployments
```

Resposta:
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

#### Obter Implantação

```http
GET /projects/{project_id}/deployments/{deployment_id}
```

#### Criar Implantação

```http
POST /projects/{project_id}/deployments
```

Requisição:
```json
{
  "version": "v1.0.0",
  "config": {
    "environment": "production"
  }
}
```

#### Reverter Implantação

```http
POST /projects/{project_id}/deployments/{deployment_id}/rollback
```

### Monitoramento

#### Obter Métricas

```http
GET /projects/{project_id}/metrics
```

Parâmetros de Consulta:
- `start_time`: Hora inicial para métricas (ISO 8601)
- `end_time`: Hora final para métricas (ISO 8601)
- `interval`: Intervalo de métricas (1m, 5m, 1h)

Resposta:
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

#### Obter Logs

```http
GET /projects/{project_id}/logs
```

Parâmetros de Consulta:
- `start_time`: Hora inicial para logs (ISO 8601)
- `end_time`: Hora final para logs (ISO 8601)
- `level`: Nível de log (debug, info, warn, error)
- `component`: Nome do componente

Resposta:
```json
{
  "logs": [
    {
      "timestamp": "2024-02-26T12:00:00Z",
      "level": "info",
      "component": "api",
      "message": "Requisição processada"
    }
  ]
}
```

### Configuração

#### Obter Configuração

```http
GET /projects/{project_id}/config
```

#### Atualizar Configuração

```http
PATCH /projects/{project_id}/config
```

Requisição:
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

### Segurança

#### Listar Chaves API

```http
GET /api-keys
```

#### Criar Chave API

```http
POST /api-keys
```

Requisição:
```json
{
  "name": "Chave de Produção",
  "permissions": ["read", "write"]
}
```

#### Revogar Chave API

```http
DELETE /api-keys/{key_id}
```

## Tratamento de Erros

### Formato de Resposta de Erro

```json
{
  "error": {
    "code": "invalid_request",
    "message": "Parâmetros de requisição inválidos",
    "details": {
      "field": "name",
      "reason": "required"
    }
  }
}
```

### Códigos de Erro Comuns

| Código | Descrição |
|--------|-----------|
| `invalid_request` | Parâmetros de requisição inválidos |
| `unauthorized` | Autenticação necessária |
| `forbidden` | Permissões insuficientes |
| `not_found` | Recurso não encontrado |
| `conflict` | Conflito de recurso |
| `rate_limited` | Limite de taxa excedido |
| `internal_error` | Erro interno do servidor |

## Melhores Práticas

1. Sempre use HTTPS
2. Implemente tratamento de erros adequado
3. Faça cache de respostas quando apropriado
4. Use paginação para grandes conjuntos de dados
5. Monitore limites de taxa
6. Mantenha chaves API seguras
7. Use métodos HTTP apropriados
8. Valide parâmetros de requisição
9. Trate timeouts graciosamente
10. Implemente lógica de retry

## SDKs

SDKs oficiais disponíveis para:

- [Python](/reference/sdk/python/)
- [JavaScript](/reference/sdk/javascript/)
- [Go](/reference/sdk/go/)
- [Java](/reference/sdk/java/)

## Webhooks

Configure webhooks para receber notificações em tempo real de eventos:

```http
POST /projects/{project_id}/webhooks
```

Requisição:
```json
{
  "url": "https://example.com/webhook",
  "events": ["deployment.completed", "deployment.failed"]
}
```

## Versionamento

A API é versionada usando o caminho da URL. A versão atual é v1.

- Versão atual: v1
- Versões depreciadas serão anunciadas com 6 meses de antecedência
- Mudanças que quebram compatibilidade serão introduzidas apenas em novas versões principais 