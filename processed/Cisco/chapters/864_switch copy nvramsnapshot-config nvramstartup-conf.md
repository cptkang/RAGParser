---
title: "switch# copy nvram:snapshot-config nvram:startup-config"
page_start: 181
page_end: 181
level: 2
---

## switch# copy nvram:snapshot-config nvram:startup-config

> **WARNING**
> Warning: this command is going to overwrite your current startup-config. Do you wish to continue? {y/n} [y] y

This example shows how to copy a running configuration to the bootflash: file system:

```cisco-ios
switch# copy system:running-config bootflash:my-config
```