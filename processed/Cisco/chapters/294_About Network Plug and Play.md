---
title: "About Network Plug and Play"
page_start: 74
page_end: 74
level: 2
---

## About Network Plug and Play

- • DNS server IP

• Domain name

The agent obtains the domain name of the customer network from the DHCP response and constructs the fully qualified domain name (FQDN). The following FQDN is constructed by the PnP agent using a preset deployment server name and the domain name information for the DHCP response. The agent then looks up the local name server and tries to resolve the IP address for the above FQDN.

Figure9:DNSLookupforpnpserver.[domainname].com

얄 띠 6\0 06106 16 00\6「60 00. 0 ㅁ 6106 61815 마 10 이 600160 (20 마 10 66006「 「(6500006 \ 따 1 0606 1『, 0070810 08016 800 02046 66006『 @ 0 ㅁ 6106 (6806 0010810 08006 800 아 68166 0「6060060『 마 66106 08106 (000560/6「.01600.0001) 300 「6501066 10「1『0 30016656 [4] 띠 6\ 061066 661801161166 00006 이 6 10 『0 마 0 56706『 391501

<

- Note The device reads domain name and creates predefined PnP server name as pnpserver.[domain name].com, for example; pnpserver.cisco.com.