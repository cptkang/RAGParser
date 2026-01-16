---
title: "Script Execution Phase"
page_start: 58
page_end: 58
level: 2
---

## Script Execution Phase

After the device bootstraps itself using the information in the DHCP acknowledgement, the script file is downloaded from the TFTP server.

The switch runs the configuration script, which downloads and installs the software image and downloads a switch-specific configuration file.

However, the configuration file is not applied to the switch at this point, because the software image that currently runs on the switch might not support all of the commands in the configuration file. After the switch reboots, it begins running the new software image, if an image was installed. At that point, the configuration is applied to the switch.

<

> **NOTE**
> Note

- If the switch loses connectivity, the script stops, and the switch reloads its original software images and bootup variables.