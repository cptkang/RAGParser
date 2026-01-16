---
title: "POAP Dynamic Breakout"
page_start: 57
page_end: 57
level: 2
---

## POAP Dynamic Breakout

Beginning with Cisco NX-OS Release 7.0(3)I4(1), POAP dynamically breaks out ports in an effort to detect a DHCP server behind one of the broken-out ports. Previously, the DHCP server used for POAP had to be directly connected to a normal cable because breakout cables were not supported.

POAP determines which breakout map (for example, 10gx4, 50gx2, 25gx4, or 10gx2) will bring up the link connected to the DHCP server. If breakout is not supported on any of the ports, POAP skips the dynamic breakout process. After the breakout loop completes, POAP proceeds with the DHCP discovery phase as normal.

<

For more information on dynamic breakout, see the interfaces configuration guide for your device.

- Note

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

41

뜰