---
title: "POAP Configuration Script"
page_start: 49
page_end: 49
level: 2
---

## POAP Configuration Script

The reference script supplied by Cisco supports the following functionality:

- • Retrieves the switch-specific identifier, for example, the serial number.

- • Downloads the nx-os software image if the files do not already exist on the switch. The nx-os image is installed on the switch and is used at the next reboot.

- • Schedules the downloaded configuration to be applied at the next switch reboot.

- • Stores the configuration as the startup configuration.

Cisco has sample configuration scripts that were developed using the Python programming language and Tool Command Language (Tcl). You can customize one of these scripts to meet the requirements of your network environment. You can access the Python script to perform POAP on the Cisco Nexus 9000 Series switch at this link: https://github.com/datacenter/nexus9000/tree/master/nx-os/poap.

The Python programming language uses two APIs that can execute CLI commands. These APIs are described in the following table. The arguments for these APIs are strings of the CLI commands.

| 01 | 066000000 |
|---|---|
| 010 | 복 604206 0416 78\ 04604 0 (71.1 0000018008, 10014010 음 46 6000601/9060181 011878 이 669. |
| 이 10(0) | 06 (01.1 60000008008 04186 94000 511., 0119 ^01 0416 46 600000800 04104110 8 0250100 016002087%. |
| 71106 6021 680 66 466141 10 4610 56870 0416 04104 01 위 10\ 0002048008. |