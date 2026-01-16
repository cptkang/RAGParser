---
title: "switch(config)# bfd interval 50 min_rx 50 multiplier 3"
page_start: 31
page_end: 31
level: 2
---

## switch(config)# bfd interval 50 min_rx 50 multiplier 3

This command overrides the values you configure for BFD session parameters on individual interfaces.

The intervals mintx and msec range from 50 milliseconds to 999 milliseconds, with a default of 50 milliseconds.

The multiplier ranges from 1 to 50. The default is 3.

- Configure the slow timer used in the echo function using the bfd slow-timer [interval] command.