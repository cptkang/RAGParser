---
title: "Running a Command Script"
page_start: 118
page_end: 119
level: 2
---

## Running a Command Script

This example displays the CLI commands specified in the script file:

```cisco-ios
switch# show file testfile configure terminal interface ethernet 2/1 no shutdown end show interface ethernet 2/1
```

This example displays the run-script command execution output:

```cisco-ios
switch# run-script testfile `configure terminal` `interface ethernet 2/1` `no shutdown` `end` `show interface ethernet 2/1 ` Ethernet2/1 is down (Link not connected)
```

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

102

ㅣ

|!