---
title: "POAP Personality Sample Script"
page_start: 70
page_end: 71
level: 2
---

## POAP Personality Sample Script

the corresponding file with the .md5 extension and is # done by this script itself.

from poap.personality import POAPPersonality import os # Location to download system image files, checksums, etc. download_path = "/var/lib/tftpboot" # The path to the personality tarball used for restoration personality_tarball = "/var/lib/tftpboot/foo.tar" # The protocol to use to download images/config protocol = "scp" # The username to download images, the personality tarball, and the # patches and RPMs during restoration username = "root" # The password for the above username password = "passwd754" # The hostname or IP address of the file server server = "2.1.1.1" # The VRF to use for downloading and restoration vrf = "default" if os.environ.has_key('POAP_VRF'): vrf = os.environ['POAP_VRF'] # Initialize housekeeping stuff (logs, temp dirs, etc.) p = POAPPersonality(download_path, personality_tarball, protocol, username, password, server, vrf) p.get_personality() p.apply_personality() sys.exit(0)

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

54

5

C H A P T E R 5