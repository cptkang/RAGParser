---
title: "Example"
page_start: 10
page_end: 10
level: 2
---

## Example

This example shows how to add a Layer 3 interface to the VRF:

```cisco-ios
switch# configure terminal switch(config)# interface loopback 0 switch(config-if)# vrf member RemoteOfficeVRF switch(config-if)# ip address 209.0.2.1/16 switch(config-if)# copy running-config startup-config
```