---
title: "Verifying the Device Configuration"
page_start: 180
page_end: 181
level: 2
---

## Verifying the Device Configuration

| 600001800 | 『00056 |
|---|---|
|  | 808157519. 268100108 \101 (21600 페 -056 《616856 10.3(2), 54010200 165\010 18 540000060 070 (21900 페 6%348 9000 862166 5\1661168. |
| 9410\ 56420410-000108 | 1219018575 016 61800042 600118478007. 띠 066 18760 3 68660 1680176 00701184180005 876 01680160 10 016 20070108-007118. 016 540\ 5617600410-060011 용 600104800 00665 ㅁ 01 01920167 01622. 10\676, 0416 06001184000006 17601810 10080 10 0416 6680002 0255, 4001 016 60003 70070108 5630000 000001800 16 060000060. |
| 940\ 0046-562000 14070108-0 ㅇ 00118 1256-0020860 | 1219018575 016 11066[84022 \1160 016 0100108 0001184180 ㅁ 070 \88 1891 01180860. |

The following example shows sample output of show running-config command with the sanitized keyword. The sanitized configuration is used to share a configuration without exposing some configuration details.

This option masks the sensitive words in running configuration output with <removed> keyword.

```cisco-ios
switch# show running-config sanitized
```

!Command: show running-config sanitized !Running configuration last done at: Wed Oct 12 09:14:54 2022 !Time: Wed Oct 12 13:52:55 2022 version 10.3(2) Bios:version 07.69 username admin password 5 <removed> role network-admin copp profile strict snmp-server user admin network-admin auth md5 <removed> priv aes-128 <removed> localizedV2key rmon event 1 log trap <removed> description FATAL(1) owner PMON@FATAL rmon event 2 log trap <removed> description CRITICAL(2) owner PMON@CRITICAL rmon event 3 log trap <removed> description ERROR(3) owner PMON@ERROR rmon event 4 log trap <removed> description WARNING(4) owner PMON@WARNING rmon event 5 log trap <removed> description INFORMATION(5) owner PMON@INFO

version 10.3(2) Bios:version 07.69

username admin password 5 <removed> role network-admin

--More--

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

164

ㅣ

|!