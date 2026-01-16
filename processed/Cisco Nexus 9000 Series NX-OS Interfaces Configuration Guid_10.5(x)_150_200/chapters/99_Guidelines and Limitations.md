---
title: "Guidelines and Limitations"
page_start: 24
page_end: 25
level: 2
---

## Guidelines and Limitations

- • Disable the BFD echo function to prevent the interface from flapping.

- • Enable BFD multihop when configuring BGP over IP unnumbered interface.

- • Set the ipv6 nd ns-interval command range to 15 under the Layer 3 interface configuration to prevent BFD sessions from flapping, when there are a large number of IPv6 adjacencies.

Alternatively, increase the BFD echo interval to avoid session instability that might occur due to CoPP drops of NS/NA packets.

- • BFD supports BGPv6.

- • BFD supports EIGRPv6.

- • BFD supports only sessions which have unique (src_ip, dst_ip, interface/vrf) combination.

- • BFD supports single-hop BFD.

- • Only single-hop static BFD is supported.

- • BFD for BGP supports single-hop EBGP and iBGP peers.

- • BFD supports keyed SHA-1 authentication.

- • BFD supports the following Layer 3 interfaces—physical interfaces, port channels, sub-interfaces, and VLAN interfaces.

- • BFD depends on a Layer 3 adjacency information to discover topology changes, including Layer 2 topology changes. A BFD session on a VLAN interface (SVI) may not be up after the convergence of the Layer 2 topology if there is no Layer 3 adjacency information available.

- • For BFD on a static route between two devices, both devices must support BFD. If one or both of the devices do not support BFD, the static routes are not programmed in the Routing Information Base (RIB).

- • Both single-hop and multi-hop BFD features are supported with specific restrictions. For multi-hop BFD features restrictions, refer to Guidelines and Limitations for BFD Multihop, on page 188 section.

- • Port channel configuration limitations:

- • For Layer 3 port channels used by BFD, you must enable LACP on the port channel.

- • For Layer 2 port channels used by SVI sessions, you must enable LACP on the port channel.

- • SVI limitations:

- • An ASIC reset causes traffic disruption for other ports and it can cause the SVI sessions on the other ports to flap. For example,if the carrierinterfaceis a virtualport channel(vPC), BFD is not supported over the SVI interface and it could cause a trigger for an ASIC reset. When a BFD session is over SVI using virtual port channel (vPC) Peer-Link, the BFD echo function is not supported. You must disable the BFD echo function for all sessions over SVI between vPC peer nodes.

An SVI on the Cisco Nexus series switches should not be configured to establish a BFD neighbor adjacency with a device connected to it via a vPC. This is because the BFD keepalives from the neighbor, if sent over the vPC member link connected to the vPC peer-switch, do not reach this SVI causing the BFD adjacency to fail.

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

|

|

151

| |

| |