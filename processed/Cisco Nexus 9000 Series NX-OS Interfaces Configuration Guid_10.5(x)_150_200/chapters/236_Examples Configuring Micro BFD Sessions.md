---
title: "Examples: Configuring Micro BFD Sessions"
page_start: 43
page_end: 44
level: 2
---

## Examples: Configuring Micro BFD Sessions

Eth1/12/1 internet_routes 40.4.1.1 40.4.1.2 1090519043/1090519052 Up 819(3) Eth1/12/2 internet_routes 40.4.1.1 40.4.1.2 1090519044/1090519053 Up 819(3) Eth1/11/1 internet_routes 40.4.1.1 40.4.1.2 1090519045/1090519054 Up 819(3) Eth1/11/2 internet_routes switch# switch# show bfd neighbors interface port-channel 1001 vrf internet_routes details OurAddr NeighAddr LD/RD RH/RS Holdown(mult) State Int Vrf 40.4.1.1 40.4.1.2 1090519041/0 Up N/A(3) Po1001 internet_routes Session state is Up Local Diag: 0 Registered protocols: eth_port_channel Uptime: 1 days 11 hrs 4 mins 8 secs Hosting LC: 0, Down reason: None, Reason not-hosted: None Parent session, please check port channel config for member info switch# switch# show bfd neighbors interface ethernet 1/12/1 vrf internet_routes details OurAddr NeighAddr LD/RD RH/RS Holdown(mult) State Int Vrf 40.4.1.1 40.4.1.2 1090519042/1090519051 Up 604(3) Eth1/12/1 internet_routes Session state is Up and not using echo function Local Diag: 0, Demand mode: 0, Poll bit: 0, Authentication: None MinTxInt: 100000 us, MinRxInt: 100000 us, Multiplier: 3 Received MinRxInt: 300000 us, Received Multiplier: 3 Holdown (hits): 900 ms (0), Hello (hits): 300 ms (458317) Rx Count: 427188, Rx Interval (ms) min/max/avg: 19/1801/295 last: 295 ms ago Tx Count: 458317, Tx Interval (ms) min/max/avg: 275/275/275 last: 64 ms ago Registered protocols: eth_port_channel Uptime: 1 days 11 hrs 4 mins 24 secs Last packet: Version: 1 - Diagnostic: 0 State bit: Up - Demand bit: 0 Poll bit: 0 - Final bit: 0 Multiplier: 3 - Length: 24 My Discr.: 1090519051 - Your Discr.: 1090519042

Min tx interval: 300000

- Min rx interval: 300000

Min Echo interval: 300000 - Authentication bit: 0

Hosting LC: 1, Down reason: None, Reason not-hosted: None

Member session under parent interface Po1001

```cisco-ios
switch# show bfd neighbors interface ethernet 1/12/2 vrf internet_routes details
```

0045220028

OurAddr

State

619162002 1206

NeighAddr

Int

LD/RD

Vrf

RH/RS

Holdown(mult)

40.4.1.1

40.4.1.2

1090519043/1090519052 Up

799(3)

Eth1/12/2

internet_routes

Session state is Up and not using echo function

Local Diag: 0, Demand mode: 0, Poll bit: 0, Authentication: None MinTxInt: 100000 us, MinRxInt: 100000 us, Multiplier: 3 Received MinRxInt: 300000 us, Received Multiplier: 3 Holdown (hits): 900 ms (0), Hello (hits): 300 ms (458336) Rx Count: 427207, Rx Interval (ms) min/max/avg: 19/1668/295 last: 100 ms ago

|

|

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

170

ㅣ

Up

Up

Up

Up

Up

Up

|!