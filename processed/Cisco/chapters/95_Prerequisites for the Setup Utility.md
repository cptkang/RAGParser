---
title: "Prerequisites for the Setup Utility"
page_start: 34
page_end: 34
level: 2
---

## Prerequisites for the Setup Utility

Figure2:SetupScriptFlow

| 51304 06 비 06 노고 56 30100 ㅁ ㅁ 255\010 100 0 ㄷ 606「5 하 냐 티 가 만 006 | 0507 660 ㅁ 00007200 00000 ^ 600019416 06 | 더 0- ㅇ 06\06 86 0 여 0-6 5306 300 3001 0009 바 레 0 ㅁ 님 도

This figure shows how to enter and exit the setup script.

You use the setup utilitymainlyfor configuringthe systeminitially, when no configurationis present.However, you can use the setup utility at any time for basic device configuration. The setup utility keeps the configured values when you skip steps in the script. For example, if you have already configured the mgmt0 interface, the setup utility does not change that configuration if you skip that step. However, if there is a default value for the step, the setup utility changes to the configuration using that default, not the configured value. Be sure to carefully check the configuration changes before you save the configuration.

<

- Note Be sure to configure the IPv4 route, the default network IPv4 address, and the default gateway IPv4 address to enable SNMP access. If you enable IPv4 routing, the device uses the IPv4 route and the default network IPv4 address. If IPv4 routing is disabled, the device uses the default gateway IPv4 address.

<

- Note

The setup script only supports IPv4.