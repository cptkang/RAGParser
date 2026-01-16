---
title: "Guidelines and Limitations"
page_start: 27
page_end: 27
level: 2
---

## Guidelines and Limitations

- • Single-hop BFD on routed port and breakout ports

- • Single-hop BFD on IPv4 and IPv6 address

- • Minimum BFD timer with 50ms

- • BFD asynchronous mode

- • BFD echo function

- • Use the bfd authentication interop command to configure BFD authenticationinteroperabilitybetween Nexus and non-Nexus platforms. If you do not configure this command, BFD authentication fails due to an invalid authentication sequence number field format.

- • BFD Authentication is not supported on Cisco Nexus 9800 platform switches.

- • Beginning with Cisco NX-OS Release 10.4(1)F, BFD supports single-hop BFD on N9KX98900CD-A and N9KX9836DM-A line cards with Cisco Nexus 9808 and 9804 switches.

- • Beginning with Cisco NX-OS Release 10.4(3)F, single hop BFD is supported on Cisco Nexus 9808 and 9804 L3 port-channel interfaces and port-channel sub-interfaces with the following limitations:

- • Per Port-channel interface, only 128 sessions are supported.

- • BFD authentication is not supported.

- • Beginning with Cisco NX-OS Release 10.4(3)F, single-hop BFD is supported on Layer 3 port channel on Cisco Nexus 9800 switches. The BFD server selects the hosting line card for the session among the available online line cards. However, this feature has the following limitations:

- • If the hosting line card changes, the ongoing session gets deleted on that line card, and the hosting is created on another line card that is available.

- • If the source IP of the BFD session changes, the ongoing session gets deleted and recreated with the new source IP.