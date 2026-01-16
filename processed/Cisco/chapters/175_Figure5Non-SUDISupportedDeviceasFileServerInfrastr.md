---
title: "Figure5:Non-SUDISupportedDeviceasFileServerInfrastructure"
page_start: 47
page_end: 47
level: 2
---

## Figure5:Non-SUDISupportedDeviceasFileServerInfrastructure

660 아 0080 키 00-840 미 -540001160 (0101194『831100 800 마 1002 (00001094160 56000 응아 56006 으 0\08「6 56006 36006 (4056 000194760) 01118) (80010 와 100 0110) 10 600[655, 『 ㅁ 000^ (200119418100 6816\80, | 8640016 아 『116 200 80010 56006, 띠 00-840 미 응 01876 800 58 에 10 다 16 830000「160 1078068 용 00101 56100 1[0618411 3816\8\ 504175 띠 6×48 58\1 아

The workflow for non-SUDI supported devices is as follows:

- • Booting device is SUDI capable and has the needed trust store to verify a SUDI certificate

- • Intermediate device that hosts a server with Root-CA bundle is also SUDI capable

- • Booting device sends out DHCP discover

- • DHCP server responds to booting device with https server details and Root-CA server details

- • Booting device reaches to intermediate device, gets the CA bundle, adds it to the trust store

- • Booting device reaches the file server to download poap.py