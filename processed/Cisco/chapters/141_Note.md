---
title: "Note"
page_start: 39
page_end: 39
level: 2
---

## Note

If you are executing the setup script after entering a write erase command, you explicitly must change the default zone policy to permit for VSAN 1 after finishing the script using the following command:

```cisco-ios
switch(config)# zone default-zone permit vsan 1
```

- d) Enter yes (no is the default) to enable a full zone set distribution.