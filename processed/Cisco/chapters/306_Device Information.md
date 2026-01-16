---
title: "Device Information"
page_start: 76
page_end: 76
level: 2
---

## Device Information

The PnP agent provides the capability to extract device inventory and other important information to the PnP server on request. The following device-profile request types are supported:

- • all—Returns complete inventory information, which includes unique device identifier (UDI), image, hardware, and file system inventory data.

- • filesystem—Returns file system inventory information, which includes file system name and type, local size (in bytes), free size (in bytes), read flag, and write flag.

- • hardware—Returns hardware inventory information, which includes hostname, vendor string, platform name, processor type, hardware revision, main memory size, I/O memory size, board ID, board rework ID, processor revision, mid-plane revision, and location.

- • image—Returnsimage inventory information, which includes version string, image name, boot variable, return to ROMMON reason, bootloader variable, configuration register, configuration register on next boot, and configuration variables.

• UDI—Returns the device UDI.