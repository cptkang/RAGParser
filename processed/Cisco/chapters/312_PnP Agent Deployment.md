---
title: "PnP Agent Deployment"
page_start: 77
page_end: 77
level: 2
---

## PnP Agent Deployment

The following steps indicate the PnP agent deployment procedure on Cisco devices:

1. A Cisco device with a PnP agent contacts the PnP server, requesting for a task, that is, the PnP agent sends UDI along with a request for work.

2.

- If the PnP server has a task for the device, for example, image installation, configuration, upgrade, and so on, it sends a work request.

3. After the PnP agent receives the work request, it executes the task and sends back a reply to the PnP server about the task status, that is whether it is successful or if an error has occurred, and the corresponding information that is requested.