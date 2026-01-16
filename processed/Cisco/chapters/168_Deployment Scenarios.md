---
title: "Deployment Scenarios"
page_start: 45
page_end: 45
level: 2
---

## Deployment Scenarios

Cisco devices have a unique identifier known as the Secure Unique Device Identifier (SUDI). The hardware SUDI can be used for authentication, as it can be used for asymmetric key operations such as encryption, decryption, signing, and verifying that allow passage of the data to be operated upon. All non-Cisco devices are classified as non-SUDI devices. For a non-SUDI device, the root-CA bundle is required to authenticate the file server. However, the file server can be hosted on either a SUDI or a non-SUDI device.

Based on all these capabilities, you can use one of the following deployment scenarios to download the POAP script in a secure way:

- • SUDI Supported Device as File Server

- • Non-SUDI Supported Device as File Server