---
title: "Example"
page_start: 3
page_end: 3
level: 2
---

## Example

This example shows how to create a loopback interface:

```cisco-ios
switch# configure terminal switch(config)# interface loopback 0 switch(config-if)# ip address 192.0.2.1/8 switch(config-if)# copy running-config startup-config
```