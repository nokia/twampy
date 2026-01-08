# AI Agent Instructions for twampy

## Project Overview

**twampy** is a Python implementation of TWAMP/TWAMP-light (RFC 5357) and STAMP (RFC 8762) for network latency measurement and validation of Nokia SR OS and SR Linux TWAMP/STAMP implementations.

- **Language**: Python
- **Dependencies**: Standard library only
- **License**: BSD 3-Clause
- **Modes**: Controller, Control Client, Session Sender, Reflector
- **Structure**: Standard Python package (src layout)

## Project Structure

```
twampy/
├── .github/
│   ├── workflows/       # GitHub Actions CI/CD
│   ├── CI.md           # CI/CD documentation
│   └── copilot-instructions.md
├── docs/                # MkDocs documentation
│   ├── index.md
│   ├── user-guide/     # User guides
│   └── reference/      # Reference documentation
├── src/twampy/          # Package source
│   ├── __init__.py      # Package initialization and metadata
│   └── __main__.py      # CLI entry point
├── tests/               # Test suite
│   ├── test_cli.py      # CLI tests
│   └── test_integration.py  # Integration tests
├── .gitignore           # Git ignore patterns
├── CHANGELOG.md         # Version history
├── LICENSE              # BSD 3-Clause License
├── mkdocs.yml           # MkDocs configuration
├── pyproject.toml       # Package configuration
├── README.md            # Project documentation
└── requirements.txt     # Dependencies (empty - stdlib only)
```

## Coding Guidelines

### Python Standards
- **Python 3.11+** minimum required
- **Type hints mandatory** for all functions and methods
- **PEP 8** style compliance
- **No external dependencies** - standard library only

### Code Quality
- **No blocking I/O in async paths** (if async code is added)
- **Structured logging only** - use logging module with proper levels
- **No global state** unless explicitly documented in comments
- **Include RFC references** for protocol-specific code
- **Use f-strings** for string formatting
- **Use context managers** for file operations and resource handling

### Testing
- **pytest** for all test cases
- **Integration tests** in `tests/test_integration.py` for end-to-end validation
- **CLI tests** in `tests/test_cli.py` for command-line interface
- **Run tests with**: `pytest -v` or `pytest --cov=twampy`
- **All tests must pass** before merging PRs

### Linting and Formatting
- **ruff** for linting and formatting
- **camelCase** allowed for function/method names (N802, N803, N806, N815, N816 ignored)
- **Run linter**: `ruff check` or `ruff check --fix`
- **Run formatter**: `ruff format`
- **All linting issues must be resolved** before merging PRs

### Documentation
- **MkDocs** with Material theme for documentation
- **Comprehensive user guides** in `docs/user-guide/`
- **Reference documentation** in `docs/reference/`
- **Keep README.md updated** with current features and usage
- **Update CHANGELOG.md** for all notable changes
- **Build docs**: `mkdocs serve` or `mkdocs build`

### Protocol Compliance
- **Strictly follow RFC 5357 (TWAMP), RFC 8762 (STAMP), and RFC 8972 (STAMP Extensions)** specifications
- **Preserve packet formats** and byte alignment
- **Document packet structures** with visual diagrams in comments
- **Test with IPv4 and IPv6**

## Key Constraints

- Main implementation in single file (`src/twampy/__main__.py`) - don't split unless necessary
- Software timestamping only (no hardware support)
- Unauthenticated mode only
- Platform differences: DF flag not supported on macOS/FreeBSD
- No external runtime dependencies - standard library only

## When Making Changes

- Verify RFC compliance for protocol changes (RFC 5357, RFC 8762, RFC 8972)
- Maintain backward compatibility
- Test cross-platform (Linux, Windows, macOS)
- Test against Nokia SR OS and SR Linux when possible
- Document platform-specific behavior
- Keep code simple and readable
- Run `ruff check --fix` and `ruff format` before committing
- Run `pytest -v` to ensure all tests pass
- Update documentation and CHANGELOG.md for user-facing changes
