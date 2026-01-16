---
title: "Verifying NXDC configuration and status"
page_start: 186
page_end: 187
level: 2
---

## Verifying NXDC configuration and status

To verify the NXDC configuration, use the following Bash commands:

To display the NXDC configuration and status information, enter one of the following commands:

| 940\ 5556(0600 0651066-060006010『 이 3100-1010: | 1216016579 016 06166 860181 페 402666, 1060 800 10(66791214[ 01121 51866. |
|---|---|
|  | 10478000 107 ㅋ 8110 (060 16 70000 ㅁ 60 10 56001008. |
| 940\ 5556(0600 001066-00006 ㅇ 6010 10 음 10 이 069170 이 000414702 이 941602001206<6 | 1216018579 06\106 000060[07 10 226598869. |

The following example shows sample output for the show system device-connector claim-info command before device is claimed:

```cisco-ios
Switch# show system device-connector claim-info
```

SerialNumber: FDO23021ZUJ SecurityToken: 9FFD4FA94DCD Duration: 599 Message: Claim state: Not Claimed

Thefollowingexampleshows sampleoutputfor theshow systemdevice-connectorclaim-infocommandafter device is claimed:

```cisco-ios
Switch# show system device-connector claim-info SerialNumber: ABCD12345E6 SecurityToken: Duration: 0 Message: Cannot fetch claim code for already claimed device Claim state: Claimed Claim time: 2024-02-18T12:00:01.77Z Claimed by: user@cisco.com Account: dc- customer Site name: Site ID:
```

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

170

ㅣ

|!