---
title: "Configuration Examples for Layer 3 Interfaces"
page_start: 17
page_end: 18
level: 2
---

## Configuration Examples for Layer 3 Interfaces

This example shows how to configure Ethernet subinterfaces:

interface ethernet 2/1.10 description Layer 3 ip address 192.0.2.1/8

This example shows how to configure a loopback interface:

interface loopback 3 ip address 192.0.2.2/32

The following examples shows the output of the SVI counters and SVI statistics rate details when hardware profile svi-and-si flex-stats-enable command is enabled.

In the show interface command, the statistics rate or polling interval of 60 seconds and 300 seconds are added starting with Cisco NX-OS Release 10.5(2)F release.

show interface vlan 2406

Vlan2406 is up, line protocol is up, autostate enabled Hardware is EtherSVI, address is 3c13.ccc9.a397 Internet Address is 20.0.0.2/24 MTU 1500 bytes, BW 1000000 Kbit, DLY 10 usec, reliability 255/255, txload 1/255, rxload 1/255 Encapsulation ARPA, loopback not set Keepalive not supported ARP type: ARPA Last clearing of "show interface" counters 00:11:03 Load-Interval #1: 1 minute (60 seconds) 60 seconds input rate 5492528 bits/sec, 10096 packets/sec 60 seconds output rate 0 bits/sec, 0 packets/sec input rate 5.49 Mbps, 10.10 Kpps; output rate 0 bps, 0 pps Load-Interval #2: 5 minute (300 seconds) 300 seconds input rate 5448741 bits/sec, 10016 packets/sec 300 seconds output rate 0 bits/sec, 0 packets/sec input rate 5.45 Mbps, 10.02 Kpps; output rate 0 bps, 0 pps L3 Switched: input: 0 pkts, 0 bytes - output: 0 pkts, 0 bytes L3 in Switched: ucast: 6643884 pkts, 451784112 bytes L3 out Switched:

ucast: 0 pkts, 0 bytes

|

|

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

144

ㅣ

|!