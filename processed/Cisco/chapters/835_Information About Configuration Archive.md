---
title: "Information About Configuration Archive"
page_start: 175
page_end: 175
level: 2
---

## Information About Configuration Archive

The configuration archive is intended to provide a mechanism to store, organize, and manage an archive of the configuration files to enhance the configuration rollback capability provided by the configure replace command. Before configuration archiving was introduced, you could save copies of the running configuration usingthecopyrunning-configdestination-urlcommand,storingthereplacementfileeitherlocallyorremotely. However, this method lacked any automated file management. The configuration replace and configuration rollback provides the capability to automatically save copies of the running configuration to the configuration archive. These archived files serve as checkpoint configuration references and can be used by the configure replace command to revert to the previous configuration states.

The archive config command allows you to save configurations in the configuration archive using a standard location and filename prefix that is automatically appended with an incremental version number (and optional timestamp) as each consecutive file is saved. This functionality provides a means for consistent identification of saved configuration files. You can specify how many versions of the running configuration are kept in the archive. After the maximum number of files are saved in the archive, the oldest file is automatically deleted when the next, most recent file is saved. The show archive command displays information for all configuration files saved in the configuration archive.

Theconfigurationarchive,whereintheconfigurationfilesarestoredandareavailableforusewiththeconfigure replace command, can be located on the following file systems: bootflash, FTP, and TFTP.

%

- Note

The TFTP and FTP for this feature use VRF management.

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

159

| |