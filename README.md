# Python tools for TWAMP and TWAMP light
Twampy is a Python implementation of the Two-Way Active Measurement
Protocol (TWAMP and TWAMP light) as defined in RFC5357. This tool
was developed to validate the Nokia SR OS TWAMP implementation.

## Supported features
* unauthenticated mode
* IPv4 and IPv6
* Support for DSCP, Padding, JumboFrames, IMIX
* Support to set DF flag (don't fragment)
* Basic Delay, Jitter, Loss statistics (jitter according to RFC1889)

##  Modes of operation
* TWAMP Controller
* TWAMP Control Client
* TWAMP Test Session Sender
* TWAMP light Reflector

## Installation
'''
$ git clone https://github.com/nokia/twampy
Cloning into 'twampy'...
'''

##  Usage Notes
Use padding to configure bidirectional packet/frame sizes:

IP Version | Padding | Packet Size | Frame Size
:---:|:---:| --- | ---
IPv4 | >=27 | Padding+42 | Padding+56
IPv6 | >=27 | Padding+62 | Padding+76

Padding default is 27 bytes (to enforce bidirectional behavior).

Use padding value '-1' for IMIX traffic generation:

L2 Size | Packets | Ratio(Packets) | Ratio(Volume)
---:|:---:| ---:| ---:
64             7          58%               10%
590            4          33%               55%
1514           1          8%                35%

TOS/DSCP user settings neet to be enabled on WINDOWS:
1. Open Registry Editor
2. Go to key:
      HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\TcpIp\Parameters
3. Create new DWORD value:
      EntryName: DisableUserTOSSetting
      Value:     0x00000000 (0)
4. Quit Registry Editor
5. Restart you computer
6. Command prompt for validation (capture needed)
      # ping <ipaddress> -v 8
Reference: http://support.microsoft.com/kb/248611

DF flag implementation supports Linux und Windows. To support other
Operating Systems such as OS X (darwin) or FreeBSD the according
code such as sockopts need to be added and validated.

## Possible Improvements
* authenticated and encrypted mode
* sending intervals variation
* enhanced statistics
  * bining and interim statistics
  * late arrived packets
  * smokeping like graphics
  * median on latency
  * improved jitter (rfc3393, statistical variance formula):
    jitter:=sqrt(SumOf((D[i]-average(D))^2)/ReceivedProbesCount)
* daemon mode: NETCONF/YANG controlled, ...
* enhanced failure handling (catch exceptions)
* per probe time-out for statistics (late arrival)
* Validation with other operating systems (such as FreeBSD)
* Support for RFC 5938 Individual Session Control
* Support for RFC 6038 Reflect Octets Symmetrical Size

## Error codes (as per RFC 4656)
--- | ---
0 | OK
1 | Failure, reason unspecified (catch-all).
2 | Internal error.
3 | Some aspect of request is not supported.
4 | Cannot perform request due to permanent resource limitations.
5 | Cannot perform request due to temporary resource limitations.
