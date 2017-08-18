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
```
$ git clone https://github.com/nokia/twampy
Cloning into 'twampy'...
```

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
64 | 7 | 58% | 10%
590 | 4 | 33% | 55%
1514 | 1 | 8% | 35%

TOS/DSCP user settings neet to be enabled on WINDOWS:
1. Open Registry Editor
2. Go to key:
      HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\TcpIp\Parameters
3. Create new DWORD value:

EntryName | Value
--- | ---
DisableUserTOSSetting | 0x00000000 (0)

4. Quit Registry Editor
5. Restart you computer
6. Command prompt for validation (capture needed)

      $ ping <ipaddress> -v 8
      
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
Error Code | Description
--- | ---
0 | OK
1 | Failure, reason unspecified (catch-all).
2 | Internal error.
3 | Some aspect of request is not supported.
4 | Cannot perform request due to permanent resource limitations.
5 | Cannot perform request due to temporary resource limitations.

## Usage example: getting help
Help on modes of operation:
```
$ ./twampy.py --help
usage: twampy.py [-h] [-v]
                 {responder,sender,controller,controlclient,dscptable} ...

positional arguments:
  {responder,sender,controller,controlclient,dscptable}
                        twampy sub-commands
    responder           TWL responder
    sender              TWL sender
    controller          TWAMP controller
    controlclient       TWAMP control client
    dscptable           print DSCP table

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
```

Specific help:
```
$ ./twampy.py sender --help
usage: twampy.py sender [-h] [-l filename] [-q | -v | -d]
                        [--tos type-of-service] [--dscp dscp-value]
                        [--ttl time-to-live] [--padding bytes]
                        [--do-not-fragment] [-i msec] [-c packets]
                        [remote-ip:port] [local-ip:port]

optional arguments:
  -h, --help            show this help message and exit
  -q, --quiet           disable logging
  -v, --verbose         enhanced logging
  -d, --debug           extensive logging

Debug Options:
  -l filename, --logfile filename
                        Specify the logfile (default: <stdout>)

IP socket options:
  --tos type-of-service        IP TOS value
  --dscp dscp-value            IP DSCP value
  --ttl time-to-live           [1..128]
  --padding bytes              IP/UDP mtu value
  --do-not-fragment            keyword (do-not-fragment)

TWL sender options:
  remote-ip:port
  local-ip:port
  -i msec, --interval msec     [100,1000]
  -c packets, --count packets  [1..9999]
```



## Usage example against SR OS TWAMP server
Router configuration:
```
A:VSR# configure test-oam
A:VSR>config>test-oam># info
----------------------------------------------
        twamp
            server
                prefix 0.0.0.0/0 create
                exit
                no shutdown
            exit
        exit
----------------------------------------------
```
Running the test:
```
$ ./twampy.py controller 192.168.255.2
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
