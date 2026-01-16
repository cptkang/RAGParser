---
title: "Guidelines and Limitations"
page_start: 26
page_end: 26
level: 2
---

## Guidelines and Limitations

- • Before configuring BFD per-link, make sure there is no BFD session running on the port-channel. If there is any BFD session running already, remove it and then proceed with bfd per-link configuration.

- • Configuring BFD per-link with link-local is not supported.

- • The supported platforms include Cisco Nexus 9500 Series switches with N9K-X9636C-R, N9K-X9636Q-R, N9K-X9636C-RX line cards.

- • Beginning with Cisco NX-OS Release 9.3(7), BFD is supported on unnumbered interfaces.

<

- Note

BFD over unnumbered Switched Virtual Interfaces (SVIs) are not supported.

Downgrade compatibility for BFD on unnumbered interface support cannot be verified using show incompatibility nxos bootflash:filename command. The compatibility will be checked during install all command.

- • Beginning with Cisco NX-OS Release 10.5(2)F, BFD over IP unnumbered is not supported on Cisco Nexus 9808 and 9804 switches.

- • When you configure BFD on a numbered interface along with OSPF and when the interface is converted to an unnumbered interface, the OSPF and BFD command remains in the running configuration but the BFD functionality may not work

- • The following BFD command configurations are not supported for configuration replace:

- • port-channel bfd track-member-link