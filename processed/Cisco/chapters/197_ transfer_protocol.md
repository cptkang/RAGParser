---
title: "• transfer_protocol"
page_start: 51
page_end: 51
level: 2
---

## • transfer_protocol

Any transfer protocol such as http, https, ftp, scp, sftp, or tftp that is supported by VSH. The default is scp.

- • config_path

The path to the configuration file on the server. Example: /tftpboot. The default is /var/lib/tftpboot.

- • target_system_image

The name of the image to download from the remote server. This is the image you get after POAP completes. This option is a required parameter for every mode except personality. The default is "".

- • target_image_path

The path to the image on the server. Example: /tftpboot. The default is /var/lib/tftpboot.