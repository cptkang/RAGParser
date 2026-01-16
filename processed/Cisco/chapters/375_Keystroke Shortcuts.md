---
title: "Keystroke Shortcuts"
page_start: 93
page_end: 93
level: 2
---

## Keystroke Shortcuts

Keystrokes Tab Description Completes the word for you after you enter the first characters of the word and then press the Tab key. All options that match are presented. Use tabs to complete the following items: • Command names • Scheme names in the file system • Server names in the file system • Filenames in the file system Example: switch(config)# xm<Tab> switch(config)# xml<Tab> switch(config)# xml server Example: switch(config)# c<Tab> callhome class-map clock cdp cli control-plane switch(config)# cl<Tab> class-map cli clock switch(config)# cla<Tab> switch(config)# class-map Example: switch# cd bootflash:<Tab> bootflash:/// bootflash://sup-1/ bootflash://sup-active/ bootflash://sup-local/ bootflash://module-27/ bootflash://module-28/ Example: switch# cd bootflash://mo<Tab> bootflash://module-27/ bootflash://module-28/

```cisco-ios
switch# cd bootflash://module-2
```

> **NOTE**
> Note

You cannot access remote machines using the cd command. If you are on slot 27 and enter the cd bootflash://module-28 command, the following message appears: "Changing directory to a non-local server is not allowed."

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

77

| |