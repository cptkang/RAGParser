---
title: "Guidelines and Limitations for POAP"
page_start: 61
page_end: 61
level: 2
---

## Guidelines and Limitations for POAP

CiscoNexus 9000 Seriesswitchto not suspend itsmemberports by using theno lacp suspend-individual command from interface configuration mode.

- • Important POAP updates are logged in the syslog and are available from the serial console.

• Critical POAP errors are logged to the bootflash. The filename format is

- date-time_poap_PID_[init,1,2].log, where date-time is in the YYYYMMDD_hhmmss format and PID is the process ID.

- • You can bypass the password and the basic POAP configuration by using the skip option at the POAP prompt. When you use the skip option, no password is configured for the admin user. The copy running-config startup-config command is blocked until a valid password is set for the admin user.

- • If the boot poap enable command (perpetual POAP) is enabled on the switch, on a reload, a POAP boot is triggered even if there is a startup configurationpresent. If you do not want to use POAP in this scenario, remove the boot poap enable configuration by using the no boot poap enable command.

- • Script logs are saved in the bootflash directory. The filename format is date-time_poap_PID_script.log, where date-time is in the YYYYMMDD_hhmmss format and PID is the process ID.

You can configure the format of the script log file. Script file log formats are specified in the script. The template of the script log file has a default format; however, you can choose a different format for the script execution log file.

- • The POAP feature does not require a license and is enabled by default. However for the POAP feature to function, appropriate licenses must be installed on the devices in the network before the deployment of the network.

- • POAP DHCP transaction may fail if the device receives high traffic rate. This issue happens when POAP uses a front panel. To avoid this issue, make sure POAP uses a management port.

- • Beginning with NX-OS 7.0(3)I7(4), RFC 3004 (User Class Option for DHCP) is supported. This enables POAP to support user-class option 77 for DHCPv4 and user-class option 15 for DHCPv6. The text displayed for the user class option for both DHCPv4 and DHCPv6 is "Cisco-POAP".

- • With RFC 3004 (User Class Option for DHCP) support, POAP over IPv6 is supported on Nexus 9000 switches.

- • Beginning with NX-OS 9.2(2), POAP over IPv6 is supported on Nexus 9504 and Nexus 9508 switches with –R line cards.

The POAP over IPv6 feature enables the POAP process to use IPv6 when IPv4 fails. The feature is designed to cycle between IPv4 and IPv6 protocols when a connection failure occurs.

- • For secure POAP, ensure that DHCP snooping is enabled.

- • To support POAP, set firewall rules to block unintended or malicious DHCP servers.

- • To maintain system security and make POAP more secure, configure the following:

- • Enable DHCP snooping.

- • Set firewall rules to block unintended or malicious DHCP servers.

- • POAP is supported on both MGMT ports and in-band ports.

- • Beginning with Cisco NX-OS Release 10.2(3)F, the Hardware SUDI for POAP/HTTPS feature provides an option to securely download the POAP script.

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

45

| |