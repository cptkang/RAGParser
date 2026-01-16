---
title: "POAP Process"
page_start: 54
page_end: 54
level: 2
---

## POAP Process

- • source_file - The name of the file to download. This is a required parameter. Example: agents.tar, script.py, and so on.

- • dest_path - The location to download the file on the switch. Any directories that do not exist earlier will be created. This is an optional parameter. The default is /bootflash.

- • dest_file - The name to give the downloaded file. This is an optional parameter. The default is unchanged source_file.

- • unpack - Indicates whether a tarball exists for unpacking. Unpacking is done with tar -xf tarfile -C /bootflash. This is an optional parameter. The default is False.

- • delete_after_unpack - Indicates whether to delete the downloaded tarball after unpack is successful. There is no effect if unpack is False. The default is False.

Using the download functionality, you can download all the agents and files needed to run POAP. To start the agents, you should have the configuration present in the running configuration downloaded by POAP. Then the agents, scheduler, and cron entry, along with EEM, can be used.