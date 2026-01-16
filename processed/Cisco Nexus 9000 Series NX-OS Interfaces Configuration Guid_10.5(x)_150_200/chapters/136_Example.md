---
title: "Example:"
page_start: 31
page_end: 31
level: 2
---

## Example:

```cisco-ios
switch(config)# bfd slow-timer 2000
```

This value determines how quickly BFD starts a new session. It specifies the rate at which asynchronous sessions send BFD control packets when the echo function is enabled.

The slow-timer value sets the interval for control packets. Echo packets use the configured BFD intervals for link failure detection. Control packets at the slower rate maintain the BFD session.

The range is from 1000 to 30,000 milliseconds. The default is 2000.

- Step 4 Configure the interface used for Bidirectional Forwarding Detection (BFD) echo frames bfd echo-interface loopback interface number