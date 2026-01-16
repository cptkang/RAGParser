---
title: "Verifying Micro BFD Sessions Configuration"
page_start: 42
page_end: 43
level: 2
---

## Verifying Micro BFD Sessions Configuration

The following example displays the show output of the show running-config interface port-channel<port-channel>, show port-channel summary, show bfd neighbors vrf internet_routes, and show bfd neighbors interface port-channel <port-channel> vrf internet_routes details commands.

```cisco-ios
switch# show running-config interface port-channel 1001
```

!Command: show running-config interface port-channel1001 !Time: Fri Oct 21 09:08:00 2016 version 7.0(3)I5(1) interface port-channel1001 no switchport vrf member internet_routes port-channel bfd track-member-link port-channel bfd destination 40.4.1.2 ip address 40.4.1.1/24 ipv6 address 2001:40:4:1::1/64 switch# show por port-channel port-profile switch# show port-channel summary Flags: D - Down P - Up in port-channel (members) I - Individual H - Hot-standby (LACP only) s - Suspended r - Module-removed b - BFD Session Wait S - Switched R - Routed U - Up (port-channel) p - Up in delay-lacp mode (member) M - Not in use. Min-links not met -------------------------------------------------------------------------------- Group Port- Type Protocol Member Ports Channel -------------------------------------------------------------------------------- 1001 Po1001(RU) Eth LACP Eth1/11/1(P) Eth1/11/2(P) Eth1/12/1(P) Eth1/12/2(P) switch# show bfd neighbors vrf internet_routes OurAddr NeighAddr LD/RD RH/RS State Int Vrf 40.4.1.1 40.4.1.2 1090519041/0 Up N/A(3) Po1001 internet_routes 40.4.1.1 40.4.1.2 1090519042/1090519051 Up 819(3)

Holdown(mult)

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

|

|

169

| |

Up

Up

| |