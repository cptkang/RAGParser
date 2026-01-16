---
title: "Erasing a Configuration"
page_start: 173
page_end: 173
level: 2
---

## Erasing a Configuration

You can erase the configuration on your device to return to the configuration defaults. "Configuration" refers to the startup configuration as seen in 'show startup'. No other internal application or process states are cleared.

Erase configuration feature is supported on the Nexus 9200-X, Nexus 9300-FX, -FX2, -FX3, and Nexus 9500 series switches.

You can erase the following configuration files saved in the persistent memory on the device:

- • Startup

- • Boot

- • Debug

The write erase command erases the entire startup configuration, except for the following:

- • Boot variable definitions

- • The IPv4 and IPv6 configuration on the mgmt0 interface, including the following:

- • Address

- • Subnet mask

- • Default Gateway/Route in the management VRF

To remove the boot variabledefinitionsand the IPv4/IPv6 configurationon the mgmt0 interface,use the write erase boot command. To remove all application persistency files such as patch rpms, third party rpms, application configuration in /etc directory other than configuration, use 'install reset'. This command was added as of the 7.0(3)I6(1) release.

%

> **NOTE**
> Note

- When there are multiple IPv6 default routes present in the management VRF, the default route that is displayed first in the show ipv6 static-route command for the management VRF just before using ‘copy r s’ gets restored after the write erase and reload.

- Note After you enter the write erase command, you must reload the ASCII configuration twice to apply the breakout configuration.

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

157

| |