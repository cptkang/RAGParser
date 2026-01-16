---
title: "Non-SUDI Supported Device as a File Server"
page_start: 46
page_end: 46
level: 2
---

## Non-SUDI Supported Device as a File Server

Figure4:SUDISupportedDeviceasFileServerInfrastructure

용 니 21-50400 ㅁ 01160 (0001194181010 800 매 10『 응아 56706 으 001\8『6 56006 36106 11165) (900 『10 와 100 0110) 10 ^00『685, 응 010 다 16 (0001094『81000 0816\8\ 『16 800 용 00101 56006. 으 01086 800 5000 다 16 1078065 ㅁ 618411 32816\8 504174 띠 6×456 5\\07

The workflow for SUDI supported devices is as follows:

- • Booting device is SUDI capable and has the needed trust store to verify a SUDI certificate

- • Booting device sends out DHCP discover

- • DHCP server responds to booting device with https server details

- • Device establishes the secure channel using standard SSL APIs

- • Authentication is done by verifying SUDI on both sides

- • Downloads poap.py