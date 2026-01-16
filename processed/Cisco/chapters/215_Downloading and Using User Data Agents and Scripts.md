---
title: "Downloading and Using User Data, Agents, and Scripts as part of POAP"
page_start: 53
page_end: 53
level: 2
---

## Downloading and Using User Data, Agents, and Scripts as part of POAP

Under the options dictionary, you can find the download_scripts_and_agents function. If you choose to downloaduserscriptsanddata,uncommentthefirstpoap_loglineandthenuseaseriesofdownload_user_app function calls to download each application. Since older Cisco NX-OS versions do not support recursive copy of directories, such directories must be put into a tarball (TAR archive) and then unpacked once on the switch. The parameters for the download_scripts_and_agents function are as follows:

- • source_path - The path to where the file or tarball is located. This is a required parameter. Example: /var/lib/tftpboot.

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

37

| |