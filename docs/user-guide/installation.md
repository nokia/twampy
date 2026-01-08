# Installation

This guide covers how to install and uninstall twampy on your system.

## Requirements

- **Python 3.11 or higher**
- **No external dependencies** - twampy uses only Python standard library modules

## Installation Methods

### Method 1: Install from Source (Recommended for Development)

Clone the repository and install in editable mode:

```bash
# Clone the repository
git clone https://github.com/nokia/twampy
cd twampy

# Install in editable mode
pip install -e .
```

After installation, the `twampy` command will be available:

```bash
twampy --version
```

### Method 2: Install from Source (Standard)

Clone and install as a regular package:

```bash
# Clone the repository
git clone https://github.com/nokia/twampy
cd twampy

# Install the package
pip install .
```

### Method 3: Direct Execution (No Installation)

You can run twampy directly without installation:

```bash
# Clone the repository
git clone https://github.com/nokia/twampy
cd twampy

# Run as a module
python -m twampy --help
```

### Method 4: Install from PyPI (Future)

!!! note
    Once published to PyPI, you'll be able to install with:
    ```bash
    pip install twampy
    ```

## Verify Installation

After installation, verify twampy is working:

```bash
# Check version
twampy --version

# Or if running as module
python -m twampy --version
```

You should see output similar to:
```
twampy 1.0
```

## Virtual Environment (Recommended)

It's recommended to install twampy in a virtual environment:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Linux/macOS:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install twampy
pip install -e .
```

## Uninstallation

To uninstall twampy:

```bash
pip uninstall twampy
```

To remove all files including the source:

```bash
# Uninstall the package
pip uninstall twampy

# Remove the cloned repository
cd ..
rm -rf twampy
```

## Platform-Specific Notes

### Linux

No special requirements. All features are supported.

### Windows

To use DSCP/TOS field settings, you need to enable user TOS settings:

1. Open Registry Editor (`regedit`)
2. Navigate to: `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\TcpIp\Parameters`
3. Create a new DWORD value named `DisableUserTOSSetting` with value `0x00000000` (0)
4. Restart your computer

Reference: [Microsoft KB248611](http://support.microsoft.com/kb/248611)

### macOS / FreeBSD

!!! warning "Limited DF Flag Support"
    The DF (Don't Fragment) flag is not currently supported on macOS and FreeBSD. All other features work normally.

## Development Installation

For development work, install additional tools:

```bash
# Clone the repository
git clone https://github.com/nokia/twampy
cd twampy

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install in editable mode with dev dependencies
pip install -e ".[dev]"
```

## Troubleshooting

### Permission Errors

If you encounter permission errors during installation:

```bash
# Install for current user only
pip install --user -e .
```

### Port Access (862)

TWAMP uses UDP port 862 by default. On Linux/macOS, you may need elevated privileges:

```bash
# Run with sudo for port 862
sudo twampy responder

# Or use a non-privileged port (>1024)
twampy responder :20862
```

### Python Version Issues

Verify your Python version:

```bash
python --version
# Should show Python 3.11 or higher
```

If you have multiple Python versions installed:

```bash
# Use specific Python version
python3.11 -m pip install -e .
python3.11 -m twampy --version
```

## Next Steps

Once installed, proceed to the [Usage Guide](usage.md) to learn how to use twampy.
