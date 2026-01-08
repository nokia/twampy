# Configuration

This guide provides detailed information about twampy configuration options and parameters.

## Command-Line Options

### Global Options

Available for all commands:

| Option | Description | Default |
|--------|-------------|---------|
| `--version, -v` | Show version and exit | - |
| `--help, -h` | Show help message and exit | - |

### Logging Options

Control logging verbosity and destination:

| Option | Description | Default |
|--------|-------------|---------|
| `--quiet, -q` | Disable logging output | `False` |
| `--verbose, -v` | Enable verbose logging | `False` |
| `--debug, -d` | Enable debug logging (most detailed) | `False` |
| `--logfile <filename>, -l <filename>` | Write logs to file instead of stdout | `stdout` |

Example:
```bash
twampy sender 192.168.1.100 --debug --logfile debug.log
```

### IP Socket Options

Configure IP-level parameters:

#### DSCP (Differentiated Services Code Point)

```bash
--dscp <value>
```

Sets the DSCP field in the IP header for QoS marking.

- **Range**: 0-63
- **Common values**:
    - `0` - Best Effort (default)
    - `8` - CS1 (Scavenger)
    - `10` - AF11
    - `18` - AF21
    - `26` - AF31
    - `34` - AF41
    - `46` - EF (Expedited Forwarding)

Example:
```bash
twampy sender 192.168.1.100 --dscp ef
```

Use `twampy dscptable` to see all DSCP values.

#### TOS (Type of Service)

```bash
--tos <value>
```

Sets the TOS field directly (alternative to DSCP).

