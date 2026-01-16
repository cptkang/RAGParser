---
title: "Guidelines and Limitations"
page_start: 23
page_end: 24
level: 2
---

## Guidelines and Limitations

BFD has the following configuration guidelines and limitations:

- • The QSFP 40/100-G BiDi comes up in the highest possible speed available on the port. For example, in the Cisco Nexus 93180LC-EX switch it comes up as 40 G in the first 28 ports and 100 G in the last 4 ports. If you need to connect to 40-G SR4 BiDi, the speed on the 40/100-G BiDi needs to be set to 40 G.

- • BFD over private-vlan is not supported Cisco Nexus 9000 Switches.

- • Beginning with Cisco NX-OS Release 10.2(1q)F, Layer 3 Unicast BFD is supported on Cisco Nexus N9K-C9332D-GX2B platform switches.

- • Forming BFD neighbors on a vPC VLAN through an orphan port is not supported on Cisco Nexus 9000 Switches.

- • Beginning with Cisco NX-OS Release 9.2(1), QSFP-40/100-SRBD comes up in the speed of 100-G and inter-operate with other QSFP-40/100-SRBD at either 40-G or 100-G speed on Cisco Nexus 9500 Switches with the N9K-X9636C-RX line card. The QSFP-40/100-SRBD can also inter-operate with QSFP-40G-SR-BD at 40G speeds. However to operate at 40G speed, you must configure the speed as 40G.

- • show commands with the internal keyword are not supported.

- • BFD per-member link support is added on Cisco Nexus 9000 Series switches.

- • BFD supports BFD version 1.

- • BFD supports IPv4 and IPv6.

- • BFD supports OSPFv3.

- • BFD supports IS-ISv6.

- • When configuring BFD over IP unnumbered interfaces, use these guidelines:

|

|

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

150

ㅣ

|!