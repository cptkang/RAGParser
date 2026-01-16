---
title: "Accessing Directories on the Standby Supervisor Module"
page_start: 145
page_end: 145
level: 2
---

## Accessing Directories on the Standby Supervisor Module

You can access all file systems on the standby supervisor module (remote) from a session on the active supervisor module. This feature is useful when copying files to the active supervisor modules requires similar files to exist on the standby supervisor module. To access the file systems on the standby supervisor module from a session on the active supervisor module, you specify the standby supervisor module in the path to the file using either filesystem://sup-remote/ or filesystem://sup-standby/.