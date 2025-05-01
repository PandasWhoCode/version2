---
title: "Monitoring Guide"
linkTitle: "Monitoring"
weight: 5
description: >
  How to monitor your VersionTwo deployments and applications
---

# Monitoring Guide

This guide explains how to set up and configure monitoring for your VersionTwo deployments and applications.

## Monitoring Overview

VersionTwo provides several monitoring capabilities:

1. System Metrics
2. Application Performance
3. Resource Utilization
4. Health Checks
5. Alerting

## System Metrics

### Basic Metrics

```bash
# Enable system metrics collection
version2 config set monitoring.system.enabled true

# Configure collection interval
version2 config set monitoring.system.interval 60s
```

### Available Metrics

| Metric | Description | Unit |
|--------|-------------|------|
| `cpu.usage` | CPU utilization | % |
| `memory.used` | Memory usage | MB |
| `disk.used` | Disk space used | GB |
| `network.in` | Network inbound traffic | MB/s |
| `network.out` | Network outbound traffic | MB/s |

## Application Performance

### Performance Monitoring

```yaml
# .versiontwo/monitoring.yaml
performance:
  enabled: true
  metrics:
    - name: response_time
      type: histogram
      labels: ["endpoint", "method"]
    - name: request_rate
      type: counter
      labels: ["endpoint", "status"]
    - name: error_rate
      type: gauge
      labels: ["endpoint", "error_type"]
```

### Tracing

```bash
# Enable distributed tracing
version2 config set monitoring.tracing.enabled true

# Configure tracing backend
version2 config set monitoring.tracing.backend jaeger
version2 config set monitoring.tracing.endpoint http://jaeger:14268
```

## Resource Utilization

### Resource Monitoring

```yaml
# .versiontwo/resources.yaml
monitoring:
  resources:
    cpu:
      threshold: 80
      window: 5m
    memory:
      threshold: 85
      window: 5m
    disk:
      threshold: 90
      window: 5m
```

### Auto-scaling

```yaml
# .versiontwo/autoscale.yaml
autoscale:
  enabled: true
  metrics:
    - name: cpu_utilization
      target: 70
      min: 1
      max: 5
    - name: memory_utilization
      target: 75
      min: 1
      max: 5
```

## Health Checks

### Basic Health Checks

```bash
# Enable health checks
version2 config set monitoring.health.enabled true

# Configure check interval
version2 config set monitoring.health.interval 30s
```

### Custom Health Checks

```yaml
# .versiontwo/health.yaml
checks:
  - name: api_health
    type: http
    endpoint: /health
    interval: 30s
    timeout: 5s
    success_threshold: 2
    failure_threshold: 3
  - name: db_health
    type: tcp
    endpoint: localhost:5432
    interval: 30s
    timeout: 5s
```

## Alerting

### Alert Configuration

```yaml
# .versiontwo/alerts.yaml
alerts:
  - name: high_cpu
    condition: "cpu.usage > 80"
    duration: "5m"
    severity: warning
    channels: ["email", "slack"]
  - name: high_memory
    condition: "memory.used > 85"
    duration: "5m"
    severity: critical
    channels: ["email", "slack", "pagerduty"]
```

### Notification Channels

```yaml
# .versiontwo/notifications.yaml
channels:
  email:
    type: smtp
    host: smtp.example.com
    port: 587
    from: alerts@versiontwo.com
    to: ["team@example.com"]
  slack:
    type: webhook
    url: https://hooks.slack.com/services/xxx
  pagerduty:
    type: api
    key: YOUR_PAGERDUTY_KEY
```

## Dashboards

### Default Dashboards

```bash
# Enable default dashboards
version2 config set monitoring.dashboards.enabled true

# Configure dashboard refresh
version2 config set monitoring.dashboards.refresh 30s
```

### Custom Dashboards

```yaml
# .versiontwo/dashboards.yaml
dashboards:
  - name: system_overview
    panels:
      - title: CPU Usage
        type: graph
        metrics: ["cpu.usage"]
      - title: Memory Usage
        type: graph
        metrics: ["memory.used"]
      - title: Disk Usage
        type: graph
        metrics: ["disk.used"]
```

## Log Management

### Log Collection

```yaml
# .versiontwo/logging.yaml
collection:
  enabled: true
  format: json
  retention: 30d
  rotation:
    max_size: 100MB
    max_files: 10
```

### Log Analysis

```bash
# Enable log analysis
version2 config set monitoring.logs.analysis true

# Configure analysis rules
version2 config set monitoring.logs.rules /path/to/rules.yaml
```

## Monitoring Best Practices

1. Set up comprehensive monitoring from the start
2. Use appropriate metrics for your use case
3. Configure meaningful alert thresholds
4. Implement proper log rotation and retention
5. Regular review of monitoring setup
6. Test alerting channels regularly
7. Document monitoring configuration
8. Regular capacity planning

## Next Steps

- Backup Guide](/docs/guides/backup/) - Protect your monitoring data
- Scaling Guide](/docs/guides/scaling/) - Scale your monitoring setup
- Reference Documentation](/docs/reference/monitoring/) - Detailed monitoring reference

## Troubleshooting

If you encounter monitoring issues:

1. Check the Troubleshooting Guide](/docs/tutorials/troubleshooting/)
2. Review monitoring logs with `version2 logs --type monitoring`
3. Check the [GitHub Issues](https://github.com/versiontwo/cli/issues) for known problems
4. Contact [Support](/support/) if you need additional help 