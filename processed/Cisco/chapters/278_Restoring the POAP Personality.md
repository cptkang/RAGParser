---
title: "Restoring the POAP Personality"
page_start: 69
page_end: 69
level: 2
---

## Restoring the POAP Personality

During the POAP script execution phase, the personality module in the script restores the POAP personality, provided that the currently booted switch image is Cisco NX-OS Release 7.0(3)I4(1) or later. If necessary, upgrade the switch to the correct software image.

<

> **NOTE**
> Note

- A personality restore is done with the same software image used for the personality backup. Upgrading to a newer image is not supported through the POAP personality feature. To upgrade to a newer image, use the regular POAP script.

<

> **NOTE**
> Note

- If the personality script fails to execute for any reason (such as not enough space in the bootflash or a script execution failure), the POAP process returns to the DHCP discovery phase.

The restore process performs the following actions:

1. Untars and unzips the personality file in the bootflash.

2. Validates the personality file.

3. Reads the configuration and package list files from the personality file to make a list of the binaries to be downloaded.

4.

- If the current image or patches are not the same as specified in the personality file, downloads the binaries to the bootflash (if not present) and reboots with the correct image and then applies the packages or patches.

5. Unzips or untars the user data files relative to "/".

6. Copies the configuration file in the POAP personality to the startup configuration.

7. Reboots the switch.