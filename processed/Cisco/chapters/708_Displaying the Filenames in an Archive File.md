---
title: "Displaying the Filenames in an Archive File"
page_start: 154
page_end: 155
level: 2
---

## Displaying the Filenames in an Archive File

You can display the names of the files in an archive files using the tar list command.

tar list {bootflash: | volatile:}archive-filename

The archive filename is not case sensitive.

```cisco-ios
switch# tar list bootflash:config-archive.tar.gz config-file new-config
```

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

138

ㅣ

|!