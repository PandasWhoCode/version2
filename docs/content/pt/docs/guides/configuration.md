---
title: "Guia de Configuração"
linkTitle: "Configuração"
weight: 2
description: >
  Como personalizar o VersionTwo para suas necessidades
---

# Guia de Configuração

Este guia explica como configurar o VersionTwo para atender ao seu fluxo de trabalho e requisitos.

## Arquivos de Configuração

O VersionTwo utiliza os seguintes arquivos de configuração:

- `~/.versiontwo/config.yaml` - Configuração global
- `./versiontwo.yaml` - Configuração específica do projeto
- `./.versiontwo/workspace.yaml` - Configurações específicas do workspace

## Configuração Global

### Configurações Básicas

```yaml
# ~/.versiontwo/config.yaml
api:
  key: SUA_CHAVE_API
  endpoint: https://api.versiontwo.com/v1

workspace:
  default: ~/versiontwo-projects
  auto_create: true

editor:
  name: vscode
  path: /usr/local/bin/code

theme:
  color_scheme: dark
  font_size: 14
```

### Configurações Disponíveis

| Configuração | Descrição | Padrão |
|--------------|-----------|---------|
| `api.key` | Sua chave de API do VersionTwo | - |
| `api.endpoint` | URL do endpoint da API | https://api.versiontwo.com/v1 |
| `workspace.default` | Caminho padrão do workspace | ~/versiontwo-projects |
| `workspace.auto_create` | Criar workspace automaticamente se não existir | true |
| `editor.name` | Editor padrão | vscode |
| `editor.path` | Caminho para o executável do editor | - |
| `theme.color_scheme` | Esquema de cores da interface | light |
| `theme.font_size` | Tamanho base da fonte | 14 |

## Configuração do Projeto

### Configuração Básica do Projeto

```yaml
# versiontwo.yaml
name: meu-projeto
version: 1.0.0

dependencies:
  - name: core
    version: ">=1.0.0"
  - name: database
    version: ">=2.1.0"

settings:
  auto_save: true
  sync_interval: 300
  backup_enabled: true
```

### Configurações do Projeto

| Configuração | Descrição | Padrão |
|--------------|-----------|---------|
| `name` | Nome do projeto | - |
| `version` | Versão do projeto | 1.0.0 |
| `dependencies` | Componentes necessários | [] |
| `settings.auto_save` | Habilitar salvamento automático | true |
| `settings.sync_interval` | Intervalo de sincronização (segundos) | 300 |
| `settings.backup_enabled` | Habilitar backups | true |

## Configuração do Workspace

### Configuração Básica do Workspace

```yaml
# .versiontwo/workspace.yaml
name: desenvolvimento
environment: dev

settings:
  git:
    auto_commit: true
    branch: main
  notifications:
    enabled: true
    channels: [slack, email]
```

### Configurações do Workspace

| Configuração | Descrição | Padrão |
|--------------|-----------|---------|
| `name` | Nome do workspace | - |
| `environment` | Tipo de ambiente | dev |
| `settings.git.auto_commit` | Commit automático de alterações | true |
| `settings.git.branch` | Branch git padrão | main |
| `settings.notifications.enabled` | Habilitar notificações | true |
| `settings.notifications.channels` | Canais de notificação | [] |

## Gerenciando Configurações

### Visualizar Configuração Atual

```bash
# Visualizar configuração global
version2 config list

# Visualizar configuração do projeto
version2 config list --project

# Visualizar configuração do workspace
version2 config list --workspace
```

### Atualizar Configuração

```bash
# Atualizar configuração global
version2 config set editor.name vim

# Atualizar configuração do projeto
version2 config set --project settings.auto_save false

# Atualizar configuração do workspace
version2 config set --workspace settings.git.auto_commit false
```

### Resetar Configuração

```bash
# Resetar configuração global
version2 config reset

# Resetar configuração do projeto
version2 config reset --project

# Resetar configuração do workspace
version2 config reset --workspace
```

## Variáveis de Ambiente

O VersionTwo também suporta configuração através de variáveis de ambiente:

```bash
export VERSIONTWO_API_KEY=sua_chave_api
export VERSIONTWO_WORKSPACE=~/workspace-personalizado
export VERSIONTWO_EDITOR=vim
```

## Próximos Passos

- [Guia de Implantação](/guides/deployment/) - Aprenda como implantar seus projetos configurados
- [Guia de Segurança](/guides/security/) - Proteja sua configuração do VersionTwo
- [Documentação de Referência](/reference/configuration/) - Referência detalhada de configuração

## Solução de Problemas

Se você encontrar problemas de configuração:

1. Verifique o [Guia de Solução de Problemas](/tutorials/troubleshooting/)
2. Verifique sua configuração com `version2 config validate`
3. Verifique os [Problemas no GitHub](https://github.com/versiontwo/cli/issues) para problemas conhecidos
4. Entre em contato com o [Suporte](/support/) se precisar de ajuda adicional 