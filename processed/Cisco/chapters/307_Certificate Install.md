---
title: "Certificate Install"
page_start: 76
page_end: 76
level: 2
---

## Certificate Install

Certificate install is a security service through which a PnP server requests the PnP agent on a device for trust pool or trust point certificate installation or uninstallation. This service also specifies the agent about the primaryandbackupserversforreconnection.Thefollowingprerequisitesarerequiredforasuccessfulcertificate installation:

- • The server from which the certificate or trust pool bundle needs to be downloaded should be reachable.

- • There should not be any permission issues to download the certificate or the bundle.

- • The PKI API should be available and accessible for the PnP agent so that the agent could call to download and install the certificate or the bundle.

- • There is enough memory on the device to save the downloaded certificate or bundle.