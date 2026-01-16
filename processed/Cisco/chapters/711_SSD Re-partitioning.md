---
title: "SSD Re-partitioning"
page_start: 155
page_end: 155
level: 2
---

## SSD Re-partitioning

You can configure SSD re-partitioning to increase the configuration storage space. This also increases the size of logflash storage. This configuration takes effect after a system reload, and the additional cfg and logflash storage space may decrease the size of the bootflash.

We recommendthatyou perform a backup of allthe softwareimages,configurations,and personaldatabefore performing the SSD re-partitioning.

Starting with Release 10.5(1), you can automatically detect SSD partition size on the switch to match the expected configured size. An information syslog is seen during bootup in the show logging log or show logging nvram commands to indicate the switch booted with an unexpected SSD partitioning size.

%PLATFORM-2-SSD_PARTITION_CHECK: Incorrect <device> partition size detected - please contact

Cisco TAC for additional information

Extended partitioning scheme is not support for platforms with a 64GB SSD.