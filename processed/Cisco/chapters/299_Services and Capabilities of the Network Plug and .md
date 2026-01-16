---
title: "Services and Capabilities of the Network Plug and Play Agent"
page_start: 75
page_end: 75
level: 2
---

## Services and Capabilities of the Network Plug and Play Agent

The PnP agent performs the following tasks:

- • Backoff

• Capability

• CLI execution

• Configuration upgrade

• Device information

• Certificate install

• Image install

- • Redirection

<

- Note The PnP controller or server provides an optional checksum tag to be used in the image installation and configuration upgrade service requests by the PnP agent. When the checksum is provided in a request, the image install process compares the checksum against the current running image checksum.

If the checksums are same, the image being installed or upgraded is the same as the current image running on the device. The image install process will not perform any other operation in this scenario.

If the checksums are not the same, the new image will be copied to the local file system, and the checksum will be calculated again and compared with the checksum provided in the request. If they are the same, the image install process continues to install the new image or upgrade the device to the new image. If the checksums are not the same, the process exits with an error.