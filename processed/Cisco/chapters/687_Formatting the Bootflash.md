---
title: "Formatting the Bootflash"
page_start: 151
page_end: 151
level: 2
---

## Formatting the Bootflash

Use the format bootflash: CLI command to format the onboard flash memory (bootflash:). If the command errorsoutduetotheDeactivate all virtual-services and try againerrormessage,destroy the Guest Shell using the guestshell destroy CLI command and rerun the format bootflash: command, for example,

```cisco-ios
switch# sh virtual-service list Virtual Service List:
```

Name

Status

Package Name

-----------------------------------------------------------------------

guestshell+

Activated

guestshell.ova

```cisco-ios
switch#
switch# guestshell destroy
```

You are about to destroy the guest shell and all of its contents. Be sure to save your work. Are you sure you want to continue? (y/n) [n] y

```cisco-ios
switch# 2018 Jan 17 18:42:24 switch %$ VDC-1 %$ %VMAN-2-ACTIVATION_STATE: Deactivating virtual service 'guestshell+'
switch#format bootflash:
```