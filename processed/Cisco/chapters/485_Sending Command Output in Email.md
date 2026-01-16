---
title: "Sending Command Output in Email"
page_start: 115
page_end: 115
level: 2
---

## Sending Command Output in Email

You can use the CLI to send the output of a show command to an email address using the pipe operator (|).

<

- Note

The email configuration remains persistent for all show command output until it is reconfigured.

When you upgrade from a release before Cisco NX-OS Release 9.3(3) to Cisco NX-OS Release 9.3(3) or later releases, email configuration will be missing. This is due to enabling DME functionality for this feature. To resolve this, you need to execute "no email" and reapply the entire email configuration.