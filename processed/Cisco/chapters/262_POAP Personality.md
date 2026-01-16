---
title: "POAP Personality"
page_start: 66
page_end: 66
level: 2
---

## POAP Personality

The POAP personality feature, which is introduced in Cisco NX-OS Release 7.0(3)I4(1), enables user data, Cisco NX-OS and third-party patches, and configuration files to be backed up and restored. In previous releases, POAP can restore only the configuration.

The POAP personality is defined by tracked files on the switch. The configuration and package list in the

personality file are ASCII files.

Binary versions are recorded in the personalityfile, but the actualbinary files are not included. Becausebinary files are typically large, they are accessed from a specified repository.

The personality file is a .tar file, which would typically be extracted into a temporary folder. Here is an example: