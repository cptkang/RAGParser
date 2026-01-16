---
title: "switch# copy samplefile mystorage/samplefile"
page_start: 159
page_end: 159
level: 2
---

## switch# copy samplefile mystorage/samplefile

This example shows how to copy a file from the active supervisor module bootflash to the standby supervisor module bootflash:

```cisco-ios
switch# copy bootflash:nx-os-image bootflash://sup-2/nx-os-image
```

This example shows how to overwrite the contents of an existing configuration in NVRAM: