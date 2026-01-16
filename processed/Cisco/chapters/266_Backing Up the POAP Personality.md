---
title: "Backing Up the POAP Personality"
page_start: 67
page_end: 67
level: 2
---

## Backing Up the POAP Personality

You can create a backup of the POAP personality either locally on the switch or remotely on the server. The personality backup taken from the switch should be restored only on a switch of the same model.

%

- Note If you are using the Cisco scheduler feature for backups, you can configure it to also back up the POAP personality, as shown in the following example. For more information on the scheduler, see the Cisco Nexus 9000 Series NX-OS System Management Configuration Guide.

```cisco-ios
switch(config)# scheduler schedule name weeklybkup switch(config-schedule)# time weekly mon:07:00 switch(config-schedule)# job name personalitybkup switch(config-schedule)# exit switch(config)# scheduler job name personalitybkup switch(config-job)# personality backup bootflash:/personality-file ; copy bootflash:/personality-file tftp://10.1.1.1/ vrf management
```