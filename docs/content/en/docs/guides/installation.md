---
title: "Installation Guide"
linkTitle: "Installation"
weight: 1
description: >
  How to install and configure VersionTwo
---

# Installation Guide

This guide will walk you through the process of installing and configuring VersionTwo on your system.

## System Requirements

Before installing VersionTwo, ensure your system meets these requirements:

- Operating System: macOS 10.15+, Linux (Ubuntu 20.04+, CentOS 8+), or Windows 10/11
- CPU: 2+ cores
- Memory: 4GB RAM minimum
- Storage: 1GB free space
- Network: Internet connection for updates and cloud features

## Installation Methods

### Using Package Manager

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

### Manual Installation

1. Download the latest release from [GitHub](https://github.com/versiontwo/cli/releases)
2. Extract the archive
3. Move the binary to your PATH:
   ```bash
   # Linux/macOS
   sudo mv versiontwo /usr/local/bin/
   
   # Windows
   # Add the extracted directory to your system PATH
   ```

## Configuration

After installation, you need to configure VersionTwo:

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
   version2 config set workspace ~/versiontwo-projects
   ```

## Verification

To verify your installation:

```bash
version2 --version
version2 doctor
```

The `doctor` command will check your installation and report any issues.

## Next Steps

- [Configuration Guide](/docs/guides/configuration/) - Configure your VersionTwo installation
- [Security Guide](/docs/guides/security/) - Secure your VersionTwo deployment
- [Overview](/docs/overview/) - Learn more about VersionTwo features

## Troubleshooting

If you encounter any issues during installation:

1. Check the Troubleshooting Guide](/docs/tutorials/troubleshooting/)
2. Run `version2 doctor` for a system check
3. Check the [GitHub Issues](https://github.com/versiontwo/cli/issues) for known problems
4. Contact [Support](/support/) if you need additional help 