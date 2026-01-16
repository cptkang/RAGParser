---
title: "Troubleshooting for POAP"
page_start: 66
page_end: 66
level: 2
---

## Troubleshooting for POAP

The following is a list of known issues and suggestions while using POAP:

- • Issue: POAP script execution fails immediately with no syslogs or output except for a "Script execution failed" statement.

Suggestion: Use the python script-name command on the server and make sure there are no syntax errors. The options dictionary is a Python dictionary so each entry must be comma separated and have the key or option and the value separated by a colon.

- • Issue: A TypeError exception occurs at various places depending on the incorrectly used option.

Suggestion: Some options use integers (for example, timeouts and other numeric values). Check the options dictionary for numeric values that are enclosed in quotes. Refer to the options list for the correct usage.

- • Issue: POAP over USB is not finding the files that are present.

Suggestion: Some devices have two USB slots. If you are using USB slot 2, you need to specify that as an option.

- • Issue: Any issue with POAP.

Suggestion: Abort POAP, and when the system boots up, run the show tech-support poap command, which displays POAP status and configuration.