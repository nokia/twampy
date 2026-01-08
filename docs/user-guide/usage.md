# Usage Guide

This guide covers how to use twampy for network latency measurement.

## Basic Command Structure

After installation, run twampy using one of these methods:

```bash
# If installed via pip
twampy [command] [options]

# Or run as a Python module
python -m twampy [command] [options]
```

## Available Commands

twampy supports multiple modes of operation:

| Command | Description |
|---------|-------------|
| `controller` | TWAMP controller (control client + session sender) |
| `controlclient` | TWAMP control client only |
| `sender` | TWAMP light session sender |
| `responder` | TWAMP light reflector |
| `dscptable` | Display DSCP/TOS values table |

## Getting Help

Display general help:

```bash
twampy --help
```

Display help for a specific command:

```bash
twampy sender --help
twampy controller --help
twampy responder --help
```

## Command Examples

### 1. TWAMP Controller

Connect to a TWAMP server and run a complete test session:

```bash
# Basic usage
twampy controller 192.168.1.100

# With custom port
twampy controller 192.168.1.100:862

# IPv6 address
twampy controller [2001:db8::1]:862

# With options
twampy controller 192.168.1.100 --count 100 --interval 100 --dscp ef
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

### 2. TWAMP Light Sender

Send test packets directly to a reflector:

```bash
# Basic usage
twampy sender 192.168.1.200:20000

# Specify local and remote addresses
twampy sender 192.168.1.200:20000 192.168.1.100:20001

# With DSCP marking
twampy sender 192.168.1.200:20000 --dscp ef

# With specific packet count and interval
twampy sender 192.168.1.200:20000 --count 1000 --interval 100
```

### 3. TWAMP Light Reflector

Start a reflector (server) listening for test packets:

```bash
# Listen on default port 862 (requires root/sudo)
sudo twampy responder

# Listen on specific port
twampy responder :20000

# Listen on specific IP and port
twampy responder 192.168.1.100:20000

# IPv6
twampy responder [::]:20000
```

### 4. DSCP Table

Display DSCP values and their meanings:

```bash
twampy dscptable
```

## Common Options

### Logging Options

```bash
# Quiet mode (minimal output)
twampy sender 192.168.1.100 --quiet

# Verbose mode (detailed output)
twampy sender 192.168.1.100 --verbose

# Debug mode (extensive logging)
twampy sender 192.168.1.100 --debug

# Log to file
twampy sender 192.168.1.100 --logfile /var/log/twampy.log
```

### IP Socket Options

```bash
# Set DSCP value (Differentiated Services Code Point)
twampy sender 192.168.1.100 --dscp ef

# Set TOS value (Type of Service)
twampy sender 192.168.1.100 --tos 184

# Set TTL value (Time to Live)
twampy sender 192.168.1.100 --ttl 64

# Set padding (packet size)
twampy sender 192.168.1.100 --padding 1000

# Enable Don't Fragment flag
twampy sender 192.168.1.100 --do-not-fragment
```

### Test Session Options

```bash
# Number of packets to send
twampy sender 192.168.1.100 --count 1000

# Interval between packets (milliseconds)
twampy sender 192.168.1.100 --interval 100
```

## Packet Sizing

Use padding to control packet and frame sizes:

### Standard Padding

| IP Version | Padding | Packet Size | Frame Size |
|:----------:|:-------:|-------------|------------|
| IPv4       | ≥27     | Padding+42  | Padding+56 |
| IPv6       | ≥27     | Padding+62  | Padding+76 |

Default padding is 27 bytes (enforces bidirectional behavior).

Example:
```bash
# 100-byte packets
twampy sender 192.168.1.100 --padding 58

# Jumbo frame (1500 bytes)
twampy sender 192.168.1.100 --padding 1444
```

### IMIX Traffic

Use `--padding -1` to generate IMIX (Internet Mix) traffic:

| L2 Size | Packets | Ratio (Packets) | Ratio (Volume) |
|--------:|:-------:|----------------:|---------------:|
| 64      | 7       | 58%             | 10%            |
| 590     | 4       | 33%             | 55%            |
| 1514    | 1       | 8%              | 35%            |

Example:
```bash
twampy sender 192.168.1.100 --padding -1 --count 1200
```

## Usage Scenarios

### Basic Latency Test

Quick test between two hosts:

```bash
# On reflector host (192.168.1.200)
twampy responder :20000

# On sender host
twampy sender 192.168.1.200:20000 --count 100
```

### QoS Testing

Test with different DSCP markings:

```bash
# EF (Expedited Forwarding) - DSCP 46
twampy sender 192.168.1.100 --dscp ef --count 1000

# AF41 (Assured Forwarding) - DSCP 34
twampy sender 192.168.1.100 --dscp af41 --count 1000

# Best Effort - DSCP 0
twampy sender 192.168.1.100 --dscp be --count 1000
```

### High-Frequency Testing

Send packets at high rate:

```bash
# 10ms interval (100 packets/second)
twampy sender 192.168.1.100 --interval 10 --count 6000

# 1ms interval (1000 packets/second)
twampy sender 192.168.1.100 --interval 1 --count 60000
```

### Testing Against Nokia SR OS

Configure Nokia SR OS TWAMP server:

```sros
configure test-oam
    twamp
        server
            prefix 0.0.0.0/0 create
            exit
            no shutdown
        exit
    exit
```

Run test from twampy:

```bash
twampy controller 192.168.255.2
```

## Understanding Results

### Output Metrics

- **Min/Max/Avg**: Minimum, maximum, and average latency
- **Jitter**: Packet delay variation (RFC 1889 algorithm)
- **Loss**: Percentage of packets lost

### Directions

- **Outbound**: Sender → Reflector
- **Inbound**: Reflector → Sender
- **Roundtrip**: Full round-trip time

## Advanced Usage

### IPv6 Testing

```bash
# IPv6 reflector
twampy responder [2001:db8::1]:20000

# IPv6 sender
twampy sender [2001:db8::2]:20000 [2001:db8::1]:20001
```

### Custom Port Ranges

```bash
# Reflector on custom port
twampy responder :30000

# Sender with custom source and destination ports
twampy sender 192.168.1.100:30000 192.168.1.200:30001
```

### Long-Running Tests

```bash
# Run for 1 hour (100ms interval, 36000 packets)
twampy sender 192.168.1.100 --interval 100 --count 36000 --logfile test.log

# Monitor continuously (high packet count)
twampy sender 192.168.1.100 --interval 1000 --count 999999
```

## Troubleshooting

### Port Already in Use

If port 862 is already in use:

```bash
# Use a different port
twampy responder :20862
```

### Permission Denied

For ports < 1024, use sudo:

```bash
sudo twampy responder :862
```

### No Response from Reflector

Check connectivity:

```bash
# Verify network connectivity
ping 192.168.1.100

# Check if reflector is running
sudo netstat -ulnp | grep 862
```

### High Latency Values

Remember that twampy uses software timestamping, which is less precise than hardware timestamping. Expected accuracy:

- Typical software timestamping accuracy: ~100μs - 2ms
- Hardware timestamping accuracy: ~10ns - 100ns

## Next Steps

- See [Configuration Guide](configuration.md) for detailed parameter descriptions
- See [Error Codes Reference](../reference/error-codes.md) for error code meanings
- See [DSCP Table Reference](../reference/dscp-table.md) for QoS values
