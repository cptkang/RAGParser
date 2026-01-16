---
title: "Example:"
page_start: 35
page_end: 36
level: 2
---

## Example:

```cisco-ios
switch(config)# bfd slow-timer 2000
```

When the BFD echo function is enabled, this value also slows down the asynchronous sessions.

This value overwrites the required minimum receive interval when the echo function is enabled. The range is from 1000 to 30,000 milliseconds. The default is 2000 milliseconds.

- Step 3 Enters interface configuration mode using the interface int-if command.

|

|

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

162

ㅣ

|!