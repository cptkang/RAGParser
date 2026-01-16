---
title: "Example"
page_start: 2
page_end: 2
level: 2
---

## Example

This example shows how to configure the Layer 3 interface on slot 7, port 3 with a static MAC address:

```cisco-ios
switch# config t switch(config)# interface ethernet 7/3 switch(config-if)# mac-address 22ab.47dd.ff89 switch(config-if)#
```