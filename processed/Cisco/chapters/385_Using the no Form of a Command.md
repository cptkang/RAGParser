---
title: "Using the no Form of a Command"
page_start: 95
page_end: 95
level: 2
---

## Using the no Form of a Command

Almost every configuration command has a no form that can be used to disable a feature, revert to a default value, or remove a configuration.

This example shows how to disable a feature:

```cisco-ios
switch# configure terminal switch(config)# feature tacacs+ switch(config)# no feature tacacs+
```

This example shows how to revert to the default value for a feature:

```cisco-ios
switch# configure terminal switch(config)# banner motd #Welcome to the switch# switch(config)# show banner motd Welcome to the switch
switch(config)# no banner motd switch(config)# show banner motd User Access Verification
```

This example shows how to remove the configuration for a feature:

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

79

| |