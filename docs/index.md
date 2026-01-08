# Welcome to twampy

**twampy** is a Python implementation of the Two-Way Active Measurement Protocol (TWAMP and TWAMP light) as defined in [RFC 5357](https://tools.ietf.org/html/rfc5357) and the Simple Two-Way Active Measurement Protocol (STAMP) as defined in [RFC 8762](https://tools.ietf.org/html/rfc8762).

This tool was developed to validate Nokia SR OS and SR Linux TWAMP/STAMP implementations and provides comprehensive network latency measurement capabilities.

## Overview

twampy is a network measurement tool that enables accurate measurement of:

- **Latency** - Round-trip delay between network endpoints
- **Jitter** - Packet delay variation (calculated per RFC 1889)
- **Packet Loss** - Percentage of packets lost in transit

## Features

- ✅ **Multiple Operation Modes** - Controller, Control Client, Session Sender, Reflector
- ✅ **Dual Stack Support** - Both IPv4 and IPv6
- ✅ **QoS Control** - DSCP/TOS field configuration
- ✅ **Flexible Packet Sizing** - Custom padding, jumbo frames, IMIX traffic
- ✅ **Fragmentation Control** - DF (Don't Fragment) flag support
- ✅ **Standards Compliant** - Follows RFC 5357, RFC 4656, RFC 1889

## Modes of Operation

### TWAMP Controller
Combined Control Client and Session Sender that establishes a control connection to a TWAMP server and initiates test sessions.

### TWAMP Control Client
Establishes control sessions with TWAMP servers to run TWAMP light test sessions.

### TWAMP Test Session Sender (TWAMP light)
Sends test packets directly to a reflector without control session negotiation.

### TWAMP light Reflector
Receives test packets and reflects them back to the sender with timestamps.

## Protocol Support

- **TWAMP** (RFC 5357) - Two-Way Active Measurement Protocol
- **TWAMP light** - Simplified variant without control channel
- **STAMP** (RFC 8762) - Simple Two-Way Active Measurement Protocol
- **STAMP Extensions** (RFC 8972) - Optional extensions including Session Identifier (SSID)
- **Unauthenticated mode** - Currently supported mode
- **IPv4 and IPv6** - Full dual-stack support

## Use Cases

- Validate TWAMP/STAMP implementations on network devices (Nokia SR OS, SR Linux)
- Measure network latency and jitter
- Test Quality of Service (QoS) configurations
- Verify network SLAs
- Troubleshoot network performance issues
- Generate traffic with specific characteristics

## Getting Started

Check out the [Installation Guide](user-guide/installation.md) to get started, then see the [Usage Guide](user-guide/usage.md) for examples.

## Limitations

!!! warning "Current Limitations"
    - **Software timestamping only** - No hardware timestamping support (less precise)
    - **Unauthenticated mode only** - Authenticated/encrypted modes not yet implemented
    - **DF flag support** - Limited to Linux and Windows (not supported on macOS/FreeBSD)

## License

This project is licensed under the BSD-3-Clause license. See [LICENSE](https://github.com/nokia/twampy/blob/master/LICENSE) for details.

## Related Projects

- **[TWAMP RFC 5357](https://tools.ietf.org/html/rfc5357)** - TWAMP protocol specification
- **[STAMP RFC 8762](https://tools.ietf.org/html/rfc8762)** - STAMP protocol specification
- **[STAMP Extensions RFC 8972](https://tools.ietf.org/html/rfc8972)** - STAMP optional extensions (Session ID)
- **[RFC 4656](https://tools.ietf.org/html/rfc4656)** - One-way Active Measurement Protocol (OWAMP)
- **[RFC 1889](https://tools.ietf.org/html/rfc1889)** - RTP jitter calculation
