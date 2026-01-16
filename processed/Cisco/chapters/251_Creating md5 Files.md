---
title: "Creating md5 Files"
page_start: 63
page_end: 63
level: 2
---

## Creating md5 Files

Every time you make a change to the configuration script, ensure that you recalculate the MD5 checksum by running # f=poap_fabric.py ; cat $f | sed '/^#md5sum/d' > $f.md5 ; sed -i "s/^#md5sum=.*/#md5sum=\"$(md5sum $f.md5 | sed 's/ .*//')\"/" $f using a bash shell.

This procedure replaces md5sum in poap_fabric.py with a new value if there was any change in that file.

<

- Note Steps 1-4 and 7-8 are needed only if you are using the BASH shell. If you have access to any other Linux server, these steps are not required.