---
title: "Installation Guide"
linkTitle: "Installation"
weight: 1
description: >
  How to install and configure Version2
---

# Installation Guide

This guide will walk you through the process of installing and configuring Version2 on your system.

## System Requirements

Before installing Version2, ensure your system meets these requirements:

- Operating System: macOS 10.15+, Linux (Ubuntu 20.04+, CentOS 8+), or Windows 10/11
- CPU: 2+ cores
- Memory: 4GB RAM minimum
- Storage: 1GB free space
- Network: Internet connection for updates and cloud features

## Installation Methods

### Using Package Manager

#### macOS (Homebrew)
```bash
brew tap version2/tap
brew install version2
```

#### Ubuntu/Debian
```bash
curl -fsSL https://packages.version2.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/version2-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/version2-archive-keyring.gpg] https://packages.version2.com/apt stable main" | sudo tee /etc/apt/sources.list.d/version2.list
sudo apt update
sudo apt install version2
```

#### Windows (Chocolatey)
```powershell
choco install version2
```

### Manual Installation

1. Download the latest release from [GitHub](https://github.com/version2/cli/releases)
2. Extract the archive
3. Move the binary to your PATH:
   ```bash
   # Linux/macOS
   sudo mv version2 /usr/local/bin/
   
   # Windows
   # Add the extracted directory to your system PATH
   ```

## Configuration

After installation, you need to configure Version2:

1. Initialize the configuration:
   ```bash
   version2 init-config
   ```

2. Set up your API key:
   ```bash
   version2 config set api-key YOUR_API_KEY
   ```

3. Configure your default workspace:
   ```bash
   version2 config set workspace ~/version2-projects
   ```

## Verification

To verify your installation:

```bash
version2 --version
version2 doctor
```

The `doctor` command will check your installation and report any issues.

## Next Steps

- [Configuration Guide](/docs/guides/configuration/) - Configure your Version2 installation
- [Security Guide](/docs/guides/security/) - Secure your Version2 deployment
- [Overview](/docs/overview/) - Learn more about Version2 features

## Troubleshooting

If you encounter any issues during installation:

1. Check the Troubleshooting Guide](/docs/tutorials/troubleshooting/)
2. Run `version2 doctor` for a system check
3. Check the [GitHub Issues](https://github.com/version2/cli/issues) for known problems
4. Contact [Support](/support/) if you need additional help 