- **Range**: 0-255
- **Note**: On Windows, requires registry modification (see [Installation Guide](installation.md#windows))

Example:
```bash
twampy sender 192.168.1.100 --tos 184
```

#### TTL (Time to Live)

```bash
--ttl <value>
```

Sets the TTL field in the IP header.

- **Range**: 1-255
- **Default**: System default (typically 64)
- **Use case**: Test routing paths, limit hop count

Example:
```bash
twampy sender 192.168.1.100 --ttl 32
```

#### Padding

```bash
--padding <bytes>
```

Sets the packet payload size.

- **Range**: 27-9000
- **Special value**: `-1` for IMIX traffic
- **Default**: 27 bytes

Packet size calculation:

| IP Version | Padding | IP Packet Size | Ethernet Frame Size |
|:----------:|:-------:|:--------------:|:-------------------:|
| IPv4       | 27      | 69 bytes       | 83 bytes            |
| IPv4       | 1000    | 1042 bytes     | 1056 bytes          |
| IPv6       | 27      | 89 bytes       | 103 bytes           |
| IPv6       | 1000    | 1062 bytes     | 1076 bytes          |

Example:
```bash
# Standard packet
twampy sender 192.168.1.100 --padding 100

# Jumbo frame
twampy sender 192.168.1.100 --padding 8000

# IMIX traffic
twampy sender 192.168.1.100 --padding -1
```

#### Don't Fragment Flag

```bash
--do-not-fragment
```

Sets the DF (Don't Fragment) bit in the IP header.

- **Supported**: Linux, Windows
- **Not supported**: macOS, FreeBSD
- **Use case**: MTU path discovery, fragmentation testing

Example:
```bash
twampy sender 192.168.1.100 --padding 1400 --do-not-fragment
```

### Test Session Options

Configure test session parameters (sender/controller modes):

#### Packet Count

```bash
--count <packets>, -c <packets>
```

Number of test packets to send.

- **Range**: 1-9999 (limited by implementation)
- **Default**: 100
- **Use case**: Control test duration

Example:
```bash
twampy sender 192.168.1.100 --count 1000
```

#### Send Interval

```bash
--interval <milliseconds>, -i <milliseconds>
```

Time between consecutive packets.

- **Range**: 1-10000 milliseconds
- **Default**: 1000 ms (1 second)
- **Note**: Lower values = higher packet rate

Packet rate examples:

| Interval (ms) | Packets/Second | Use Case |
|:-------------:|:--------------:|----------|
| 1000          | 1              | Basic monitoring |
| 100           | 10             | Standard testing |
| 10            | 100            | High-frequency testing |
| 1             | 1000           | Stress testing |

Example:
```bash
# 10 packets per second
twampy sender 192.168.1.100 --interval 100 --count 600

# 100 packets per second (high rate)
twampy sender 192.168.1.100 --interval 10 --count 6000
```

## Address Specification

### Format

Addresses can be specified in multiple formats:

```
[IP-address][:port]
```

### IPv4 Examples

```bash
# IP only (uses default port 862)
twampy sender 192.168.1.100

# IP with port
twampy sender 192.168.1.100:20000

# Port only (binds to all interfaces)
twampy responder :20000
```

### IPv6 Examples

```bash
# IPv6 only
twampy sender 2001:db8::1

# IPv6 with port (brackets required)
twampy sender [2001:db8::1]:20000

# IPv6 all interfaces
twampy responder [::]:20000
```

### Local and Remote Addresses

Some commands accept both local and remote addresses:

```bash
twampy sender <remote-address> [local-address]
```

Example:
```bash
# Explicit source and destination
twampy sender 192.168.1.100:20000 192.168.1.200:30000

# Use specific source IP
twampy sender 192.168.1.100:20000 192.168.1.200
```

## Configuration Examples

### Basic Latency Measurement

```bash
twampy sender 192.168.1.100 --count 100 --interval 100
```

### High-Priority Traffic (EF)

```bash
twampy sender 192.168.1.100 --dscp ef --count 1000 --interval 10
```

### Large Packet Testing

```bash
twampy sender 192.168.1.100 --padding 1400 --do-not-fragment --count 500
```

### IMIX Traffic Profile

```bash
twampy sender 192.168.1.100 --padding -1 --count 1200 --interval 10
```

### IPv6 with QoS

```bash
twampy sender [2001:db8::1]:862 --dscp af41 --ttl 64 --count 1000
```

### Long-Duration Test with Logging

```bash
twampy sender 192.168.1.100 \
  --count 36000 \
  --interval 100 \
  --dscp 46 \
  --logfile /var/log/twampy-test.log \
  --verbose
```

## Environment Considerations

### Software Timestamping Limitations

twampy uses software timestamping, which has inherent limitations:

- **Typical accuracy**: 100μs - 2ms
- **Factors affecting accuracy**:
    - System load
    - CPU scheduling
    - Network stack processing
    - Virtualization overhead

**Recommendation**: For sub-millisecond accuracy requirements, use hardware-based TWAMP implementations.

### Platform-Specific Considerations

#### Linux

- Full feature support
- DF flag supported
- Recommended for production use

#### Windows

- Full feature support
- DF flag supported
- Requires registry modification for TOS/DSCP (see [Installation Guide](installation.md#windows))

#### macOS / FreeBSD

- Most features supported
- **DF flag NOT supported**
- Socket options may need platform-specific adjustments

### Port Permissions

- **Ports < 1024**: Require root/administrator privileges
- **Recommended**: Use ports ≥ 1024 for non-privileged operation

```bash
# Requires root
sudo twampy responder :862

# No root required
twampy responder :20862
```

## Best Practices

### 1. Start with Defaults

Begin testing with default parameters:

```bash
twampy controller 192.168.1.100
```

### 2. Gradually Increase Load

Increase packet rate progressively:

```bash
# Start: 1 packet/second
twampy sender 192.168.1.100 --interval 1000 --count 100

# Medium: 10 packets/second
twampy sender 192.168.1.100 --interval 100 --count 1000

# High: 100 packets/second
twampy sender 192.168.1.100 --interval 10 --count 6000
```

### 3. Use Appropriate Packet Sizes

Choose packet sizes based on your test scenario:

- **Small packets (64-100 bytes)**: PPS testing
- **Medium packets (500-600 bytes)**: Typical traffic
- **Large packets (1400-1500 bytes)**: Throughput testing
- **IMIX**: Realistic traffic mix

### 4. Enable Logging for Diagnostics

For troubleshooting, enable verbose logging:

```bash
twampy sender 192.168.1.100 --debug --logfile debug.log
```

### 5. Use DSCP for QoS Testing

Test different traffic classes:

```bash
# Voice (EF)
twampy sender 192.168.1.100 --dscp 46

# Video (AF41)
twampy sender 192.168.1.100 --dscp 34

# Best Effort
twampy sender 192.168.1.100 --dscp 0
```

## Next Steps

- Return to [Usage Guide](usage.md) for practical examples
- See [Error Codes Reference](../reference/error-codes.md)
- See [DSCP Table Reference](../reference/dscp-table.md)
