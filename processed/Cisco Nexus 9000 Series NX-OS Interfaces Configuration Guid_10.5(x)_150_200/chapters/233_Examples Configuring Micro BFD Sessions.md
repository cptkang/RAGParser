---
title: "Examples: Configuring Micro BFD Sessions"
page_start: 42
page_end: 42
level: 2
---

## Examples: Configuring Micro BFD Sessions

port-channel bfd track-member-link port-channel bfd destination 10.1.1.2 port-channel bfd start 60 ip address 10.1.1.1/24

The sample configuration of switch 2 is as follows:

feature bfd

configure terminal interface port-channel 10 port-channel bfd track-member-link port-channel bfd destination 10.1.1.1 port-channel bfd start 60 ip address 10.1.1.2/24