---
title: "Defining Command Aliases"
page_start: 99
page_end: 99
level: 2
---

## Defining Command Aliases

- • Command aliases persist across reboots if you save them to the startup configuration.

- • Command alias translation always takes precedence over any keyword in any configuration mode or submode.

- • Command alias configuration takes effect for other user sessions immediately.

- • The Cisco NX-OS software provides one default alias, alias, which is the equivalent to the show cli alias command that displays all user-defined aliases.

- • You cannot delete or change the default command alias alias.

- • You can nest aliases to a maximum depth of 1. One command alias can refer to another command alias that must refer to a valid command, not to another command alias.

- • A command alias always replaces the first command keyword on the command line.

- • You can define command aliases for commands in any command mode.

- • If you reference a CLI variable in a command alias, the current value of the variable appears in the alias, not the variable reference.

- • You can use command aliases for show command searching and filtering.

<

> **NOTE**
> Note

- When using the cli alias name command, few keywords are reserved and cannot be used. To view the list of reserved keywords, type the show cli internal keywords common command. The reserved keywords match either partially or fully. For instance, in the cli alias name i show version command, i is a partial match. To prevent the use of reserved keywords, enable strict checking using the cli alias check strict command. This command is not enabled by default. After enabling the command, if a user attempts to use any reserved keywords, the switch displays an error.