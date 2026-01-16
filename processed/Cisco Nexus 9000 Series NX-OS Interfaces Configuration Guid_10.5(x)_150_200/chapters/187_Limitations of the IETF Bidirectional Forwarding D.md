---
title: "Limitations of the IETF Bidirectional Forwarding Detection"
page_start: 37
page_end: 37
level: 2
---

## Limitations of the IETF Bidirectional Forwarding Detection

- • IETF Micro-BFD sessions supports only single-hop BFD sessions. We recommend that you do not configure IPs from different subnets to establish the Micro-BFD sessions.

- • It cannot co-exist with BFD over logical port-channels or proprietary BFD per-member links. BFD IPv6 logical/proprietary per-link session is also not supported when BFD IETF IPv4 is configured on PC.

- • When you configure logical BFD session under any routing protocol, make sure that is not applied to any IETF port-channel. Having both logical and IETF configuration for same port-channel results in undefined behavior during ISSU/reloads.

- • IETF BFD IPv6 is not supported.

- • Echo functionality is not supported for Micro-BFD sessions.

- • Port-channel interfaces should be directly connected between two switches that are running the BFD sessions. No intermediate Layer 2 switches are expected.

- • EthPCM/LACP Limitations

- • If a LACP port-channel has members in hot-standby state, BFD failure in one of the active links may not cause the hot-standby link to come up directly. Once the active link with BFD failure goes down, the hot-standby member becomes active. However, it may not be able to prevent the port-channel from going down before the hot-standby link comes up, in cases where port-channel min-link condition is hit.

- • General Limitations:

- • It is supported only on Layer 3 port-channels.

- • It is not supported on the following:

- • vPC

- • Layer 3 sub-interfaces

- • Layer 2 port-channels/Layer 2 Fabric Path

- • FPC/HIF PC

- • Layer 3 sub-interfaces

- • SVI over port-channels