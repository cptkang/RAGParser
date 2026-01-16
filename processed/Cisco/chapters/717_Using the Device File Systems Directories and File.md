---
title: "Using the Device File Systems, Directories, and Files"
page_start: 156
page_end: 157
level: 2
---

## Using the Device File Systems, Directories, and Files

sda

8:0

0 119.2G 0 disk

|-sda1 8:1 0 512M 0 part |-sda2 8:2 0 32M 0 part /mnt/plog |-sda3 8:3 0 128M 0 part /mnt/pss |-sda4 8:4 0 114.5G 0 part /isan/vdc_1/virtual-instance/guestshell+/rootfs/bootflash |-sda5 8:5 0 64M 0 part /mnt/cfg/0 |-sda6 8:6 0 64M 0 part /mnt/cfg/1 `-sda7 8:7 0 4G 0 part /logflash target scheme is sda 8:0 0 64G|120GB|250GB 0 disk |-sda1 8:1 0 512M 0 part |-sda2 8:2 0 32M 0 part /mnt/plog |-sda3 8:3 0 128M 0 part /mnt/pss |-sda4 8:4 0 110.5G 0 part /bootflash |-sda5 8:5 0 64M 0 part /mnt/cfg/0 |-sda6 8:6 0 64M 0 part /mnt/cfg/1 |_sda7 8:7 0 8G 0 part /logflash

Continue? (y/n) [n] y

A module reload is required for the resize operation to proceed Please, do not power off the module during this process.

Following is an example for extended resize:

```cisco-ios
switch# system flash sda resize extended
```

!!!! WARNING !!!!

Attempts will be made to preserve drive contents during the resize operation, but risk of data loss does exist. Backing up of bootflash, logflash, and running configuration is recommended prior to proceeding.

!!!! WARNING !!!!

current scheme is sda 8:0 0 119.2G 0 disk |-sda1 8:1 0 512M 0 part |-sda2 8:2 0 32M 0 part /mnt/plog |-sda3 8:3 0 128M 0 part /mnt/pss |-sda4 8:4 0 110.5G 0 part /bootflash |-sda5 8:5 0 64M 0 part /mnt/cfg/0 |-sda6 8:6 0 64M 0 part /mnt/cfg/1 `-sda7 8:7 0 8G 0 part /logflash target scheme is sda 8:0 0 120GB|250GB 0 disk |-sda1 8:1 0 512M 0 part |-sda2 8:2 0 32M 0 part /mnt/plog |-sda3 8:3 0 128M 0 part /mnt/pss |-sda4 8:4 0 rem 0 part /bootflash |-sda5 8:5 0 1.0G 0 part /mnt/cfg/0 |-sda6 8:6 0 1.0G 0 part /mnt/cfg/1 |_sda7 8:7 0 39G 0 part /logflash Continue? (y/n) [n] y A module reload is required for the resize operation to proceed

A module reload is required for the resize operation to proceed Please, do not power off the module during this process.

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

ㅣ

|!