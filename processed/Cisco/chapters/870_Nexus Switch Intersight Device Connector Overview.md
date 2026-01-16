---
title: "Nexus Switch Intersight Device Connector Overview"
page_start: 183
page_end: 183
level: 2
---

## Nexus Switch Intersight Device Connector Overview

Devices are connected to the Cisco Intersight portal through a Nexus Switch Intersight Device Connector (NXDC) that is embedded in the Cisco NX-OS image of each system.

Beginning with Cisco NX-OS Release 10.2(3)F, the Device Connector on NX-OS feature is supported which provides a secure way for the connected devices to send information and receive control instructions from the Cisco Intersight portal, using a secure Internet connection.

The NXDC is enabled by default on all Cisco Nexus series switches and it starts at boot by default, and attemptstoconnecttothecloudservice.Onceasecureconnectionhasbeenestablishedandthedeviceconnector is registered with the Intersight service, the device connector collects detailed inventory, health status and sends the adoption telemetry data to the Intersight database. Inventory is refreshed once in a day.

The NXDC supports the AutoUpdate feature where it gets automatically updated to the latest version through a refresh by the Intersight service when you connect to Intersight.

TheNXDCalsosupports theConnectedTAC featureto collecttech-supportdatafrom devicesthatareclaimed.

The NXDC feature integration was done to resolve the standalone Nexus switches with the following

capabilities:

- • It provides fast and quick solution to gather basic data from standalone Nexus switches.

- • It stores and manages private data securely in the cloud.

- • It is flexible for future capabilities and enables the ability to upgrade NXDC.

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

167