"""
Basic tests for twampy CLI functionality
"""

import subprocess
import sys


def run_twampy(*args):
    """Helper to run twampy command"""
    result = subprocess.run([sys.executable, "-m", "twampy"] + list(args), capture_output=True, text=True, timeout=5)
    return result


def test_version():
    """Test that --version flag works"""
    result = run_twampy("--version")

    assert result.returncode == 0, f"Version command failed: {result.stderr}"
    assert "twampy" in result.stdout.lower() or "1.0" in result.stdout


def test_help():
    """Test that --help flag works"""
    result = run_twampy("--help")

    assert result.returncode == 0, f"Help command failed: {result.stderr}"
    assert "usage" in result.stdout.lower()
    assert "twampy" in result.stdout.lower()


def test_help_shows_commands():
    """Test that help displays available commands"""
    result = run_twampy("--help")

    assert result.returncode == 0
    output = result.stdout.lower()

    # Check for main commands
    assert "controller" in output
    assert "sender" in output
    assert "responder" in output
    assert "controlclient" in output or "control" in output


def test_controller_help():
    """Test that controller subcommand help works"""
    result = run_twampy("controller", "--help")

    assert result.returncode == 0, f"Controller help failed: {result.stderr}"
    assert "usage" in result.stdout.lower()
    assert "controller" in result.stdout.lower()


def test_sender_help():
    """Test that sender subcommand help works"""
    result = run_twampy("sender", "--help")

    assert result.returncode == 0, f"Sender help failed: {result.stderr}"
    assert "usage" in result.stdout.lower()
    assert "sender" in result.stdout.lower()


def test_responder_help():
    """Test that responder subcommand help works"""
    result = run_twampy("responder", "--help")

    assert result.returncode == 0, f"Responder help failed: {result.stderr}"
    assert "usage" in result.stdout.lower()
    assert "responder" in result.stdout.lower()


def test_dscptable_help():
    """Test that dscptable subcommand help works"""
    result = run_twampy("dscptable", "--help")

    assert result.returncode == 0, f"DSCP table help failed: {result.stderr}"
    assert "usage" in result.stdout.lower()


def test_invalid_command():
    """Test that invalid command returns error"""
    result = run_twampy("invalidcommand")

    assert result.returncode != 0, "Invalid command should fail"
    assert "invalid" in result.stderr.lower() or "usage" in result.stderr.lower()


def test_no_arguments():
    """Test running without arguments shows help or error"""
    result = run_twampy()

    # Should either show help (exit 0) or error (exit non-zero)
    # Either is acceptable
    assert "usage" in result.stdout.lower() or "usage" in result.stderr.lower()
