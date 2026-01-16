---
title: "SUDI Supported Device as File Server"
page_start: 45
page_end: 45
level: 2
---

## SUDI Supported Device as File Server

The SUDI supported devices are Cisco devices. Unlike the earlier implementation, the DHCP server now provides a https location rather than http/tftp. In this scenario, only the DHCP server and the SUDI supported script server (HTTPS server) are required, other than one or more servers that contain the required software images and configuration files.

<

- Note SUDI only supports TLSv1.2 or below. Also, the SUDI solution only considers secure download using https, but not sftp.

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

29

| |