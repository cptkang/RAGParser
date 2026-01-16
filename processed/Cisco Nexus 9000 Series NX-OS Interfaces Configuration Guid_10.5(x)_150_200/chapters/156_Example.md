---
title: "Example:"
page_start: 33
page_end: 33
level: 2
---

## Example:

```cisco-ios
switch(config-if)# bfd authentication keyed-sha1 keyid 1 ascii_key cisco123
```

(Optional) Configures SHA-1 authentication for all BFD sessions on the interface. The ascii_key string is a secret key shared among BFD peers. The id value, a number between 0 and 255, is assigned to this particular ascii_key . BFD packets specify the key by id , allowing the use of multiple active keys.

To disable SHA-1 authentication on the interface, use the no form of the command.

- Step 5 Use the bfd authentication interop command to configure BFD authentication interoperability between Nexus and non-Nexus platforms.