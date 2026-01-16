---
title: "Backing Up Configuration Files"
page_start: 181
page_end: 181
level: 2
---

## Backing Up Configuration Files

This example shows how to back up the startup configuration to the bootflash: file system (ASCII file):

```cisco-ios
switch# copy startup-config bootflash:my-config
```

This example shows how to back up the startup configuration to the TFTP server (ASCII file):

```cisco-ios
switch# copy startup-config tftp://172.16.10.100/my-config
```

This example shows how to back up the running configuration to the bootflash: file system (ASCII file):

```cisco-ios
switch# copy running-config bootflash:my-config
```