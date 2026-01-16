## Configuring Layer 3 Interfaces

| |

## Configuring a Static MAC Address on a Layer 3 Interface

## Example

This example shows how to create a VLAN interface:

```cisco-ios
switch# configure terminal switch(config)# feature interface-vlan switch(config)# interface vlan 10 switch(config-if)# ip address 192.0.2.1/8 switch(config-if)# copy running-config startup-config
```

## Configuring a Static MAC Address on a Layer 3 Interface

You can configure static MAC addresses on Layer 3 interfaces. You cannot configure broadcast or multicast addresses as static MAC addresses.

You cannot configure static MAC addresses on tunnel interfaces.

- Note

> **NOTE**
> Note

- Thisconfigurationis limitedto 16 VLAN interfaces.Applyingtheconfigurationto additionalVLAN interfaces results in a down state for the interface with a Hardware prog failed. status.

## SUMMARY STEPS

1. config t

- interface [ethernet slot/port | ethernet slot/port.number | port-channel number | vlan vlan-id]

3. mac-address mac-address

4. exit

5. (Optional) show interface [ethernet slot/port | ethernet slot/port.number | port-channel number | vlan vlan-id]

6.

(Optional) copy running-config startup-config

## DETAILED STEPS

Procedure

|  | 600007800 0726000 | 『00 ㅁ 056 |
|---|---|---|
| 51601 | 00008 60801016: 8 듀 1 느 00# 06216 느 으 1606 (6020 조 10) 부 | 뜨 26606 60011841780070 00006. |
| 5160 2 | 10606 다 206 [004010065/07422077 | 00167006[ 57072077.7707706/' | ㅁ 00 타 -002070 이 72207206/7| 위 82 17077-22| 6801016: | | 50601165 0416 1.8767 3 10(60806 800 601679 016 10660806 0600118418000 00006. 미 06 |

|

|

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

128

ㅣ

|!

## Configuring Layer 3 Interfaces

## Configuring a Loopback Interface

|  | 600001800 0726000 | 『00 ㅁ 056 |
|---|---|---|
|  | 81600 (602 ㅁ 죄 19) 10 ㄴ 6252206 66065206 | 포 040049667686(604161.8767 3 10160306 661076 704 080 89518 46 66666 4: 3007685. |
| 5160 3 | 2080-8001[6@95 77200-0007656 6801016: 81600 (06005,10-17)\ ㅠ ㅁ 320-300 ㅁ 655 요다 (60208,106-1 조 ) 부 | 306011160 8 96800 541 ㅅ () 3007666 10 8300 10 0416 18567 3 10660806. |
| 5160 4 | @[ 6801016: 으 뒤 프 00 (6020 조 196-1 조 ) 퓨 611 으 1606 (6020 조 10) 부 | 트 찌 (9 0416 104160306 22006. |
| 5160 5 | (0000081) 5060\10660206 [001000606.5/707.27077 5/072077.72707706/ ㆍ | 200 타 -006800 이 77207706/'| 6801016: 8 뒤 1600# 61668 10 ㄴ 65206 666206 | 1219218575 101010080070 80041 016 1.8567 3 10660806. |
| 5160 6 | (0000081) 602057000108-000108 564060410-6070118 6801016: 38 뒤 160150# 60209 12400109- ㅇ 012 ㅁ 619 8 ㄴ 2 | (200166 0416 210010 용 00011841780070 (0 016 618002 060011841800270. |

## Example

This example shows how to configure the Layer 3 interface on slot 7, port 3 with a static MAC address:

```cisco-ios
switch# config t switch(config)# interface ethernet 7/3 switch(config-if)# mac-address 22ab.47dd.ff89 switch(config-if)#
```

## Configuring a Loopback Interface

You can configure a loopback interface to create a virtual interface that is always up.

## Before you begin

Ensure that the IP address of the loopback interface is unique across all routers on the network.

## SUMMARY STEPS

1. configure terminal

2.

interface loopback instance

3.

[ip address ip-address/length | ipv6 address ipv6-address/length]

4. show interface loopback instance

5. copy running-config startup-config

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

|

|

129

| |

## Configuring Layer 3 Interfaces

| |

## Configuring PBR on SVI on the Gateway

## DETAILED STEPS

## Procedure

| 51601 | 000847@ 6(60001021 60801016: 3016010# 007 ㅁ 5*1094 ㅠ 6 ㄴ 62 ㅋ 0 ㅁ 17 ㅁ 21 으 1606 (6020 조 10) 부 | 뜨 26606 60011841780070 00006. |
|---|---|---|
| 5160 2 | 1066 다 200100002067779707206 60801016: 31605 (0002?10) + 106622206 10058520 요다 (60208,106-1 조 ) 부 | (2768666 81007260806 10160406. 1116 78086 16 12020 0 10 1023. |
| 5160 3 | 112 8001@55 777-0007655/76787/2 | 106 400655 22226-0007655/760787/1] 60801016: 38016050 (600219-12) 16 2002655 192.0.2.1/8 | *(00011841766 80 102 3007669 107 04116 10160806. 566 016 (21900 께 6348 9000 56068 찌 -(08 0016891 《0400 음 2001184780070 (604106 107 00076 1010072180070 80041 12 800169969. |
| 『 래 80106: 941606 (000519-16)* 10696 200 ㄷ 066 2001:0088::11/8 | *(00011841766 80 1276 8007696 107 0119 146(6 다 806. 566 046 (21900 페 6048 9000 86068 폐 -08 0010689[ 0410120 음 (260684180020 (04104610710407610[007081100 86041 1076 800169969. |
| 5160 4 | 9410\ 101600140601001010801677757077060 60801016: 31605 (0050219-1<) + 5860 10 ㄴ 66=2206 1005520 | (060060081) 1219201876 016 100700806 10160806 5180160108. |
| 5160 5 | 6003 7000108-60018 56『060040-607018 60801016: 31606 (0020219-12) 후 0029 029402 ㅁ 1 ㅁ 9- ㅇ ㅇ ㅁ 8 ㅎ ㄴ 2 ㄴ ㄴ ㄷ ㅁ 6-0 ㅇ 02 ㅁ 5219 | (06000081) 58768 0416 0001184780070 0118086. |

## Example

This example shows how to create a loopback interface:

```cisco-ios
switch# configure terminal switch(config)# interface loopback 0 switch(config-if)# ip address 192.0.2.1/8 switch(config-if)# copy running-config startup-config
```

## Configuring PBR on SVI on the Gateway

This procedure configures PBR on the primary SVI interface in the gateway.

|

|

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

130

ㅣ

|!

## Configuring Layer 3 Interfaces

## Configuring PBR on SVI on the Gateway

<

- Note Steps 2 through 6 are needed if you want to configure a PBR policy on the unnumbered Primary/Secondary VLAN interfaces. This is not mandatory for IP unnumbered on the SVI feature.

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

## DETAILED STEPS

Procedure

| 51601 | <001841@ 6(60001021 | 26@6 일 00861 000118478000 00006. |
|---|---|---|
| 6068000016: 3 뒤 16015 ㅇ 00222191406 ㅅ ㄴ 6 ㅇ 01221 |
| 5160 2 | 10 800699-115[ 7797-7207760 608001016: 31606 (00019) * 16 2006565-1156 ㄴ ㅁ 56 ㄴ -520616 | (200118476 800689 1196. |
|  | 608001016: 31606 (00201 ㅁ 19-8601) * 26201 ㄴ ㅇ ㅁ 5 2056 10 .1 . 1 . 1 ㅁ 05 티 192.168.2.1 60 80 |  |

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

|

|

131

| |

## Configuring Layer 3 Interfaces

| |

## Configuring PBR on SVI on the Gateway

|  | 600001800 0746000 | 『00 ㅁ 056 |
|---|---|---|
| 5660 4 | 6 608001016: 을 디프 (602012190-2601 ) # @ 흐 는 | 1 000118478000 20006. |
| 5160 5 | 101466-02080 7070/6-77072-770770 608001016: 31606 (000119) * 00466- ㅁ 225 ㅁ 565-520016@ | (206866 8 70416-2082 07 60167 70416-00820 000000800 0006. |
| 5160 6 | 08604 120 400669 0400699-779/-7707776 608001016: 8 듀 1600 (000119- ㄴ 0 ㅁ 466-0 ㅁ 260) * 02058 16 2002=6566 ㅁ 256=-5206016@ | 16601 81066 17010 016 70410128 18616. |
| 5160 7 | 56610 00000 40077 608001016: 81606 (002 ㅁ 1219- ㄴ 00466- 때 20) 56 128 ㅁ 6 ㄴ - ㅁ 2052 192.168.1.1 | 366 12 43007669 01 0446 06 1102. |
| 5160 8 | 6 608001016: 을 데프 20 (0020119- ㄴ 0 ㅇ ㅁ 466- 따 26) # @ 페 흐 는 | 811 000000800 20006. |
| 5660 9 | 1066 타 26@ 이 80 127077-70' 606801016: 30100 (0001710) * 170 ㅁ 66 ㅋ 22206 ㅠ 132 ㅁ 2003 | (2768668 8 스지 14660406 800 60666 10160806 0001184178000 00006. 11167808 ㅇ 616 10000 1 800 4094.11118 16 1466 0000807 투 트 스 피 . |
| 5160 10 | 10 8001@65 7772-0007" 608001016: 3841600 (0002190-12)* 16 8002=655 10.0.0.1/8 | 20011847068 80 102 3007669 107 0416 101601806. |
| 5160 11 | 20 10 1060166065 608001016: 으 데프 (0001219-12) ㅁ ㅇ 0 16 ㅋ 601260 ㄴ 5 | 떼 6608 (0 66 0001184760 070 811 40040066760 00008 800 560000817 스티 146(6 다 3069. |
| 5160 12 | (06000081)10 20116 70141(6-02280 20-5802016 608001016: 31600 (000219- ㄱ 12) 12 ㅁ 20110 ㄴ 0466-0 ㅁ 258 ㅁ =565-52021 히 | 0167 0116 600001800 11 704 \80[10 80217 8 28 ㅁ 01167 02 14466 40040066760 200028777960000817 스티 10(6 다 306. |
| 5660 13 | 6 608001016: | 1 000001800 00006. |

Step 14

hsrp version 2

Set the HSRP version.

Example:

```cisco-ios
switch(config-if)# hsrp version 2
```

|

|

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

132

ㅣ

|!

## Configuring Layer 3 Interfaces

## Configuring IP Unnumbered on SVI Secondary VLAN on the Gateway

|  | 600001800 0746000 |  | 『400056 |
|---|---|---|---|
| 5160 15 | 190870102-77700772 6068000016: 으 데프 (0001219-12) 유 66268 | 200 | 366 06 1682 60000 2 ㅁ 40206 |
| 5160 16 | 28106 7207770-707 6068000016: 을 데프 20 (00201219-1 노 -695206) 구 | 22006 꾼 느 13026 우 | 200118476 016 7260000800 2 ㅁ 8026 50040. |
| 5160 17 | 102 22-000/ 608001016: 8 데 프 006 (0001219-1-6620) 우 16 | 10.0.0.100 | 2001184768 80 102 3007689. |
| 5160 18 | 20 9414100\77 ㅁ 608001016: 으 뒤 프 00 (00201219-1,-16820) 퓨 프 | 5 프 ㅁ 680 되 드 | 띠 688668 9114[001\0. |

## Configuring IP Unnumbered on SVI Secondary VLAN on the Gateway

This procedure configures IP unnumbered on the secondary SVI in the gateway. Beginning Cisco NX-OS Release 9.3(6), this feature is supported on Cisco Nexus N9K-C9316D-GX, N9K-C93600CD-GX, N9K-C9364C-GX switches.

## SUMMARY STEPS

1. configure terminal

2.

0

interface vlan vlan-list

3.

ip unnumbered vlan primary-vlan-id

4.

(Optional) ip policy route-map pbr-sample

5.

no ip redirects

5. 7010 10601606065

6.

hsrp version 2

6. 1910 ㅋ 5605910 ㅁ 2

7.

hsrp group-num

- 7 190 870102-722077

8.

follow name

8. 1010\7290776

9.

ip ip-addr

9. 10 22000

10. no shutdown

## DETAILED STEPS

Procedure

|  | 600001800 0746000 | 『400056 |
|---|---|---|
| 51601 | <00108466 (60001021 | 0167 000118418000 00006. |
| 608001016: |  |
| ㅇ 00222191406 ㅅ ㄴ 6 ㅇ 01221 |  |

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

|

|

133

| |

## Configuring Layer 3 Interfaces

| |

## Configuring SVI TCAM Region

| 5660 2 | 1066 타 26@ 디 80 17077-7797 터 3 바 미란 미하 81600 (0001710) * 170 ㅁ 6682206 ㅠ | 132 ㅁ 2001 | (2768668 8 스지 14660406 800 60666 10160806 06001184178000 00006. 1116 70086 19 10000 1 10 4094. 11119 15 446 6600008027 스페. |
|---|---|---|---|
| 5160 3 | 10 4004400106660 뀌 841 608001016: 도 (0001190-12) 16 | 7277772077-2077-20 140040066 ㅋ 60 ㅠ 120 ㅁ 2003 | 0860166 102 000065910 응 00 80 10[60406 \101041 896182010 음 80 6%01101[ 10 4007696 (0 80 106(60806. |
| 5160 4 | (00000861)10 ㅁ ㅁ 20116 『701416-02020 608001016: 31600 (000219- ㄱ 12) 12 ㅁ 20110 | 20605800016@ ㄴ 0466-0 ㅁ 258 ㅁ =565-52021 히 | 0167 0116 6000018600 11 704 \80[10 30217 8 23 보 ㅁ 01105 01 14466 40040066760 200028777960000817 스티 10(6 다 306. |
| 5160 5 | 20 10 16010601[9 608001016: 으 데프 (0001219-12) ㅁ ㅇ 0 16 ㅋ | 601260 ㄴ 5 | 떼 6608 (0 66 0001184760 070 811 40040066760 00008 800 560000817 스티 146(6 다 3069. |
| 5660 6 | 16910 ㅋ 605100 2 608001016: 으 데프 (0001219-12) 쿠 626 | 7625310 ㅁ 그 | 566 016 브 60 7676107. |
| 5160 7 | 190 870102-722077 608001016: 으 데프 (0001219-12) 유 66268 200 |  | 366 06 1682 60000 2 ㅁ 40206 |
| 5160 8 | 10110\ 7207776 608001016: 을 데 프 020 (0001219-1-6326) 구 소 | 01210 ㅁ 81026 고 7 | (200118476 016 00472 10 66 10110\60. |
| 5160 9 | 102 22-000/ 608001016: 8 데 프 006 (0001219-1-6620) 우 16 | 10.0.0.100 | 브 2(666 85 1274 300 6669 0416 10481 10 3007688. |
| 5160 10 | 20 9414100\77 ㅁ 608001016: |  | 띠 68866 9144600\2. |

Enter this command if you want to apply a PBR policy on

## Configuring SVI TCAM Region

Beginning Cisco NX-OS Release 9.3(3), you can display Layer 3 statistics on SVI interfaces on Cisco Nexus 3100 Series switches. You can change the size of the SVI ternary content addressable memory (TCAM) regions in the hardware to display the Layer 3 incoming unicast counters on SVI interfaces.

|

|

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

134

ㅣ

|!

## Configuring Layer 3 Interfaces

## Configuring SVI TCAM Region

## SUMMARY STEPS

1. hardware profile tcam region {arpacl | e-racl} | ifacl | nat | qos} |qoslbl | racl} | vacl | svi } tcam_size

2. copy running-config startup-config

3. switch(config)# show hardware profile tcam region

4. switch(config)# reload

## DETAILED STEPS

Procedure

|  | 600001800 0726000 | 『00 ㅁ 056 |
|---|---|---|
| 80 1 | 13200\2466010116 (0000 706810 ㅁ {18008 이 | 6-00 이 | | 4201 | | 80866 076 스 (1. 1(: ㅅ 51 768100 5126. |
|  | 7286 405} |409101 | 다이) | 져 이 | 5 다 | 70077 59220 | ㆍ 8008 이 --(:001184766 416 9126 01 0416 ㅅ 007669 《660141107 브 010001( ㅅ 02) 40@1.( ㅅ 0401.) 1(' ㅅ 51 7268107 ㅁ . |
|  |  | *@-8 이 --(1001184166 416 5126 01 0416 687668 스페 ^(21. (6 토 41.) 16501 7268107. |
|  |  | *16801--(10011841768 0416 6126 01 416 104160806 (」1. (11801) 고 7681070. 1116 0186%101410 0 ㅁ 40066 01 600168 16 1500. |
|  |  | * ㆍ 7 ㅁ 86--('02011841766 0416 5126 01 016 페 스 1 (11 768107. |
|  |  | (005) 151 7681072. * ㆍ 009101-(1001184166 416 5126 01426 (005 Ｌ81601 (0405101) |
|  |  | 4541 768102. |
|  |  | ㆍ 『8 이 --(:001184768 0416 59126 01 0416 704166 (11 ( 쿄 ㅅ (1.) 4541 768102. |
|  |  | *8 여 --()001184766 0416 5126 01016 스지 (11. ( 누 4(21.) 4541 768102. |
|  |  | * ㆍ 70077 5720--1(( ㅅ 101 9126. 1116 20086 16 12010 0 10 2.14.74, 83, 647 600168. 띠 066 |
|  |  | 8301 300 @-58 이 (151 7681005 910410 66 566 (0 016 58006 9126. |

Step 1

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

|

|

135

| |

## Configuring Layer 3 Interfaces

| |

## Assigning an Interface to a VRF

:

| 5160 2 | 6003 7000108-60018 56『060040-607018 60801016: 81600 (0072219) 00072 120001 | 00- ㅇ 0252 1 의 | 옹 3 ㅋ 69 016 01806 266916660117 041004811 70[00065 300 7696829 167 00205008 016 0100108 0001184780070 60 0416 51804 > 0005008 8 법 버 060011841800270. |
|---|---|---|---|
| 51660 3 | 8\1101(0020118)# 900\ 12800\216 60801016: 31606 (607 ㅁ 210) 5560 1022200226 | 『7081070 ㅁ 16910 ㅇ 피 | 1219018579 416 1(: ㅅ 51 91209 016[(\11166 83021168016 02 ㅁ 01606 161080 01 0416 5\1604. |
| 51660 4 | 98\101(0020118)# 01080 60801016: |  | (200166 0416 210010 용 00011841780070 (0 016 618002 060011841800270. |
| 81600 (600,10)# 26108 |  | 띠 066 7116706\91261810466 876 0[601146 0017 4000 016 ㅁ 6※[761080 31667 58108 016 0003 7007010 용 -6071 응 (60 56400410-607108. |

Step 2

Step 3

Step 4

## Example

The following example shows how to change the size of the SVI TCAM region:

```cisco-ios
switch(config)# hardware profile tcam region svi 256 [SUCCESS] New tcam size will be applicable only at boot time. You need to 'copy run start' and 'reload'
switch(config)# copy running-config startup-config switch(config)# reload WARNING: This command will reboot the system Do you want to continue? (y/n) [n] y
```

## Assigning an Interface to a VRF

You can add a Layer 3 interface to a VRF.

## SUMMARY STEPS

1. configure terminal

인순 88

interface interface-type number

3. vrf member vrf-name

ip address ip-prefix/length

5. show vrf [vrf-name] interface interface-type number

6. copy running-config startup-config

|

|

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

136

ㅣ

|!

## Configuring Layer 3 Interfaces

## Configuring a DHCP Client on an Interface

## DETAILED STEPS

Procedure

|  | 600001800 0726000 | 『00 ㅁ 056 |
|---|---|---|
| 51601 | 000841@ 6(60001021 6801016: 3016010# 007 ㅁ 5*1094 ㅠ 6 ㄴ 62 ㅋ 0 ㅁ 17 ㅁ 21 으 1606 (6020 조 10) 부 | 뜨 26606 60011841780070 00006. |
| 5160 2 | 1066 타 206 77770/77000-777276 77207700/" 6801016: 31605 (0002?10) + 106622206 10058520 요다 (60208,106-1 조 ) 부 | 느 26(606 10[60406 000118418000 00006. |
| 5160 3 | 끼 다 22460201060 177-770776 6801016: 81600 (0600216-12) 부 2 2760066 ㅋ 프 2 | 스 008 0116 1016 다 306 10 8 키사 |
| 5160 4 | 10 8001@59 777-72767206/767787/ 6801016: 38916050 (6002196-12) 16 2002655 192.0.2.1/16 | (2001184168 80 10 4007699 107 0116 10416 다 306. 04 00481 00: 14019 6662 81667 704 895180 0119 10160806 10 8 다. |
| 5160 5 | 9110\ 지터 |177-7/70770] 106001200 7777077000-77270 6801016: 31605 (60202,19-17122) ㅋ 95606 752 포 ㅁ ㄴ 665205156 100585620 0 | (06060081) 121921855 카자) 14100208007. |
| 5160 6 | 6003 7000108-60018 56『060040-607018 6801016: 31606 (0020219-12) 후 0029 029402 ㅁ 1 ㅁ 9- 8 ㅎ ㄴ 2 ㄴ ㄴ ㄷ ㅁ 6-0 ㅇ 02 ㅁ 5219 | (06000081) 58768 0416 0001184780070 0118086. |

## Example

This example shows how to add a Layer 3 interface to the VRF:

```cisco-ios
switch# configure terminal switch(config)# interface loopback 0 switch(config-if)# vrf member RemoteOfficeVRF switch(config-if)# ip address 209.0.2.1/16 switch(config-if)# copy running-config startup-config
```

## Configuring a DHCP Client on an Interface

You can configure the DHCP client on an SVI, a management interface, or a physical Ethernet interface for

IPv4 or IPv6 address

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

|

|

137

| |

## Configuring Layer 3 Interfaces

| |

## Configuring a DHCP Client on an Interface

## SUMMARY STEPS

- switch# configure terminal

2. switch(config)# interface ethernet type slot/port | mgmt mgmt-interface-number | vlan vlan id

3. switch(config-if)# [no] ipv6 address use-link-local-only

4. switch(config-if)# [no] [ip | ipv6] address dhcp

- (Optional) switch(config)# copy running-config startup-config

## DETAILED STEPS

Procedure

| 51601 | 98\1101#2 600108466 (60001021 | 트 마 666 인 06861 00011841780070 20006. |
|---|---|---|
| 5160 2 | 9\1101(6020118)# 1066 타 400 0010006[ 71776 5/072077 | 2 ㅁ 48006 7787777-77270/7006-2207706/' | 위 80 17072 72 | | (768166 8 211761081 01620 10160306, 8 22808 용 60260 106600806, 07 8 "스티 1016 다 306. 7116 70086 01 7077 7016 ㅁ 0100 1 10 4094. |
| 5160 3 | 98\101(0020118-1)# [ ㅁ 0] 106 4007655 456-110416-10021-07015 | | 206108766 107 760466[10 016 1011(12 66006 ㄷ 띠 066 71119 000000800 19 02017 7260412760 107 80 10276 80017688. |
| 5160 4 | 8\1604(0020118-14)# [00] |142× ㅠ | 126] 40017055 0800 | 복 604666 0416 1011('2 66006 107 80 1074 07 10276 8007688. 7116.00 10070 01 04116 000001800 76000 ㅠ 65 80 8001685 0181 \89 80041260. |
| 5160 5 | (0000081) 5\0101(0020118)# 0005 70400108-000108 56306000-000118 | 옹 3 ㅋ 66 016 이 18086 26691666010157 041204811 76000065 3040 169181 1697 0025108 016 20100108 60001184780070 (0 016 6180002 060011841800270. |

Saves the change persistently through reboots and restarts

## Example

This example shows how to configure the IP address of a DHCP client on an SVI:

```cisco-ios
switch# configure terminal switch(config)# interface vlan 15 switch(config-if)# ip address dhcp
```

This example shows how to configure an IPv6 address of a DHCP client on a management interface:

```cisco-ios
switch# configure terminal switch(config)# interface mgmt 0 switch(config-if)# ipv6 address use-link-local-only switch(config-if)# ipv6 address dhcp
```

|

|

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

138

ㅣ

|!

## Configuring Layer 3 Interfaces

## Configuring SVI and Subinterface Ingress/Egress Unicast Counters

## Configuring SVI and Subinterface Ingress/Egress Unicast Counters

Beginning Cisco NX-OS Release 9.3(3), SVI and subinterface unicast counters are supported on Cisco Nexus 9300-EX, 9300-FX/FX2 switches; and Cisco Nexus 9500 series switches with X9700-EX and X9700-FX line cards.

Beginning Cisco NX-OS Release 9.3(5), SVI and subinterface unicast counters are supported on Cisco Nexus N9K-C9316D-GX, N9K-C93600CD-GX, N9K-C9364C-GX switches.

Beginning Cisco NX-OS Release 10.5(2)F, if the hardware profile svi-and-si flex stats enable flex-stats command is enabled, SVI statistics rate is supported on Cisco Nexus 9300-FX, FX2, FX3, GX, GX2, H2R, H1 Series ToR switches and 9500 Series EoR switches with 9700-EX, FX, FX3, and GX line cards.

<

> **NOTE**
> Note

- • Enabling this feature disables VXLAN, MPLS, Tunnel, Multicast, and ERSPAN counters. Reload the switch for the changes to take effect.

- • For a vPC setup, the peer-gateway feature must be enabled under the vpc domain on both vPC peers. Otherwise, SVI counters may be inconsistent.

- • Multicast counters are not supported.

- • In EOR switches, the statistics rate is supported only for ports in the first ASIC (ASIC 0). If ingress or egress ports are in a different ASIC other than the first ASIC, then the statistics rate is not supported.

To configure SVI and subinterface ingress and/or egress unicast counters on a device, follow these steps:

## SUMMARY STEPS

1. configure terminal

2.

[no] hardware profile svi-and-si flex-stats-enable

3. copy running-config startup-config

4. reload

## DETAILED STEPS

Procedure

|  | 600001800 0726000 | 『00 ㅁ 056 |
|---|---|---|
| 51601 | 000841@ 6(60001021 6801016: 3016010# 007 ㅁ 5*1094 ㅠ 6 ㄴ 62 ㅋ 0 ㅁ 17 ㅁ 21 으 1606 (6020 조 10) 부 | 트 마 666 인 06861 00011841780070 20006. |
| 5160 2 | 1200] 6200\216 01016 51-800-51 116※-56365-6021016@ | (2001184169 016 1081699/680666 4010689[ 60040[605 00 51 300 9461016 다 306. |
| 6801016: 53\016056 (0002?10) + 6220\226 ㅁ ㄴ ㅇ *116 5 ㅠ 1-27 ㅁ 0-5 흐 ?16×-5 ㄴ 2 ㄴ 5 ㅎ -67 ㅁ 25616 요다 (60208,106-1 조 ) 부 | 띠 066 도 004.204666586 016 6001184086000 800 761080 0416 5\110611 10 ㅠ 4019 600004800 10 \04(. |

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

|

|

139

| |

## Configuring Layer 3 Interfaces

| |

## Configuring Subinterface Multicast and Broadcast Counters

|  | 600007800 0726000 |  | 『00 ㅁ 056 |
|---|---|---|---|
| 5160 3 | 6003 7000108-60018 60801016: 31606 (0020219-12) 후 0029 8 ㅎ ㄴ 2 ㄴ ㄴ ㄷ ㅁ 6-0 ㅇ 02 ㅁ 5219 | 56『060040-607018 029402 ㅁ 1 ㅁ 9- ㅇ ㅇ ㅁ =19 | 옹 3 ㅋ 66 0116 607011841786 ㅁ 070. |
| 5160 4 | 11080 60801016: 3016006(600210- ㄱ 12) | 61020 | 폭 이 080 016 5\11011. |

## Configuring Subinterface Multicast and Broadcast Counters

Beginning Cisco NX-OS Release 9.3(6), subinterface multicast and broadcast counters are supported on Cisco Nexus N9K-C9336C-FX2 and N9K-C93240YC-FX2 switches.

To configure multicast and broadcast counters on a device, follow these steps:

## SUMMARY STEPS

1. configure terminal

2.

[no] hardware profile sub-interface flex-stats

3. copy running-config startup-config

4. reload

## DETAILED STEPS

Procedure

| 51601 | 000847@ 6(60001021 | 트 마 666 인 06861 00011841780070 20006. |
|---|---|---|
|  | 60801016: 3016010# 007 ㅁ 5*1094 ㅠ 6 ㄴ 62 ㅋ 0 ㅁ 17 ㅁ 21 으 1606 (6020 조 10) 부 |  |
| 5160 2 | 1200] 6200\21@ 01016 5010-106(0 다 2060 116 노 -56265 60801016: 3\016056 (0002?10) + 162200\226 ㅁ ㄴ 0 ㅇ 5116 5146-10 ㅁ ㄴ ㄷ 6 ㄴ 2206 조 16×-8 ㄴ 265 요다 (60208,106-1 조 ) 부 | 쿄 0816166 541610160306 116 61815 107 004100881 800 60080088[ 00401668. |
|  | 60801016: 31606 (0020219-12) 후 0029 029402 ㅁ 1 ㅁ 9- ㅇ ㅇ ㅁ =19 8 ㅎ ㄴ 2 ㄴ ㄴ ㄷ ㅁ 6-0 ㅇ 02 ㅁ 5219 |  |

|

|

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

140

ㅣ

|!

## Configuring Layer 3 Interfaces

## Configuring Subinterface Multicast and Broadcast Counters

| 101020 | 폭 이 080 016 5\11011. |  |
|---|---|---|
| 6801016: |  |  |
| 3016006(600210- ㄱ 12) 61020 |  |  |

Step 4

## Example

The following exampledisplays the subinterfacemulticastand broadcast counters as a result of show interface counters command:

| 39016056 (602 ㅁ 2106) * 580 17 ㅁ ㄷ | 66206 1/31/4 .1 ㅇ 00 ㅁ ㅁ ㄴ 6 ㅋ 5 |  |
|---|---|---|
|  | 1000 ㄴ 6 ㄴ 5 | 100028\ ㄴ 2 ㅁ = ㄴ 6 |
| 20 는 | 101820400 ㄷ 6 ㄴ ㄷ ㅎ ㅁ | 1012040028\ ㄴ ㅁㄴ |
| 표 타 217 3174 2 | 0 | 0 |
| 20 는 | 101207414028 ㄴ ㅁㄴ | 10182048028\ ㄴ ㅁㄴ |
| 표 타 217 3174 2 | 0 | 0 |
| 20 는 | 101820600 ㄴ ㄷ 6 ㄴ 5 | 101820600288 ㄴ ㅁㄴ |
| 표 타 217 3174 2 | 0 | 0 |
| 20 는 | 101207680028 ㄴ ㅁㄴ | 10182068028 ㄴ ㅁㄴ |
| 표 타 217 3174 2 | 0 | 0 |
| 20 는 표 타 217 3174 2 | 004600 ㄴ 666 0 | 04600286 ㄴ 26 0 |
| 20 는 | 04110286 ㄴ 26 | 04682026 ㄴ 2 ㄴ 6 |
| 표 타 217 3174 2 | 0 | 0 |
| 20 는 | 004 ㄴ 20400 ㄴ 66 | 004 ㄴ 2040028 ㄴ 2 ㄴ 6 |
| 표 타 217 3174 2 0 0 |

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

|

|

141

| |

## Configuring Layer 3 Interfaces

| |

## Verifying the Layer 3 Interfaces Configuration

| 0217 3174 . | 0 | 0 |
|---|---|---|
| 20 | 0046 ㄴ 20600 ㄴ 66 | 006 ㄴ 2060028 ㄴ 26 |
| 0217 3174 . | 0 | 0 |
| 20 | 00420 60028 ㄴ 26 | 004 ㄴ 20 ㅁ 68028 ㄴ 26 |

Eth1/31/4.1

Port

Eth1/31/4.1

Port

Eth1/31/4.1

## Verifying the Layer 3 Interfaces Configuration

To display the Layer 3 configuration, perform one of the following tasks:

| 9110\ 101600140@ 60166061 5/0722077 | 1219 21079 0416 16567 3 10(60406 00701184180 ㅁ 07, 58048, 300 60406666 (10014010 을 0416 5-0110466 6%0006010811 060 78 이 8760 200110 용 4460886 01 10400400 800 04000400 이 400 6566 78168). |
|---|---|
| 9410\ 101600140@ 6016606[ 5/0727077 0 피 라 | 19218575 016 18567 3 106(60806 07061800081 96048. |
| 910\ 1016001406@ 6016106065/0727077 080810141066 | 1921875 016 18567 3 106(6 다 806 680860111166, 10014010 음 200 6006. 50660, 300 04016. |
| 9410\ 101600[406@ 00161060[570727077 00650000 ㅁ 070 | 19218575 016 18567 3 106(60806 06600700 ㅁ 070. |
| 9410\ 10160018406@ 60166060[570777077 568045 | 191218578 016 17856 3 1066 다 806 8010210161081176 8[8049, 7200720006, 50660, 400 04216. |
| 9110\ 10160018406@ 6016606@[ 5/0727077.77207706/" | 191218578 016 941010160806 00011841780070, 568048, 800 00142066769 (10014010 을 016 1-0110416 6%1000600811 060 78 이 8760 200110 용 4460886 01 10400400 800 04000400 이 400 6566 78168). |
| 9110\ 101600140@ 00『6-011814 이 007077776/-70.72207706/" | 1219 21879 0416 00 다 - 이 180061 9410106(60306 00201184780 ㅁ 07, 968046, 800 60406668 (10014010 을 416 5-0410416 6080 0061008115 0608760 200110 용 48460886 01 10400400 300 04060400 08066 800 6516 78165). |
| 9110\ 101600240010010108066777077/706/" | 1219 300 00406668. 21879 41610070080 10160806 00701184180 ㅁ 07, 56045, |
| 9410\ 10160040010000806777077/767/'0 파 2 | 1019018575 016 1007210806 10160806 00608007081 6[8048. |
| 940\ 1016(00640010010020577707706/' 006600100 ㅁ 070 | 1019018575 016 10072010806 101608066 0660000 ㅁ 07. |
| 9410\ 10160014061001010201677707706/' 56045 | 1219018575 0416 10010080 101603066 8010010160080 ㅋ 6 6[6048 8300 00060001 6[8049. |

|

|

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

142

ㅣ

|!

## Configuring Layer 3 Interfaces

## Monitoring the Layer 3 Interfaces

| 600001800 | 『4010056 |
|---|---|
| 9810\ 101600120@ 위 77207706/" | 1019018575 016 스티 10160306 0001184080070, 56045, 800 60406668. |
| 9810\ 1010020@ 위 77207706/' 02010 | 1219018575 016 스티 101(60306 0060800081 6[8049. |
| 910\ 10160014066@ 위 70 77207706/' 06500100 ㅁ 070 | 1019018575 016 스지 10160306 0660000072. |
| 9410 1016001206@ 위 0 77207706/' 56045 | 1219018575 016 스티 10160306 80001019668076 66048 800 00060001 6[8049. |

## Monitoring the Layer 3 Interfaces

Use the following commands to display Layer 3 statistics:

Command

| 1080-1066『21 {1060581.56007705 {1 | 2 | 3} | | (21900 페 6348 9000 86066 06\1066 661 41766 011[67006 58142110 응 101(677819 10 61[-7816 800 280166[-『786(6 6[806068 |
|---|---|
| 7116 70080 107 스티 260\00 따 6 10160406 15 60 10 300 56001008, 800 016 70086 107 Ｌ ㄴ 8567 106(608065 16 30 10 300 6600008. |
| 110\ 106(6 다 400 00166066[ 5707/22077 001406666 | 10219018575 016 18567 3 10160806 656805008 (4010896, 10416088(, 8040 600800891). |
| 110\ 1066 다 400 00160066[ 5707/27077 0040(665 0210 | 1019018575 016 18567 3 101600806 10041 800 04041 060401668. |
| 110\ 106(60200 00160066 66005 5/707/2077 00(2400 4] | 1019018575 016 18567 3 10160806 61805008. 704 087 000008117 10401406 811 32-61 300 64-61 0866 400 16516 60401609 (010014010 을 660078). |
| 110\ 106(6 다 400 00106061 66005 5/07/27077 004706(666 00019 | 1216901876 0416 18567 3 10160806 10041 000 041041 60078 |
| 110\ 106(6 다 400 00106061 66005 5/07/27077 004706(666 50002 | 1019018575 016 18567 3 10160806 00401676 16001[60 105 오지 41188. |
| 110\ 106(6 다 400 001666066[ 5707/2077.77707706/' 00401(665 | 1216218578 0416 941010160366 9[8080108 (401089[, 01410085[ 800 600800890. |
| 110\ 1066 타 400 [ ㅁ 0016-01181001 0/7072770/-70.77207706/" 『0014106615 | 101901855 016 202-01180061 594101016 다 306 568080105 (4016896, 2041606896, 840 670800890. |
| 110\ 1066 다 400100002077707776/ ㆍ 004706(665 | 10190185765 016 10072160806 101606066 10041 800 04104 0014206676 (4016896, 2041606896, 840 670800890. |
| 110\ 1066 다 00100002077707776/7^ 0063460 [211] | 1019018575 016 10072160806 10160466 518090068. 04 082 000008117 10401406 811 32-61 300 64-61 0866 400 |

Purpose

[all]

errors

snmp

counters

byte counters (including errors).

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

|

|

143

| |

## Configuring Layer 3 Interfaces

| |

## Configuration Examples for Layer 3 Interfaces

| 600001800 | 『4010056 |
|---|---|
| 9410\ 101006406010010020577707706/' 004016『5 66005 | | 101901675 016 1002160806 10160366 10041 800 04104 600078. |
| 9410\ 101600366@ 위 370 77207706/' 00406(065 | 1019018575 016 스티 101(60306 1004 800 041041 60141 26669 (401688[, 20416688[, 800 6008006890). |
| 9110\ 1066 타 4066 뒤 40 77207706/ ㆍ 0000(665 0063460 [211] | 1219 21879 0416 스지 14(6 다 306 9[6090068. 04 082 0000081171001406 8111.8760 3 08066 400 6516 0040(669 (401689 800 204166890. |
| 9110 10160014066@ 위 70 77207706/ ㆍ 00406(665 50000 | 1219 21879 0416 스피 14(60406 00406(676 76002160 65 옹 테 12 1188. |

## Configuration Examples for Layer 3 Interfaces

This example shows how to configure Ethernet subinterfaces:

interface ethernet 2/1.10 description Layer 3 ip address 192.0.2.1/8

This example shows how to configure a loopback interface:

interface loopback 3 ip address 192.0.2.2/32

The following examples shows the output of the SVI counters and SVI statistics rate details when hardware profile svi-and-si flex-stats-enable command is enabled.

In the show interface command, the statistics rate or polling interval of 60 seconds and 300 seconds are added starting with Cisco NX-OS Release 10.5(2)F release.

show interface vlan 2406

Vlan2406 is up, line protocol is up, autostate enabled Hardware is EtherSVI, address is 3c13.ccc9.a397 Internet Address is 20.0.0.2/24 MTU 1500 bytes, BW 1000000 Kbit, DLY 10 usec, reliability 255/255, txload 1/255, rxload 1/255 Encapsulation ARPA, loopback not set Keepalive not supported ARP type: ARPA Last clearing of "show interface" counters 00:11:03 Load-Interval #1: 1 minute (60 seconds) 60 seconds input rate 5492528 bits/sec, 10096 packets/sec 60 seconds output rate 0 bits/sec, 0 packets/sec input rate 5.49 Mbps, 10.10 Kpps; output rate 0 bps, 0 pps Load-Interval #2: 5 minute (300 seconds) 300 seconds input rate 5448741 bits/sec, 10016 packets/sec 300 seconds output rate 0 bits/sec, 0 packets/sec input rate 5.45 Mbps, 10.02 Kpps; output rate 0 bps, 0 pps L3 Switched: input: 0 pkts, 0 bytes - output: 0 pkts, 0 bytes L3 in Switched: ucast: 6643884 pkts, 451784112 bytes L3 out Switched:

ucast: 0 pkts, 0 bytes

|

|

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

144

ㅣ

|!

## Configuring Layer 3 Interfaces

## Related Documents

## Related Documents

| 『61!0660 0000016066 | 000001601 1106 |
|---|---|
| 12 | (76900 00005 9000 .567769 20225 (.7770057 4010778 (7072077810077077 07006 |
| 노 트 스 지요 | (76900 00005 9000 56776 20.42(29 7.0116/' 2 .51270707778 (7072077810077077 07006 |

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

|

|

145

| |

| |

## Related Documents

|

|

146

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

## Configuring Layer 3 Interfaces

ㅣ

6

C H A P T E R 6

## ConfiguringBidirectionalForwardingDetection

- • Bidirectional Forwarding Detection, on page 147

- • Prerequisites for BFD, on page 150

- • Guidelines and Limitations, on page 150

- • Default Settings, on page 155

- • Configuring BFD, on page 156

- • Configuring BFD Support for Routing Protocols, on page 171

- • Configuring BFD Interoperability, on page 182

- • Verifying the BFD Configuration, on page 186

- • Monitoring BFD, on page 187

- • BFD Multi-sessions (concept), on page 187

- • BFD Multihop, on page 187

- • BFD vPC sub-second convergence in failure scenarios, on page 191

- • Configuration Examples for BFD, on page 195

- • Related Documents, on page 196

- • RFCs, on page 196

## Bidirectional Forwarding Detection

Bidirectional Forwarding Detection (BFD) is a protocol designed to quickly identify faults in the forwarding pathbetweentwodevices.BFDsimplifiesnetworkprofilingandplanningbyofferingpredictablereconvergence

time.

BFD detects forwarding path failures across various media types, encapsulations, topologies, and routing protocols. It provides subsecond failure detection between two adjacent devices, distributing some load onto the data plane on supported modules. BFD can be less CPU-intensive than protocol hello messages.

## Asynchronous mode

BFD asynchronous mode is a BFD session mode that:

- • involves the exchange of periodic control packets to monitor connectivity,

- • establishes and maintains BFD neighbor sessions, and

- • negotiates session parameters.

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

|

|

147

## Configuring Bidirectional Forwarding Detection

| |

## BFD Detection of Failures

## BFD session parameters

The table lists the BFD session parameters and the intervals.

Table11:BFDsessionparameters

| 10661760 0010100410 0 ㅁ 80611 10167781 | | 1116 10160081 81 \11101 0416 06106 16 0001184760 10 5600 3012 16110 106898869. |
|---|---|
| 복 6041160 001141014100 7606196 106(67781 | | 1116 0010104410 10161781 8[ \111011 416 06106 080 8000101 812 16110 106698869 10000 8000167 312 06106. |
| 10616 2241021166 | 7116 0400667 01 070169108 1212 16110 2270568805 10041160 [0 061601[5 8 13441 10 016 1020\0800108 2802. |

The number of missing BFD hello messages required to detects a fault

## BFD neighbor workflow

The figure details the BFD neighbor sessions establishment between two routers.

Figure6:EstablishingaBFDNeighborRelationship

1 0 아 0 ㅁ 6191160「5 05 마 < [에 05 마 고 바 ㅁ ㅁ 6191160「5 3 을. 슬 을 | 172.16.10.2 172.16.10.1 ㅣ 2 172.18.0.1 으아 배 06 아 08 172.17.0.1

The stages that establish a BFD neighbor session are:

1. The OSPF process discovers a BFD neighbor.

2. The local BFD process gets a request to start a session BFD neighbor session with the OSPF neighbor router.

3. The session is established between the BFD neighbor with the OSPF neighbor router.

## BFD Detection of Failures

Once a BFD session has been established and timer negotiations are complete, BFD neighbors send BFD control packets that act in the same manner as an IGP hello protocol to detect liveliness, except at a more accelerated rate. BFD detects a failure, but the protocol must take action to bypass a failed peer.

BFD sends a failure detection notice to the BFD-enabled protocols when it detects a failure in the forwarding path. The local device can then initiate the protocol recalculation process and reduce the overall network convergence time.

The following figure shows what happens when a failure occurs in the network (1). The BFD neighbor session with the OSPF neighbor router is torn down (2). BFD notifies the local OSPF process that the BFD neighbor is no longer reachable (3). The local OSPF process tears down the OSPF neighbor relationship (4). If an alternative path is available, the routers immediately start converging on it.

|

|

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

148

ㅣ

|!

## Configuring Bidirectional Forwarding Detection

## Distributed Operation

<

- Note Note The BFD failure detection occurs in less than a second, which is much faster than OSPF Hello messages could detect the same failure.

Figure7:TearingDownanOSPFNeighborRelationship

4 0259 ㅁ 619116015 06 배 주 % 05 매 3 바 ㅁ ㅁ 6191160「5 3 < ※ [ 저 바 ㅁ 코 바 ㅁ 1 = 인 1 래 100 「 - 텐 겨 시 ㅣ [가 172.16.10.2 술 * 72.16101 내어 로 172.18.0.1 나가오 ㅁ ㅇ 4666 172.17.0.1

## Distributed Operation

Cisco NX-OS can distributethe BFD operation to compatiblemodules that support BFD. This process offloads the CPU load for BFD packet processing to the individual modules that connect to the BFD neighbors. All BFD session traffic occurs on the module CPU. The module informs the supervisor when a BFD failure is detected.

## BFD Echo Function

Echo packets are defined and processed only by the transmitting system. For IPv4 and IPv6, the echo packets' destination address is that of the transmitting device. It is chosen in such a way as to cause the remote system to forward the packet back to the local system. This bypasses the routing lookup on the remote system and relies on the forwarding information base (FIB) instead. BFD can use the slow timer to slow down the asynchronous session when the echo function is enabled and reduce the number of BFD control packets that are sent between two BFD neighbors. The Echo function tests only the forwarding path of the remote system by having the remote (neighbor) system loop them back, so there is less inter-packet delay variability and faster failure detection times.

## Security

Cisco NX-OS uses the packet Time to Live (TTL) value to verify that the BFD packets came from an adjacent BFD peer. For all asynchronous and echo request packets, the BFD neighbor sets the TTL value to 255 and the local BFD process verifies the TTL value as 255 before processing the incoming packet. For the echo response packet, BFD sets the TTL value to 254.

You can configure SHA-1 authentication of BFD packets.

## High Availability

BFD supports stateless restarts. After a reboot or supervisor switchover, Cisco NX-OS applies the running configuration and BFD immediately sends control packets to the BFD peers.

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

|

|

149

| |

## Configuring Bidirectional Forwarding Detection

| |

## Virtualization Support

## Virtualization Support

BFD supports virtual routing and forwarding instances (VRFs). VRFs exist within virtual device contexts (VDCs). By default, Cisco NX-OS places you in the default VDC and default VRF.

## Prerequisites for BFD

Ensure you meet these prerequisites before you configure BFD.

- • Enable the BFD feature.

- • Disable ICMP redirect messages on interfaces where BFD is enabled.

- • Disable the IP packet verification check for identical IP source and destination addresses.

- • Review the detailed prerequisites in the configuration tasks.

## Guidelines and Limitations

BFD has the following configuration guidelines and limitations:

- • The QSFP 40/100-G BiDi comes up in the highest possible speed available on the port. For example, in the Cisco Nexus 93180LC-EX switch it comes up as 40 G in the first 28 ports and 100 G in the last 4 ports. If you need to connect to 40-G SR4 BiDi, the speed on the 40/100-G BiDi needs to be set to 40 G.

- • BFD over private-vlan is not supported Cisco Nexus 9000 Switches.

- • Beginning with Cisco NX-OS Release 10.2(1q)F, Layer 3 Unicast BFD is supported on Cisco Nexus N9K-C9332D-GX2B platform switches.

- • Forming BFD neighbors on a vPC VLAN through an orphan port is not supported on Cisco Nexus 9000 Switches.

- • Beginning with Cisco NX-OS Release 9.2(1), QSFP-40/100-SRBD comes up in the speed of 100-G and inter-operate with other QSFP-40/100-SRBD at either 40-G or 100-G speed on Cisco Nexus 9500 Switches with the N9K-X9636C-RX line card. The QSFP-40/100-SRBD can also inter-operate with QSFP-40G-SR-BD at 40G speeds. However to operate at 40G speed, you must configure the speed as 40G.

- • show commands with the internal keyword are not supported.

- • BFD per-member link support is added on Cisco Nexus 9000 Series switches.

- • BFD supports BFD version 1.

- • BFD supports IPv4 and IPv6.

- • BFD supports OSPFv3.

- • BFD supports IS-ISv6.

- • When configuring BFD over IP unnumbered interfaces, use these guidelines:

|

|

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

150

ㅣ

|!

## Configuring Bidirectional Forwarding Detection

## Guidelines and Limitations

- • Disable the BFD echo function to prevent the interface from flapping.

- • Enable BFD multihop when configuring BGP over IP unnumbered interface.

- • Set the ipv6 nd ns-interval command range to 15 under the Layer 3 interface configuration to prevent BFD sessions from flapping, when there are a large number of IPv6 adjacencies.

Alternatively, increase the BFD echo interval to avoid session instability that might occur due to CoPP drops of NS/NA packets.

- • BFD supports BGPv6.

- • BFD supports EIGRPv6.

- • BFD supports only sessions which have unique (src_ip, dst_ip, interface/vrf) combination.

- • BFD supports single-hop BFD.

- • Only single-hop static BFD is supported.

- • BFD for BGP supports single-hop EBGP and iBGP peers.

- • BFD supports keyed SHA-1 authentication.

- • BFD supports the following Layer 3 interfaces—physical interfaces, port channels, sub-interfaces, and VLAN interfaces.

- • BFD depends on a Layer 3 adjacency information to discover topology changes, including Layer 2 topology changes. A BFD session on a VLAN interface (SVI) may not be up after the convergence of the Layer 2 topology if there is no Layer 3 adjacency information available.

- • For BFD on a static route between two devices, both devices must support BFD. If one or both of the devices do not support BFD, the static routes are not programmed in the Routing Information Base (RIB).

- • Both single-hop and multi-hop BFD features are supported with specific restrictions. For multi-hop BFD features restrictions, refer to Guidelines and Limitations for BFD Multihop, on page 188 section.

- • Port channel configuration limitations:

- • For Layer 3 port channels used by BFD, you must enable LACP on the port channel.

- • For Layer 2 port channels used by SVI sessions, you must enable LACP on the port channel.

- • SVI limitations:

- • An ASIC reset causes traffic disruption for other ports and it can cause the SVI sessions on the other ports to flap. For example,if the carrierinterfaceis a virtualport channel(vPC), BFD is not supported over the SVI interface and it could cause a trigger for an ASIC reset. When a BFD session is over SVI using virtual port channel (vPC) Peer-Link, the BFD echo function is not supported. You must disable the BFD echo function for all sessions over SVI between vPC peer nodes.

An SVI on the Cisco Nexus series switches should not be configured to establish a BFD neighbor adjacency with a device connected to it via a vPC. This is because the BFD keepalives from the neighbor, if sent over the vPC member link connected to the vPC peer-switch, do not reach this SVI causing the BFD adjacency to fail.

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

|

|

151

| |

| |

## Configuring Bidirectional Forwarding Detection

## Guidelines and Limitations

- • When you change the topology (for example, add or delete a link into a VLAN, delete a member from a Layer 2 port channel, and so on), the SVI session could be affected. It may go down first and then come up after the topology discovery is finished.

- • BFD over FEX HIF interfaces is not supported.

- • When a BFD session is over SVI using virtual port-channel (vPC) Peer-Link (either BCM or GEM based ports), the BFD echo function is not supported. You must disable the BFD echo function for all sessions over SVI between vPC peer nodes using the no bfd echo command at the SVI configuration level.

Tip

- If you do not want the SVI sessions to flap and you need to change the topology, you can disable the BFD feature before making the changes and re-enable BFD after the changes have been made. You can also configure the BFD timer to be a large value (for example, 5 seconds), and change it back to a fast timer after the above events complete.

- • When you configure the BFD Echo function on the distributed Layer 3 port channels, reloading a member module flaps the BFD session hosted on that module, which results in a packet loss.

If you connect the BFD peers directly without a Layer 2 switch in between, you can use the BFD per-link mode as an alternative solution.

<

> **NOTE**
> Note

- Using BFD per-link mode and sub-interface optimization simultaneously on a Layer 3 port channel is not supported.

- • When you specify a BFD neighbor prefix in the clear {ip | ipv6} route prefix command, the BFD echo session flaps.

- • The clear {ip | ipv6} route * command causes BFD echo sessions to flap.

- • HSRP for IPv4 is supported with BFD.

- • BFD packets generated by the Cisco NX-OS device line cards are sent with COS 6/DSCP CS6. The DSCP/COS values for BFD packets are not user configurable.

- • When configuring BFDv6 in no-bfd-echo mode, it is recommended to run with timers of 150 ms with a multiplier of 3.

- • BFDv6 is not supported for VRRPv3 and HSRP for v6.

- • IPv6 eigrp bfd cannot be disabled on an interface.

- • IETF BFD is not supported on N9K-X96136YC-R, N9K-X9636C-R, N9K-X9636C-RX and N9K-X9636Q-R line cards.

- • Port channel configuration notes:

- • When the BFD per-link mode is configured, the BFD echo function is not supported. You must disablethe BFD echo functionusing the no bfd echo commandbefore configuringthe bfd per-link command.

|

|

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

152

ㅣ

|!

## Configuring Bidirectional Forwarding Detection

## Guidelines and Limitations

- • Before configuring BFD per-link, make sure there is no BFD session running on the port-channel. If there is any BFD session running already, remove it and then proceed with bfd per-link configuration.

- • Configuring BFD per-link with link-local is not supported.

- • The supported platforms include Cisco Nexus 9500 Series switches with N9K-X9636C-R, N9K-X9636Q-R, N9K-X9636C-RX line cards.

- • Beginning with Cisco NX-OS Release 9.3(7), BFD is supported on unnumbered interfaces.

<

- Note

BFD over unnumbered Switched Virtual Interfaces (SVIs) are not supported.

Downgrade compatibility for BFD on unnumbered interface support cannot be verified using show incompatibility nxos bootflash:filename command. The compatibility will be checked during install all command.

- • Beginning with Cisco NX-OS Release 10.5(2)F, BFD over IP unnumbered is not supported on Cisco Nexus 9808 and 9804 switches.

- • When you configure BFD on a numbered interface along with OSPF and when the interface is converted to an unnumbered interface, the OSPF and BFD command remains in the running configuration but the BFD functionality may not work

- • The following BFD command configurations are not supported for configuration replace:

- • port-channel bfd track-member-link

## • port-channel bfd destination destination-ip-address

- • Cisco Nexus 9800 platform switches have the following limitation for BFD IPv6 sessions:

- • Each ASIC unit in supervisor switch mode of line card supports a maximum of 256 BFD IPv6 sessions. If more BFD IPv6 sessions are required, sessions must be spread across ASIC units or line cards.

- • BeginningwithCiscoNX-OSRelease10.3(1)F,BFDsupportssingle-hopBFDonroutedport,routed-sub interface, and breakout port of Cisco Nexus 9808 platform switches.

- • BeginningwithCiscoNX-OS Release10.4(1)F, BFDsupports single-hopBFDon routedport, routed-sub interface, and breakout port of Cisco Nexus 9804 platform switches.

- • Beginning with Cisco NX-OS Release10.4(2)F the following are applicablefor Cisco Nexus C9232E-B1 switch:

- • Single-hop BFD on routed port, routed-sub interface, and breakout ports are supported.

- • BFD Authentication is not supported.

- • Beginning with Cisco NX-OS Release 10.5(3)F, the Cisco Nexus 93C64E-SG2-Q switch supports these features.

- • Single-hop BFD on Layer 3 physical interfaces and physical subinterfaces

- • Single-hop BFD on Layer 3 port channel and port channel subinterfaces

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

|

|

153

| |

| |

## Configuring Bidirectional Forwarding Detection

## Guidelines and Limitations

- • Single-hop BFD on routed port and breakout ports

- • Single-hop BFD on IPv4 and IPv6 address

- • Minimum BFD timer with 50ms

- • BFD asynchronous mode

- • BFD echo function

- • Use the bfd authentication interop command to configure BFD authenticationinteroperabilitybetween Nexus and non-Nexus platforms. If you do not configure this command, BFD authentication fails due to an invalid authentication sequence number field format.

- • BFD Authentication is not supported on Cisco Nexus 9800 platform switches.

- • Beginning with Cisco NX-OS Release 10.4(1)F, BFD supports single-hop BFD on N9KX98900CD-A and N9KX9836DM-A line cards with Cisco Nexus 9808 and 9804 switches.

- • Beginning with Cisco NX-OS Release 10.4(3)F, single hop BFD is supported on Cisco Nexus 9808 and 9804 L3 port-channel interfaces and port-channel sub-interfaces with the following limitations:

- • Per Port-channel interface, only 128 sessions are supported.

- • BFD authentication is not supported.

- • Beginning with Cisco NX-OS Release 10.4(3)F, single-hop BFD is supported on Layer 3 port channel on Cisco Nexus 9800 switches. The BFD server selects the hosting line card for the session among the available online line cards. However, this feature has the following limitations:

- • If the hosting line card changes, the ongoing session gets deleted on that line card, and the hosting is created on another line card that is available.

- • If the source IP of the BFD session changes, the ongoing session gets deleted and recreated with the new source IP.

## BFD Support on Nexus Switches

BFD support is availableon the Nexus platforms in these releases.For more information,see platform support matrix.

Table12:BFDSupportonNexusSwitches

| 비 34007 | 100600066010 01600 84%-05 『1616856 |
|---|---|
| 피 93-(1648-6(62-0 | 10.5.37 |
| 피 9-(009364(:-11 | 10.4.37 |
| 피 9-0934001.10-11 | 10.4.27 |
| 찌 9-(0092328-81 |  |
| 제 6%46 9804 | 10.4.1『 |
| 지 9-(0933212-12 쿄 |  |

|

|

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

154

ㅣ

|!

## Configuring Bidirectional Forwarding Detection

## Default Settings

| 떼 6%48 9808 | 10.3.1『 |
|---|---|
| 제 9-(:934812-(6%2 ㅅ | 10.2.3 |
| 제 9(-(:936412-(6%2 ㅅ |  |
| 제 9《-(0933212-(6×%28 |  |
| (21600 찌 66465 9300-6※, 9300-0×, 9300-0×2. 93003, 300 9300-06% |  |
| 9364(:-06× | 9.3.3 |
| 931610-0× |
| 93600@212-0× |
| 제 9《-※96136(-《, 지 9-%9636('-《. |

## Default Settings

The following table lists the default settings for BFD parameters.

Table13:DefaultBFDParameters

| 20120 1680176 | 101686160 |
|---|---|
| 복 6041760 00101014100 7606176 12660081 | 50 7011116600008 |
| 10661760 10010100410 6 ㅁ 80610 14160081 | 50 7011116600008 |
| 10616 2241021166 | 3 |
| 트 010 140001020 | 80860160 |
| 1006 | 스 9500110000149 |
| 20 다 -001800 이 | 트 081681200006(0065669100 ㅁ 767 504706-0660080007081Ｌ 8007696) |
| 오 10\ 10467 | 2000 7011119600008 |

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

|

|

155

| |

## Configuring Bidirectional Forwarding Detection

| |

## Configuring BFD

## Configuring BFD

## Best Practices for BFD configuration hierarchy and inheritance

Consider these points when you configure BFD at:

- • Interface-level configuration versus global configuration

- • Member ports and port channels

## Interface-level configuration versus global configuration

Configure BFD at both the global level and at the interface level.

<

- Note

Interface-level configuration overrides the global configuration.

## Inheritance for member ports and port channels

Configure the member port to inherit the BFD configuration of the primary port channel.

## Task Flow for Configuring BFD

Follow these steps in the following sections to configure BFD:

- • Enabling the BFD Feature.

- • Configuring Global BFD Parameters or Configuring BFD on an Interface.

## Enable BFD feature

Enable the BFD feature to configure BFD on an interface and protocol.

## Procedure

- Enter the configuration mode with the configure terminal command.

## Example:

```cisco-ios
switch# configure terminal switch(config)#
```

- Step 2 Enable BFD with the feature bfd command.

## Example:

```cisco-ios
switch(config)# feature bfd
```

- (Optional) View the status of features with the show feature | include bfd command.

|

|

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

156

ㅣ

|!

## Configuring Bidirectional Forwarding Detection

## Disable BFD

## Example:

```cisco-ios
switch(config)# show feature | include bfd
```

- (Optional) Save the configuration with the copy running-config startup-config command.

## Example:

```cisco-ios
switch(config)# copy running-config startup-config
```

## Disable BFD

## Procedure

|  | 600001800 0726000 |  | 『00 ㅁ 056 |  |
|---|---|---|---|---|
| 5660 1 | 10168616 016 12) 1680176 800 00011841780009 \101 416 40 | 76000\6 811 48560018[60. 1686004@ 010 06010100800. |  |  |
| 6801016: |  |  |  |
| 3891600 (60010) ㅁ 0 62006 | 1520 |  |  |

Step 1

## Configure global BFD parameters

Configure default session behaviors for all BFD (BidirectionalForwarding Detection) sessions on your device.

BFD global parameters set the timer and detection characteristics for all BFD sessions. You can override these parameters at the interface.

You can configure these settings for all BFD sessions on the device. Both BFD peers negotiate the session parameters in a three-way handshake.

To override these global session parameters on an interface, see Configuring BFD on an Interface.

Use these steps to configure global BFD parameters.

## Before you begin

Enable the BFD feature, see Configure global BFD parameters, on page 157

## Procedure

- Enter configuration mode using the configure terminal command.

## Example:

```cisco-ios
switch# configure terminal switch(config)#
```

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

|

|

157

## Configuring Bidirectional Forwarding Detection

| |

## Configure global BFD parameters

- Step 2 Configure the BFD session parameters for all BFD sessions using the bfd interval mintx min_rx msec multiplier value command.

## Example:

## switch(config)# bfd interval 50 min_rx 50 multiplier 3

This command overrides the values you configure for BFD session parameters on individual interfaces.

The intervals mintx and msec range from 50 milliseconds to 999 milliseconds, with a default of 50 milliseconds.

The multiplier ranges from 1 to 50. The default is 3.

- Configure the slow timer used in the echo function using the bfd slow-timer [interval] command.

## Example:

```cisco-ios
switch(config)# bfd slow-timer 2000
```

This value determines how quickly BFD starts a new session. It specifies the rate at which asynchronous sessions send BFD control packets when the echo function is enabled.

The slow-timer value sets the interval for control packets. Echo packets use the configured BFD intervals for link failure detection. Control packets at the slower rate maintain the BFD session.

The range is from 1000 to 30,000 milliseconds. The default is 2000.

- Step 4 Configure the interface used for Bidirectional Forwarding Detection (BFD) echo frames bfd echo-interface loopback interface number

## Example:

## switch(config)# bfd echo-interface loopback 1 3

This command changes the source address for the echo packets to the one configured on the specified loopback interface. The interface number range is from 0 to 1023.

- (Optional) Display the BFD running configuration using the show running-config bfd command.

## Example:

```cisco-ios
switch(config)# show running-config bfd
```

Step 6

- (Optional) Save the configuration using the copy running-config startup-config command.

## Example:

```cisco-ios
switch(config)# copy running-config startup-config
```

Your device uses the specified default BFD parameters for all BFD sessions unless you override them on an interface.

|

|

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

158

ㅣ

|!

## Configuring Bidirectional Forwarding Detection

## Configure BFD on an Interface

## Example

## Configure BFD on an Interface

You can configure the BFD session parameters for all BFD sessions on an interface. The BFD session parameters are negotiated between the BFD peers in a three-way handshake.

This configuration overrides the global session parameters for the configured interface.

## Before you begin

Ensure that Internet Control Message Protocol (ICMP) redirect messages are disabled on BFD-enabled interfaces. Use the no ip redirects command or the no ipv6 redirects command on the interface.

Enable the BFD feature. See the Enabling the BFD Feature section.

## Procedure

## Step 1 configure terminal

## Example:

```cisco-ios
switch# configure terminal switch(config)#
```

Enters configuration mode.

## Step 2 interface int-if

## Example:

```cisco-ios
switch(config)# interface ethernet 2/1 switch(config-if)#
```

Enters interface configuration mode. Use the ? keyword to display the supported interfaces.

## Step 3 bfd interval mintx min_rx msec multiplier value

## Example:

```cisco-ios
switch(config-if)# bfd interval 50 min_rx 50 multiplier 3
```

Configures the BFD session parameters for all BFD sessions on the device. This command overrides these values by configuring the BFD session parameters on an interface. The mintx and msec range is from 50 to 999 milliseconds and the default is 50. The multiplier range is from 1 to 50. The multiplier default is 3.

Beginning with Cisco NX-OS Release 9.3(5), configuring BFD session parameters under interface with default timer values using the bfd interval 50 min_rx 50 multiplier 3 command is functionally equivalent to no bfd interval command.

Once BFD session parameters under interface are set to default values, those BFD sessions running on that interface will inherit global session parameters, if present.

## Step 4 bfd authentication keyed-sha1 keyid id key ascii_key

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

|

|

159

| |

## Configuring Bidirectional Forwarding Detection

| |

## Configuring BFD on a Port Channel

## Example:

```cisco-ios
switch(config-if)# bfd authentication keyed-sha1 keyid 1 ascii_key cisco123
```

(Optional) Configures SHA-1 authentication for all BFD sessions on the interface. The ascii_key string is a secret key shared among BFD peers. The id value, a number between 0 and 255, is assigned to this particular ascii_key . BFD packets specify the key by id , allowing the use of multiple active keys.

To disable SHA-1 authentication on the interface, use the no form of the command.

- Step 5 Use the bfd authentication interop command to configure BFD authentication interoperability between Nexus and non-Nexus platforms.

## Example:

```cisco-ios
switch(config-if)# bfd authentication interop
```

## Step 6 show running-config bfd

## Example:

```cisco-ios
switch(config-if)# show running-config bfd
```

(Optional) Displays the BFD running configuration.

## Step 7 copy running-config startup-config

## Example:

```cisco-ios
switch(config-if)# copy running-config startup-config
```

(Optional) Saves the configuration change.

## Example

## What to do next

•

## Configuring BFD on a Port Channel

You can configure the BFD session parameters for all BFD sessions on a port channel. If per-link mode is used for Layer 3 port channels, BFD creates a session for each link in the port channel and provides an aggregate result to client protocols. For example, if the BFD session for one link on a port channel is up, BFD informs clientprotocols,such as OSPF, that the port channelis up. The BFD session parametersare negotiated between the BFD peers in a three-way handshake.

This configuration overrides the global session parameters for the configured port channel. The member ports of the port channel inherit the port channel BFD session parameters.

## Before you begin

Ensure that you enable LACP on the port channel before you enable BFD.

|

|

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

160

ㅣ

|!

## Configuring Bidirectional Forwarding Detection

## Configuring BFD on a Port Channel

Ensure that Internet Control Message Protocol (ICMP) redirect messages are disabled on BFD-enabled interfaces. Use the no ip redirects command on the interface.

Enable the BFD feature. See the Enabling the BFD Feature section.

## SUMMARY STEPS

1. configure terminal

2.

interface port-channel number

3. bfd per-link

4. bfd interval mintx min_rx msec multiplier value

5. bfd authentication keyed-sha1 keyid id key ascii_key

6. show running-config bfd

7.

copy running-config startup-config

## DETAILED STEPS

Procedure

|  | 600001800 0726000 | 『00 ㅁ 056 |
|---|---|---|
| 51601 | 000841@ 6(60001021 6801016: 3016010# 007 ㅁ 5*1094 ㅠ 6 ㄴ 62 ㅋ 0 ㅁ 17 ㅁ 21 으 1606 (6020 조 10) 부 | 트 마 666 인 06861 00011841780070 20006. |
| 5160 2 | 1066 타 06 00 타 -01128070 이 772077706/" 8 배 기 0: 31605 (60021) + 106622206 ㅁ 0 ㄴ ㄴ ㄷ -01 ㅁ 20061 그 요다 (60208,106-1 조 ) 부 | 트 26669 000-001800 이 600118408000 20006. 4266 016 ? 65\010 10 0190187 016 940001160 0 ㅁ 40106 78086. |
| 5160 3 | 1010 060-110 토 6801016: 38160056 (060202196-1<) 우 520 662- 끄 320 | (2001184169 016 12 56661009 107 68011 1106 10 016 2002 이 1800 히 . |
| 5160 4 | 16010 1066521 77777 0010 _ < 77960 21410101166 10716 타마미 미하 : 50108 나서 떠 1266221 50 피 크 므 조제 100161136 폰 | (06000081) (0001184166 0416 812) 5696100 0818016(676 107 811 2012 56661005 00 10416 2002 011801 이 . 11116 6000001800 0 ㅋ 6101068 14466677810466 67 0001184008 0416 1312 5669100 08180066(668. 7116 77071 800 77900 78086 16 010 50 10 999 7711116600008 300 0416 061341[18 50. 1116 20410701167 28086 19 12010 1 10 50. 7116 20410701167 0613411 16 3. |
| 5160 5 | 1010 340160008000166560-51101 16510 72 1665 29077 6 6801016: 3801600(000210-17)+ 1520 20 ㄴ ㄷ ㅁ 67 ㅁ ㄴ ㄷ 1 ㅇ 2 ㄴ ㅁㅁ 6760-81621 6710 1 25011 67 0 ㅇ 1500123 | | (0000081) (00201184766 51 ㅅ -1 340160008000 107 811 32 56661009 07 0416 10160406. 1116 05077 611 90108 19 8 56070 67 9118700 80200 212 76076. 1116 70 8106, 8 24020 16660660 0 300 255, 16 89618060 10 04116 08 디 04187 05677 67. 10 0806665 5060117 016 6657 6057 70, 4110\108 016 466 01 10410016 80006 6658. |

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

|

|

161

| |

## Configuring Bidirectional Forwarding Detection

| |

## Configure the BFD Echo function (task)

|  |  | 70 0198616 61 ㅅ -1 34101601168000 070 0416 10(60306, 456 0416 20 10020 01 416 6020001800. |
|---|---|---|
| 160 6 | 9410\ 704070108-000108 010 60801016: 31606 (0020219-1 ㅁ 2) 580 2904001 ㅁ 9- ㅇ 0 ㅁ ㄷ 19 520 | (06000081) 1219201876 016 812 0100108 00011841780 ㅁ 07. |
| 160 7 | 003 70070108-000118 564『0410-607018 60801016: 31606 (0020219-12) 후 0029 029402 ㅁ 1 ㅁ 9- ㅇ ㅇ ㅁ =19 8 ㅎ ㄴ 2 ㄴ ㄴ ㄷ ㅁ 6-0 ㅇ 02 ㅁ 5219 | (06000081) 58768 0416 0001184780070 0118086. |

Step 6

Step 7

## Configure the BFD Echo function (task)

You can configure the BFD echo function on one or both ends of a BFD-monitored link. The echo function slows down the required minimum receive interval, based on the configured slow timer. The RequiredMinEchoRx BFD session parameter remains nonzero if you disable the echo function to comply with RFC 5880 When you enable the echo function, the slow timer value becomes the required minimum receive interval.

## Before you begin

Enable the BFD feature. See the Enable BFD feature.

Configure the BFD session parameters. See Configuring Global BFD Parameters or Configuring BFD on an Interface.

Disable Internet Control Message Protocol (ICMP) redirect messages on BFD-enabled interfaces using the no ip redirects command on the interface.

## Procedure

- Enter the configuration mode using the configure terminal command.

## Example:

```cisco-ios
switch# configure terminal switch(config)#
```

Step 2

Set the slow timer to determine when BFD starts a new sesion using the bfd slow-timer echo-interval command.

## Example:

```cisco-ios
switch(config)# bfd slow-timer 2000
```

When the BFD echo function is enabled, this value also slows down the asynchronous sessions.

This value overwrites the required minimum receive interval when the echo function is enabled. The range is from 1000 to 30,000 milliseconds. The default is 2000 milliseconds.

- Step 3 Enters interface configuration mode using the interface int-if command.

|

|

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

162

ㅣ

|!

## Configuring Bidirectional Forwarding Detection

## Configuring Per-Member Link BFD Sessions

## Example:

```cisco-ios
switch(config)# interface ethernet 2/1 switch(config-if)#
```

Use the ? keyword to display the supported interfaces.

- Step 4 Enable the echo function using the bfd echo command.

## Example:

```cisco-ios
switch(config-if)# bfd echo
```

The default is enabled.

- Step 5 (Optional) Display the BFD running configuration using the show running-config bfd command.

## Example:

```cisco-ios
switch(config-if)# show running-config bfd
```

- Step 6 (Optional) Saves the configuration using the copy running-config startup-config command.

## Example:

```cisco-ios
switch(config-if)# copy running-config startup-config
```

## Configuring Per-Member Link BFD Sessions

BFD per-member link support is added on Cisco Nexus 9000 Series switches. See the following sections for more information.

## BFD Enhancement to Address Per-link Efficiency

The Bidirectional Forwarding (BFD) enhancement to address per-link efficiency, called as IETF Micro BFD, lets you configure the individual BFD sessions on every Link Aggregation Group (LAG) member interfaces (as defined in RFC 7130).

With this enhancement, the BFD sessions run on each member link of the port-channel. If BFD detects a link failure, the member link is removed from the forwarding table. This mechanismdelivers faster failure detection as the BFD sessions are created on an individual port-channel interface.

The BFD sessions running on member links of the port-channel are called as Micro BFD sessions. You can configure RFC 7130 BFD over main port-channel interface, that performs bandwidth monitoring over LAG by having one MicroBFD sessionover eachmember. If any of the memberport goes down, the port is removed from the forwarding table and this prevents traffic disruption on that member.

Micro BFD sessions are supported for both LACP and non-LACP based-port channels. For more information on how to configure Micro BFD sessions, see Configuring Micro BFD Sessions.

## Limitations of the IETF Bidirectional Forwarding Detection

See the following limitations of the IETF Bidirectional Forwarding Detection:

- • BFD Limitations

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

|

|

163

| |

| |

## Configuring Bidirectional Forwarding Detection

## Limitations of the IETF Bidirectional Forwarding Detection

- • IETF Micro-BFD sessions supports only single-hop BFD sessions. We recommend that you do not configure IPs from different subnets to establish the Micro-BFD sessions.

- • It cannot co-exist with BFD over logical port-channels or proprietary BFD per-member links. BFD IPv6 logical/proprietary per-link session is also not supported when BFD IETF IPv4 is configured on PC.

- • When you configure logical BFD session under any routing protocol, make sure that is not applied to any IETF port-channel. Having both logical and IETF configuration for same port-channel results in undefined behavior during ISSU/reloads.

- • IETF BFD IPv6 is not supported.

- • Echo functionality is not supported for Micro-BFD sessions.

- • Port-channel interfaces should be directly connected between two switches that are running the BFD sessions. No intermediate Layer 2 switches are expected.

- • EthPCM/LACP Limitations

- • If a LACP port-channel has members in hot-standby state, BFD failure in one of the active links may not cause the hot-standby link to come up directly. Once the active link with BFD failure goes down, the hot-standby member becomes active. However, it may not be able to prevent the port-channel from going down before the hot-standby link comes up, in cases where port-channel min-link condition is hit.

- • General Limitations:

- • It is supported only on Layer 3 port-channels.

- • It is not supported on the following:

- • vPC

- • Layer 3 sub-interfaces

- • Layer 2 port-channels/Layer 2 Fabric Path

- • FPC/HIF PC

- • Layer 3 sub-interfaces

- • SVI over port-channels

## Guidelines for Migration/Configuration of IETF Per-Member Sessions:

See the following guidelines for migration/configuration of IETF per-member sessions:

- • The logical BFD sessions that are created using the routing protocols over port-channel sub-interfaces (where RFC 7130 cannot run) are still supported. The main port-channel interface however does not support both logical and RFC 7130 sessions that co-exist. It can support only either of them.

- • YoucanconfigureRFC7130BFDoverthemainport-channelinterfacethatperformbandwidthmonitoring over the LAG by having one Micro-BFD session over each member. If any of the member port goes down, BFD notifies it to the port-channelmanager that removes the port from the LTL, thereby preventing blackholing of the traffic on that member.

|

|

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

164

ㅣ

|!

## Configuring Bidirectional Forwarding Detection

## Configuring Port Channel Interface

- • If the minimum number of links required to have the port-channel operationally up is not met in the above case, the port-channel is brought down by the port-channel manager. This in turn brings down the port-channel sub-interfaces if they are configured and thereby the logical BFD session also comes down notifying the routing protocol.

- • When you are using RFC 7130 on the main port-channel and logical BFD on the sub-interfaces, the logical BFD session should be run with lesser aggressive timers than the RFC 7130 BFD session. You canhaveRFC7130 configuredon theport-channelinterfaceor you canhaveitconfiguredin conjunction with the logical BFD sessions on the port-channel sub-interfaces.

- • When a proprietary per-link is configured, enabling IETF Micro-BFD sessions is not allowed on a port channelandvice-versa.Youhavetoremovetheproprietaryper-linkconfiguration.Currentimplementation of proprietary per-link does not allow changing the configuration (no per-link), if there is any BFD session that is bootstrapped by the applications. You need to remove the BFD tracking on the respective applications and remove per-link configuration. The migration path from the proprietary per-link to IETF Micro-BFD is as follows:

- • Remove the BFD configuration on the applications.

- • Remove the per-link configuration.

- • Enable the IETF Micro-BFD command.

- • Enable BFD on the applications.

The same migration path can be followed for proprietary BFD to IETF Micro-BFD on the main port-channel interface.

## Configuring Port Channel Interface

## Before you begin

Ensure that the BFD feature is enabled.

## SUMMARY STEPS

1.

```cisco-ios
switch(config)# interface port-channel port-number
```

2. switch(config-if)# no switchport

## DETAILED STEPS

## Procedure

## Step 1 switch(config)# interface port-channel port-number

Configures interface port-channel.

- Step 2 switch(config-if)# no switchport

Configures interface as Layer 3 port-channel.

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

|

|

165

| |

## Configuring Bidirectional Forwarding Detection

| |

## (Optional) Configuring BFD Start Timer

## What to do next

- • Configuring BFD Start Timer

- • Enabling IETF Per-link BFD

## (Optional) Configuring BFD Start Timer

Complete the following steps to configure the BFD start timer:

## SUMMARY STEPS

- switch(config-if)# port-channel bfd start 60

## DETAILED STEPS

## Procedure

## switch(config-if)# port-channel bfd start 60

Configures the BFD start timer for a port-channel.

## Note

The default value is infinite (that is no timer is running). The range of BFD Start Timer value for port-channel is from 60 to 3600 seconds. For start timer to work, configure start timer value before completing the port-channel BFD configurations (that is before port-channel bfd track-member-link and port-channel bfd destination are configured for Layer 3 port-channel interface with the active members).

## What to do next

- • Enabling IETF Per-link BFD

- • Configuring BFD Destination IP Address

## Enabling IETF Per-link BFD

## SUMMARY STEPS

1.

```cisco-ios
switch(config-if)# port-channel bfd track-member-link
```

## DETAILED STEPS

## Procedure

```cisco-ios
switch(config-if)# port-channel bfd track-member-link
```

|

|

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

166

ㅣ

|!

## Configuring Bidirectional Forwarding Detection

## Configuring BFD Destination IP Address

Enables IETF BFD on port-channel interface.

## What to do next

- • Configuring BFD Destination IP Address

- • Verifying Micro BFD Session Configurations

## Configuring BFD Destination IP Address

Complete the following steps to configure the BFD destination IP address:

## SUMMARY STEPS

1.

```cisco-ios
switch(config-if)# port-channel bfd destinationip-address
```

## DETAILED STEPS

## Procedure

## switch(config-if)# port-channel bfd destinationip-address

Configures an IPv4 address to be used for the BFD sessions on the member links.

## What to do next

- • Verifying Micro BFD Sessions Configuration

## Verifying Micro BFD Session Configurations

Use the following commands to verify the Micro BFD session configurations.

## SUMMARY STEPS

1. Displays the port-channel and port-channel member operational state.

인우

2. switch# show bfd neighbors

3. switch# show bfd neighbors details

4. switch# show tech-support bfd

5. switch# show tech-support lacp all

6. switch# show running-config interface port-channel port-channel-number

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

|

|

167

| |

## Configuring Bidirectional Forwarding Detection

| |

## Examples: Configuring Micro BFD Sessions

## DETAILED STEPS

## Procedure

- Displays the port-channel and port-channel member operational state.

```cisco-ios
switch# show port-channel summary
```

- Step 2 switch# show bfd neighbors

Displays Micro BFD sessions on port-channel members.

## Step 3 switch# show bfd neighbors details

Displays BFD session for a port channel interface and the associated Micro BFD sessions on members.

## Step 4 switch# show tech-support bfd

Displays the technical support information for BFD.

## Step 5 switch# show tech-support lacp all

Displays the technical support information for Ethernet Port Manager, Ethernet Port-channel Manager, and LACP.

## Step 6 switch# show running-config interface port-channel port-channel-number

Displays the running configuration information of the port-channel interface.

## Examples: Configuring Micro BFD Sessions

See the following examples for configuring Micro BFD sessions.

## Configuring Micro BFD Sessions

In this example, the following topology is used.

Figure8:ConfiguringMicroBFDSession

Ｌ ㄴ 8206『「 3 『00-0718006 바 ㅁ 80665 4 < 바 ㅁ ㅁ 800605 바 ㅁ 8065 ㅡ > <-- 바 ㅁ 80165 바 ㅁ 8065 - ㅡ > <-- 바 ㅁ 80165 Ｌ ㄴ 806 3 『0「 ㄴ 08006 50010 1 510 2 36454

The sample configuration of switch 1 is as follows:

feature bfd configure terminal interface port-channel 10

|

|

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

168

ㅣ

|!

## Configuring Bidirectional Forwarding Detection

## Examples: Configuring Micro BFD Sessions

port-channel bfd track-member-link port-channel bfd destination 10.1.1.2 port-channel bfd start 60 ip address 10.1.1.1/24

The sample configuration of switch 2 is as follows:

feature bfd

configure terminal interface port-channel 10 port-channel bfd track-member-link port-channel bfd destination 10.1.1.1 port-channel bfd start 60 ip address 10.1.1.2/24

## Verifying Micro BFD Sessions Configuration

The following example displays the show output of the show running-config interface port-channel<port-channel>, show port-channel summary, show bfd neighbors vrf internet_routes, and show bfd neighbors interface port-channel <port-channel> vrf internet_routes details commands.

```cisco-ios
switch# show running-config interface port-channel 1001
```

!Command: show running-config interface port-channel1001 !Time: Fri Oct 21 09:08:00 2016 version 7.0(3)I5(1) interface port-channel1001 no switchport vrf member internet_routes port-channel bfd track-member-link port-channel bfd destination 40.4.1.2 ip address 40.4.1.1/24 ipv6 address 2001:40:4:1::1/64 switch# show por port-channel port-profile switch# show port-channel summary Flags: D - Down P - Up in port-channel (members) I - Individual H - Hot-standby (LACP only) s - Suspended r - Module-removed b - BFD Session Wait S - Switched R - Routed U - Up (port-channel) p - Up in delay-lacp mode (member) M - Not in use. Min-links not met -------------------------------------------------------------------------------- Group Port- Type Protocol Member Ports Channel -------------------------------------------------------------------------------- 1001 Po1001(RU) Eth LACP Eth1/11/1(P) Eth1/11/2(P) Eth1/12/1(P) Eth1/12/2(P) switch# show bfd neighbors vrf internet_routes OurAddr NeighAddr LD/RD RH/RS State Int Vrf 40.4.1.1 40.4.1.2 1090519041/0 Up N/A(3) Po1001 internet_routes 40.4.1.1 40.4.1.2 1090519042/1090519051 Up 819(3)

Holdown(mult)

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

|

|

169

| |

Up

Up

| |

## Configuring Bidirectional Forwarding Detection

## Examples: Configuring Micro BFD Sessions

Eth1/12/1 internet_routes 40.4.1.1 40.4.1.2 1090519043/1090519052 Up 819(3) Eth1/12/2 internet_routes 40.4.1.1 40.4.1.2 1090519044/1090519053 Up 819(3) Eth1/11/1 internet_routes 40.4.1.1 40.4.1.2 1090519045/1090519054 Up 819(3) Eth1/11/2 internet_routes switch# switch# show bfd neighbors interface port-channel 1001 vrf internet_routes details OurAddr NeighAddr LD/RD RH/RS Holdown(mult) State Int Vrf 40.4.1.1 40.4.1.2 1090519041/0 Up N/A(3) Po1001 internet_routes Session state is Up Local Diag: 0 Registered protocols: eth_port_channel Uptime: 1 days 11 hrs 4 mins 8 secs Hosting LC: 0, Down reason: None, Reason not-hosted: None Parent session, please check port channel config for member info switch# switch# show bfd neighbors interface ethernet 1/12/1 vrf internet_routes details OurAddr NeighAddr LD/RD RH/RS Holdown(mult) State Int Vrf 40.4.1.1 40.4.1.2 1090519042/1090519051 Up 604(3) Eth1/12/1 internet_routes Session state is Up and not using echo function Local Diag: 0, Demand mode: 0, Poll bit: 0, Authentication: None MinTxInt: 100000 us, MinRxInt: 100000 us, Multiplier: 3 Received MinRxInt: 300000 us, Received Multiplier: 3 Holdown (hits): 900 ms (0), Hello (hits): 300 ms (458317) Rx Count: 427188, Rx Interval (ms) min/max/avg: 19/1801/295 last: 295 ms ago Tx Count: 458317, Tx Interval (ms) min/max/avg: 275/275/275 last: 64 ms ago Registered protocols: eth_port_channel Uptime: 1 days 11 hrs 4 mins 24 secs Last packet: Version: 1 - Diagnostic: 0 State bit: Up - Demand bit: 0 Poll bit: 0 - Final bit: 0 Multiplier: 3 - Length: 24 My Discr.: 1090519051 - Your Discr.: 1090519042

Min tx interval: 300000

- Min rx interval: 300000

Min Echo interval: 300000 - Authentication bit: 0

Hosting LC: 1, Down reason: None, Reason not-hosted: None

Member session under parent interface Po1001

```cisco-ios
switch# show bfd neighbors interface ethernet 1/12/2 vrf internet_routes details
```

0045220028

OurAddr

State

619162002 1206

NeighAddr

Int

LD/RD

Vrf

RH/RS

Holdown(mult)

40.4.1.1

40.4.1.2

1090519043/1090519052 Up

799(3)

Eth1/12/2

internet_routes

Session state is Up and not using echo function

Local Diag: 0, Demand mode: 0, Poll bit: 0, Authentication: None MinTxInt: 100000 us, MinRxInt: 100000 us, Multiplier: 3 Received MinRxInt: 300000 us, Received Multiplier: 3 Holdown (hits): 900 ms (0), Hello (hits): 300 ms (458336) Rx Count: 427207, Rx Interval (ms) min/max/avg: 19/1668/295 last: 100 ms ago

|

|

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

170

ㅣ

Up

Up

Up

Up

Up

Up

|!

## Configuring Bidirectional Forwarding Detection

## Configuring BFD Support for Routing Protocols

Tx Count: 458336, Tx Interval (ms) min/max/avg: 275/275/275 last: 251 ms ago Registered protocols: eth_port_channel Uptime: 1 days 11 hrs 4 mins 30 secs Last packet: Version: 1 - Diagnostic: 0 State bit: Up - Demand bit: 0 Poll bit: 0 - Final bit: 0 Multiplier: 3 - Length: 24 My Discr.: 1090519052 - Your Discr.: 1090519043 Min tx interval: 300000 - Min rx interval: 300000 Min Echo interval: 300000 - Authentication bit: 0 Hosting LC: 1, Down reason: None, Reason not-hosted: None Member session under parent interface Po1001 switch#

## Configuring BFD Support for Routing Protocols

## Configuring BFD on BGP

You can configure BFD for the Border Gateway Protocol (BGP).

## Before you begin

Enable the BFD feature. See the Enabling the BFD Feature section.

ConfiguretheBFDsessionparameters.SeetheConfiguringGlobalBFDParameterssectionortheConfiguring BFD on an Interface section.

Enable the BGP feature. See the Cisco Nexus 9000 Series NX-OS Unicast Routing Configuration Guide for more information.

## SUMMARY STEPS

1. configure terminal

2. router bgp as-number

3. neighbor (ip-address | ipv6-address) remote-as as-number

4. bfd [multihop | singlehop]

5. update-source interface

6. show running-config bgp

7.

copy running-config startup-config

## DETAILED STEPS

Procedure

|  | 600001800 0726000 | 『00 ㅁ 056 |
|---|---|---|
| 51601 | ㅇ 0008406 (60001021 | 21666 000118408000 20006. |

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

|

|

171

| |

## Configuring Bidirectional Forwarding Detection

' |

## Configuring BFD on EIGRP

| 5160 2 | 10466 082 45-721072706/" 터 3 머 만 미하 91608 (000519)# ㅠ 0066 ㅁ 5695 64496 81601 (602 호 19- ㄴ 00466) 0 | 8086166 83632 300 3561805 016 스 8 ㅁ 04020667 (0 0416 10081 8( 가 9506866. 1116 스 8 ㅁ 001060 080 06 8 16-0141 10168 07 8 32-11 106686[ 10 016 10070 01 8 418067 16-611 06010181 0402067 800 8.10\66 16-611 06010781440166/ 10 33363 10008. |
|---|---|---|
| 5160 3 | 프 리 유 1006 (772200007659 | 22220-0007659) 760006(6-85 09-772077/76/' 터 3 머 만 미하 31600 (00202,19- ㄴ 04662) 코 2 ㅁ 6319560 노 209.165.201.1 ㅜ ㅠ 6040 ㄴ 6 ㅇ -325 64497 81600 (602 ㅁ 19- ㅋ 04662- ㅁ 6191605) * | | (0001184165 0416 1074 07 1076 8007688 800 ^ 0 ㅁ 00106 107 8 1600016 83632 7660. 1116 227-0007659 10078 16 ×%.×.×. 1116 22106-0007659 100086(16 ^183:1(':12. |
| 5160 4 | 1010 [ 따 비 0002 | 91081680002] 터 3 머 만 미하 _ 901600 (0005197004666006198605)* 520 001611002 | (2001184168 0416 812 20411 1102 07 510816 11070 5669107 07 16 06\066. 1116 061341616 \10100 65\010. \1160 704 00 001 9060117 805 665\010 800 11 016 0667 19 01060017 000060160 14460 8 91016 1102 5655100 15 56160660, 1 016 0667 16 00 000060660 04160 80416 11072 56891072 [706 16 561606(60. \1161 304 6060117 8 ""2041101102" 07 "910816402'"" 00007, 016 6669101 1970616 [07000 10 8 06106 800070108 10 016 ((1.1 00 ㅁ 027. |
| 5160 5 | 1400866-501416@ 7777077000 터 3 머 만 미하 3816056 (000219-1 ㄴ ㅋ 04665- ㅁ 6191000 ㄴ ) * 146002 ㄴ 6-501 ㅁ ~ ㄴ 06 66620 ㅁ 66 2/1 | 스 110\9 8630 66961009 (0 456 0416 00101877 10 40076869 17010 6 7280010418710162306 89 0416 10081 3007689 \160 10701108 8 2690 6656107 ㅁ \101 8 001811607 800 6080169 8702 (0 76815167 39 3 01160 \101 872, ： |
| 5160 6 | 9410\ 70070108-00008 082 60801016: 81600 (602 ㅁ ,19- ㅋ 04662- ㅁ 6191602) * 90 듀 포 040 ㅁ 0 ㅁ 1 ㅁ 09- ㅇ 07 ㅁ = ㅋ 19 52952 | (06000081) 219201876 016 89402 0 ㅁ 100108 0001184780 ㅁ 07. |
| 5160 7 | 6003 7000108-60018 56『060040-607018 60801016: 31600 (0020219- ㄴ ㅋ 04662- ㅁ 61910605) 기 0002 포 42 ㅁ 0 ㅁ 10 ㅁ 09- ㅇ 072 ㅋ 19 5 ㄴ 2 ㄴ ㅋ ㄴ 060-0 ㅇ 0 ㅁ 219 | (0000081) 58765 016 6001184180070 0118086. |

## Configuring BFD on EIGRP

You can configure BFD for the Enhanced Interior Gateway Routing Protocol (EIGRP).

## Before you begin

Enable the BFD feature. See the Enabling the BFD Feature section.

ConfiguretheBFDsessionparameters.SeetheConfiguringGlobalBFDParameterssectionortheConfiguring BFD on an Interface section.

Enable the EIGRP feature. See the Cisco Nexus 9000 Series NX-OS Unicast Routing Configuration Guide for more information.

|

|

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

172

ㅣ

|!

## Configuring Bidirectional Forwarding Detection

## Configuring BFD on EIGRP

## SUMMARY STEPS

1. configure terminal

2. router eigrp instance-tag

3. bfd [ipv4 | ipv6]

4. interface int-if

5.

ip eigrp instance-tag bfd

6. show ip eigrp [vrf vrf-name] [ interfaces if]

7.

copy running-config startup-config

## DETAILED STEPS

Procedure

| 51601 | 000841@ 6(60001021 6801016: 3016010# 007 ㅁ 5*1094 ㅠ 6 ㄴ 62 ㅋ 0 ㅁ 17 ㅁ 21 으 1606 (6020 조 10) 부 | 뜨 26606 60011841780070 00006. |
|---|---|---|
| 5160 2 | 10416 01800 7779707/700-78 6801016: 31606 (0020219) 부 20404662 61928 또 66 느 1 | (2768666 820\ 616 100000658 \101 0416 0001184160 10968006 응 . 1116 10918006 108 음 080 66 807 0896-660616176, 히 218041006116 50020 응 42 (0 20 011878 이 668. |
| 51608 (0072 ㅁ 519- ㄴ 04666) | 704 000118416 80 10918006-188 04186 0068 001 0481117 85 870 스 832 ㅁ 00166 704 20466 496 016 441000100145-5556604 10 0600118416 016 스 68 ㅁ 04101667 6%011010 07 04116 1632 10968006 \111 7600810 10 016 9114100\70 66816. |
| 5160 4 | 1066 타 406 77277" 6801016: 31600 (6022,19- ㄴ 04662-0 ㅁ 619100605) 쿠 12 ㅁ 6622206 @65 ㅁ 62 ㅁ 6 ㄴ 2/1 요다 (60208,106-1 조 ) 부 | 뜨 까 (666 10660806 6000118478000 00006. 04066 016 ? 65\010 10 0192187 0416 547000060 106(603069. 2080 00 |
| 5160 5 | 10 이 00 7779707700-7248 010 606801016: 3016006 (0020219-1 ㅁ 2) 16 61928 661 520 | (06000081) 8080165 07 016860166 312 0 ㅁ 80 01660 1041601306. 7116 10968006 18 080 06 807 0866-660910176, 81011804106010 ; 5000 응 42 160 20 01187801668. 7116 061341118 01686160. |
| 5160 6 | 940\ 190 01800 [히드 177-770770] | 1066 타 40605 27/] 6801016: | (0000081) 12190187510100708000 80041 10642 1116 777707776 0820 66 807 0856-9609106, 8101180410046016 50148 472 (0 32 이 180806669. |

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

|

|

173

렐

## Configuring Bidirectional Forwarding Detection

|

## Configuring BFD on OSPF

:

|  | 600007800 0726000 | 『00 ㅁ 056 |
|---|---|---|
| 0160 7 | 6003 7000108-60018 56『060040-607018 | (06000081) 58768 0416 0001184780070 0118086. |
| 60801016: |  |
| 31606 (6020219-12) 우 0002 |  |

Step 7

## Configuring BFD on OSPF

You can configure BFD for the Open Shortest Path First.

## Before you begin

Enable the BFD feature. See the Enabling the BFD Feature section.

ConfiguretheBFDsessionparameters.SeetheConfiguringGlobalBFDParameterssectionortheConfiguring BFD on an Interface section.

Enable the OSPF feature. See the Cisco Nexus 9000 Series NX-OS Unicast Routing Configuration Guide for more information.

## SUMMARY STEPS

1. configure terminal

이윤 언 온 8=

2. router ospf instance-tag

3. bfd [ipv4 | ipv6]

- interface int-if

5. ip ospf bfd

6. show ip ospf [vrf vrf-name] [ interfaces if]

7.

copy running-config startup-config

## DETAILED STEPS

Procedure

|  | 600007800 0726000 | 『00 ㅁ 056 |
|---|---|---|
| 51601 | 000847@ 6(60001021 60801016: 3016010# 007 ㅁ 5*1094 ㅠ 6 ㄴ 62 ㅋ 0 ㅁ 17 ㅁ 21 으 1606 (6020 조 10) 부 | 트 마 666 인 06861 00011841780070 20006. |
| 5160 2 | 10416 0901 7779707700-78 60801016: 31606 (60202,19) 우 2004662 0552 200 으 라 포 00 (60208,196- ㄴ 04662) 퓨 | (2768666 826\ 06 반 7 10618006 \101 416 00201184760 10968006 응 . 1116 10918006 108 음 080 66 807 0896-660616176, 뼈 히 218041006116 50020 응 42 (0 20 011878 이 668. |
| 5160 3 | 1010 [1024 | 1056] 60801016: | (0000081) 80860166 3012 107 311 060 1416 다 3068. |

|

|

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

174

ㅣ

|!

## Configuring Bidirectional Forwarding Detection

## Configuring BFD on IS-IS

|  | 81600 (6002106- ㄴ 04662) 520 |  |
|---|---|---|
| 5160 4 | 1066 타 406 77277" 8 배 기 0: 3801600(600210- ㄴ 04662) + 12 ㅁ 6622206 @65 ㅁ 62 ㅁ 6 ㄴ 2/1 조 ) | 뇨 26666 10660806 60201184780020 00006. 04066 016 ? 65\070 10 0190187 016 5940001060 106(608068. |
| 5160 5 | 10 0501 1010 6801016: 3901606 (0020219-12) 부 126 ㅇ 05282 520 | (06000081) 80860166 07 01680168 212 02 80 (06 바 7 104(6 다 306. 7116 061341118 01686160. |
| 5160 6 | 5940\ 110 0501 [두다 177-770770] | 106(0 다 2005 77] 6801016: 31606 (0020219-12) 에 5860 16 ㅇ 5 푼 주 | (060002081) 21621876 10100208000 80041 08 바 6. 1116 77-7204776 0820 66 807 0856-9609106, 8101180410046016 50148 472 (0 32 이 180806669. |
| 5160 7 | 003 70070108-000118 564『0410-607018 6801016: 31606 (6020219-12) 우 0002 포 42 ㅁ 0 ㅁ 10 ㅁ 09- ㅇ 072 ㅋ 19 5 ㄴ 2 ㄴ ㅋ ㄴ 060-0 ㅇ 0 ㅁ 219 | (06000081) 58768 0416 0001184780070 0118086. |

## Example Configurations for BFD on OSPF

Example configuration where BFD is enabled under a non-default VRF (OSPFv3 neighbors in vrf3).

configure terminal router ospfv3 10 vrf vrf3 bfd

## Configuring BFD on IS-IS

You can configure BFD for the Intermediate System-to-Intermediate System (IS-IS) protocol.

## Before you begin

Enable the BFD feature. See the Enabling the BFD Feature section.

ConfiguretheBFDsessionparameters.SeetheConfiguringGlobalBFDParameterssectionortheConfiguring BFD on an Interface section.

Enable the IS-IS feature. See the Cisco Nexus 9000 Series NX-OS Unicast Routing Configuration Guide for more information.

## SUMMARY STEPS

1. configure terminal

2. router isis instance-tag

3. bfd [ipv4 | ipv6]

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

|

|

175

## Configuring Bidirectional Forwarding Detection

|

## Configuring BFD on IS-IS

4. interface int-if

5. isis bfd

6. show isis [vrf vrf-name] [ interface if]

- copy running-config startup-config

## DETAILED STEPS

Procedure

| 51601 | 000847@ 6(60001021 60801016: 3016010# 007 ㅁ 5*1094 ㅠ 6 ㄴ 62 ㅋ 0 ㅁ 17 ㅁ 21 으 1606 (6020 조 10) 부 | 트 마 666 인 06861 00011841780070 20006. |
|---|---|---|
| 5160 2 | 10416 1515 77759707200-708 60801016: 81600 (60016) 부 2006682 15615 100 81600 (6022196- ㄴ 04162) 26. 49.0001.1720.1600.1001.00 31600 (06025219- ㄴ 04662) 쑤 20026565- 에 20117 12876 1 ㅁ 0 ㅁ 10 ㅇ 288 | (2768666 82 ㅁ 6\ 19-19 106[8006 \101 416 00701184160 7775707706 708. @ |
| 5160 3 | 1010 [1024 | 1056] 60801016: 81600 (6002106- ㄴ 04662) 520 | (0000081) 80860166 3012 107 311 060 1416 다 3068. |
| 5160 4 | 1066 타 406 77277" 60801016: 3801600(600210- ㄴ 04662) + 12 ㅁ 6622206 @65 ㅁ 62 ㅁ 6 ㄴ 2/1 요다 (60208,106-1 조 ) 부 | 뜨 26(666 106(6 다 806 60020118478000 00006. 04066 016 ? 65\010 10 0192187 0416 547000060 106(603069. 나니 00 |
| 5160 5 | 1515 010 60801016: 8016006(600210-12) 18615 1520 | (06000081) 08660166 07 01680166 812 00 80 19-19 106(60306. 7116 061341118 01686160. |
| 5160 6 | 5410 뉴 1515 [두다 177-770776] | 1060 다 400 77] 60801016: 을 리 2600 (06020216-1<) 부 980 19518 | (060060081) 121921875 1041000080100 00041 19-19. 1116 177-770776 080 66 80 0856-960911976, 812011890410216016 50710 40 10 32 벌 802 이 180806669. |
| 5160 7 | 003 70070108-000118 564『0410-607018 60801016: 31606 (6020219-12) 우 0002 | (06000081) 58768 0416 0001184780070 0118086. |

|

|

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

176

ㅣ

|!

## Configuring Bidirectional Forwarding Detection

## Configuring BFD on HSRP

## Example Configurations for BFD on IS-IS

Example configuration for IS-IS where BFD is enabled under IPv4 and an IPv6 address family.

configure terminal

router isis isis-1 bfd address-family ipv6 unicast bfd

## Configuring BFD on HSRP

You can configure BFD for the Hot Standby Router Protocol (HSRP). The active and standby HSRP routers track each other through BFD. If BFD on the standby HSRP router detects that the active HSRP router is down, the standby HSRP router treats this event as an active time rexpiry and takes over as the active HSRP router.

The show hsrp detail command shows this event as BFD@Act-down or BFD@Sby-down.

## Before you begin

Enable the BFD feature. See the Enabling the BFD Feature section.

ConfiguretheBFDsessionparameters.SeetheConfiguringGlobalBFDParameterssectionortheConfiguring BFD on an Interface section.

Enable the HSRP feature. See the Cisco Nexus 9000 Series NX-OS Unicast Routing Configuration Guide for more information.

## SUMMARY STEPS

1. configure terminal

2. hsrp bfd all-interfaces

3.

0

interface int-if

4. hsrp bfd

5. show running-config hsrp

6. copy running-config startup-config

## DETAILED STEPS

Procedure

|  | 600001800 0726000 | 『00 ㅁ 056 |
|---|---|---|
| 51601 | 000841@ 6(60001021 | 트 마 666 인 06861 00011841780070 20006. |

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

|

|

177

## Configuring Bidirectional Forwarding Detection

## Configuring BFD on VRRP

|  | 600007800 0726000 | 『00 ㅁ 056 |
|---|---|---|
| 5160 2 | 1390 010 2311-1066 타 4006 60801016: 3016050* 18620 520 211-1 ㅁ ㄴ ㄷ 6 ㄴ | (06000081) 8080166 07 01680166 312 00 311 152 101603068. 7116 061341118 01686160. |
| 5160 3 | 1066 타 406 77277" 8 배 10: 3801600(600210- ㄴ 04662) + 12 ㅁ 6622206 @65 ㅁ 62 ㅁ 6 ㄴ 2/1 요다 (60208,106-1 조 ) 부 | 뇨 26666 10660806 60201184780020 00006. 04066 016 ? 65\070 10 0190187 016 5940001060 106(608068. |
| 5160 4 | 6500 010 60801016: 31608 (600219-12) 구 56926 520 | (06000081) 8080166 07 01986166 812 00 00 152 101(60306. 7116 061341118 01686160. |
| 5660 5 | 9410\ 1704070108-000108 1500 60801016: 31606 (0020219-12) 부 580 294001 | (06000081) 219218576 016 216 2100108 0021184780 ㅁ 07. |
| 5660 6 | 003 70070108-000118 564『0410-607018 60801016: 31606 (6020219-12) 우 0002 포 42 ㅁ 0 ㅁ 10 ㅁ 09- ㅇ 072 ㅋ 19 5 ㄴ 2 ㄴ ㅋ ㄴ 060-0 ㅇ 0 ㅁ | (06000081) 58768 0416 0001184780070 0118086. |

## Configuring BFD on VRRP

You can configure BFD for the Virtual Router Redundancy Protocol (VRRP). The active and standby VRRP routers track each other through BFD. If BFD on the standby VRRP router detects that the active VRRP router is down, the standby VRRP router treats this event as an active time rexpiry and takes over as the active VRRP router.

The show vrrp detail command shows this event as BFD@Act-down or BFD@Sby-down.

## Before you begin

Enable the BFD feature. See the Enabling the BFD Feature section.

ConfiguretheBFDsessionparameters.SeetheConfiguringGlobalBFDParameterssectionortheConfiguring BFD on an Interface section.

Enable the VRRP feature. See the Cisco Nexus 9000 Series NX-OS Unicast Routing Configuration Guide for more information.

## SUMMARY STEPS

1. configure terminal

2.

interface int-if

3. vrrp group-no

4. vrrp bfd address

|

|

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 10.5(x)

178

ㅣ