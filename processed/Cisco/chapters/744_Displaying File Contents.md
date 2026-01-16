---
title: "Displaying File Contents"
page_start: 160
page_end: 160
level: 2
---

## Displaying File Contents

This example shows how to display the contents of a file on an external flash device:

```cisco-ios
switch# show file usb1:test configure terminal interface ethernet 1/1 no shutdown end show interface ethernet 1/1
```

This example shows how to display the contents of a file that resides in the current directory:

```cisco-ios
switch# show file myfile
```