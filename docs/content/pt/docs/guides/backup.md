---
title: "Guia de Backup"
linkTitle: "Backup"
weight: 6
description: >
  Como configurar e gerenciar backups para suas implantações VersionTwo
---

# Guia de Backup

Este guia explica como configurar e gerenciar backups para suas implantações VersionTwo, garantindo a segurança dos dados e a recuperação de desastres.

## Visão Geral do Backup

O VersionTwo suporta vários tipos de backup:

1. Backups Completos
2. Backups Incrementais
3. Backups Diferenciais
4. Recuperação Pontual
5. Backups de Configuração

## Configuração de Backup

### Configuração Básica

```bash
# Habilitar serviço de backup
version2 config set backup.enabled true

# Configurar agendamento de backup
version2 config set backup.schedule "0 0 * * *"  # Diariamente à meia-noite
```

### Configuração de Armazenamento

```yaml
# .versiontwo/backup.yaml
storage:
  type: s3
  bucket: versiontwo-backups
  region: us-west-2
  path: /backups
  retention: 30d
```

## Tipos de Backup

### Backup Completo

```bash
# Criar um backup completo
version2 backup create --type full

# Agendar backups completos
version2 config set backup.full.schedule "0 0 * * 0"  # Semanalmente no domingo
```

### Backup Incremental

```bash
# Criar um backup incremental
version2 backup create --type incremental

# Configurar backup incremental
version2 config set backup.incremental.schedule "0 0 * * *"  # Diariamente
version2 config set backup.incremental.retention 7d
```

### Backup Diferencial

```bash
# Criar um backup diferencial
version2 backup create --type differential

# Configurar backup diferencial
version2 config set backup.differential.schedule "0 0 * * 0"  # Semanalmente
version2 config set backup.differential.retention 30d
```

## Componentes de Backup

### Backup de Banco de Dados

```yaml
# .versiontwo/backup.yaml
database:
  enabled: true
  type: postgresql
  schedule: "0 1 * * *"  # Diariamente às 1h
  retention: 30d
  compression: true
  encryption: true
```

### Backup do Sistema de Arquivos

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
  schedule: "0 2 * * *"  # Diariamente às 2h
```

### Backup de Configuração

```yaml
# .versiontwo/backup.yaml
config:
  enabled: true
  schedule: "0 3 * * *"  # Diariamente às 3h
  include:
    - /etc/versiontwo
    - ~/.versiontwo
  retention: 90d
```

## Gerenciamento de Backup

### Listar Backups

```bash
# Listar todos os backups
version2 backup list

# Listar backups por tipo
version2 backup list --type full
version2 backup list --type incremental
```

### Restaurar Backups

```bash
# Restaurar de um backup
version2 backup restore --id backup-123

# Restaurar componentes específicos
version2 backup restore --id backup-123 --component database
version2 backup restore --id backup-123 --component filesystem
```

### Verificar Backups

```bash
# Verificar integridade do backup
version2 backup verify --id backup-123

# Testar restauração do backup
version2 backup test-restore --id backup-123
```

## Armazenamento de Backup

### Armazenamento Local

```yaml
# .versiontwo/backup.yaml
storage:
  type: local
  path: /var/backups/versiontwo
  retention: 30d
  compression: true
  encryption: true
```

### Armazenamento em Nuvem

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

## Segurança de Backup

### Criptografia

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

### Controle de Acesso

```yaml
# .versiontwo/backup.yaml
access:
  iam:
    role: versiontwo-backup-role
    policy: versiontwo-backup-policy
  encryption:
    kms_key: arn:aws:kms:region:account:key/key-id
```

## Monitoramento de Backups

### Status do Backup

```bash
# Verificar status do backup
version2 backup status

# Monitorar progresso do backup
version2 backup monitor
```

### Alertas de Backup

```yaml
# .versiontwo/alerts.yaml
backup:
  - name: backup_falhou
    condition: "backup.status == 'failed'"
    severity: critical
    channels: ["email", "slack"]
  - name: backup_atrasado
    condition: "backup.last_success > 24h"
    severity: warning
    channels: ["email"]
```

## Melhores Práticas de Backup

1. Implementar a regra 3-2-1 de backup
2. Teste e verificação regular de backups
3. Criptografar dados sensíveis de backup
4. Usar políticas de retenção apropriadas
5. Monitorar sucesso e falhas de backup
6. Documentar procedimentos de backup e restauração
7. Planejamento regular de capacidade de backup
8. Testar procedimentos de recuperação de desastres

## Próximos Passos

- [Guia de Recuperação de Desastres](/guides/disaster-recovery/) - Planejar recuperação de desastres
- [Guia de Segurança](/guides/security/) - Proteger seus backups
- [Documentação de Referência](/reference/backup/) - Referência detalhada de backup

## Solução de Problemas

Se você encontrar problemas com backup:

1. Verifique o [Guia de Solução de Problemas](/tutorials/troubleshooting/)
2. Revise os logs de backup com `version2 logs --type backup`
3. Verifique os [Problemas no GitHub](https://github.com/versiontwo/cli/issues) para problemas conhecidos
4. Entre em contato com o [Suporte](/support/) se precisar de ajuda adicional 