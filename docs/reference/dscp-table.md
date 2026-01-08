# DSCP Table Reference

Differentiated Services Code Point (DSCP) values for Quality of Service (QoS) marking.

## Quick Reference

To display the DSCP table from the command line:

```bash
twampy dscptable
```

## DSCP Values

DSCP is a 6-bit field in the IP header used for packet classification and QoS.

### Class Selector (CS) PHBs

Class Selector PHBs provide backward compatibility with IP Precedence:

| DSCP | Binary | Decimal | Name | Description | Use Case |
|:----:|:------:|:-------:|:----:|-------------|----------|
| CS0 | 000000 | 0 | Default | Best Effort | Regular traffic |
| CS1 | 001000 | 8 | Scavenger | Lower than best effort | Bulk/background |
| CS2 | 010000 | 16 | OAM | Operations, Administration, Management | Network management |
| CS3 | 011000 | 24 | Broadcast Video | Broadcast/streaming | Video streaming |
| CS4 | 100000 | 32 | Real-Time Interactive | Real-time apps | Video conferencing |
| CS5 | 101000 | 40 | Signaling | Signaling traffic | VoIP signaling |
| CS6 | 110000 | 48 | Network Control | Network control traffic | Routing protocols |
| CS7 | 111000 | 56 | Reserved | Reserved for future use | Reserved |

### Assured Forwarding (AF) PHBs

AF provides reliable delivery with different drop precedences:

| DSCP | Binary | Decimal | Name | Class | Drop Prob | Use Case |
|:----:|:------:|:-------:|:----:|:-----:|:---------:|----------|
| AF11 | 001010 | 10 | AF11 | 1 | Low | High-priority data |
| AF12 | 001100 | 12 | AF12 | 1 | Medium | High-priority data |
| AF13 | 001110 | 14 | AF13 | 1 | High | High-priority data |
| AF21 | 010010 | 18 | AF21 | 2 | Low | Medium-priority data |
| AF22 | 010100 | 20 | AF22 | 2 | Medium | Medium-priority data |
| AF23 | 010110 | 22 | AF23 | 2 | High | Medium-priority data |
| AF31 | 011010 | 26 | AF31 | 3 | Low | Multimedia streaming |
| AF32 | 011100 | 28 | AF32 | 3 | Medium | Multimedia streaming |
| AF33 | 011110 | 30 | AF33 | 3 | High | Multimedia streaming |
| AF41 | 100010 | 34 | AF41 | 4 | Low | Multimedia conferencing |
| AF42 | 100100 | 36 | AF42 | 4 | Medium | Multimedia conferencing |
| AF43 | 100110 | 38 | AF43 | 4 | High | Multimedia conferencing |

### Expedited Forwarding (EF) PHB

EF provides low-loss, low-latency, low-jitter service:

| DSCP | Binary | Decimal | Name | Description | Use Case |
|:----:|:------:|:-------:|:----:|-------------|----------|
| EF | 101110 | 46 | Expedited Forwarding | Premium service | VoIP, real-time |

### Voice Admit (VA) PHB

| DSCP | Binary | Decimal | Name | Description | Use Case |
|:----:|:------:|:-------:|:----:|-------------|----------|
| VA | 101100 | 44 | Voice Admit | Call admission control | VoIP CAC |

## Common DSCP Mappings

### By Traffic Type

| Traffic Type | Recommended DSCP | Decimal | Description |
|--------------|:----------------:|:-------:|-------------|
| Voice (VoIP) | EF | 46 | Low latency, guaranteed |
| Video Conferencing | AF41 | 34 | Interactive video |
| Streaming Video | AF31 | 26 | One-way video |
| Signaling (SIP/H.323) | CS5 | 40 | Call control |
| Network Management | CS2 | 16 | SNMP, NetFlow |
| Routing Protocols | CS6 | 48 | OSPF, BGP |
| Transactional Data | AF21 | 18 | Business-critical |
| Bulk Data | CS1 | 8 | FTP, backup |
| Best Effort | CS0/DF | 0 | Default traffic |

### By Priority Level

