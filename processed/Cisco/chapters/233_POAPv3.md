---
title: "POAPv3"
page_start: 58
page_end: 59
level: 2
---

## POAPv3

PowerOn Auto Provisioning version 3 (POAPv3) is introduced in Cisco NX-OS Release 9.3(5). With this feature you can install license, RPM, and certificate through POAP.

Perform the following steps to install license or RPM or certificate through POAP.

1. Create a folder on the POAP server with serial number of the box as the name.

2. Create .yaml or .yml file with files to be installed. Make sure the file name is in <serial-number>.yaml or <serial-number>.yml format.

3. Create MD5 checksum for the .yaml or .yml file.

4. Make sure the format of the .yaml file should be similar to the below format:

Version : 1

Target-image : nxos.9.3.4.bin Description : Yaml for box XYZ12345 poap provisioning. N9k Leaf mode box License : [license1.lic, XYZ12345/license2.lic, folder1/license3.lic] RPM :

- - rpm1.rpm

- - patches/reload/rpm2-reload.rpm

- - rpm3.rpm

Certificate : [ssh1.pub, XYZ12345/ssh2key.pub]

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

42

ㅣ

|!