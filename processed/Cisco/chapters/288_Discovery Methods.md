---
title: "Discovery Methods"
page_start: 72
page_end: 72
level: 2
---

## Discovery Methods

A PnP agent discovers the PnP controller or server using one of the following methods:

- • DHCP-based discovery

• DNS-based discovery

• PnP connect

After the discovery, the PnP agent writes the discoveredinformationinto a file, which is then used to handshake with the PnP server (DNA controller/DNA-C).

The following tasks are carried out by the agent in the PnP discovery phase:

- • Brings up all the interfaces.

- • Sends a DHCP request in parallel for all the interfaces.

- • On receiving a DHCP reply, configures the IP address and mask, default route, DNS server, domain name, and writes the PnP server IP in a lease-parsing file. Note that there is no DHCP client in Cisco Nexus Switches and static configuration is required.

• Brings down all the interfaces.

%

> **NOTE**
> Note

- POAP is the first order of choice for Day 0 provisioning. Only when there is no valid POAP offer, PnP discovery is attempted. Also, PnP is supported only on Cisco Nexus 9000 EoR models N9K-C9504, N9K-C9508, and N9K-C9516. PnP is not supported on Cisco Nexus 9000 ToRs.