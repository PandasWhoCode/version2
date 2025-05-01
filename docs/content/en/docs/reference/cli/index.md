---
title: "CLI Reference"
linkTitle: "CLI"
weight: 2
description: >
  Complete reference for VersionTwo CLI commands and usage
---

# CLI Reference

The VersionTwo CLI provides a command-line interface for managing your VersionTwo deployments.

## Basic Commands

### version2 init

Initialize a new VersionTwo project in the current directory.

```bash
version2 init [project-name] [flags]
```

Flags:
- `--template`: Template to use (default "basic")
- `--path`: Path to initialize project (default ".")

### version2 status

Show the status of the current project.

```bash
version2 status [flags]
```

Flags:
- `--output`: Output format (json|yaml|table) (default "table")

## Project Management

### version2 project

Manage VersionTwo projects.

```bash
version2 project [command] [flags]
```

Commands:
- `list`: List all projects
- `create`: Create a new project
- `delete`: Delete a project
- `update`: Update project settings

### version2 workspace

Manage VersionTwo workspaces.

```bash
version2 workspace [command] [flags]
```

Commands:
- `list`: List all workspaces
- `create`: Create a new workspace
- `delete`: Delete a workspace
- `switch`: Switch to a different workspace

## Configuration

### version2 config

Manage VersionTwo configuration.

```bash
version2 config [command] [flags]
```

Commands:
- `view`: View current configuration
- `set`: Set configuration values
- `unset`: Unset configuration values
- `reset`: Reset configuration to defaults

### version2 env

Manage environment variables.

```bash
version2 env [command] [flags]
```

Commands:
- `list`: List environment variables
- `set`: Set environment variables
- `unset`: Unset environment variables

## Deployment

### version2 deploy

Deploy the current project.

```bash
version2 deploy [flags]
```

Flags:
- `--environment`: Target environment (default "development")
- `--version`: Version tag for the deployment
- `--wait`: Wait for deployment to complete

### version2 rollback

Rollback to a previous deployment.

```bash
version2 rollback [deployment-id] [flags]
```

Flags:
- `--wait`: Wait for rollback to complete

## Monitoring

### version2 logs

View logs for the current project.

```bash
version2 logs [flags]
```

Flags:
- `--follow`: Follow log output
- `--since`: Show logs since timestamp
- `--tail`: Number of lines to show from the end
- `--level`: Minimum log level (debug|info|warn|error)

### version2 metrics

View metrics for the current project.

```bash
version2 metrics [flags]
```

Flags:
- `--start`: Start time for metrics
- `--end`: End time for metrics
- `--interval`: Metrics interval (1m|5m|1h)

## Security

### version2 keys

Manage API keys.

```bash
version2 keys [command] [flags]
```

Commands:
- `generate`: Generate a new API key
- `list`: List all API keys
- `revoke`: Revoke an API key

### version2 auth

Manage authentication.

```bash
version2 auth [command] [flags]
```

Commands:
- `login`: Log in to VersionTwo
- `logout`: Log out from VersionTwo
- `status`: Show authentication status

## Maintenance

### version2 update

Update VersionTwo CLI to the latest version.

```bash
version2 update [flags]
```

Flags:
- `--channel`: Update channel (stable|beta)

### version2 cleanup

Clean up temporary files and caches.

```bash
version2 cleanup [flags]
```

Flags:
- `--all`: Remove all caches and temporary files

## Troubleshooting

### version2 doctor

Check VersionTwo installation for common issues.

```bash
version2 doctor [flags]
```

Flags:
- `--fix`: Attempt to fix issues automatically

### version2 diagnose

Generate a diagnostic report.

```bash
version2 diagnose [flags]
```

Flags:
- `--output`: Output format (json|yaml|text)
- `--include-logs`: Include recent logs in report

## Global Options

These options are available for all commands:

- `--help`: Show help for command
- `--debug`: Enable debug output
- `--quiet`: Suppress all output except errors
- `--config`: Path to config file
- `--workspace`: Workspace to use
- `--output`: Output format (json|yaml|table)

## Environment Variables

The CLI respects the following environment variables:

- `VERSION2_API_KEY`: API key for authentication
- `VERSION2_WORKSPACE`: Default workspace
- `VERSION2_CONFIG_FILE`: Path to config file
- `VERSION2_DEBUG`: Enable debug output (1|true)
- `VERSION2_OUTPUT`: Default output format

## Exit Codes

The CLI uses the following exit codes:

| Code | Description |
|------|-------------|
| 0 | Success |
| 1 | General error |
| 2 | Invalid usage |
| 3 | Configuration error |
| 4 | Network error |
| 5 | Authentication error |
| 6 | Permission error |

## Usage Examples

1. Initialize a new project:
```bash
version2 init my-project --template basic
```

2. Deploy to production:
```bash
version2 deploy --environment production --version v1.0.0
```

3. View logs:
```bash
version2 logs --follow --level error
```

4. Generate and use a new API key:
```bash
version2 keys generate --name "CI/CD Key"
export VERSION2_API_KEY="..."
```

5. Switch workspaces:
```bash
version2 workspace switch development
``` 