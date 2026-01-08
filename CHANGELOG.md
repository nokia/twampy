# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2] - 2026-01-07

### Added
- Standard Python package structure with src layout
- Modern packaging with `pyproject.toml` (PEP 517/518)
- Comprehensive MkDocs documentation site
- GitHub Actions CI/CD pipeline with automated testing and linting
- Integration tests for sender/responder functionality
- Unit tests for CLI commands (help, version)
- Ruff linter and formatter configuration
- Support for `pip install` with entry point (`twampy` command)
- Module execution support (`python -m twampy`)
- AI-friendly repository structure with copilot instructions
- CHANGELOG.md for version tracking
- Support for STAMP (RFC 8762) and STAMP Extensions (RFC 8972)
- Documentation for Nokia SR Linux configuration
- Test coverage reporting with pytest-cov
- `.gitignore` for Python projects
- `requirements.txt` (no external dependencies)

### Changed
- Restructured project from single file to proper package layout
- Updated documentation to mention STAMP protocol support
- Updated documentation to include both Nokia SR OS and SR Linux
- Modernized Python code style (f-strings, context managers)
- Improved README with quick start guide and clear feature list
- Enhanced user documentation with installation, usage, and configuration guides

### Fixed
- Module-level logger configuration for proper CLI execution
- Main entry point function for pip-installed command
- Ruff linting issues (UP031, SIM115)
- File opening with proper context managers

### Developer Experience
- Pre-configured linting and formatting tools
- Automated test execution in CI/CD
- Cross-platform testing (Linux, Windows, macOS)
- Python 3.11 and 3.12 support validation
- Clear contributing guidelines in CI documentation

## [1.1] - 2024-12-02

### Changed
- Updated for Python 3.12 compatibility
- Minor bug fixes and improvements

## [1.0] - 2017-08-18

### Added
- Initial release
- TWAMP/TWAMP-light implementation (RFC 5357)
- Support for unauthenticated mode
- IPv4 and IPv6 support
- DSCP/TOS marking support
- Packet padding and IMIX traffic generation
- Don't Fragment (DF) flag support
- Basic delay, jitter, and loss statistics (RFC 1889)
- Multiple operation modes:
  - TWAMP Controller
  - TWAMP Control Client
  - TWAMP Test Session Sender
  - TWAMP light Reflector
- Cross-platform support (Linux, Windows, macOS, FreeBSD)

### Limitations
- Software timestamping only (no hardware support)
- Unauthenticated mode only
- DF flag not supported on macOS/FreeBSD
