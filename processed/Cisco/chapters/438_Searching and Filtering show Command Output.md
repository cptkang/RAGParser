---
title: "Searching and Filtering show Command Output"
page_start: 105
page_end: 105
level: 2
---

## Searching and Filtering show Command Output

Often,theoutputfromshowcommandscanbelengthyandcumbersome.TheCiscoNX-OSsoftwareprovides the means to search and filter the output so that you can easily locate information. The searching and filtering options follow a pipe character (|) at the end of the show command. You can display the options using the CLI context-sensitive help facility:

```cisco-ios
switch# show running-config | ?
```

cut Print selected parts of lines. diff Show difference between current and previous invocation (creates temp files: remove them with 'diff-clean' command and don't use it on commands with big outputs, like 'show tech'!) egrep Egrep - print lines matching a pattern grep Grep - print lines matching a pattern head Display first lines

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

89

| |