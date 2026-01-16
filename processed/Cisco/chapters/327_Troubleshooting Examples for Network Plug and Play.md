---
title: "Troubleshooting Examples for Network Plug and Play"
page_start: 80
page_end: 80
level: 2
---

## Troubleshooting Examples for Network Plug and Play

time: 08:31:36 Jan 11 capability status: Success time: 08:33:50 Jan 11 backoff status: Success time: 08:41:26 Jan 11 topology status: Success time: 08:33:54 Jan 11

```cisco-ios
Switch# show pnp version PnP Agent Version Summary
```

PnP Agent: 1.6.0 Platform Name: nxos PnP Platform: 1.5.0.rc2

```cisco-ios
Switch# show pnp profiles Created by UDI DHCP Discovery PID:N9K-C9504,VID:V01,SN:FOX1813GCZ8
```

Primary transport: https Address: 10.105.194.248 Port: 443 CA file: /etc/pnp/certs/trustpoint/pnplabel

Work-Request Tracking:

Pending-WR: Correlator=

Cisco-PnP-POSIX-nxos-1.6.0-21-589a466a-0d88-427b-a17e-69afb7d0a226-1

Last-WR:

Correlator=

Cisco-PnP-POSIX-nxos-1.6.0-20-ab225de4-b0ef-46c5-9c4f-e3bd9f7c6b87-1

PnP Response Tracking:

Last-PR:

Correlator=

Cisco-PnP-POSIX-nxos-1.6.0-20-ab225de4-b0ef-46c5-9c4f-e3bd9f7c6b87-1

```cisco-ios
Switch# show pnp lease
```

"lease": { "uptime": "Fri Jan 11 05:32:17 2019", "intf": "Vlan1", "ip_addr": "10.77.143.239", "mask": "255.255.255.0", "gw": "10.77.143.1", "domain": "", "opt_43": "5A1D;B2;K4;I10.105.194.248;J80", "lease": "3600", "server": "10.77.143.231", "vrf": "1" }

{

}