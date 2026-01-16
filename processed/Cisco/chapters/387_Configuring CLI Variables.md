---
title: "Configuring CLI Variables"
page_start: 96
page_end: 96
level: 2
---

## Configuring CLI Variables

```cisco-ios
switch# configure terminal switch(config)# radius-server host 10.10.2.2 switch(config)# show radius-server retransmission count:0 timeout value:1 deadtime value:1 total number of servers:1 following RADIUS servers are configured: 10.10.1.1: available for authentication on port:1812 available for accounting on port:1813 10.10.2.2: available for authentication on port:1812 available for accounting on port:1813
switch(config)# no radius-server host 10.10.2.2
switch(config)# show radius-server
```

retransmission count:0

timeout value:1

deadtime value:1

total number of servers:1

following RADIUS servers are configured: 10.10.1.1: available for authentication on port:1812 available for accounting on port:1813

This example shows how to use the no form of a command in EXEC mode:

```cisco-ios
switch# cli var name testinterface ethernet1/2 switch# show cli variables SWITCHNAME="switch" TIMESTAMP="2013-05-12-13.43.13" testinterface="ethernet1/2"
switch# cli no var name testinterface switch# show cli variables SWITCHNAME="switch" TIMESTAMP="2013-05-12-13.43.13"
```