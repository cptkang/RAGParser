---
title: "Using the System-Defined Timestamp Variable"
page_start: 117
page_end: 117
level: 2
---

## Using the System-Defined Timestamp Variable

This example uses $(TIMESTAMP) when redirecting show command output to a file:

```cisco-ios
switch# show running-config > rcfg.$(TIMESTAMP)
```

Preparing to copy....done switch# dir 12667 May 01 12:27:59 2013 rcfg.2013-05-01-12.27.59 Usage for bootflash://sup-local 8192 bytes used 20963328 bytes free 20971520 bytes total