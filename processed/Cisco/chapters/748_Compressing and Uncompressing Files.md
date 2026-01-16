---
title: "Compressing and Uncompressing Files"
page_start: 161
page_end: 161
level: 2
---

## Compressing and Uncompressing Files

This example shows how to compress a file:

```cisco-ios
switch# dir 1525859 Jul 04 00:51:03 2013 Samplefile ... switch# gzip volatile:Samplefile switch# dir 266069 Jul 04 00:51:03 2013 Samplefile.gz ...
```

This example shows how to uncompress a compressed file:

```cisco-ios
switch# dir 266069 Jul 04 00:51:03 2013 Samplefile.gz ... switch# gunzip samplefile switch# dir 1525859 Jul 04 00:51:03 2013 Samplefile
```

...