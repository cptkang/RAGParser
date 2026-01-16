---
title: "Example:"
page_start: 32
page_end: 32
level: 2
---

## Example:

```cisco-ios
switch(config-if)# bfd interval 50 min_rx 50 multiplier 3
```

Configures the BFD session parameters for all BFD sessions on the device. This command overrides these values by configuring the BFD session parameters on an interface. The mintx and msec range is from 50 to 999 milliseconds and the default is 50. The multiplier range is from 1 to 50. The multiplier default is 3.

Beginning with Cisco NX-OS Release 9.3(5), configuring BFD session parameters under interface with default timer values using the bfd interval 50 min_rx 50 multiplier 3 command is functionally equivalent to no bfd interval command.

Once BFD session parameters under interface are set to default values, those BFD sessions running on that interface will inherit global session parameters, if present.