---
title: "For example:"
page_start: 53
page_end: 53
level: 2
---

## For example:

host MyDevice { option dhcp-client-identifier "\000SAL12345678"; fixed-address 2.1.1.10; option routers 2.1.1.1; option host-name "MyDevice"; option bootfile-name "poap_nexus_script.py"; option tftp-server-address 2.1.1.1;

}

The below example shows Configuring DHCPv6 for POAP over IPv6:

# This statement configures actual values to be sent # RTPREFIX option code = 243, RTPREFIX length = 22 # Ignore value 22. It is something related to option-size RT_PREFIX option length. # lifetime = 9000 seconds # route ETH1_IPV6_GW/64 # metric 1 option dhcp6.next-hop-rt-prefix 2003::2222 243 22 9000 0 1 ::; #ipv6 ::/0 2003::2222 #Another example - support not there in NXOS - CSCvs05271: #option dhcp6.next-hop-rt-prefix 2003::2222 243 22 9000 112 1 2003::1:2:3:4:5:0; #ipv6 2003::1:2:3:4:5:0/112 2003::2222 # Additional options #option dhcp6.name-servers fec0:0:0:1::1; #option dhcp6.domain-search "domain.example"; range6 2003::b:1111 2003::b:9999; #range6 2003::c:2222 2003::c:2222; option dhcp6.bootfile-url "tftp://2003::1111/poap_github_v6.py";

default-lease-time 3600;

max-lease-time 3600;

log-facility local7;

subnet6 2003::/64 {