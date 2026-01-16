---
title: "Example"
page_start: 9
page_end: 9
level: 2
---

## Example

The following example shows how to change the size of the SVI TCAM region:

```cisco-ios
switch(config)# hardware profile tcam region svi 256 [SUCCESS] New tcam size will be applicable only at boot time. You need to 'copy run start' and 'reload'
switch(config)# copy running-config startup-config switch(config)# reload WARNING: This command will reboot the system Do you want to continue? (y/n) [n] y
```