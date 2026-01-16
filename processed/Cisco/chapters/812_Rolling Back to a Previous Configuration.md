---
title: "Rolling Back to a Previous Configuration"
page_start: 171
page_end: 171
level: 2
---

## Rolling Back to a Previous Configuration

Problems, such as memory corruption, can occur that make it necessary for you to recover your configuration from a backed up version.

<

- Note Each time that you enter a copy running-config startup-config command, a binary file is created and the ASCII file is updated. A valid binary configuration file reduces the overall boot time significantly. A binary file cannot be uploaded, but its contents can be used to overwrite the existing startup configuration. The write erase command clears the binary file.