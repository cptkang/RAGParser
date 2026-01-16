---
title: "Configuring Port Channel Interface"
page_start: 38
page_end: 38
level: 2
---

## Configuring Port Channel Interface

- • If the minimum number of links required to have the port-channel operationally up is not met in the above case, the port-channel is brought down by the port-channel manager. This in turn brings down the port-channel sub-interfaces if they are configured and thereby the logical BFD session also comes down notifying the routing protocol.

- • When you are using RFC 7130 on the main port-channel and logical BFD on the sub-interfaces, the logical BFD session should be run with lesser aggressive timers than the RFC 7130 BFD session. You canhaveRFC7130 configuredon theport-channelinterfaceor you canhaveitconfiguredin conjunction with the logical BFD sessions on the port-channel sub-interfaces.

- • When a proprietary per-link is configured, enabling IETF Micro-BFD sessions is not allowed on a port channelandvice-versa.Youhavetoremovetheproprietaryper-linkconfiguration.Currentimplementation of proprietary per-link does not allow changing the configuration (no per-link), if there is any BFD session that is bootstrapped by the applications. You need to remove the BFD tracking on the respective applications and remove per-link configuration. The migration path from the proprietary per-link to IETF Micro-BFD is as follows:

- • Remove the BFD configuration on the applications.

- • Remove the per-link configuration.

- • Enable the IETF Micro-BFD command.

- • Enable BFD on the applications.

The same migration path can be followed for proprietary BFD to IETF Micro-BFD on the main port-channel interface.