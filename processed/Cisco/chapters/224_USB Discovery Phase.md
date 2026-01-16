---
title: "USB Discovery Phase"
page_start: 56
page_end: 56
level: 2
---

## USB Discovery Phase

When POAP starts, the process searches the root directory of all accessible USB devices for the POAP script file (the Python script file, poap_script.py), configuration files, and system and kickstart images.

If the script file is found on a USB device, POAP begins running the script. If the script file is not found on the USB device, POAP executes DHCP discovery. (When failures occur, the POAP process alternatesbetween USB discovery and DHCP discovery, until POAP succeeds or you manually abort the POAP process.)

If the software image and switch configuration files specified in the configuration script are present, POAP uses those files to install the software and configure the switch. If the software image and switch configuration files are not on the USB device, POAP does some cleanup and starts DHCP phase from the beginning.