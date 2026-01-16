---
title: "Secure Download of POAP Script"
page_start: 42
page_end: 43
level: 2
---

## Secure Download of POAP Script

Beginning with Cisco NX-OS Release 10.2(3)F, you have the option of securely downloading the POAP script. When a device with the POAP feature boots and does not find the startup configuration, the device enters POAP mode, locates a DHCP server, and bootstraps itself with its interface IP address, gateway, and DNS server IP addresses. The device also obtains the IP address of an HTTPS server and downloads POAP script securely. The script enables the switch to download and install the appropriate software image and configuration file.

TodownloadthePOAPscriptsecurely,youneedtoselectspecificPOAPoptions.UntilCiscoNX-OSRelease 10.2(3)F, POAP used options 66 and 67 for IPv4, and options 77 and 15 for IPv6 to extract the booting script information. However, the transfer of the script uses http, and is not very secure. Beginning with Cisco NX-OS Release 10.2(3)F, option 43 specifies the secure POAP related provisioning script information for IPv4 and option 17 specifies the same for IPv6. Additionally, these options allow the POAP to reach the file server in a secure manner. The POAP options 66, 67, 77, and 15 continue to be supported in Cisco NX-OS Release10.2(3)F. Furthermore, if you are using option 43 or 17, you can use the earlier options as fallback options, if required. From Cisco NX-OS Release 10.4(1)F, you can use Root-CA bundles instead of single .pem certificate for Secure POAP.

<

- The maximum character length is 512 bytes for both option 43 and option 17.

The sub-options available for option 43 and option 17 are discussed in the following sections:

- • Option 43 - IPv4

- • Option 17 - IPv6

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

26

ㅣ

|!