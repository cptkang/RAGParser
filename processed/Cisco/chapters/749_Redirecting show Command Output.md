---
title: "Redirecting show Command Output"
page_start: 161
page_end: 161
level: 2
---

## Redirecting show Command Output

This example shows how to direct the output to a file on the bootflash: file system:

```cisco-ios
switch# show interface > bootflash:switch1-intf.cfg
```

This example shows how to direct the output to a file on external flash memory:

```cisco-ios
switch# show interface > usb1:switch-intf.cfg
```

This example shows how to direct the output to a file on a TFTP server:

```cisco-ios
switch# show interface > tftp://10.10.1.1/home/configs/switch-intf.cfg Preparing to copy...done
```

This example shows how to direct the output of the show tech-support command to a file:

```cisco-ios
switch# show tech-support > Samplefile Building Configuration ... switch# dir 1525859 Jul 04 00:51:03 2013 Samplefile Usage for volatile:// 1527808 bytes used 19443712 bytes free 20971520 bytes total
```