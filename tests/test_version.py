"""
Test version consistency across package metadata
"""

import subprocess
import sys
import tomllib  # Python 3.11+ built-in


def test_version_consistency():
    """
    Verify that version is consistent across:
    - pyproject.toml
    - twampy.__version__
    - CLI --version output
    """
    # Read version from pyproject.toml
    with open("pyproject.toml", "rb") as f:
        pyproject = tomllib.load(f)
    toml_version = pyproject["project"]["version"]

    # Import version from package
    import twampy

    package_version = twampy.__version__

    # Get version from CLI
    result = subprocess.run(
        [sys.executable, "-m", "twampy", "--version"],
        capture_output=True,
        text=True,
    )
    cli_output = result.stdout.strip()
    cli_version = cli_output.split()[-1]  # Extract version from "twampy X.Y"

    # Assert all versions match
    assert package_version == toml_version, f"Package version {package_version} != pyproject.toml {toml_version}"
    assert cli_version == toml_version, f"CLI version {cli_version} != pyproject.toml {toml_version}"
