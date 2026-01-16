---
title: "Guidelines and Limitations for POAP"
page_start: 60
page_end: 61
level: 2
---

## Guidelines and Limitations for POAP

POAP configuration guidelines and limitations are as follows:

- • The bootflash:poap_retry_debugs.log is a file populated by POAP-PNP for internal purposes only. This file has no relevance in case of any POAP failures.

- • Due to limitations in Syslog, securePOAP pem file name characters length is limited to 230 characters, though secure POAP supports 256 characters length for a pem file name.

- • The switch software image must support POAP for this feature to function.

- • POAP does not support provisioning of the switch after it has been configured and is operational. Only auto-provisioning of a switch with no startup configuration is supported.

- • The https_ignore_certificate option should be turned on to use the ignore-certificate keyword with https protocol in POAP. This would enable you to successfully perform HTTPS transfer in the POAP script and without this option https as protocol cannot work with POAP.

- • ForthosewhousesHTTP/HTTPSserversforDay0provisioning,provisioninginstructionswillbegiven based on the MAC information and other related details in the HTTP header. POAP uses these details from HTTP GET headers so that the correct provisioning script is identified and used. This was available for other vendors (and other Cisco OSs).These additional information will be available in HTTP get headers from Cisco NX-OS Release 10.2(1) for Cisco Nexus 9000. This feature will be available by default for POAP and non-POAP HTTP get operations.

- • When you use copy http/https GET commands, the following fields are shared as part of the HTTP header:

Host: IP address User-Agent: cisco-nxos X-Vendor-SystemMAC: System MAC X-Vendor-ModelName: Switch-Model X-Vendor-Serial: Serial_Num X-Vendor-HardwareVersion: Hardwareversion X-Vendor-SoftwareVersion: sw_version X-Vendor-Architecture: Architecture

- • If you use POAP to bootstrap a Cisco Nexus device that is a part of a virtual port channel (vPC) pair using static port channels on the vPC links, the Cisco Nexus device activates all of its links when POAP starts up. The dually connected device at the end of the vPC links might start sending some or all of its traffic to the port-channel member links that are connected to the Cisco Nexus device, which causes traffic to get lost.

To work around this issue, you can configure Link Aggregation Control Protocol (LACP) on the vPC links so that the links do not incorrectly start forwarding traffic to the Cisco Nexus device that is being bootstrapped using POAP.

- • If you use POAP to bootstrap a Cisco Nexus device that is connected downstream to a Cisco Nexus 9000 Series switch through a LACP port channel, the Cisco Nexus 9000 Series switch defaults to suspend its member port if it cannot bundle it as a part of a port channel. To work around this issue, configure the

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

44

ㅣ

|!