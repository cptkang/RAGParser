---
title: "SUMMARY STEPS"
page_start: 4
page_end: 4
level: 2
---

## SUMMARY STEPS

1. configure terminal

2.

ip access-list list-name

3.

permit tcp host ipaddr host ipaddr eq port-number

4. exit

5.

route-map route-map-name

6. match ip address access-list-name

7.

set ip next-hop addr1

8. exit

9.

interface vlan vlan-id

10.

- ip address ip-addr

11.

- no ip redirects

12.

(Optional) ip policy route-map pbr-sample

13. exit

14. hsrp version 2

15. hsrpgroup-num

16. name name-val

17. ip ip-addr

18. no shutdown