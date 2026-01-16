---
title: "Configuring SVI and Subinterface Ingress/Egress Unicast Counters"
page_start: 12
page_end: 12
level: 2
---

## Configuring SVI and Subinterface Ingress/Egress Unicast Counters

Beginning Cisco NX-OS Release 9.3(3), SVI and subinterface unicast counters are supported on Cisco Nexus 9300-EX, 9300-FX/FX2 switches; and Cisco Nexus 9500 series switches with X9700-EX and X9700-FX line cards.

Beginning Cisco NX-OS Release 9.3(5), SVI and subinterface unicast counters are supported on Cisco Nexus N9K-C9316D-GX, N9K-C93600CD-GX, N9K-C9364C-GX switches.

Beginning Cisco NX-OS Release 10.5(2)F, if the hardware profile svi-and-si flex stats enable flex-stats command is enabled, SVI statistics rate is supported on Cisco Nexus 9300-FX, FX2, FX3, GX, GX2, H2R, H1 Series ToR switches and 9500 Series EoR switches with 9700-EX, FX, FX3, and GX line cards.

<

> **NOTE**
> Note

- • Enabling this feature disables VXLAN, MPLS, Tunnel, Multicast, and ERSPAN counters. Reload the switch for the changes to take effect.

- • For a vPC setup, the peer-gateway feature must be enabled under the vpc domain on both vPC peers. Otherwise, SVI counters may be inconsistent.

- • Multicast counters are not supported.

- • In EOR switches, the statistics rate is supported only for ports in the first ASIC (ASIC 0). If ingress or egress ports are in a different ASIC other than the first ASIC, then the statistics rate is not supported.

To configure SVI and subinterface ingress and/or egress unicast counters on a device, follow these steps: