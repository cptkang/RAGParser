---
title: "Configuring BFD on HSRP"
page_start: 50
page_end: 50
level: 2
---

## Configuring BFD on HSRP

You can configure BFD for the Hot Standby Router Protocol (HSRP). The active and standby HSRP routers track each other through BFD. If BFD on the standby HSRP router detects that the active HSRP router is down, the standby HSRP router treats this event as an active time rexpiry and takes over as the active HSRP router.

The show hsrp detail command shows this event as BFD@Act-down or BFD@Sby-down.