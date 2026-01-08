# twampy

**Python implementation of TWAMP/TWAMP-light (RFC 5357) and STAMP (RFC 8762)**

twampy is a network measurement tool for latency, jitter, and packet loss testing. Originally developed to validate Nokia SR OS and SR Linux TWAMP implementations, it provides a standards-compliant implementation of the Two-Way Active Measurement Protocol and Simple Two-Way Active Measurement Protocol.

## Features

- ✅ **Multiple Operation Modes** - Controller, Control Client, Session Sender, Reflector
- ✅ **Dual Stack** - IPv4 and IPv6 support
- ✅ **QoS Testing** - DSCP/TOS marking for quality of service validation
- ✅ **Flexible Sizing** - Custom padding, jumbo frames, IMIX traffic patterns
- ✅ **RFC Compliant** - Implements RFC 5357 (TWAMP), RFC 8762 (STAMP), RFC 8972 (STAMP Extensions)
- ✅ **No Dependencies** - Uses Python standard library only

## Quick Start

### Installation

```bash
# Clone and install
git clone https://github.com/nokia/twampy
cd twampy
pip install -e .
```

### Basic Usage

```bash
# Start a reflector
twampy responder :862

# Run a test (from another terminal/host)
twampy controller 192.168.1.100
```

Example output:
```
===============================================================================
Direction         Min         Max         Avg          Jitter     Loss
-------------------------------------------------------------------------------
  Outbound:       92.89ms    196.63ms     95.15ms       576us      0.0%
  Inbound:            0us         0us         0us         0us      0.0%
  Roundtrip:        339us    103.53ms      1.91ms       638us      0.0%
-------------------------------------------------------------------------------
                                                    Jitter Algorithm [RFC1889]
===============================================================================
```

## Command Overview

| Command | Description |
|---------|-------------|
| `controller` | Full TWAMP controller (control + sender) |
| `sender` | TWAMP light session sender |
| `responder` | TWAMP light reflector |
| `controlclient` | TWAMP control client only |
| `dscptable` | Display DSCP/QoS reference table |

## Common Options
```bash
# Send 1000 packets at 10ms intervals with DSCP EF marking
twampy sender 192.168.1.100 --count 1000 --interval 10 --dscp ef

# Run controller with verbose logging
twampy controller 192.168.1.100 --verbose

# Start reflector on custom port
twampy responder :20000
```

## Requirements

- Python 3.11 or higher
- No external dependencies (standard library only)

## Documentation

📚 **[Full Documentation](https://nokia.github.io/twampy/)** (or see [docs/](docs/))

- [Installation Guide](docs/user-guide/installation.md) - Detailed installation instructions
- [Usage Guide](docs/user-guide/usage.md) - Examples and use cases
- [Configuration Reference](docs/user-guide/configuration.md) - All parameters explained
- [Error Codes](docs/reference/error-codes.md) - Protocol error reference
- [DSCP Table](docs/reference/dscp-table.md) - QoS values reference

## Platform Support

| Platform | Status | Notes |
|----------|:------:|-------|
| Linux | ✅ Full | All features supported |
| Windows | ✅ Full | Requires registry mod for DSCP |
| macOS | ⚠️ Partial | DF flag not supported |
| FreeBSD | ⚠️ Partial | DF flag not supported |

## Limitations

- Software timestamping only (typical accuracy: 100μs - 2ms)
- Unauthenticated mode only (no encryption/authentication)


## License

This project is licensed under the BSD-3-Clause license - see the [LICENSE](https://github.com/nokia/twampy/blob/master/LICENSE).

twampy can be imported and used in Python programs:

```python
import twampy

# Your code here (API documentation coming soon)
```

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

Licensed under the BSD-3-Clause License. See [LICENSE](LICENSE) for details.

## Author

**Sven Wisotzky** - Nokia

## References

- [RFC 5357 - TWAMP](https://tools.ietf.org/html/rfc5357)
- [RFC 8762 - STAMP](https://tools.ietf.org/html/rfc8762)
- [RFC 8972 - STAMP Optional Extensions (Session ID)](https://tools.ietf.org/html/rfc8972)
- [RFC 4656 - OWAMP](https://tools.ietf.org/html/rfc4656)
- [RFC 1889 - RTP (Jitter Calculation)](https://tools.ietf.org/html/rfc1889)