---
title: "Configuration Guide"
linkTitle: "Configuration"
weight: 2
description: >
  How to customize Version2 for your needs
---

# Configuration Guide

This guide explains how to configure Version2 to match your workflow and requirements.

## Configuration Files

Version2 uses the following configuration files:

- `~/.version2/config.yaml` - Global configuration
- `./version2.yaml` - Project-specific configuration
- `./.version2/workspace.yaml` - Workspace-specific settings

## Global Configuration

### Basic Settings

```yaml
# ~/.version2/config.yaml
api:
  key: YOUR_API_KEY
  endpoint: https://api.version2.com/v1

workspace:
  default: ~/version2-projects
  auto_create: true

editor:
  name: vscode
  path: /usr/local/bin/code

theme:
  color_scheme: dark
  font_size: 14
```

### Available Settings

| Setting | Description | Default |
|---------|-------------|---------|
| `api.key` | Your Version2 API key | - |
| `api.endpoint` | API endpoint URL | https://api.version2.com/v1 |
| `workspace.default` | Default workspace path | ~/version2-projects |
| `workspace.auto_create` | Auto-create workspace if missing | true |
| `editor.name` | Default editor | vscode |
| `editor.path` | Path to editor executable | - |
| `theme.color_scheme` | UI color scheme | light |
| `theme.font_size` | Base font size | 14 |

## Project Configuration

### Basic Project Setup

```yaml
# version2.yaml
name: my-project
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

### Project Settings

| Setting | Description | Default |
|---------|-------------|---------|
| `name` | Project name | - |
| `version` | Project version | 1.0.0 |
| `dependencies` | Required components | [] |
| `settings.auto_save` | Enable auto-save | true |
| `settings.sync_interval` | Sync interval (seconds) | 300 |
| `settings.backup_enabled` | Enable backups | true |

## Workspace Configuration

### Basic Workspace Setup

```yaml
# .version2/workspace.yaml
name: development
environment: dev

settings:
  git:
    auto_commit: true
    branch: main
  notifications:
    enabled: true
    channels: [slack, email]
```

### Workspace Settings

| Setting | Description | Default |
|---------|-------------|---------|
| `name` | Workspace name | - |
| `environment` | Environment type | dev |
| `settings.git.auto_commit` | Auto-commit changes | true |
| `settings.git.branch` | Default git branch | main |
| `settings.notifications.enabled` | Enable notifications | true |
| `settings.notifications.channels` | Notification channels | [] |

## Managing Configuration

### View Current Configuration

```bash
# View global config
version2 config list

# View project config
version2 config list --project

# View workspace config
version2 config list --workspace
```

### Update Configuration

```bash
# Update global setting
version2 config set editor.name vim

# Update project setting
version2 config set --project settings.auto_save false

# Update workspace setting
version2 config set --workspace settings.git.auto_commit false
```

### Reset Configuration

```bash
# Reset global config
version2 config reset

# Reset project config
version2 config reset --project

# Reset workspace config
version2 config reset --workspace
```

## Environment Variables

Version2 also supports configuration through environment variables:

```bash
export VERSION2_API_KEY=your_api_key
export VERSION2_WORKSPACE=~/custom-workspace
export VERSION2_EDITOR=vim
```

## Next Steps

- Deployment Guide](/docs/guides/deployment/) - Learn how to deploy your configured projects
- Security Guide](/docs/guides/security/) - Secure your Version2 configuration
- Reference Documentation](/docs/reference/configuration/) - Detailed configuration reference

## Troubleshooting

If you encounter configuration issues:

1. Check the Troubleshooting Guide](/docs/tutorials/troubleshooting/)
2. Verify your configuration with `version2 config validate`
3. Check the [GitHub Issues](https://github.com/version2/cli/issues) for known problems
4. Contact [Support](/support/) if you need additional help 