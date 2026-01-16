---
title: "Setting up the DHCP Server without DNS for POAP"
page_start: 53
page_end: 53
level: 2
---

## Setting up the DHCP Server without DNS for POAP

Beginning with Cisco NX-OS Release 7.0(3)I6(1), the tftp-server-name can be used without the DNS option. To enable POAP functionality without DNS on earlier releases, a custom option of 150 must be used to specify the tftp-server-address.

To use the tftp-server-address option, specify the following at the start of your dhcpd.conf file.

option tftp-server-address code 150 = ip-address;