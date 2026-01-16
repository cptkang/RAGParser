---
title: "Sending Commands to Modules"
page_start: 114
page_end: 114
level: 2
---

## Sending Commands to Modules

You can send commands directly to modules from the supervisor module session using the slot command.

The slot has the following syntax:

slot slot-number [quoted] command-string

By default, the keyword and arguments in the command-string argument are separated by a space. To send more than one command to a module, separate the commands with a space character, a semicolon character (;), and a space character.

The quoted keyword indicates that the command string begins and ends with double quotation marks ("). Use this keyword when you want to redirect the module command output to a filtering utility, such as diff, that is supported only on the supervisor module session.

This example shows how to display and filter module information: