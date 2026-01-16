---
title: "Configuring BFD on VRRP"
page_start: 51
page_end: 51
level: 2
---

## Configuring BFD on VRRP

You can configure BFD for the Virtual Router Redundancy Protocol (VRRP). The active and standby VRRP routers track each other through BFD. If BFD on the standby VRRP router detects that the active VRRP router is down, the standby VRRP router treats this event as an active time rexpiry and takes over as the active VRRP router.

The show vrrp detail command shows this event as BFD@Act-down or BFD@Sby-down.