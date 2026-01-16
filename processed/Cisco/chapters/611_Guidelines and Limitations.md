---
title: "Guidelines and Limitations"
page_start: 141
page_end: 141
level: 2
---

## Guidelines and Limitations

Guidelines and limitations for device file systems, directories, and files are as follows:

- • The show tech-support details command cannot be terminated using Ctrl+Z. Instead, use Ctrl+C to terminate the command.

- • Utilize a user with the "network-admin" role to make changes to files in the bootflash.

- • Starting with Release 10.5(1), you can automatically detect SSD partition size on the Nexus 9000 to match the expected configured size. An information syslog is seen during bootup in the show logging log or show logging nvram commands to indicate the NX-OS Nexus 9000 booted with an unexpected SSD partitioning size.

%PLATFORM-2-SSD_PARTITION_CHECK: Incorrect <device> partition size detected - please contact Cisco TAC for additional information