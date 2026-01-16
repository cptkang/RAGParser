---
title: "SUMMARY STEPS"
page_start: 11
page_end: 11
level: 2
---

## SUMMARY STEPS

- switch# configure terminal

2. switch(config)# interface ethernet type slot/port | mgmt mgmt-interface-number | vlan vlan id

3. switch(config-if)# [no] ipv6 address use-link-local-only

4. switch(config-if)# [no] [ip | ipv6] address dhcp

- (Optional) switch(config)# copy running-config startup-config