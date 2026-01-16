---
title: "Sending Command Output in Email"
page_start: 119
page_end: 120
level: 2
---

## Sending Command Output in Email

This example shows how to send the output of the show interface brief command to an email address using

the pipe operator (|):

switch<config># email switch(config-email)# smtp-host 198.51.100.1 smtp-port 25 switch(config-email)# vrf management switch(config-email)# from admin@Mycompany.com switch(config-email)# reply-to admin@Mycompany.com switch(config-email)# exit switch(config)# exit switch# show email SMTP host: 198.51.100.1 SMTP port: 25 Reply to: admin@Mycompany.com From: admin@Mycompany.com VRF: management switch# show interface brief | email subject show-interface admin@Mycompany.com

Email sent

Theemailsenttoadmin@Mycompany.comwiththesubject"show-interface"showstheoutputofthecommand:

<snip>

---------------------------------------------------------------------

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

103

| |

| |