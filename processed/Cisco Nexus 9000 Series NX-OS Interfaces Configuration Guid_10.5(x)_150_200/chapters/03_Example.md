---
title: "Example"
page_start: 1
page_end: 1
level: 2
---

## Example

This example shows how to create a VLAN interface:

```cisco-ios
switch# configure terminal switch(config)# feature interface-vlan switch(config)# interface vlan 10 switch(config-if)# ip address 192.0.2.1/8 switch(config-if)# copy running-config startup-config
```