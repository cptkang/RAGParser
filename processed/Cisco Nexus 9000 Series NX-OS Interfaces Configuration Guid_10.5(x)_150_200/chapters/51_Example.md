---
title: "Example"
page_start: 11
page_end: 12
level: 2
---

## Example

This example shows how to configure the IP address of a DHCP client on an SVI:

```cisco-ios
switch# configure terminal switch(config)# interface vlan 15 switch(config-if)# ip address dhcp
```

This example shows how to configure an IPv6 address of a DHCP client on a management interface:

```cisco-ios
switch# configure terminal switch(config)# interface mgmt 0 switch(config-if)# ipv6 address use-link-local-only switch(config-if)# ipv6 address dhcp
```

|

|

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

138

ㅣ

|!