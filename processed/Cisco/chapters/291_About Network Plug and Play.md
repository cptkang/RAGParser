---
title: "About Network Plug and Play"
page_start: 73
page_end: 73
level: 2
---

## About Network Plug and Play

• Domain name

If the agent configuration fails, you should manually intervene and configure the switch.

DHCP discovery has the following flow:

- • Power on the switch.

- • Switch will boot up, the PnP process will be started, as there is no configuration present.

- • Start DHCP discovery.

- • DHCP Server replies with the PnP server configuration.

- • PnP agent handshakes with the PnP server.

- • Download the image, install, and reload.

- • Download and apply the configuration from the controller.

A device with no startup configuration in the NV-RAM triggers the day 0 provisioning and goes through the POAP process (as detailed in m_using_poweron_auto_provisioning_92x.ditamap#id_70221). When there is no valid POAP offer, the PnP agent is initiated. The DHCP server can be configured to insert additional information using vendor-specific Option 43. Upon receiving Option 60 from the device with the string (cisco pnp), to pass on the IP address or hostname of the PnP server to the requesting device. When the DHCP responseis receivedby thedevice,thePnP agentextractstheOption43 from theresponseto gettheIP address or the hostname of the PnP server. The PnP agent then uses this IP address or hostname to communicate with the PnP server.

Figure8:DHCPDiscoveryProcessforPnPServer

60 06106 16 00\6「60 00. 0 ㅁ 6106 6185 마 10『 16006 66006 1『10 00100 43 8009 \ 따 06466 『 6\ 061066 661801161166 00006 10 『000 56006『 @ @ 마 310 66006『「 (66000056 \ 마 00 391499