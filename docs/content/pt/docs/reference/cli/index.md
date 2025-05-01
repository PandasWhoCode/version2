---
title: "Interface de Linha de Comando"
linkTitle: "CLI"
weight: 1
description: >
  Referência completa para comandos CLI do VersionTwo
---

# Interface de Linha de Comando

A CLI do VersionTwo fornece um conjunto abrangente de comandos para gerenciar suas implantações do VersionTwo.

## Comandos Básicos

### version2

```bash
# Exibir informações de versão
version2 --version

# Exibir informações de ajuda
version2 --help

# Exibir ajuda do comando
version2 <comando> --help
```

### version2 init

```bash
# Inicializar novo projeto VersionTwo
version2 init

# Inicializar com configuração específica
version2 init --config config.yaml

# Inicializar em diretório específico
version2 init --dir /caminho/para/projeto
```

### version2 status

```bash
# Verificar status do sistema
version2 status

# Verificar status de componente específico
version2 status --component api
version2 status --component database
version2 status --component cache
```

## Gerenciamento de Projetos

### version2 project

```bash
# Criar novo projeto
version2 project create

# Listar projetos
version2 project list

# Obter detalhes do projeto
version2 project get <id-do-projeto>

# Atualizar projeto
version2 project update <id-do-projeto>

# Excluir projeto
version2 project delete <id-do-projeto>
```

### version2 workspace

```bash
# Criar workspace
version2 workspace create

# Listar workspaces
version2 workspace list

# Alternar workspace
version2 workspace switch <id-do-workspace>

# Excluir workspace
version2 workspace delete <id-do-workspace>
```

## Configuração

### version2 config

```bash
# Obter configuração
version2 config get

# Definir configuração
version2 config set <chave> <valor>

# Listar configurações
version2 config list

# Resetar configuração
version2 config reset

# Exportar configuração
version2 config export
```

### version2 env

```bash
# Listar variáveis de ambiente
version2 env list

# Definir variável de ambiente
version2 env set <chave> <valor>

# Obter variável de ambiente
version2 env get <chave>

# Excluir variável de ambiente
version2 env delete <chave>
```

## Implantação

### version2 deploy

```bash
# Implantar projeto
version2 deploy

# Implantar com configuração específica
version2 deploy --config config.yaml

# Implantar em ambiente específico
version2 deploy --env production
```

### version2 rollback

```bash
# Reverter implantação
version2 rollback

# Reverter para versão específica
version2 rollback --version v1.0.0

# Reverter com confirmação
version2 rollback --confirm
```

## Monitoramento

### version2 logs

```bash
# Visualizar logs
version2 logs

# Filtrar logs por componente
version2 logs --component api

# Filtrar logs por nível
version2 logs --level error

# Acompanhar logs
version2 logs --follow
```

### version2 metrics

```bash
# Visualizar métricas
version2 metrics

# Obter métrica específica
version2 metrics --metric cpu

# Obter métricas do componente
version2 metrics --component api
```

## Segurança

### version2 auth

```bash
# Login
version2 auth login

# Logout
version2 auth logout

# Verificar autenticação
version2 auth status
```

### version2 keys

```bash
# Gerar chave API
version2 keys generate

# Listar chaves API
version2 keys list

# Revogar chave API
version2 keys revoke <id-da-chave>
```

## Manutenção

### version2 backup

```bash
# Criar backup
version2 backup create

# Listar backups
version2 backup list

# Restaurar backup
version2 backup restore <id-do-backup>
```

### version2 update

```bash
# Verificar atualizações
version2 update check

# Atualizar CLI
version2 update self

# Atualizar projeto
version2 update project
```

## Solução de Problemas

### version2 diagnose

```bash
# Executar diagnósticos
version2 diagnose

# Diagnosticar componente específico
version2 diagnose --component api

# Gerar relatório de diagnóstico
version2 diagnose --report
```

### version2 debug

```bash
# Habilitar modo debug
version2 debug enable

# Definir nível de debug
version2 debug level verbose

# Coletar informações de debug
version2 debug collect
```

## Opções Globais

Todos os comandos suportam as seguintes opções globais:

- `--config`: Especificar arquivo de configuração
- `--debug`: Habilitar saída de debug
- `--quiet`: Suprimir saída
- `--verbose`: Aumentar verbosidade
- `--version`: Mostrar informações de versão
- `--help`: Mostrar informações de ajuda

## Variáveis de Ambiente

A CLI pode ser configurada usando as seguintes variáveis de ambiente:

- `VERSION2_API_KEY`: Chave API para autenticação
- `VERSION2_API_URL`: URL do endpoint da API
- `VERSION2_CONFIG`: Caminho para arquivo de configuração
- `VERSION2_DEBUG`: Habilitar modo debug
- `VERSION2_WORKSPACE`: ID do workspace padrão

## Códigos de Saída

A CLI usa os seguintes códigos de saída:

- `0`: Sucesso
- `1`: Erro geral
- `2`: Erro de configuração
- `3`: Erro de autenticação
- `4`: Erro de permissão
- `5`: Recurso não encontrado
- `6`: Erro de validação
- `7`: Erro de rede
- `8`: Erro de timeout
- `9`: Erro de sistema

## Exemplos

### Uso Básico

```bash
# Inicializar novo projeto
version2 init

# Implantar projeto
version2 deploy

# Verificar status
version2 status
```

### Uso Avançado

```bash
# Implantar com configuração personalizada
version2 deploy --config custom.yaml --env staging

# Monitorar componente específico
version2 logs --component api --level error --follow

# Gerar e usar chave API
version2 keys generate
export VERSION2_API_KEY=$(version2 keys list --latest)
```

### Solução de Problemas

```bash
# Executar diagnósticos
version2 diagnose --component api --report

# Habilitar modo debug
version2 debug enable
version2 deploy --debug

# Verificar logs
version2 logs --component api --level error
``` 