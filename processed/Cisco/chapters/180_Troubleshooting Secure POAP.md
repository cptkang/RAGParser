---
title: "Troubleshooting Secure POAP"
page_start: 48
page_end: 48
level: 2
---

## Troubleshooting Secure POAP

Perform the following steps to collect debugging information regarding secure POAP:

1. Set the debug option for IPv4 in option 43 to 1 and for IPv6 in option 17.

The debug option enables additional logs.

2. Allow the switch to run one cycle of POAP.

3. Abort POAP.

4. When the system boots up, run the show tech-support poap command.

This command displays POAP status and configuration.