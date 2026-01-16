---
title: "Non-SUDI Supported Device as a File Server"
page_start: 46
page_end: 47
level: 2
---

## Non-SUDI Supported Device as a File Server

In this scenario, the Root-CA bundle must be installed in the booting device. The Root-CA bundle is required for authentication.Here, the DHCP server, intermediatedevice,and non-SUDI supported scriptserver (HTTPS server) are required, other than one or more servers that contain the required software images and configuration

files.

The DHCP offer has the details of intermediate server that has the Root-CA bundle available. The intermediate device should support SUDI. The booting device uses the intermediate device to download the Root-CA bundle, install it, and then communicate with the file server. The intermediate devices should be provisioned first.

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

30

|

|