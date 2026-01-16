---
title: "Completing a Partial Command Name"
page_start: 94
page_end: 95
level: 2
---

## Completing a Partial Command Name

If you cannot remember a complete command name or if you want to reduce the amount of typing you have to perform, enter the first few letters of the command, and then press the Tab key. The command line parser will complete the command if the string entered is unique to the command mode. If your keyboard does not have a Tab key, press Ctrl-I instead.

The CLI recognizes a command once you have entered enough characters to make the command unique. For example, if you enter conf in EXEC mode, the CLI will be able to associate your entry with the configure command, because only the configure command begins with conf.

In the following example, the CLI recognizes the unique string for conf in EXEC mode when you press the Tab key:

```cisco-ios
switch# conf<Tab> switch# configure
```

When you use the command completion feature, the CLI displays the full command name. The CLI does not executethe commanduntilyou press the Return or Enter key. This featureallowsyou to modify the command if the full command was not what you intended by the abbreviation. If you enter a set of characters that could indicate more than one command, a list of matching commands displays.

For example, entering co<Tab> lists all commands available in EXEC mode beginning with co:

```cisco-ios
switch# co<Tab> configure copy switch# co
```

> **NOTE**
> Note that the characters you entered appear at the prompt again to allow you to complete the command entry.

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

78

ㅣ

|!