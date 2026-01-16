---
title: "Disabling POAP"
page_start: 48
page_end: 49
level: 2
---

## Disabling POAP

POAP is enabled when there is no configuration in the system. It runs as a part of bootup. However, you can bypass POAP enablement during initial setup. If you want to disable POAP permanently (even when there is no configuration in the system), you can use the 'system no poap' command. This command ensures that POAP is not started during the next boot (even if there is no configuration). To enable POAP, use the 'system poap' command or the 'write erase poap' command. The 'write erase poap' command erases the POAP flag and enables POAP.

- • Example: Disabling POAP

```cisco-ios
switch# system no poap
switch# sh boot Current Boot Variables: sup-1 NXOS variable = bootflash:/nxos.9.2.1.125.bin Boot POAP Disabled
```

POAP permanently disabled using 'system no poap'

Boot Variables on next reload:

sup-1 NXOS variable = bootflash:/nxos.9.2.1.125.bin Boot POAP Disabled

POAP permanently disabled using 'system no poap'

```cisco-ios
switch# sh system poap
```

System-wide POAP is disabled using exec command 'system no poap' POAP will be bypassed on write-erase reload. (Perpetual POAP cannot be enabled when system-wide POAP is disabled)

- • Example: Enabling POAP

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

32

ㅣ

|!