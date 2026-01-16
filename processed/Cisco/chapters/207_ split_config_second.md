---
title: "• split_config_second"
page_start: 52
page_end: 52
level: 2
---

## • split_config_second

Thenametouseforthesecondconfigurationportioniftheconfigurationissplit.Thedefaultispoap_2.cfg.

• timeout_config

The timeout in seconds for copying the configuration file. The default is 120. For non-legacy images, this option is not used, and the POAP process times out. For legacy images, FTP uses this timeout for the login process and not for the copy process, while scp and other protocols use this timeout for the copy process.

- • timeout_copy_system

The timeout in seconds for copying the system image. The default is 2100. For non-legacy images, this option is not used, and the POAP process times out. For legacy images, FTP uses this timeout for the login process and not for the copy process, while scp and other protocols use this timeout for the copy process.