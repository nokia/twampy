# twampy CI/CD

This project uses GitHub Actions for continuous integration and continuous deployment.

## Workflows

### CI Workflow (`.github/workflows/ci.yml`)

Runs on every push and pull request to main/master/develop branches.

#### Jobs

**1. Lint**
- Runs on Python 3.11
- Checks code style with `ruff`
- Validates formatting

**2. Test**
- Runs on Python 3.11 and 3.12
- Tests on Linux, Windows, and macOS
- Executes pytest test suite
- Validates CLI commands

**3. Coverage**
- Measures test coverage
- Uploads results to Codecov
- Runs on Python 3.11 (Linux)

## Running Locally

### Linting

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run linter
ruff check src/ tests/

# Auto-fix issues
ruff check --fix src/ tests/

# Check formatting
ruff format --check src/ tests/

# Auto-format
ruff format src/ tests/
```

### Testing

```bash
# Install test dependencies
pip install -e ".[test]"

# Run all tests
pytest

# Run with verbose output
pytest -v

# Run only integration test
pytest tests/test_integration.py -v

# Run with coverage
pip install pytest-cov
pytest --cov=twampy --cov-report=html
```

### Integration Test

The integration test starts a real responder and tests sender/responder interaction:

```bash
# Run the integration test
pytest tests/test_integration.py -v
```

**Test scenario:**
- Starts responder on 127.0.0.1:40862
- Sends 100 packets at 10ms intervals with DSCP 'ef' (Expedited Forwarding)
- Verifies all 100 packets are reflected back
- Stops responder gracefully

## Pre-commit Checks

Before submitting a PR, ensure:

1. ✅ All tests pass: `pytest -v`
2. ✅ Linting passes: `ruff check src/ tests/`
3. ✅ Formatting is correct: `ruff format --check src/ tests/`
4. ✅ CLI works: `python -m twampy --version`

## Status Badges
2. ✅ Linting passes: `ruff check src/ tests/`
3. ✅ Formatting is correct: `ruff format --check src/ tests/`
4. ✅ CLI works: `python -m twampy --version`

## Status Badges

Add these to README.md once workflows are active:

```markdown
[![CI](https://github.com/nokia/twampy/workflows/CI/badge.svg)](https://github.com/nokia/twampy/actions)
[![codecov](https://codecov.io/gh/nokia/twampy/branch/main/graph/badge.svg)](https://codecov.io/gh/nokia/twampy)
```
