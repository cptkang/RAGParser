---
title: "Recalling a Command"
page_start: 111
page_end: 111
level: 2
---

## Recalling a Command

You can recall a command in the command history to optionally modify and enter again.

This example shows how to recall a command and reenter it:

```cisco-ios
switch(config)# show cli history
```

0 11:04:07 configure terminal 1 11:04:28 show interface ethernet 2/24 2 11:04:39 interface ethernet 2/24 3 11:05:13 no shutdown 4 11:05:19 exit 5 11:05:25 show cli history switch(config)# !1 switch(config)# show interface ethernet 2/24

You can also use the Ctrl-P and Ctrl-N keystroke shortcuts to recall commands.