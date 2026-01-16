---
title: "Guidelines for Migration/Configuration of IETF Per-Member Sessions:"
page_start: 37
page_end: 38
level: 2
---

## Guidelines for Migration/Configuration of IETF Per-Member Sessions:

See the following guidelines for migration/configuration of IETF per-member sessions:

- • The logical BFD sessions that are created using the routing protocols over port-channel sub-interfaces (where RFC 7130 cannot run) are still supported. The main port-channel interface however does not support both logical and RFC 7130 sessions that co-exist. It can support only either of them.

- • YoucanconfigureRFC7130BFDoverthemainport-channelinterfacethatperformbandwidthmonitoring over the LAG by having one Micro-BFD session over each member. If any of the member port goes down, BFD notifies it to the port-channelmanager that removes the port from the LTL, thereby preventing blackholing of the traffic on that member.

|

|

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

164

ㅣ

|!