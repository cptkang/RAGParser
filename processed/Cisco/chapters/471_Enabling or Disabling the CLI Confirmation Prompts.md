---
title: "Enabling or Disabling the CLI Confirmation Prompts"
page_start: 113
page_end: 113
level: 2
---

## Enabling or Disabling the CLI Confirmation Prompts

```cisco-ios
switch(config)# show cli history exec-mode
```

This example shows how to display only the commands in the command history for the current command mode:

```cisco-ios
switch(config-if)# show cli history this-mode-only
```

Thisexampleshowshowtodisplayonlythecommandsinthecommandhistorywithoutthecommandnumber and timestamp:

```cisco-ios
switch(config)# show cli history unformatted
```