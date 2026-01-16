---
title: "Example:"
page_start: 179
page_end: 179
level: 2
---

## Example:

The following example displays the configuration log entries for a specified username.

```cisco-ios
switch# show archive log config user user02 INDEX LINE USER LOGGED COMMAND 3 console0 user02 | system default switchport shutdown 4 console0 user02 | interface mgmt0 5 console0 user02 | no shutdown
```

- Step 3 switch# show archive log config user username first-index start-number [last-index end-number ]

Displays the configuration log entries by the index numbers. If you specify a number for the optional last-index, all the log entries with the index numbers in the range from the value entered for the start-number through the end-number for the specified user are displayed.