---
title: "Accessing Directories on Standby Supervisor Modules"
page_start: 158
page_end: 158
level: 2
---

## Accessing Directories on Standby Supervisor Modules

This example shows how to list the files on the standby supervisor module:

```cisco-ios
switch# dir bootflash://sup-remote
```

4096 Oct 03 23:55:55 2013 .patch/ ... 16384 Jan 01 13:23:30 2011 lost+found/ 297054208 Oct 21 18:55:36 2013 n9000-dk9.6.1.2.I1.1.bin ... Usage for bootflash://sup-remote 1903616000 bytes used 19234234368 bytes free 21137850368 bytes total

This example shows how to delete a file on the standby supervisor module:

```cisco-ios
switch# delete bootflash://sup-remote/aOldConfig.txt
```