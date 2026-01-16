---
title: "Saving and Restoring a Command Mode"
page_start: 88
page_end: 89
level: 2
---

## Saving and Restoring a Command Mode

The Cisco NX-OS software allows you to save the current command mode, configure a feature, and then restore the previous command mode. The push command saves the command mode, and the pop command restores the command mode.

The following example shows how to save and restore a command mode:

```cisco-ios
switch# configure terminal
switch(config)# event manager applet test switch(config-applet)# push switch(config-applet)# configure terminal switch(config)# username testuser password newtest switch(config)# pop switch(config-applet)#
```

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

72

ㅣ

|!