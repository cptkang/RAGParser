---
title: "Example"
page_start: 165
page_end: 165
level: 2
---

## Example

This example shows how to copy the configuration file to a remote server:

```cisco-ios
switch# copy running-config tftp://10.10.1.1/sw1-run-config.bak switch# copy startup-config tftp://10.10.1.1/sw1-start-config.bak
```