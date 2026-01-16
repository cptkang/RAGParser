---
title: "Rolling Back to a Previous Configuration"
page_start: 181
page_end: 182
level: 2
---

## Rolling Back to a Previous Configuration

To roll back your configuration to a snapshot copy of a previously saved configuration, you need to perform the following steps:

1. Clear the current running image with the write erase command.

2. Restart the device with the reload command.

3. Copy the previously saved configuration file to the running configuration with the copy configuration-file running-configuration command.

4. Copy the running configuration to the start-up configuration with the copy running-config startup-config command.

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

165

| |

| |