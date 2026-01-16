---
title: "Mini AWK Utility"
page_start: 109
page_end: 109
level: 2
---

## Mini AWK Utility

AWK is a simple but powerful utility to summarize text output. You can use this utility after a pipe (|) to further process the text output of a command. Cisco NX-OS supports a mini AWK, which takes an inline program as an argument.

This example shows how the mini AWK utility can be used to summarize the text output of the show ip route summary vrf all command:

```cisco-ios
switch# show ip route summary vrf all | grep "Total number of routes" Total number of routes: 3 Total number of routes: 10
switch# show ip route summary vrf all | grep "Total number of routes" | awk '{ x = x + $5} END { print x }'
```

13