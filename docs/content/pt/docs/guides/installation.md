---
title: "Guia de Instalação"
linkTitle: "Instalação"
weight: 1
description: >
  Como instalar e configurar o VersionTwo
---

# Guia de Instalação

Este guia irá orientá-lo através do processo de instalação e configuração do VersionTwo em seu sistema.

## Requisitos do Sistema

Antes de instalar o VersionTwo, certifique-se de que seu sistema atende a estes requisitos:

- Sistema Operacional: macOS 10.15+, Linux (Ubuntu 20.04+, CentOS 8+), ou Windows 10/11
- CPU: 2+ núcleos
- Memória: 4GB RAM mínimo
- Armazenamento: 1GB de espaço livre
- Rede: Conexão com a internet para atualizações e recursos em nuvem

## Métodos de Instalação

### Usando Gerenciador de Pacotes

#### macOS (Homebrew)
```bash
brew tap versiontwo/tap
brew install versiontwo
```

#### Ubuntu/Debian
```bash
curl -fsSL https://packages.versiontwo.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/versiontwo-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/versiontwo-archive-keyring.gpg] https://packages.versiontwo.com/apt stable main" | sudo tee /etc/apt/sources.list.d/versiontwo.list
sudo apt update
sudo apt install versiontwo
```

#### Windows (Chocolatey)
```powershell
choco install versiontwo
```

### Instalação Manual

1. Baixe a última versão do [GitHub](https://github.com/versiontwo/cli/releases)
2. Extraia o arquivo
3. Mova o binário para seu PATH:
   ```bash
   # Linux/macOS
   sudo mv versiontwo /usr/local/bin/
   
   # Windows
   # Adicione o diretório extraído ao PATH do sistema
   ```

## Configuração

Após a instalação, você precisa configurar o VersionTwo:

1. Inicialize a configuração:
   ```bash
   version2 init-config
   ```

2. Configure sua chave de API:
   ```bash
   version2 config set api-key SUA_CHAVE_API
   ```

3. Configure seu workspace padrão:
   ```bash
   version2 config set workspace ~/versiontwo-projects
   ```

## Verificação

Para verificar sua instalação:

```bash
version2 --version
version2 doctor
```

O comando `doctor` verificará sua instalação e reportará quaisquer problemas.

## Próximos Passos

- [Guia de Configuração](/docs/guides/configuration/) - Configure sua instalação do VersionTwo
- [Guia de Segurança](/docs/guides/security/) - Proteja sua implantação do VersionTwo
- [Visão Geral](/docs/overview/) - Saiba mais sobre os recursos do VersionTwo

## Solução de Problemas

Se você encontrar problemas durante a instalação:

1. Verifique o [Guia de Solução de Problemas](/tutorials/troubleshooting/)
2. Execute `version2 doctor` para uma verificação do sistema
3. Verifique os [Problemas no GitHub](https://github.com/versiontwo/cli/issues) para problemas conhecidos
4. Entre em contato com o [Suporte](/support/) se precisar de ajuda adicional 