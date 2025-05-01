---
title: "Backup Guide"
linkTitle: "Backup"
weight: 6
description: >
  How to set up and manage backups for your VersionTwo deployments
---

# Backup Guide

This guide explains how to set up and manage backups for your VersionTwo deployments, ensuring data safety and disaster recovery.

## Backup Overview

VersionTwo supports several backup types:

1. Full Backups
2. Incremental Backups
3. Differential Backups
4. Point-in-Time Recovery
5. Configuration Backups

## Backup Configuration

### Basic Setup

```bash
# Enable backup service
version2 config set backup.enabled true

# Configure backup schedule
version2 config set backup.schedule "0 0 * * *"  # Daily at midnight
```

### Storage Configuration

```yaml
# .versiontwo/backup.yaml
storage:
  type: s3
  bucket: versiontwo-backups
  region: us-west-2
  path: /backups
  retention: 30d
```

## Backup Types

### Full Backup

```bash
# Create a full backup
version2 backup create --type full

# Schedule full backups
version2 config set backup.full.schedule "0 0 * * 0"  # Weekly on Sunday
```

### Incremental Backup

```bash
# Create an incremental backup
version2 backup create --type incremental

# Configure incremental backup
version2 config set backup.incremental.schedule "0 0 * * *"  # Daily
version2 config set backup.incremental.retention 7d
```

### Differential Backup

```bash
# Create a differential backup
version2 backup create --type differential

# Configure differential backup
version2 config set backup.differential.schedule "0 0 * * 0"  # Weekly
version2 config set backup.differential.retention 30d
```

## Backup Components

### Database Backup

```yaml
# .versiontwo/backup.yaml
database:
  enabled: true
  type: postgresql
  schedule: "0 1 * * *"  # Daily at 1 AM
  retention: 30d
  compression: true
  encryption: true
```

### File System Backup

```yaml
# .versiontwo/backup.yaml
filesystem:
  enabled: true
  paths:
    - /var/versiontwo/data
    - /var/versiontwo/config
  exclude:
    - "*.tmp"
    - "*.log"
  schedule: "0 2 * * *"  # Daily at 2 AM
```

### Configuration Backup

```yaml
# .versiontwo/backup.yaml
config:
  enabled: true
  schedule: "0 3 * * *"  # Daily at 3 AM
  include:
    - /etc/versiontwo
    - ~/.versiontwo
  retention: 90d
```

## Backup Management

### List Backups

```bash
# List all backups
version2 backup list

# List backups by type
version2 backup list --type full
version2 backup list --type incremental
```

### Restore Backups

```bash
# Restore from backup
version2 backup restore --id backup-123

# Restore specific components
version2 backup restore --id backup-123 --component database
version2 backup restore --id backup-123 --component filesystem
```

### Verify Backups

```bash
# Verify backup integrity
version2 backup verify --id backup-123

# Test backup restoration
version2 backup test-restore --id backup-123
```

## Backup Storage

### Local Storage

```yaml
# .versiontwo/backup.yaml
storage:
  type: local
  path: /var/backups/versiontwo
  retention: 30d
  compression: true
  encryption: true
```

### Cloud Storage

```yaml
# .versiontwo/backup.yaml
storage:
  type: s3
  provider: aws
  bucket: versiontwo-backups
  region: us-west-2
  path: /backups
  retention: 30d
  encryption: true
  lifecycle:
    enabled: true
    rules:
      - type: transition
        days: 90
        storage: glacier
```

## Backup Security

### Encryption

```yaml
# .versiontwo/backup.yaml
security:
  encryption:
    enabled: true
    algorithm: aes-256-gcm
    key_rotation: 90d
  access:
    iam_role: versiontwo-backup-role
    kms_key: arn:aws:kms:region:account:key/key-id
```

### Access Control

```yaml
# .versiontwo/backup.yaml
access:
  iam:
    role: versiontwo-backup-role
    policy: versiontwo-backup-policy
  encryption:
    kms_key: arn:aws:kms:region:account:key/key-id
```

## Monitoring Backups

### Backup Status

```bash
# Check backup status
version2 backup status

# Monitor backup progress
version2 backup monitor
```

### Backup Alerts

```yaml
# .versiontwo/alerts.yaml
backup:
  - name: backup_failed
    condition: "backup.status == 'failed'"
    severity: critical
    channels: ["email", "slack"]
  - name: backup_delayed
    condition: "backup.last_success > 24h"
    severity: warning
    channels: ["email"]
```

## Backup Best Practices

1. Implement the 3-2-1 backup rule
2. Regular backup testing and verification
3. Encrypt sensitive backup data
4. Use appropriate retention policies
5. Monitor backup success and failures
6. Document backup and restore procedures
7. Regular backup capacity planning
8. Test disaster recovery procedures

## Next Steps

- Disaster Recovery Guide](/docs/guides/disaster-recovery/) - Plan for disaster recovery
- Security Guide](/docs/guides/security/) - Secure your backups
- Reference Documentation](/docs/reference/backup/) - Detailed backup reference

## Troubleshooting

If you encounter backup issues:

1. Check the Troubleshooting Guide](/docs/tutorials/troubleshooting/)
2. Review backup logs with `version2 logs --type backup`
3. Check the [GitHub Issues](https://github.com/versiontwo/cli/issues) for known problems
4. Contact [Support](/support/) if you need additional help 