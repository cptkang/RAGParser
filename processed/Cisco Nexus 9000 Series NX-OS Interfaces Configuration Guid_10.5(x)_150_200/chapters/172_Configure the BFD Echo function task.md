---
title: "Configure the BFD Echo function (task)"
page_start: 35
page_end: 35
level: 2
---

## Configure the BFD Echo function (task)

You can configure the BFD echo function on one or both ends of a BFD-monitored link. The echo function slows down the required minimum receive interval, based on the configured slow timer. The RequiredMinEchoRx BFD session parameter remains nonzero if you disable the echo function to comply with RFC 5880 When you enable the echo function, the slow timer value becomes the required minimum receive interval.