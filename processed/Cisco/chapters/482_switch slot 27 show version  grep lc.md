---
title: "switch# slot 27 show version | grep lc"
page_start: 114
page_end: 114
level: 2
---

## switch# slot 27 show version | grep lc

This example shows how to filter module information on the supervisor module session:

```cisco-ios
switch# slot 27 quoted "show version" | diff switch# slot 28 quoted "show version" | diff -c *** /volatile/vsh_diff_1_root_8430_slot__quoted_show_version.old 2013 --- - Wed Apr 29 20:10:41 2013 *************** *** 1,5 **** ! RAM 1036860 kB ! lc27 Software BIOS: version 6.20 system: version 6.1(2)I1(1) [build 6.1(2)] --- 1,5 ---- ! RAM 516692 kB ! lc28 Software BIOS: version 6.20 system: version 6.1(2)I1(1) [build 6.1(2)]
```

Wed Apr 29 20:10:41

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

98

ㅣ