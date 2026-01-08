"""
Integration test for twampy - tests sender/responder interaction
"""

import re
import signal
import subprocess
import sys
import time


def test_sender_responder_integration():
    """
    Integration test: Start responder, send 100 packets, verify all received.

    Test setup:
    - Responder on 127.0.0.1:40862
    - Sender sends 100 packets at 10ms intervals with DSCP 'ef' (Expedited Forwarding)
    - Verify all 100 packets are reflected back
    """
    # Start responder on port 40862
    responder = subprocess.Popen(
        [sys.executable, "-m", "twampy", "responder", "127.0.0.1:40862"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    # Give responder time to start
    time.sleep(2)

    # Check if responder started successfully
    if responder.poll() is not None:
        stdout, stderr = responder.communicate()
        raise AssertionError(f"Responder failed to start:\nSTDOUT: {stdout}\nSTDERR: {stderr}")

    try:
        # Run sender: 100 packets, 10ms interval, DSCP EF
        sender = subprocess.run(
            [
                sys.executable,
                "-m",
                "twampy",
                "sender",
                "127.0.0.1:40862",
                ":40863",
                "--count",
                "100",
                "--interval",
                "10",
                "--dscp",
                "ef",
            ],
            capture_output=True,
            text=True,
            timeout=30,
        )

        # Check sender completed successfully
        assert sender.returncode == 0, (
            f"Sender failed with return code {sender.returncode}:\nSTDOUT: {sender.stdout}\nSTDERR: {sender.stderr}"
        )

        # Parse output to verify packet statistics
        output = sender.stdout + sender.stderr

        # Look for Roundtrip loss percentage (format: "Roundtrip: ... X.X%")
        match = re.search(r"Roundtrip:.*?(\d+\.?\d*)%", output)
        if match:
            loss_percent = float(match.group(1))
            assert loss_percent == 0.0, f"Expected 0.0% packet loss, got {loss_percent}% (some packets were lost)"
        else:
            raise AssertionError(f"Could not find Roundtrip statistics in output:\n{output}")

    finally:
        # Stop responder gracefully
        responder.send_signal(signal.SIGINT)
        try:
            responder.wait(timeout=5)
        except subprocess.TimeoutExpired:
            # Force kill if graceful shutdown fails
            responder.kill()
            responder.wait()
