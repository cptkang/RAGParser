---
title: "Defining Command Aliases"
page_start: 118
page_end: 118
level: 2
---

## Defining Command Aliases

This example shows how to define command aliases:

cli alias name ethint interface ethernet cli alias name shintbr show interface brief cli alias name shintupbr shintbr | include up | include ethernet

This example shows how to use a command alias:

```cisco-ios
switch# configure terminal switch(config)# ethint 2/3 switch(config-if)#
```