| Priority | DSCP | Decimal | Queue | Description |
|:--------:|:----:|:-------:|:-----:|-------------|
| Highest | EF | 46 | P1 | Real-time voice |
| High | AF41 | 34 | P2 | Video, interactive |
| Medium | AF31 | 26 | P3 | Streaming media |
| Normal | AF21 | 18 | P4 | Business apps |
| Low | CS1 | 8 | P5 | Background/bulk |
| Default | CS0 | 0 | P6 | Best effort |

## Usage with twampy

### Set DSCP for Test Traffic

```bash
# Voice traffic (EF)
twampy sender 192.168.1.100 --dscp ef

# Video conferencing (AF41)
twampy sender 192.168.1.100 --dscp af41

# Best effort (default)
twampy sender 192.168.1.100 --dscp be
```

### Test Different QoS Classes

```bash
# Priority 1: Voice
twampy sender 192.168.1.100 --dscp ef --count 1000 --interval 20

# Priority 2: Video
twampy sender 192.168.1.100 --dscp af41 --count 1000 --interval 33

# Priority 3: Data
twampy sender 192.168.1.100 --dscp af21 --count 1000 --interval 100
```

## DSCP to TOS Conversion

DSCP occupies the upper 6 bits of the TOS byte:

```
TOS = DSCP << 2
```

| DSCP | DSCP (Dec) | TOS (Dec) | TOS (Hex) |
|:----:|:----------:|:---------:|:---------:|
| EF | 46 | 184 | 0xB8 |
| AF41 | 34 | 136 | 0x88 |
| AF31 | 26 | 104 | 0x68 |
| AF21 | 18 | 72 | 0x48 |
| CS5 | 40 | 160 | 0xA0 |
| CS0 | 0 | 0 | 0x00 |

### Using TOS Value Directly

```bash
# Equivalent to --dscp 46
twampy sender 192.168.1.100 --tos 184

# Equivalent to --dscp 34
twampy sender 192.168.1.100 --tos 136
```

## PHB Descriptions

### Assured Forwarding (AF)

AF provides assurance of delivery under prescribed conditions. Format: `AFxy`

- **x** (1-4): AF class (traffic category)
- **y** (1-3): Drop precedence (1=low, 2=medium, 3=high)

**Example**: AF41 = Class 4, Low drop precedence

### Expedited Forwarding (EF)

EF provides:
- Low delay
- Low jitter
- Low loss
- Assured bandwidth

**Best for**: VoIP, real-time gaming

### Class Selector (CS)

CS provides 8 classes based on IP Precedence:
- CS0 (0): Default/Best Effort
- CS1 (8): Scavenger/Bulk
- CS2-CS7: Increasing priority

## Platform Considerations

### Windows

Requires registry modification to enable user-space TOS/DSCP setting:

```
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\TcpIp\Parameters
DisableUserTOSSetting = 0x00000000
```

See [Installation Guide](../user-guide/installation.md#windows) for details.

### Linux

Full DSCP/TOS support without special configuration.

### macOS / FreeBSD

DSCP/TOS marking supported, but may require elevated privileges.

## Testing QoS Configuration

### Verify DSCP Preservation

Test that network devices preserve DSCP markings:

```bash
# Send with DSCP EF
twampy sender 192.168.1.100 --dscp ef --count 100

# Capture on receiver and verify DSCP value
```

### Compare Treatment Across Classes

Run tests with different DSCP values and compare results:

```bash
# EF (should get priority treatment)
twampy sender 192.168.1.100 --dscp ef > ef-results.txt

# Best Effort (normal treatment)
twampy sender 192.168.1.100 --dscp be > be-results.txt

# Compare latency/loss between classes
```

## References

- [RFC 2474 - Definition of the Differentiated Services Field](https://tools.ietf.org/html/rfc2474)
- [RFC 2475 - An Architecture for Differentiated Services](https://tools.ietf.org/html/rfc2475)
- [RFC 3246 - An Expedited Forwarding PHB](https://tools.ietf.org/html/rfc3246)
- [RFC 2597 - Assured Forwarding PHB Group](https://tools.ietf.org/html/rfc2597)
- [Configuration Guide](../user-guide/configuration.md) - Parameter details
- [Usage Guide](../user-guide/usage.md) - Practical examples
