---
title: "Procedure"
page_start: 62
page_end: 62
level: 2
---

## Procedure

Step 1

- Modify the basic configuration script provided by Cisco or create your own script. For information, see the Python Scripting and API Configuration Guide.

- Step 2 Every time you make a change to the configuration script, ensure that you recalculate the MD5 checksum by running # f=poap_nexus_script.py ; cat $f | sed '/^#md5sum/d' > $f.md5 ; sed -i "s/^#md5sum=.*/#md5sum=\"$(md5sum $f.md5 | sed 's/ .*//')\"/" $f using a bash shell. For more information, see the Python API Reference Guide.

Step 3

- (Optional) Put the POAP script and any other desired software image and switch configuration files on a USB device accessible to the switch.

Step 4

- Deploy a DHCP server and configure it with the interface, gateway, and TFTP server IP addresses and a bootfile with the path and name of the configuration script file. (This information is provided to the switch when it first boots.) You do not need to deploy a DHCP server if all software image and switch configuration files are on the USB device.

Step 5

- Deploy a TFTP or HTTP server to host the configuration script. In order to trigger the HTTP request to the server, prefix HTTP:// to the TFTP server name. HTTPS is not supported.

- Add the URL portion into the TFTP script name to show correct path to the file name.

Step 6

- Deploy one or more servers to host the software images and configuration files.