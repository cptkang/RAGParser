---
title: "Displaying the Command History"
page_start: 112
page_end: 113
level: 2
---

## Displaying the Command History

You can display the command history using the show cli history command.

The show cli history command has the following syntax:

show cli history [lines] [config-mode | exec-mode | this-mode-only] [unformatted]

By default, the number of lines displayed is 12 and the output includes the command number and timestamp.

This example shows how to display the default number of lines of the command history:

```cisco-ios
switch# show cli history
```

This example shows how to display 20 lines of the command history:

```cisco-ios
switch# show cli history 20
```

This example shows how to display only the configuration commands in the command history:

- One of the parametersavailablefor the show cli history config-mode command is Number of lines to display (from end). The line number here is dependent on the show cli list line numbers (from end) and not on show cli history config-mode output line number. This parameter is mainly intended to be used with the show cli history command.

> **NOTE**
> Note

```cisco-ios
switch(config)# show cli history config-mode
```

This example shows how to display only the EXEC commands in the command history:

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

96

ㅣ

|!