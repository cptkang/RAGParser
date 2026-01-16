---
title: "Distributed Operation"
page_start: 22
page_end: 22
level: 2
---

## Distributed Operation

Cisco NX-OS can distributethe BFD operation to compatiblemodules that support BFD. This process offloads the CPU load for BFD packet processing to the individual modules that connect to the BFD neighbors. All BFD session traffic occurs on the module CPU. The module informs the supervisor when a BFD failure is detected.