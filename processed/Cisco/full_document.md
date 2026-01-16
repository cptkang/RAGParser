이 이 111 01560.

## Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

First Published: 2025-08-13

## Americas Headquarters

Cisco Systems, Inc. 170 West Tasman Drive San Jose, CA 95134-1706 USA http://www.cisco.com Tel: 408 526-4000 800 553-NETS (6387) Fax: 408 527-0883

THE SPECIFICATIONS AND INFORMATION REGARDING THE PRODUCTS REFERENCED IN THIS DOCUMENTATION ARE SUBJECT TO CHANGE WITHOUT NOTICE. EXCEPT AS MAY OTHERWISE BE AGREED BY CISCO IN WRITING, ALL STATEMENTS, INFORMATION, AND RECOMMENDATIONS IN THIS DOCUMENTATION ARE PRESENTED WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED.

The Cisco End User License Agreement and any supplemental license terms govern your use of any Cisco software, including this product documentation, and are located at: https://www.cisco.com/c/en/us/about/legal/cloud-and-software/software-terms.html. Cisco product warranty information is available at https://www.cisco.com/c/en/us/products/ warranty-listing.html. US Federal Communications Commission Notices are found here https://www.cisco.com/c/en/us/products/us-fcc-notice.html.

IN NO EVENT SHALL CISCO OR ITS SUPPLIERS BE LIABLE FOR ANY INDIRECT, SPECIAL, CONSEQUENTIAL, OR INCIDENTAL DAMAGES, INCLUDING, WITHOUT LIMITATION, LOST PROFITS OR LOSS OR DAMAGE TO DATA ARISING OUT OF THE USE OR INABILITY TO USE THIS MANUAL, EVEN IF CISCO OR ITS SUPPLIERS HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

Any products and features described herein as in development or available at a future date remain in varying stages of development and will be offered on a when-and if-available basis. Any such product or feature roadmaps are subject to change at the sole discretion of Cisco and Cisco will have no liability for delay in the delivery or failure to deliver any products or feature roadmap items that may be set forth in this document.

Any Internet Protocol (IP) addresses and phone numbers used in this document are not intended to be actual addresses and phone numbers. Any examples, command display output, network topology diagrams, and other figures included in the document are shown for illustrative purposes only. Any use of actual IP addresses or phone numbers in illustrative content is unintentional and coincidental.

The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product.

Cisco and the Cisco logo are trademarks or registered trademarks of Cisco and/or its affiliates in the U.S. and other countries. To view a list of Cisco trademarks, go to this URL: https://www.cisco.com/c/en/us/about/legal/trademarks.html. Third-party trademarks mentioned are the property of their respective owners. The use of the word partner does not imply a partnership relationship between Cisco and any other company. (1721R)

© 2025 Cisco Systems, Inc. All rights reserved.

C O N T E N T S

| 대 타 4 안 |  |  |  |
|---|---|---|---|
|  |  | 4016006 3001 |  |  |
|  |  | 10004104610[(0007600008 3001 |  |  |
|  |  | 100000060680070 107 (21600 페 6%46 9000 5612166 | 5\1601169 | - 300 |
|  |  | 10004146101[8000『6606806 30 |  |  |
|  |  | (2070000401068060108, 56001068, 800 8001110081 ㅁ | 10107000800 0 300 |  |
|  |  | 248 56870 1001 0 |  |  |
|  |  | 10004100601[80080 16606806 06 |  |  |
| 매 30168 | 1 | 130860 10100043000 1 |  |  |
|  | 800 (]180860 10100708000 1 |  |  |
| 매 2『16 | 2 |  |  |  |
|  | 1660910 은 복 604106046016 8 |  |  |
|  | 4000060 ?131020006 3 |  |  |
|  | 0110\0876 10886 3 |  |  |
|  | 011\876 ()00008061160 4 |  |  |
|  | 0106/168 10001085 4 |  |  |
|  | 1004167 5011\816 1066180 ㅁ 4 |  |  |
|  | 6001068601167 4 |  |  |
|  | \110160 202 ㅅ 6815260 4 |  |  |
|  | 0080815260 5 |  |  |
|  | (811 0006 5 |  |  |
|  | 0201106 10188008008 5 |  |  |

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

iii

| | 060066065

## Contents

C H A P T E R 3

Embedded Event Manager 5 Manageability 5 Simple Network Management Protocol 5 Configuration Verification and Rollback 5 Role-Based Access Control 6 Cisco NX-OS Device Configuration Methods 6 Programmability 6 Python API 6 Tcl 6 Cisco NX-API 6 Bash Shell 7 Broadcom Shell 7 Traffic Routing, Forwarding, and Management 7 Ethernet Switching 7 IP Routing 8 IP Services 8 IP Multicast 8 Quality of Service 9 Network Security Features 9 Supported Standards 10 Using the Cisco NX-OS Setup Utility 17 About the Cisco NX-OS Setup Utility 17 Prerequisites for the Setup Utility 18

Setting Up Your Cisco NX-OS Device

19

Additional References for the Setup Utility 24

Related Documents for the Setup Utility 24

- C H A P T E R 4 Using PowerOn Auto Provisioning 25

- About PowerOn Auto Provisioning 25

Network Requirements for POAP 25

Secure Download of POAP Script

26

Network Requirements for Secure POAP 29

- Deployment Scenarios 29

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

iv

SUDI Supported Device as File Server 29 Non-SUDI Supported Device as a File Server 30 Benchmark Configured Device 31 Secure POAP on a Device Shipped with Old Image 31 Troubleshooting Secure POAP 32 Disabling POAP 32 POAP Configuration Script 33 POAP Configuration Script 33 Using the POAP Script and POAP Script Options 34 Setting up the DHCP Server without DNS for POAP 37 Downloading and Using User Data, Agents, and Scripts as part of POAP 37 POAP Process 38 Power-Up Phase 39 USB Discovery Phase 40 DHCP Discovery Phase 40 Script Execution Phase 42 Post-Installation Reload Phase 42 POAPv3 42 Guidelines and Limitations for POAP 44 Setting Up the Network Environment to Use POAP 46 Configuring a Switch Using POAP 46 Creating md5 Files 47 Verifying the Device Configuration 49 Troubleshooting for POAP 50 Managing the POAP Personality 50 POAP Personality 50 Backing Up the POAP Personality 51 Configuring the POAP Personality 51 Restoring the POAP Personality 53

- POAP Personality Sample Script 53

- C H A P T E R 5 Using Network Plug and Play 55

About Network Plug and Play 55

Guidelines and Limitations for Network Plug and Play 62

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

060066065 | |

## Contents

v

| | 060066065

## Contents

C H A P T E R 6

vi

|

|

- Troubleshooting Examples for Network Plug and Play 63

Understanding the Command-Line Interface 69 About the CLI Prompt 69 Command Modes 70 EXEC Command Mode 70 Global Configuration Command Mode 70 Interface Configuration Command Mode 71 Subinterface Configuration Command Mode 72 Saving and Restoring a Command Mode 72 Exiting a Configuration Command Mode 73 Command Mode Summary 73 Special Characters 74 Keystroke Shortcuts 75 Abbreviating Commands 78 Completing a Partial Command Name 78 Identifying Your Location in the Command Hierarchy 79 Using the no Form of a Command 79 Configuring CLI Variables 80 About CLI Variables 80 Configuring CLI Session-Only Variables 81 Configuring Persistent CLI Variables 81 Command Aliases 82 About Command Aliases 82 Defining Command Aliases 83 Configuring Command Aliases for a User Session 84 Command Scripts 85 Running a Command Script 85 Echoing Information to the Terminal 85 Delaying Command Action 86 Context-Sensitive Help 87 Understanding Regular Expressions 88

Special Characters

Multiple-Character Patterns

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

C H A P T E R 7

Anchoring 89 Searching and Filtering show Command Output 89 Filtering and Searching Keywords 90 diff Utility 91 grep and egrep Utilities 92 less Utility 93 Mini AWK Utility 93 sed Utility 93 sort Utility 93 Searching and Filtering from the --More-- Prompt 94 Using the Command History 95 Recalling a Command 95 Controlling CLI History Recall 95 Configuring the CLI Edit Mode 96 Displaying the Command History 96 Enabling or Disabling the CLI Confirmation Prompts 97 Setting CLI Display Colors 97 Sending Commands to Modules 98 Sending Command Output in Email 99 BIOS Loader Prompt 101 Examples Using the CLI 101 Using the System-Defined Timestamp Variable 101 Using CLI Session Variables 101 Defining Command Aliases 102 Running a Command Script 102 Sending Command Output in Email 103 Configuring Terminal Settings and Sessions 105 About Terminal Settings and Sessions 105 Terminal Session Settings 105 Console Port 105

Virtual Terminals

-

106

Default Settings for File System Parameters

106

Configuring the Console Port

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

060066065 | |

## Contents

vii

| | 060066065

## Contents

Configuring Virtual Terminals

108

Configuring the Inactive Session Timeout

108

Configuring the Session Limit

109

Clearing Terminal Sessions

110

Displaying Terminal and Session Information 110

- C H A P T E R 8 Basic Device Management 113

About Basic Device Management

113

Device Hostname

113

Message-of-the-Day Banner

113

Device Clock 113

Clock Manager 114

Time Zone and Summer Time (Daylight Saving Time)

User Sessions

-

114

Default Settings for Basic Device Parameters

114

Changing the Device Hostname

114

Configuring the MOTD Banner

115

Configuring the Time Zone

117

Configuring Summer Time (Daylight Saving Time)

117

Manually Setting the Device Clock 119

Setting the Clock Manager

119

Managing Users

120

Displaying Information about the User Sessions

120

Sending a Message to Users

121

Verifying the Device Configuration 121

- C H A P T E R 9 Using the Device File Systems, Directories, and Files 123

About the Device File Systems, Directories, and Files

123

File Systems 123

Directories 124

## Files 124

Guidelines and Limitations 125

Default Settings for File System Parameters

125

Configuring the FTP, HTTP, or TFTP Source Interface

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

viii

114

Working with Directories 126 Identifying the Current Directory 126 Changing the Current Directory 126 Creating a Directory 127 Displaying Directory Contents 127 Deleting a Directory 128 Accessing Directories on the Standby Supervisor Module Working with Files 129 Moving Files 129 Copying Files 130 Copying Files Using HTTP or HTTPS 131 Deleting Files 131 Displaying File Contents 132 Displaying File Checksums 132 Compressing and Uncompressing Files 133 Displaying the Last Lines in a File 133 Redirecting show Command Output to a File 134 Finding Files 134 Formatting the Bootflash 135 Working with Archive Files 136 Creating an Archive File 136 Appending Files to an Archive File 137 Extracting Files from an Archive File 138 Displaying the Filenames in an Archive File 138 SSD Re-partitioning 139 Enable or Disable Tech-Support Command 141 Displaying Tech-support Blocked CLIs 141

129

Examples of Using the File System 142

Accessing Directories on Standby Supervisor Modules

Moving Files 142

Copying Files 143

Deleting a Directory 143

Displaying File Contents 144

Displaying File Checksums

144

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

060066065 | |

## Contents

ix

| | 060066065

## Contents

C H A P T E R 1 0

C H A P T E R 1 1

x

|

|

Compressing and Uncompressing Files 145 Redirecting show Command Output 145 Finding Files 146

Working with Configuration Files

147

About Configuration Files 147 Types of Configuration Files 147 Guidelines and Limitations for Configuration Files 148 Managing Configuration Files 148 Saving the Running Configuration to the Startup Configuration 148 Copying a Configuration File to a Remote Server 148 Downloading the Running Configuration From a Remote Server 149 Downloading the Startup Configuration From a Remote Server 150 Copying Configuration Files to an External Flash Memory Device 152 Copying the Running Configuration from an External Flash Memory Device Copying the Startup Configuration From an External Flash Memory Device Copying Configuration Files to an Internal File System 154 Rolling Back to a Previous Configuration 155 Removing the Configuration for a Missing Module 156 Erasing a Configuration 157 Clearing Inactive Configurations 158 Configuration Archive and Configuration Log 159 Information About Configuration Archive 159 Configuring the Characteristics of the Configuration Archive 160 Information About Configuration Log 161 Displaying Configuration Log Entries 162 Verifying the Device Configuration 163 Examples of Working with Configuration Files 165 Copying Configuration Files 165 Backing Up Configuration Files 165 Rolling Back to a Previous Configuration 165 Nexus Switch Intersight Device Connector 167 Nexus Switch Intersight Device Connector Overview 167 153 154

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

Guidelines and Limitations

Configuring Nexus Switch to Intersight 168 Verifying NXDC configuration and status 170 Claiming Nexus Switches in Intersight 171

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

060066065 | |

## Contents

xi

| | 060066065

## Contents

xii

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

## Preface

This preface includes the following sections:

- • Audience, on page xiii

- • Document Conventions, on page xiii

- • Related Documentation for Cisco Nexus 9000 Series Switches, on page xiv

- • Documentation Feedback, on page xiv

- • Communications, services, and additional information, on page xiv

## Audience

This publication is for network administrators who install, configure, and maintain Cisco Nexus switches.

## Document Conventions

Command descriptions use the following conventions:

| 10010 | 2010 (6 100168666 0416 6000018008 800 65\0108 04186 704 60167 11678117 89 91101\0. |
|---|---|
| 77070 | 11311 (6 1001068166 818404606[6 1017 \1110611 704 54721 06 81468. |
| |] | 옥 64816 608 아 665 60 이 056 80 02000081 이 600601 (6657\070 07 81 용 404600. |
| | | 옥 64816 608 이 6665 60 이 09108 65\0708 07 8184016066 0186 8206 560878(60 605 87600106816871040108[6 830 02000081 00166. |
| {8 | 까 | 278068 60 이 0610 음 65\0109 07 818410046066 0418 8706 5608186(60 67 8 7600081 1687 10010866 8 70041760 0110106. |
| [8 1512} ] | 제 66660 661 01 50448176 018 아 6[5 07 078065 14010866 00001081 07 76041260 00010666 \104110 0000481 07 76041760 인 60016015. 3178069 800 8 ㅋ 6001681 687 \10110 504816 678066669 14016816 8 76041060 0110166 \10110 80 000 ㅁ 07081 이 60060 |

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

xiii

## Preface

| |

## Related Documentation for Cisco Nexus 9000 Series Switches

| 78 ㅁ 12616@ | 1001068666 878281616 107 1\111011 704 5420015 81468, 10 0017016※% \11606 1181108 68000 66 4560. |
|---|---|
| 9011 음 | 스 200040160 66 01 이 18080 이 669. 120 ㅁ 001 466 040180070 048 다 6 8704200 1016 9011 을 07 0416 660040 응 10014068 0416 04018007 0481469. |

Examples use the following conventions:

| 50 ㄴ 667 ㅁ ,02 ㅁ ㄴㄴ |  | 그 60001081 56661005 800 1010100081107 016 5\4011 0160185 876 10 50000 101 |
|---|---|---|
| 15010*2206 50 ㄴ 6 ㅎ 66 ㅁ | .ｌ.0 ㄴ | 10[000080080 01866 704 00496 60167 16 10 60101306 507600 10201. |
| 7707/70 50766007. 70777 |  | 스 7841006066 107 \11014 704 94701 81466 816 10 118116 507660 10701. |
| <> |  | 떼 001201001 을 아 180006(668, 54011 89 2896\0109, 816 10 8016 018016618. |
| [] |  | 1061341[766000969 10 5761610 0001007066 876 10 504816 6078016665. |
| 트고 |  | 스 ㅁ 68 이 30480020 20106 (!) 0『 8 00400 51920 (#) 81 016 66810010 을 01 8 110 이 600061040168669 8 600000606[ 1106. |

Terminal sessions and information the switch displays are in screen font.

An exclamation point (!) or a pound sign (#) at the beginning of a line

## Related Documentation for Cisco Nexus 9000 Series Switches

The entire Cisco Nexus 9000 Series switch documentation set is available at the following URL:

https://www.cisco.com/en/US/products/ps13386/tsd_products_support_series_home.html

## Documentation Feedback

To provide technical feedback on this document, or to report an error or omission, please send your comments to nexus9k-docfeedback@cisco.com. We appreciate your feedback.

## Communications, services, and additional information

- • To receive timely, relevant information from Cisco, sign up at Cisco Profile Manager.

- • To get the business impact you’re looking for with the technologies that matter, visit Cisco Services.

- • To submit a service request, visit Cisco Support.

- • To discover and browse secure, validated enterprise-class apps, products, solutions, and services, visit Cisco DevNet.

- • To obtain general networking, training, and certification titles, visit Cisco Press.

- • To find warranty information for a specific product or product family, access Cisco Warranty Finder.

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

xiv

ㅣ

|

## Preface

## Cisco Bug Search Tool

## Cisco Bug Search Tool

CiscoBug SearchTool (BST) is a gatewayto the Ciscobug-trackingsystem,which maintainsa comprehensive list of defects and vulnerabilities in Cisco products and software. The BST provides you with detailed defect information about your products and software.

## Documentation feedback

To provide feedback about Cisco technical documentation, use the feedback form available in the right pane of every online document.

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

xv

| |

| |

## Documentation feedback

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

xvi

## Preface

ㅣ

1

C H A P T E R 1

## New and Changed Information

- • New and Changed Information, on page 1

## New and Changed Information

## Table1:NewandChangedFeatures

| 『680116 | 066000000 | 0180960 10 『1016056 | \1616 00000160160 |
|---|---|---|---|
| 200 900000 ㅁ 020 지 9336()-91 | 스 0060 940000107204 ㅅ 0 00 (1900 페 9336(:-6019\11001 | | 10.6(1)『 | (3410611068 800 1.0201660008 10720 ㅅ 0. 00 72886 44 |

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

1

| |

## New and Changed Information

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

2

## New and Changed Information

ㅣ

2

C H A P T E R 2

## Overview

This chapter contains these sections:

- • Licensing Requirements, on page 3

- • Supported Platforms, on page 3

- • Software Image, on page 3

- • Software Compatibility, on page 4

- • Serviceability, on page 4

- • Manageability, on page 5

- • Programmability, on page 6

- • Traffic Routing, Forwarding, and Management, on page 7

- • Quality of Service, on page 9

- • Network Security Features, on page 9

- • Supported Standards, on page 10

## Licensing Requirements

For a complete explanation of Cisco NX-OS licensing recommendations and how to obtain and apply licenses, see the Cisco NX-OS Licensing Guide and the Cisco NX-OS Licensing Options Guide .

## Supported Platforms

Use the Nexus Switch Platform Support Matrix to know from which Cisco NX-OS releases various Cisco Nexus 9000 and 3000 switches support a selected feature.

## Software Image

The Cisco NX-OS software consists of one NXOS software image.

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

3

## Overview

| |

## Software Compatibility

## Software Compatibility

The Cisco NX-OS software interoperates with Cisco products that run any variant of the Cisco IOS software. The Cisco NX-OS software also interoperates with any networking operating system that conforms to the IEEE and RFC compliance standards.

## Spine/Leaf Topology

The Cisco Nexus 9000 Series switches support a two-tier spine/leaf topology.

## Figure1:Spine/LeafTopology

This figure shows an example of a spine/leaf topology with four leaf switches (Cisco Nexus 9396 or 93128) connecting into two spine switches (Cisco Nexus 9508) and two 40G Ethernet uplinks from each leaf to each

띠 6015 9508 시 645 9508 ㄴ 6 하 1 Ｌ6 라 그 61 3 Ｌ ㄴ 6214 30448 1×4066

spine.

## Modular Software Design

The Cisco NX-OS software supports distributed multithreaded processing on symmetric multiprocessors (SMPs), multi-core CPUs, and distributed data module processors. The Cisco NX-OS software offloads computationally intensive tasks, such as hardware table programming, to dedicated processors distributed across the data modules. The modular processes are created on demand, each in a separate protected memory space. Processes are started and system resources are allocated only when you enable a feature. A real-time preemptive scheduler helps to ensure the timely processing of critical functions.

## Serviceability

The Cisco NX-OS software has serviceability functions that allow the device to respond to network trends and events. These features help you with network planning and improving response times.

## Switched Port Analyzer

The Switched Port Analyzer (SPAN) feature allows you to analyze all traffic between ports (called the SPAN source ports) by nonintrusively directing the SPAN session traffic to a SPAN destination port that has an external analyzer attached to it. For more information about SPAN, see the Cisco Nexus 9000 Series NX-OS System Management Configuration Guide.

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

4

|

|

## Overview

## Ethanalyzer

## Ethanalyzer

Ethanalyzer is a Cisco NX-OS protocol analyzer tool based on the Wireshark (formerly Ethereal) open source code. Ethanalyzer is a command-line version of Wireshark for capturing and decoding packets. You can use Ethanalyzer to troubleshoot your network and analyze the control-plane traffic. For more information about Ethanalyzer, see the Cisco Nexus 9000 Series NX-OS Troubleshooting Guide.

## Smart Call Home

The Call Home feature continuously monitors hardware and software components to provide e-mail-based notificationofcriticalsystemevents.Aversatilerangeofmessageformatsisavailableforoptimalcompatibility with standard e-mail and XML-based automated parsing applications. It offers alert grouping capabilities and customizable destination profiles. You can use this feature, for example, to send an e-mail message to a network operations center (NOC) and employ Cisco AutoNotify services to directly generate a case with the Cisco Technical Assistance Center (TAC). For more information about Smart Call Home, see the Cisco Nexus 9000 Series NX-OS System Management Configuration Guide.

## Online Diagnostics

Ciscogenericonlinediagnostics(GOLD)verifythathardwareandinternaldatapathsareoperatingasdesigned. Boot-timediagnostics, continuous monitoring, and on-demand and scheduled tests are part of the Cisco GOLD feature set. GOLD allows rapid fault isolation and continuous system monitoring. For information about configuring GOLD, see the Cisco Nexus 9000 Series NX-OS System Management Configuration Guide.

## Embedded Event Manager

CiscoEmbeddedEventManager(EEM)isadeviceandsystemmanagementfeaturethathelpsyoutocustomize behavior based on network events as they happen. For information about configuring EEM, see the Cisco Nexus 9000 Series NX-OS System Management Configuration Guide.

## Manageability

This section describes the manageability features for the Cisco Nexus 9000 Series switches.

## Simple Network Management Protocol

The Cisco NX-OS software is compliant with Simple Network Management Protocol (SNMP) version 1, version 2, and version 3. A large number of MIBs is supported. For more information about SNMP, see the Cisco Nexus 9000 Series NX-OS System Management Configuration Guide.

## Configuration Verification and Rollback

The Cisco NX-OS software allows you to verify the consistency of a configuration and the availability of necessary hardware resources prior to committing the configuration. You can preconfigure a device and apply the verified configuration at a later time. Configurations also include checkpoints that allow you to roll back to a known good configuration as needed. For more information about rollbacks, see the Cisco Nexus 9000 Series NX-OS System Management Configuration Guide.

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

5

| |

## Overview

| |

## Role-Based Access Control

## Role-Based Access Control

With role-based access control (RBAC), you can limit access to device operations by assigning roles to users. You can customize access and restrict it to the users who require it. For more information about RBAC, see the Cisco Nexus 9000 Series NX-OS Security Configuration Guide.

## Cisco NX-OS Device Configuration Methods

You can use these methods to configure Cisco NX-OS devices:

- • The CLI from a Secure Shell (SSH) session, a Telnet session, or the console port. SSH provides a secure connection to the device. The CLI configuration guides are organized by feature. For more information, see the Cisco NX-OS configuration guides. For more information about SSH and Telnet, see the Cisco Nexus 9000 Series NX-OS Security Configuration Guide.

- • The XML management interface, which is a programmatic method based on the NETCONF protocol that complements the CLI. For more information, see the Cisco NX-OS XML Interface User Guide.

- • The Cisco Nexus Dashboard Fabric Controller (NDFC) client, which runs on your local PC and uses web services on the Cisco NDFC server. The Cisco NDFC server configures the device over the XML management interface. For more information about the Cisco NDFC client, see the Cisco NDFC Fundamentals Guide.

## Programmability

This section describes the programmability features for the Cisco Nexus 9000 Series switches.

## Python API

Python is an easy-to-learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python's elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms. The Python interpreter and the extensive standard library are freely available in source or binary form for all major platforms from the Python website: http://www.python.org/. The Python scripting capability gives programmatic access to the CLI to perform various tasks and Power-On Auto Provisioning (POAP) or Embedded Event Manager (EEM) actions. For more information about the Python API and Python scripting, see the Cisco Nexus 9000 Series NX-OS Programmability Guide.

## Tcl

Tool Command Language (Tcl) is a scripting language. With Tcl, you gain more flexibility in your use of the CLI commands on the device. You can use Tcl to extract certain values in the output of a show command, perform switch configurations, run Cisco NX-OS commands in a loop, or define EEM policies in a script.

## Cisco NX-API

The Cisco NX-API provides web-based programmatic access to the Cisco Nexus 9000 Series switches. This support is delivered through the NX-API open-source web server. The Cisco NX-API exposes the complete configuration and management capabilities of the command-line interface (CLI) through web-based APIs.

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

6

|

|

## Overview

## Bash Shell

You can configure the switch to publish the output of the API calls in either XML or JSON format. For more information about the Cisco NX-API, see the Cisco Nexus 9000 Series NX-OS Programmability Guide.

<

- Note NX-API performs authentication through a programmable authentication module (PAM) on the switch. Use cookies to reduce the number of PAM authentications and thus reduce the load on PAM.

## Bash Shell

The Cisco Nexus 9000 Series switches support direct Linux shell access. With Linux shell support, you can access the Linux system on the switch in order to use Linux commands and manage the underlying system. For more information about Bash shell support, see the Cisco Nexus 9000 Series NX-OS Programmability Guide.

## Broadcom Shell

The Cisco Nexus 9000 Series switch front-panel and fabric module line cards contain several Broadcom ASICs. You can use the CLI to access the command-line shell (bcm shell) for these ASICs. The benefit of using this method to access the bcm shell is that you can use Cisco NX-OS command extensions such as pipe include and redirect output to file to manage the output. In addition, the activity is recorded in the system accountinglogforauditpurposes,unlikecommandsentereddirectlyfromthebcmshell,whicharenotrecorded in the accounting log. For more information about Broadcom shell support, see the Cisco Nexus 9000 Series NX-OS Programmability Guide.

&

- Caution UseBroadcomshellcommandswithcautionandonlyunderthedirectsupervisionor requestof CiscoSupport personnel.

이

## Traffic Routing, Forwarding, and Management

This section describes the traffic routing, forwarding, and managementfeatures supported by the Cisco NX-OS software.

## Ethernet Switching

The Cisco NX-OS software supports high-density, high-performance Ethernet systems and provides the following Ethernet switching features:

- • IEEE 802.1D-2004 Rapid and Multiple Spanning Tree Protocols (802.1w and 802.1s)

- • IEEE 802.1Q VLANs and trunks

- • IEEE 802.3ad link aggregation

- • Unidirectional Link Detection (UDLD) in aggressive and standard modes

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

7

| |

## IP Routing

## IP Routing

## IP Services

## IP Multicast

8

|

|

For more information, see the Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide and the Cisco Nexus 9000 Series NX-OS Layer 2 Switching Configuration Guide.

The Cisco NX-OS software supports IP version 4 (IPv4) and IP version 6 (IPv6) and the following routing protocols:

- • Open Shortest Path First (OSPF) Protocol Versions 2 (IPv4) and 3 (IPv6)

- • Intermediate System-to-Intermediate System (IS-IS) Protocol (IPv4 and IPv6)

- • Border Gateway Protocol (BGP) (IPv4 and IPv6)

- • Enhanced Interior Gateway Routing Protocol (EIGRP) (IPv4 only)

- • Routing Information Protocol Version 2 (RIPv2) (IPv4 only)

The Cisco NX-OS software implementations of these protocols are fully compliant with the latest standards and include 4-byte autonomous system numbers (ASNs) and incremental shortest path first (SPF). All unicast protocols support Non-Stop Forwarding Graceful Restart (NSF-GR). All protocols support all interface types, including Ethernet interfaces, VLAN interfaces, subinterfaces, port channels, and loopback interfaces.

For more information, see the Cisco Nexus 9000 Series NX-OS Unicast Routing Configuration Guide.

The following IP services are available in the Cisco NX-OS software:

- • Virtual routing and forwarding (VRF)

- • Dynamic Host Configuration Protocol (DHCP) helper

- • Hot Standby Router Protocol (HSRP)

- • Enhanced object tracking

- • Policy-based routing (PBR)

- • Unicast graceful restart for all protocols in IPv4 unicast graceful restart for OPSFv3 in IPv6

For more information, see the Cisco Nexus 9000 Series NX-OS Unicast Routing Configuration Guide.

The Cisco NX-OS software includes the following multicast protocols and functions:

- • Protocol Independent Multicast (PIM) Version 2 (PIMv2)

- • PIM sparse mode (Any-Source Multicast [ASM] for IPv4)

- • Anycast rendezvous point (Anycast-RP)

- • Multicast NSF for IPv4

- • RP-Discovery using bootstrap router (BSR) (Auto-RP and static)

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

## Overview

|

|

## Overview

## Quality of Service

- • Internet Group Management Protocol (IGMP) Versions 1, 2, and 3 router role

- • IGMPv2 host mode

- • IGMP snooping

- • Multicast Source Discovery Protocol (MSDP) (for IPv4)

<

> **NOTE**
> Note

The Cisco NX-OS software does not support PIM dense mode.

For more information, see the Cisco Nexus 9000 Series NX-OS Multicast Routing Configuration Guide.

## Quality of Service

The Cisco NX-OS software supports quality of service (QoS) functions for classification, marking, queuing, policing, and scheduling. Modular QoS CLI (MQC) supports all QoS features. You can use MQC to provide uniform configurations across various Cisco platforms. For more information, see the Cisco Nexus 9000 Series NX-OS Quality of Service Configuration Guide.

## Network Security Features

The Cisco NX-OS software includes the following security features:

- • Control Plane Policing (CoPP)

- • Message-digest algorithm 5 (MD5) routing protocol authentication

- • Authentication, authorization, and accounting (AAA)

- • RADIUS and TACACS+

- • SSH Protocol Version 2

- • SNMPv3

- • Policies based on MAC and IPv4 addresses supported by named ACLs (port-based ACLs [PACLs], VLAN-based ACLs [VACLs], and router-based ACLs [RACLs])

- • Traffic storm control (unicast, multicast, and broadcast)

For more information, see the Cisco Nexus 9000 Series NX-OS Security Configuration Guide.

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

9

| |

| |

## Supported Standards

## Supported Standards

This table lists the IEEE compliance standards.

Table2:IEEEComplianceStandards

| 802.112 | 따스: 30066 |
|---|---|
| 802.17 | 21869 01 5600106 1888108 107 00160061 1280068 |
| 802.10 | 부 트 스 테 188810 음 |
| 802.18 | 1410216 50800108 17266 020010001 |
| 802.1\ | 6010 30800108 1766 020010001 |
| 802.386 | 100088356-1 (10/1007/1000 00160060[ 0760 00000) |
| 802.330 | 1106 888068860020 \1011 ㅅ (7 |
| 802.336 | 10-06188601 01600 |

This table lists the RFC compliance standards. For information on each RFC, see www.ietf.org.

Table3:RFCComplianceStandards

Standard

Description

| 867『 |  |
|---|---|
| 때” 1997 | 26772 (207727770777769 47777/07/76 |
| 때: 2385 | 207076007077 07277? 569570779 470 706 7672 72725 .5787707706 (20700 |
| 때” 2439 | 2677? 407/76.7/7422 40702078 |
| 때” 2519 | 거 270007701007.707/' 772707-7/20770277 00076 40976907707 |
| 때: 2545 | (796 07 26774 7470/77227070007 소 07607970779 7071 77276 777707/-7/207770777 고 00022778 |
| 때 2858 | 20700072227070007 406707570779 707" 26724 |
| 때” 2918 | 07076 67765) (70020077/7702 707" 26724 |
| 때” 3065 | 거 000720770779 5157601 (707700670770775 202 |

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

10

## Overview

|

|

## Overview

## Supported Standards

| 51800810 | 066000000 |
|---|---|
| 때” 3392 | (702007777765 4017607775600770077 4707 26724 |
| 때 (6 4271 | 2(022 76757077 4 |
| ] 때 (6 4273 | 27724 7472 - 72670077770775 07" 220770860 (070760075 7077 20724 |
| 때” 4456 | 2677? 40706 46/76007077- 477 기 7/7077707776 70 70777 4265/7 7777077707 2672 (72062) |
| 때” 4486 | 506000069.7077 2007? 00056 72077770077077 770695080 |
| ] 때 (6 4724 | (770067007/ /697077 240000777577.70/" 2062 |
| 때” 4893 | 2677? .52022077.70/ ㆍ 7070~00767 45 202070706/' 52006 |
| ] 때 (2 5004 | 20070 20072 2697 727/2 7707757770775 77002 (0770 430707770/ 70 47707/76/" |
| ] 때 (： 5396 | 763007007 207765600770770072 07 거 000770770769 51157607 (4.5) 20770720607/5 티 066 때: 5396 16 006018117 5040200060. 7116 8901810 800 36001 ㅁ 0130005 816 940000 ㅁ 60, 641 0416 8600 ㅠ 7 ㅁ 018002 ㅁ 0 19 001. |
| ] 때 (： 5549 | 겨 007677757778 77?74 206710077 7.016/" 고 0000700777777 7722707777077077 17772 0772 72206 20700 2202. |
| 때 5668 | 4-007067/ 45 .50760070 207? 430007000 (7077272207720 |
| 160-000 트 | 26900801 ㅁ 80610100 801080066 (078-160-1087010-68061400-05.600 |
| 160-000 트 | 2667 18616 06016066 (0781[-160-10-68204-0010-15.600 |

ietf-draft

Dynamic Capability

(draft-ietf-idr-dynamic-cap-03.txt)

IP Multicast

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

11

| |

| |

## Supported Standards

|

|

12

| 때” 2236 | 77027077707 07070) 420774980070077 2/070007/, 12757077 2 |
|---|---|
| 때 (2 3376 | 77027077707 07070) 420774980070077 27/070007/, 12757077 3 |
| 때: 3446 | 거 72070097 46770062707/5 70277 (42) 727200/70727577 76578 7?7070007 27770027007007077 7247/7/770057 (20744) 0070 22707/770057 507006 /279001677/ 27/070007 (025222) |
| ] 때 (： 3569 | 거 72 (2026777010 07 .507/7/00-527000770 2270772720097 (55047) |
| 때 (〉 3618 | 22707/770057 507006 /279001677/ 27/070007 (025222) |
| 때” 4601 | 27070007 772002700700777 747//770057 - 5270756 42006 (2774-504): 77070007 5776027/70077077 (40142900) |
| 때 (〉 4607 | .50207/06-527600770 44707/770057 707 72 |
| 때! 4610 | 거 72070097-72 (/527778 707070007 277700200700777 747/7/770057 (22774) |
| 때” 6187 | 제 50903 (167727700769.70/' .560206@ 5/76// 4707/7077770077077 |
| 때 9465 | 2774 207///-2087976/ 7200778 |
| 160-000 트 | 16806 660067 14001102081167. (0 720000868 0100806-『60468[8, 018[-160-10000-080600416-1000-07.60 |
| 12 56601065 |
| 때 768 | (7722 |
| 때 783 | 7272 |
| 때 791 | 72 |
| 때 792 | 70022 |

RFC 793

TCP

RFC 826

ARP

RFC 854

Telnet

RFC 959

FTP

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

## Overview

|

|

## Overview

## Supported Standards

| 51800810 | 066000000 |
|---|---|
| 때: 1027 | 20001 4242 |
| 때 8573 | 과 772 506070771 75 00/1072000 17772 740 겨 4.5726(7044(' 0700/760777007707 77200/70727572 |
| 때 7822 | 2072.14 |
| (66 1305 | 2072.13 |
| (0 1519 | 07722 |
| 때: 1542 | 20077? 76707 |
| ] 재 (〉 1591 | 72209 07007 |
| ] 때 (6 1812 | 70214 707070/5 |
| 때 (6 2131 | 70727(672 2720/000/ |
| (0 2338 | 122 |
| 19-16 |  |
| 때 (〉! 1142 (051 10589) | (257 70569 7770777007070 51157007 70 202767777007076 57157607 777770-00770777 70202778 00600707796 27070007 |
| 때: 1195 | (796 07 (0057 75-795 7071 7070007778 702 2703.27 0020 07007 00127072770077 |
| 때 (1 2763 | 20177077770 72705777077706 4200/707780 2200/070727577.707' 75-79' |
| 때: 2966 | 2007770777-700 27070 7275777/0707077 772 7100-7.0007 75-79 |
| 때 2973 | 7575 2265/) (7702025 |
| 때 (2 3277 | 7527.95 770775707077 2700407070 거 007007700 |
| 때” 3373 | 7777600-1/27 2207705/700 707: 75-79 207777-70-702777 40/4007/70705 |
| 때: 3567 | 7979 (792277087000/70 4707/100777007707 |

RFC 3847

Restart Signaling for IS-IS

ietf-draft

Internet Draft Point-to-point

operation over LAN in link-state

routing protocols

(draft-ietf-isis-igp-p2p-over-lan-06.txt)

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

13

| |

| |

## Supported Standards

|

|

14

## Overview

Standard

Description

| 0580 |  |
|---|---|
| ] 때 (6 2328 | (25200 18757077 2 |
| 때 (： 2370 | (25220 (20200160 /.54 (020707 |
| 때 (〉! 2740 | (25/20707/1 72706 (05220 1767/57007 3) |
| 때 (〉 3101 | (<2.57207007-50-571/0/02-4700 (27594) (22007 |
| 때 (2 3137 | (2570.57 /407076/: 40176077790070077 |
| 때: 3509 | 기 /7077707776 7772/607760770770779 07 (2572404760 20706/' 207067/5 |
| ] 때 (6 3623 | (770067007/ 25707 20697077 |
| ] 때 (2 4750 | (25200 16757077 2 4270 |
| 66800 60020 (288) |
| 때: 2597 | 기 59107600 207700707778 /?772 (67002 |
| 때 (： 3246 | 기 77 230760770020770070778 7770 |
| 7 |
| ] 재 (6: 1724 | 72202 7272 0060797077 |
| 때” 2082 | 개 /2202 72725 4707/2060777007707 |
| ] 따 (〉 2453 | 개 /72 1867/97077 2 |
| 너나 |
| 때: 2579 | 7600007 (7077060702770779 707: 542712 |
| ] 때 (〉! 2819 | 고 007076 206240072407777077778 2207208600707077 772707777077077 2256 |
| 때” 2863 | 7776 7770070065 07007 72702 |
| 때 (〉( 3164 | 7716 2.572 595708 7?7070007 |
| ] 때 (〉 3176 | 277222077 (70722070770775 50010 4 220607700 7077 2407277077778 770/770 272 .510770/700 0770 207/700 2702707765 |

Simple Network Management

Protocol (SNMP) Management

Frameworks

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

## Overview

## Supported Standards

| 51800810 | 066000000 |
|---|---|
| 때 (6 3413 | .57777276 2076710072207720480070077 20070007 (520047?) 4722/7200770775 |
| 때 (〉 3417 | 77077527077440/72707785 707'7/76 57777270 고 07007 2407208007007 77020007/ (52022) |
| 보 2080800022810141165 |  |
| 때” 8040 | 과 57(0(02002727070007 |

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

15

| |

| |

## Supported Standards

|

|

16

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

## Overview

|

3

C H A P T E R 3

## Using the Cisco NX-OS Setup Utility

This chapter contains these sections:

- • About the Cisco NX-OS Setup Utility, on page 17

- • Prerequisites for the Setup Utility, on page 18

- • Setting Up Your Cisco NX-OS Device, on page 19

- • Additional References for the Setup Utility, on page 24

## About the Cisco NX-OS Setup Utility

The Cisco NX-OS setup utility is an interactive command-line interface (CLI) mode that guides you through a basic (also called a startup) configuration of the system. The setup utility allows you to configure only enough connectivity for system management.

The setup utility allows you to build an initial configuration file using the System Configuration Dialog. The setup starts automatically when a device has no configuration file in NVRAM. The dialog guides you through initial configuration. After the file is created, you can use the CLI to perform additional configuration.

You can press Ctrl-C at any prompt to skip the remaining configuration options and proceed with what you have configured up to that point, except for the administrator password. If you want to skip answers to any questions, press Enter. If a default answer is not available (for example, the device hostname), the device uses what was previously configured and skips to the next question.

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

17

## Using the Cisco NX-OS Setup Utility

| |

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

## Prerequisites for the Setup Utility

The setup utility has the following prerequisites:

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

18

ㅣ

|!

## Using the Cisco NX-OS Setup Utility

## Setting Up Your Cisco NX-OS Device

- • Have a password strategy for your network environment.

- • Connect the console port on the supervisor module to the network. If you have dual supervisor modules, connect the console ports on both supervisor modules to the network.

- • Connect the Ethernet management port on the supervisor module to the network. If you have dual supervisor modules, connect the Ethernet management ports on both supervisor modules to the network.

## Setting Up Your Cisco NX-OS Device

To configure basic management of the Cisco NX-OS device using the setup utility, follow these steps:

## Procedure

- Step 1 Power on the device.

- Step 2 Enable or disable password-strength checking.

A strong password has the following characteristics:

- • At least eight characters long

- • Does not contain many consecutive characters (such as "abcd")

- • Does not contain many repeating characters (such as "aaabbb")

- • Does not contain dictionary words

- • Does not contain proper names

- • Contains both uppercase and lowercase characters

- • Contains numbers

## Example:

---- System Admin Account Setup ----

Do you want to enforce secure password standard (yes/no) [y]: y

- Step 3 Enter the new password for the administrator.

## Note

If a password is trivial (such as a short, easy-to-decipherpassword), your password configuration is rejected.Passwords are case sensitive. Be sure to configure a strong password that has at least eight characters, both uppercase and lowercase letters, and numbers.

## Example:

Enter the password for "admin": <password>

Confirm the password for "admin": <password>

---- Basic System Configuration Dialog ----

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

19

| |

## Using the Cisco NX-OS Setup Utility

60009

## Setting Up Your Cisco NX-OS Device

This setup utility will guide you through the basic configuration of the system. Setup configures only enough connectivity for management of the system.

Please register Cisco Nexus 9000 Family devices promptly with your supplier. Failure to register may affect response times for initial service calls. Nexus devices must be registered to receive entitled support services.

Press Enter at anytime to skip a dialog. Use ctrl-c at anytime to skip the remaining dialogs.

- Step 4 Enter the setup mode by entering yes.

## Example:

Would you like to enter the basic configuration dialog (yes/no): yes

## Step 5 Create additional accounts by entering yes (no is the default).

## Example:

Create another login account (yes/no) [n]:yes

- a) Enter the user login ID.

## Example:

Enter the User login Id : user_login

## Caution

Usernames must begin with an alphanumeric character and can contain only these special characters: ( + = . _ \ -). The # and ! symbols are not supported. If the username contains characters that are not allowed, the specified user is unable to log in.

b) Enter the user password.

## Example:

Enter the password for "user1": user_password Confirm the password for "user1": user_password

- c) Enter the default user role.

## Example:

Enter the user role (network-operator|network-admin) [network-operator]: default_user_role

For information on the default user roles, see the Cisco Nexus 9000 Series NX-OS Security Configuration Guide.

- Step 6 Configure an SNMP community string by entering yes.

## Example:

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

20

ㅣ

|!

## Using the Cisco NX-OS Setup Utility

## Setting Up Your Cisco NX-OS Device

Configure read-only SNMP community string (yes/no) [n]: yes SNMP community string : snmp_community_string

For information on SNMP, see the Cisco Nexus 9000 Series NX-OS System Management Configuration Guide.

- Step 7 Enter a name for the device (the default name is switch).

## Example:

Enter the switch name: switch_name

- Step 8

Configure out-of-band management by entering yes. You can then enter the mgmt0 IPv4 address and subnet mask.

## Note

You can only configure IPv4 address in the setup utility. For information on configuring IPv6, see the Cisco Nexus 9000 Series NX-OS Unicast Routing Configuration Guide.

## Example:

Continue with Out-of-band (mgmt0) management configuration? [yes/no]: yes Mgmt0 IPv4 address: mgmt0_ip_address Mgmt0 IPv4 netmask: mgmt0_subnet_mask

- Step 9 Configure the IPv4 default gateway (recommended) by entering yes. You can then enter its IP address.

## Example:

Configure the default-gateway: (yes/no) [y]: yes IPv4 address of the default-gateway: default_gateway

- Step 10

Configure advanced IP options such as the static routes, default network, DNS, and domain name by entering yes.

## Example:

Configure Advanced IP options (yes/no)? [n]: yes

- Step 11 Configure a static route (recommended) by entering yes. You can then enter its destination prefix, destination prefix mask, and next hop IP address.

## Example:

Configure static route: (yes/no) [y]: yes Destination prefix: dest_prefix Destination prefix mask: dest_mask Next hop ip address: next_hop_address

- Step 12 Configure the default network (recommended) by entering yes. You can then enter its IPv4 address.

## Note

The default network IPv4 address is the same as the destination prefix in the static route configuration.

## Example:

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

21

| |

## Using the Cisco NX-OS Setup Utility

| |

## Setting Up Your Cisco NX-OS Device

Configure the default network: (yes/no) [y]: yes Default network IP address [dest_prefix]: dest_prefix

- Step 13

Configure the DNS IPv4 address by entering yes. You can then enter the address.

## Example:

Configure the DNS IP address? (yes/no) [y]: yes DNS IP address: ipv4_address

- Configure the default domain name by entering yes. You can then enter the name.

## Example:

Configure the DNS IP address? (yes/no) [y]: yes DNS IP address: ipv4_address

- Step 15 Enable the Telnet service by entering yes.

## Example:

Enable the telnet service? (yes/no) [y]: yes

- Step 16 Enable the SSH service by entering yes. You can then enter the key type and number of key bits. For more information, see the Cisco Nexus 9000 Series NX-OS Security Configuration Guide.

## Example:

Enable the ssh service? (yes/no) [y]: yes Type of ssh key you would like to generate (dsa/rsa) : key_type Number of key bits <768-2048> : number_of_bits

- Step 17 Configure the NTP server by entering yes. You can then enter its IP address. For more information, see the Cisco Nexus 9000 Series NX-OS System Management Configuration Guide.

## Example:

Configure NTP server? (yes/no) [n]: yes NTP server IP address: ntp_server_IP_address

- Step 18 Specify a default interface layer (L2 or L3).

## Example:

Configure default interface layer (L3/L2) [L3]: interface_layer

- Step 19 Enter the default switchport interface state (shutdown or no shutdown). A shutdown interface is in an administratively down state. For more information, see the Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide.

## Example:

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

22

ㅣ

|!

## Using the Cisco NX-OS Setup Utility

## Setting Up Your Cisco NX-OS Device

Configure default switchport interface state (shut/noshut) [shut]: default_state

Step 20

Enter yes (no is the default) to configure basic Fibre Channel configurations.

## Example:

Enter basic FC configurations (yes/no) [n]: yes

## Note

This step is available only on platforms that support SAN switching.

- a) Enter shut (noshut is the default) to configure the default Fibre Channel switch port interface to the shut (disabled) state.

## Example:

Configure default physical FC switchport interface state (shut/noshut) [noshut]: shut

- b) Enter on (on is the default) to configure the switch port trunk mode

## Example:

Configure default physical FC switchport trunk mode (on/off/auto) [on]: on

- c) Enter permit (deny is the default) to permit a default zone policy configuration.

## Example:

Configure default zone policy (permit/deny) [deny]: permit

Permits traffic flow to all members of the default zone.

## Example:

## Note

If you are executing the setup script after entering a write erase command, you explicitly must change the default zone policy to permit for VSAN 1 after finishing the script using the following command:

```cisco-ios
switch(config)# zone default-zone permit vsan 1
```

- d) Enter yes (no is the default) to enable a full zone set distribution.

## Example:

Enable full zoneset distribution (yes/no) [n]: yes

Step 21

- Enter the best practices profile for control plane policing (CoPP). For more information, see the Cisco Nexus 9000 Series NX-OS Security Configuration Guide.

## Example:

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

23

| |

## Using the Cisco NX-OS Setup Utility

| |

## Additional References for the Setup Utility

Configure best practices CoPP profile (strict/moderate/lenient/none) [strict]: moderate

The system now summarizes the complete configuration and asks if you want to edit it.

- Step 22 Continue to the next step by entering no. If you enter yes, the setup utility returns to the beginning of the setup and repeats each step.

## Example:

Would you like to edit the configuration? (yes/no) [y]: yes

- Step 23 Use and save this configurationby enteringyes. If you do not save the configurationat this point, none of your changes are part of the configuration the next time the device reboots. Enter yes to save the new configuration. This step ensures that the boot variables for the nx-os image are also automatically configured.

## Example:

Use this configuration and save it? (yes/no) [y]: yes

## Caution

If you do not save the configuration at this point, none of your changes are part of the configuration the next time that the device reboots. Enter yes to save the new configuration to ensure that the boot variables for the nx-os image are also automatically configured.

## Additional References for the Setup Utility

This section includes additional information related to using the setup utility.

## Related Documents for the Setup Utility

| 뜨 1060910 을 | (7900 2209 7.70070752778 077006 |
|---|---|
| 옹 8 터 300 16106 | (77900 00065 9000 .567765 2042-(25 560707711 (070727/781077077077 01006 |
| 10667 10168 | (77900 00065 9000 .567765 2042-(25 560707711 (070727/781077077077 01006 |
| 18274 800 18076 | | (7900 20005 9000 56776 042(29 (.7770057 407007778 (7072779707077072 (01006 |
| 오제 300 자 17 | (76900 20609 9000 567765 20425 .5157677 2407204860770777 (7072779100777071 (07700 |

Cisco Nexus 9000 Series NX-OS System Management Configuration Guide

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

24

ㅣ

4

C H A P T E R 4

## Using PowerOn Auto Provisioning

This chapter contains the following sections:

- • About PowerOn Auto Provisioning, on page 25

- • POAPv3, on page 42

- • Guidelines and Limitations for POAP, on page 44

- • Setting Up the Network Environment to Use POAP, on page 46

- • Configuring a Switch Using POAP, on page 46

- • Creating md5 Files, on page 47

- • Verifying the Device Configuration, on page 49

- • Troubleshooting for POAP, on page 50

- • Managing the POAP Personality, on page 50

## About PowerOn Auto Provisioning

PowerOn Auto Provisioning (POAP) automates the process of upgrading software images and installing configuration files on devices that are being deployed in the network for the first time.

When a device with the POAP feature boots and does not find the startup configuration, the device enters POAP mode, locates a DHCP server, and bootstraps itself with its interface IP address, gateway, and DNS server IP addresses. The device also obtains the IP address of a TFTP server and downloads a configuration script that enables the switch to download and install the appropriate software image and configuration file.

<

> **NOTE**
> Note

The DHCP information is used only during the POAP process.

## Network Requirements for POAP

POAP requires the following network infrastructure:

- • A DHCP server to bootstrapthe interfaceIP address, gatewayaddress, and DomainNameSystem(DNS) server.

- • A TFTP server that contains the configuration script used to automate the software image installation and configuration process.

- • One or more servers that contains the desired software images and configuration files.

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

25

## Using PowerOn Auto Provisioning

66000

## Secure Download of POAP Script

- • If you use USB, then no DHCP server or TFTP server are required for POAP.

## Figure3:POAPNetworkInfrastructure

8000! 561006「 (1777 800 『1『0)561006 (00011941810170 800 5801[0\08「6 56006 매 10 56006「 (600 『10 아 10. 0770) 0 10 .8001656, 081608. ㅣ 501008[6 10 ㅁ 8965 00009 바 80100 『16 800 50001 56006 800 5000 다 6 ㅁ 61841! 3816\0827 331649 띠 6×046 5\07

## Secure Download of POAP Script

Beginning with Cisco NX-OS Release 10.2(3)F, you have the option of securely downloading the POAP script. When a device with the POAP feature boots and does not find the startup configuration, the device enters POAP mode, locates a DHCP server, and bootstraps itself with its interface IP address, gateway, and DNS server IP addresses. The device also obtains the IP address of an HTTPS server and downloads POAP script securely. The script enables the switch to download and install the appropriate software image and configuration file.

TodownloadthePOAPscriptsecurely,youneedtoselectspecificPOAPoptions.UntilCiscoNX-OSRelease 10.2(3)F, POAP used options 66 and 67 for IPv4, and options 77 and 15 for IPv6 to extract the booting script information. However, the transfer of the script uses http, and is not very secure. Beginning with Cisco NX-OS Release 10.2(3)F, option 43 specifies the secure POAP related provisioning script information for IPv4 and option 17 specifies the same for IPv6. Additionally, these options allow the POAP to reach the file server in a secure manner. The POAP options 66, 67, 77, and 15 continue to be supported in Cisco NX-OS Release10.2(3)F. Furthermore, if you are using option 43 or 17, you can use the earlier options as fallback options, if required. From Cisco NX-OS Release 10.4(1)F, you can use Root-CA bundles instead of single .pem certificate for Secure POAP.

<

- The maximum character length is 512 bytes for both option 43 and option 17.

The sub-options available for option 43 and option 17 are discussed in the following sections:

- • Option 43 - IPv4

- • Option 17 - IPv6

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

26

ㅣ

|!

## Using PowerOn Auto Provisioning

## Secure Download of POAP Script

## IPv4

Option 43 has the following sub-options for IPv4:

- • option space poap length width 2;

- • option poap.version code 1 = unsigned integer 8;

<

> **NOTE**
> Note

This sub-option is mandatory.

- • option poap.ca_list code 50 = text;

- • option poap.url code 2 = text;

<

> **NOTE**
> Note

This sub-option is mandatory.

- • option poap.debug code 51 = unsigned integer 8;

- • option poap.ntp code 3 = ip-address;

<

> **NOTE**
> Note

This sub-option is only supported for IPv4 (Option 43).

- • option poap.flag code 52 = unsigned integer 8;

%

- Note

Flag is used to skip server certificate validation in the client.

Sample configuration for IPv4 is as follows:

host dhclient-n9kv { hardware ethernet 00:50:56:85:c5:30; fixed-address 3.3.3.1; default-lease-time 3600; option broadcast-address 192.168.1.255; #option log-servers 1.1.1.1; max-lease-time 3600; option subnet-mask 255.255.255.0; option routers 10.77.143.1; #option domain-name-servers 1.1.1.1; vendor-option-space poap; option poap.version 1; option poap.ca_list "https://<ip>/poap/ca_file1.pem, https://<ip>/poap/ca_file2.pem"; option poap.url "https://<url>/poap.py"; option poap.debug 1; option poap.ntp 10.1.1.39; option poap.flag 0; }

## Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

27

| |

| |

## Using PowerOn Auto Provisioning

## Secure Download of POAP Script

## IPv6

Option 17 has the following sub-options for IPv6:

- • option space poap_v6 length width 2;

- • option poap_v6.version code 1 = unsigned integer 8;

<

> **NOTE**
> Note

This sub-option is mandatory.

- • option poap_v6.ca_list code 50 = text;

- • option poap_v6.url code 3 = text;

<

> **NOTE**
> Note

This sub-option is mandatory.

- • option poap_v6.debug code 51 = unsigned integer 8;

- • option vsio.poap_v6 code 9 = encapsulate poap_v6;

Sample configuration for IPv6 is as follows:

option dhcp6.next-hop-rt-prefix code 242 = { ip6-address, unsigned integer 16, unsigned integer 16, unsigned integer 32, unsigned integer 8, unsigned integer 8, ip6-address };

option dhcp6.bootfile-url code 59 = string;

default-lease-time 3600;

max-lease-time 3600;

log-facility local7;

subnet6 2003::/64 {

# This statement configures actual values to be sent

# RTPREFIX option code = 243, RTPREFIX length = 22

# Ignore value 22. It is something related to option-size RT_PREFIX option length.

# lifetime = 9000 seconds

~

# route ETH1_IPV6_GW/64

# metric 1

option dhcp6.next-hop-rt-prefix 2003::2222 243 22 9000 0 1 ::;

#ipv6 ::/0 2003::2222

#Another example - support not there in NXOS - CSCvs05271:

#option dhcp6.next-hop-rt-prefix 2003::2222 243 22 9000 112 1 2003::1:2:3:4:5:0;

#ipv6 2003::1:2:3:4:5:0/112 2003::2222

# Additional options #option dhcp6.name-servers fec0:0:0:1::1; #option dhcp6.domain-search "domain.example";

range6 2003::b:1111 2003::b:9999; option dhcp6.bootfile-url "tftp://2003::1111/poap_github_v6.py"; vendor-option-space poap_v6; option poap_v6.version 1; option poap_v6.ca_list "https://<ip>/new_ca.pem,https://<ip>/another_ca.pem"; option poap_v6.url "https://<ip>/poap_github_v4.py";

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

28

ㅣ

|!

## Using PowerOn Auto Provisioning

## Network Requirements for Secure POAP

option poap_v6.debug 1; }

## Network Requirements for Secure POAP

Secure POAP requires the following network infrastructure:

- • A DHCP server to bootstrapthe interfaceIP address, gatewayaddress, and DomainNameSystem(DNS) server.

- • An HTTPS server that contains the POAP script used for software image installation and configuration process.

<

> **NOTE**
> Note

- • In case of secure download of POAP script, the TFTP server is replaced with the HTTPS server. Hence, when you read the content related to the TFTPserverinthischapter, remembertoreadtheTFTPserverastheHTTPS server.

- • One or more servers that contain the desired software images and configuration files.

## Deployment Scenarios

Cisco devices have a unique identifier known as the Secure Unique Device Identifier (SUDI). The hardware SUDI can be used for authentication, as it can be used for asymmetric key operations such as encryption, decryption, signing, and verifying that allow passage of the data to be operated upon. All non-Cisco devices are classified as non-SUDI devices. For a non-SUDI device, the root-CA bundle is required to authenticate the file server. However, the file server can be hosted on either a SUDI or a non-SUDI device.

Based on all these capabilities, you can use one of the following deployment scenarios to download the POAP script in a secure way:

- • SUDI Supported Device as File Server

- • Non-SUDI Supported Device as File Server

## SUDI Supported Device as File Server

The SUDI supported devices are Cisco devices. Unlike the earlier implementation, the DHCP server now provides a https location rather than http/tftp. In this scenario, only the DHCP server and the SUDI supported script server (HTTPS server) are required, other than one or more servers that contain the required software images and configuration files.

<

- Note SUDI only supports TLSv1.2 or below. Also, the SUDI solution only considers secure download using https, but not sftp.

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

29

| |

## Using PowerOn Auto Provisioning

| |

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

## Non-SUDI Supported Device as a File Server

In this scenario, the Root-CA bundle must be installed in the booting device. The Root-CA bundle is required for authentication.Here, the DHCP server, intermediatedevice,and non-SUDI supported scriptserver (HTTPS server) are required, other than one or more servers that contain the required software images and configuration

files.

The DHCP offer has the details of intermediate server that has the Root-CA bundle available. The intermediate device should support SUDI. The booting device uses the intermediate device to download the Root-CA bundle, install it, and then communicate with the file server. The intermediate devices should be provisioned first.

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

30

|

|

## Using PowerOn Auto Provisioning

## Benchmark Configured Device

## Figure5:Non-SUDISupportedDeviceasFileServerInfrastructure

660 아 0080 키 00-840 미 -540001160 (0101194『831100 800 마 1002 (00001094160 56000 응아 56006 으 0\08「6 56006 36006 (4056 000194760) 01118) (80010 와 100 0110) 10 600[655, 『 ㅁ 000^ (200119418100 6816\80, | 8640016 아 『116 200 80010 56006, 띠 00-840 미 응 01876 800 58 에 10 다 16 830000「160 1078068 용 00101 56100 1[0618411 3816\8\ 504175 띠 6×48 58\1 아

The workflow for non-SUDI supported devices is as follows:

- • Booting device is SUDI capable and has the needed trust store to verify a SUDI certificate

- • Intermediate device that hosts a server with Root-CA bundle is also SUDI capable

- • Booting device sends out DHCP discover

- • DHCP server responds to booting device with https server details and Root-CA server details

- • Booting device reaches to intermediate device, gets the CA bundle, adds it to the trust store

- • Booting device reaches the file server to download poap.py

## Benchmark Configured Device

The root CA certificate chain file for the Non-SUDI-supported script server must be placed in /bootflash/poap/sudi_fs on the Benchmark Configured Server.

<

- Note To change port on the Benchmark Configured Device, use the file-server <port-number> command. Avoid using standard ports such as port 80 (http) and port 443 (https).

The file-server <port-number> command only serves content over the management interface.

## Secure POAP on a Device Shipped with Old Image

Support for secure POAP will be available only for devices that are shipped with image that has secure POAP

feature.

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

31

| |

## Using PowerOn Auto Provisioning

| |

## Troubleshooting Secure POAP

If the device does not have the secure POAP feature, then use the legacy DHCP options to move the device to a later version of the image that supports secure POAP. Then these devices can be reloaded and use the secure POAP feature.

## Troubleshooting Secure POAP

Perform the following steps to collect debugging information regarding secure POAP:

1. Set the debug option for IPv4 in option 43 to 1 and for IPv6 in option 17.

The debug option enables additional logs.

2. Allow the switch to run one cycle of POAP.

3. Abort POAP.

4. When the system boots up, run the show tech-support poap command.

This command displays POAP status and configuration.

## Disabling POAP

POAP is enabled when there is no configuration in the system. It runs as a part of bootup. However, you can bypass POAP enablement during initial setup. If you want to disable POAP permanently (even when there is no configuration in the system), you can use the 'system no poap' command. This command ensures that POAP is not started during the next boot (even if there is no configuration). To enable POAP, use the 'system poap' command or the 'write erase poap' command. The 'write erase poap' command erases the POAP flag and enables POAP.

- • Example: Disabling POAP

```cisco-ios
switch# system no poap
switch# sh boot Current Boot Variables: sup-1 NXOS variable = bootflash:/nxos.9.2.1.125.bin Boot POAP Disabled
```

POAP permanently disabled using 'system no poap'

Boot Variables on next reload:

sup-1 NXOS variable = bootflash:/nxos.9.2.1.125.bin Boot POAP Disabled

POAP permanently disabled using 'system no poap'

```cisco-ios
switch# sh system poap
```

System-wide POAP is disabled using exec command 'system no poap' POAP will be bypassed on write-erase reload. (Perpetual POAP cannot be enabled when system-wide POAP is disabled)

- • Example: Enabling POAP

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

32

ㅣ

|!

## Using PowerOn Auto Provisioning

## POAP Configuration Script

```cisco-ios
switch# system poap
```

## switch# sh system poap

System-wide POAP is enabled

- • Example: Erase POAP

```cisco-ios
switch# write erase poap
```

This command will erase the system wide POAP disable flag only if it is set. Do you wish to proceed anyway? (y/n) [n] y System wide POAP disable flag erased.

```cisco-ios
switch# sh system poap
```

System-wide POAP is enabled

## POAP Configuration Script

The reference script supplied by Cisco supports the following functionality:

- • Retrieves the switch-specific identifier, for example, the serial number.

- • Downloads the nx-os software image if the files do not already exist on the switch. The nx-os image is installed on the switch and is used at the next reboot.

- • Schedules the downloaded configuration to be applied at the next switch reboot.

- • Stores the configuration as the startup configuration.

Cisco has sample configuration scripts that were developed using the Python programming language and Tool Command Language (Tcl). You can customize one of these scripts to meet the requirements of your network environment. You can access the Python script to perform POAP on the Cisco Nexus 9000 Series switch at this link: https://github.com/datacenter/nexus9000/tree/master/nx-os/poap.

The Python programming language uses two APIs that can execute CLI commands. These APIs are described in the following table. The arguments for these APIs are strings of the CLI commands.

| 01 | 066000000 |
|---|---|
| 010 | 복 604206 0416 78\ 04604 0 (71.1 0000018008, 10014010 음 46 6000601/9060181 011878 이 669. |
| 이 10(0) | 06 (01.1 60000008008 04186 94000 511., 0119 ^01 0416 46 600000800 04104110 8 0250100 016002087%. |
| 71106 6021 680 66 466141 10 4610 56870 0416 04104 01 위 10\ 0002048008. |

## POAP Configuration Script

We provide a sample configuration script that is developed using the Python programming language. We recommendusingtheprovidedscriptandmodifyingittomeettherequirementsofyournetworkenvironment.

The POAP script can be found at https://github.com/datacenter/nexus9000/blob/master/nx-os/poap/poap.py.

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

33

| |

## Using PowerOn Auto Provisioning

| |

## Using the POAP Script and POAP Script Options

To modify the script using Python, see the Cisco NX-OS Python API Reference Guide for your platform.

## Using the POAP Script and POAP Script Options

Before using the POAP script, perform the following actions:

1. Edit the options dictionary at the top of the script to ensure that all relevant options for your setup are included in the script. Do not change the defaults (in the default options function) directly.

2. Update the MD5 checksum of the POAP script as shown using shell commands.

f=poap_nexus_script.py ; cat $f | sed '/^#md5sum/d' > $f.md5 ; sed -i "s/^#md5sum=.*/#md5sum=\"$(md5sum $f.md5 | sed 's/ .*//')\"/" $f

3. If the device has a startup configuration, perform a write erase and reload the device.

The following POAP script options can be specified to alter the POAP script behavior. When you download files from a server, the hostname, username, and password options are required. For every mode except personality, the target_system_image is also required. Required parameters are enforced by the script, and the script aborts if the required parameters are not present. Every option except hostname, username, and password has a default option. If you do not specify the option in the options dictionary, the default is used.

• username

The username to use when downloading files from the server.

## • password

The password to use when downloading files from the server.

- • hostname

The name or address of the server from which to download files.

• mode

## The default is serial_number.

Use one of the following options:

## • personality

A method to restore the switch from a tarball.

## • serial_number

The serial number of the switch to determine the configuration filename. The format for the serial number in the configuration file is conf.serialnumber. Example: conf.FOC123456

- • hostname

The hostname as received in the DHCP options to determine the configuration filename. The format for the hostname in the configuration file is conf_hostname.cfg. Example: conf_3164-RS.cfg

• mac

The interface MAC address to determine the configuration filename. The format for the hostname in the configuration file is conf_macaddress.cfg. Example: conf_7426CC5C9180.cfg

• raw

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

34

ㅣ

|!

## Using PowerOn Auto Provisioning

## Using the POAP Script and POAP Script Options

The configuration filename is used exactly as provided in the options. The filename is not altered in any way.

- • location

The CDP neighbors are used to determine the configuration filename. The format for the location in the configuration file is conf_host_intf.cfg, where host is the host connected to the device over the POAP interface, and intf is the remote interface to which the POAP interface is connected. Example: conf_remote-switch_Eth1_8.cfg

## • required_space

The required space in KB for that particular iteration of POAP. The default is 100,000. For multi-step upgrades, specify the size of the last image in the upgrade path of the target image.

## • transfer_protocol

Any transfer protocol such as http, https, ftp, scp, sftp, or tftp that is supported by VSH. The default is scp.

- • config_path

The path to the configuration file on the server. Example: /tftpboot. The default is /var/lib/tftpboot.

- • target_system_image

The name of the image to download from the remote server. This is the image you get after POAP completes. This option is a required parameter for every mode except personality. The default is "".

- • target_image_path

The path to the image on the server. Example: /tftpboot. The default is /var/lib/tftpboot.

## • destination_path

The path to which to download images and MD5 sums. The default is /bootflash.

- • destination_system_image

The name for the destination image filename. If not specified, the default will be the target_system_image name.

## • user_app_path

The path on the server where the user scripts, agents, and user data are located. The default is

/var/lib/tftpboot.

- • disable_md5

This is True if MD5 checking should be disabled. The default is False.

## • midway_system_image

The name of the image to use for the midway system upgrade. By default, the POAP script finds the name of any required midway images in the upgrade path and uses them. Set this option if you prefer to pick a different midway image for a two-step upgrade. The default is "".

## • source_config_file

The name of the configuration file when raw mode is used. The default is poap.cfg.

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

35

| |

| |

## Using PowerOn Auto Provisioning

## Using the POAP Script and POAP Script Options

## • vrf

TheVRFtousefordownloadsandsoon.TheVRFisautomaticallysetbythePOAPprocess.Thedefault is the POAP_VRF environment variable.

## • destination_config

The name to use for the downloaded configuration. The default is poap_replay.cfg.

## • split_config_first

The name to use for the first configuration portion if the configuration needs to be split. It is applicable only when the configuration requires a reload to take effect. The default is poap_1.cfg.

## • split_config_second

Thenametouseforthesecondconfigurationportioniftheconfigurationissplit.Thedefaultispoap_2.cfg.

• timeout_config

The timeout in seconds for copying the configuration file. The default is 120. For non-legacy images, this option is not used, and the POAP process times out. For legacy images, FTP uses this timeout for the login process and not for the copy process, while scp and other protocols use this timeout for the copy process.

- • timeout_copy_system

The timeout in seconds for copying the system image. The default is 2100. For non-legacy images, this option is not used, and the POAP process times out. For legacy images, FTP uses this timeout for the login process and not for the copy process, while scp and other protocols use this timeout for the copy process.

## • timeout_copy_personality

The timeout in seconds for copying the personality tarball. The default is 900. For non-legacy images, this option is not used, and the POAP process times out. For legacy images, FTP uses this timeout for the login process and not for the copy process, while scp and other protocols use this timeout for the copy process.

- • timeout_copy_user

The timeout in seconds for copying any user scripts and agents. The default is 900. For non-legacy images, this option is not used, and the POAP process times out. For legacy images, FTP uses this timeout for the login process and not for the copy process, while scp and other protocols use this timeout for the copy process.

## • personality_path

The remote path from which to download the personality tarball. Once the tarball is downloaded and the personality process is started, the personality will download all files in the future from locations specified inside the tarball configuration. The default is /var/lib/tftpboot.

## • source_tarball

The name of the personality tarball to download. The default is personality.tar.

- • destination_tarball

The name for the downloaded personality tarball after it is downloaded. The default is personality.tar.

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

36

ㅣ

|!

## Using PowerOn Auto Provisioning

## Setting up the DHCP Server without DNS for POAP

## Setting up the DHCP Server without DNS for POAP

Beginning with Cisco NX-OS Release 7.0(3)I6(1), the tftp-server-name can be used without the DNS option. To enable POAP functionality without DNS on earlier releases, a custom option of 150 must be used to specify the tftp-server-address.

To use the tftp-server-address option, specify the following at the start of your dhcpd.conf file.

option tftp-server-address code 150 = ip-address;

## For example:

host MyDevice { option dhcp-client-identifier "\000SAL12345678"; fixed-address 2.1.1.10; option routers 2.1.1.1; option host-name "MyDevice"; option bootfile-name "poap_nexus_script.py"; option tftp-server-address 2.1.1.1;

}

The below example shows Configuring DHCPv6 for POAP over IPv6:

# This statement configures actual values to be sent # RTPREFIX option code = 243, RTPREFIX length = 22 # Ignore value 22. It is something related to option-size RT_PREFIX option length. # lifetime = 9000 seconds # route ETH1_IPV6_GW/64 # metric 1 option dhcp6.next-hop-rt-prefix 2003::2222 243 22 9000 0 1 ::; #ipv6 ::/0 2003::2222 #Another example - support not there in NXOS - CSCvs05271: #option dhcp6.next-hop-rt-prefix 2003::2222 243 22 9000 112 1 2003::1:2:3:4:5:0; #ipv6 2003::1:2:3:4:5:0/112 2003::2222 # Additional options #option dhcp6.name-servers fec0:0:0:1::1; #option dhcp6.domain-search "domain.example"; range6 2003::b:1111 2003::b:9999; #range6 2003::c:2222 2003::c:2222; option dhcp6.bootfile-url "tftp://2003::1111/poap_github_v6.py";

default-lease-time 3600;

max-lease-time 3600;

log-facility local7;

subnet6 2003::/64 {

## Downloading and Using User Data, Agents, and Scripts as part of POAP

Under the options dictionary, you can find the download_scripts_and_agents function. If you choose to downloaduserscriptsanddata,uncommentthefirstpoap_loglineandthenuseaseriesofdownload_user_app function calls to download each application. Since older Cisco NX-OS versions do not support recursive copy of directories, such directories must be put into a tarball (TAR archive) and then unpacked once on the switch. The parameters for the download_scripts_and_agents function are as follows:

- • source_path - The path to where the file or tarball is located. This is a required parameter. Example: /var/lib/tftpboot.

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

37

| |

## Using PowerOn Auto Provisioning

| |

## POAP Process

- • source_file - The name of the file to download. This is a required parameter. Example: agents.tar, script.py, and so on.

- • dest_path - The location to download the file on the switch. Any directories that do not exist earlier will be created. This is an optional parameter. The default is /bootflash.

- • dest_file - The name to give the downloaded file. This is an optional parameter. The default is unchanged source_file.

- • unpack - Indicates whether a tarball exists for unpacking. Unpacking is done with tar -xf tarfile -C /bootflash. This is an optional parameter. The default is False.

- • delete_after_unpack - Indicates whether to delete the downloaded tarball after unpack is successful. There is no effect if unpack is False. The default is False.

Using the download functionality, you can download all the agents and files needed to run POAP. To start the agents, you should have the configuration present in the running configuration downloaded by POAP. Then the agents, scheduler, and cron entry, along with EEM, can be used.

## POAP Process

The POAP process has the following phases:

1. Power up

2. USB discovery

3. DHCP discovery

4. Script execution

5. Post-installation reload

Within these phases, other process and decision points occur. The following illustration shows a flow diagram of the POAP process.

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

38

ㅣ

|!

## Using PowerOn Auto Provisioning

## Power-Up Phase

Figure6:POAPProcess

10046 배아. ; 16 68001 노 10006 버터 19216 000104812600. 60087 07510 태 0100660 56040 006 560810009016. 900 10000 0 1001 800000/00458, 00000? 80 6@60066 마 (0 06006 9410065 위 00) 800 0000065 1? 3001665 800 다 7170 96701 8001665 10816, 0002 906 106 (65065. 166 | 50001 00000805006 『0452 0001106 900 670600690 600835500060 816 00396 00160 0006 90101100? 1516 나 1001771005 880 10000 |, | 00160 01 1190 9010 500010616000065 006 0800601 006 000000 혜 00 | \65 100 900 00000805 토 \ 드라 18000(9. 5900 100005 06 0006094 레 00060 100089180 1190 9 배 다.

## Power-Up Phase

When you powerup the device for the first time, it loads the software image that is installed at manufacturing and tries to find a configuration file from which to boot. When a configuration file is not found, POAP mode

starts.

During startup, a prompt appears asking if you want to abort POAP and continue with a normal setup. You can choose to exit or continue with POAP.

<

- Note No user intervention is required for POAP to continue. The prompt that asks if you want to abort POAP remains available until the POAP process is complete.

If you exit POAP mode, you enter the normal interactive setup script. If you continue in POAP mode, all the front-panel interfaces are set up in the default configuration.

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

39

| |

## Using PowerOn Auto Provisioning

| |

## USB Discovery Phase

## USB Discovery Phase

When POAP starts, the process searches the root directory of all accessible USB devices for the POAP script file (the Python script file, poap_script.py), configuration files, and system and kickstart images.

If the script file is found on a USB device, POAP begins running the script. If the script file is not found on the USB device, POAP executes DHCP discovery. (When failures occur, the POAP process alternatesbetween USB discovery and DHCP discovery, until POAP succeeds or you manually abort the POAP process.)

If the software image and switch configuration files specified in the configuration script are present, POAP uses those files to install the software and configure the switch. If the software image and switch configuration files are not on the USB device, POAP does some cleanup and starts DHCP phase from the beginning.

## DHCP Discovery Phase

The switch sends out DHCP discover messages on the front-panel interfaces or the MGMT interface that solicit DHCP offers from the DHCP server or servers. (See the following figure.) The DHCP client on the Cisco Nexus switch uses the switch serial number in the client-identifier option to identify itself to the DHCP server. The DHCP server can use this identifier to send information, such as the IP address and script filename, back to the DHCP client.

POAP requires a minimum DHCP lease period of 3600 seconds (1 hour). POAP checks the DHCP lease period. If the DHCP lease period is set to less than 3600 seconds (1 hour), POAP does not complete the DHCP negotiation.

The DHCP discover message also solicits the following options from the DHCP server:

- • TFTP server name or TFTP server address—The DHCP server relays the TFTP server name or TFTP server address to the DHCP client. The DHCP client uses this information to contact the TFTP server to obtain the script file.

- • Bootfile name—The DHCP server relays the bootfile name to the DHCP client. The bootfile name includes the complete path to the bootfile on the TFTP server. The DHCP client uses this information to download the script file.

When multiple DHCP offers that meet the requirement are received, the one arriving first is honored and the POAPprocessmovestonextstage.ThedevicecompletestheDHCPnegotiation(requestandacknowledgment) with the selected DHCP server, and the DHCP server assigns an IP address to the switch. If a failure occurs in any of the subsequent steps in the POAP process, the IP address is released back to the DHCP server.

If no DHCP offers meet the requirements, the switch does not complete the DHCP negotiation (request and acknowledgment) and an IP address is not assigned.

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

40

ㅣ

|

## Using PowerOn Auto Provisioning

## POAP Dynamic Breakout

Figure7:DHCPDiscoveryProcess

매 애 미 5000 ㄷ 6 00 『「00 ㄴ 03061 1068713086 마 1463147 101207208 00 0000 000 때 ㅁ 01816 200 5016 더 1 때 매 야 0 다 태 수 매 야 야 터 9 ~ 156160180? 노아 766 \ ㄴㄴ ㅁ 매 1 아 16006 ㄷ 57 176 58160080 아 다 타 100009416 10 2001866 07 176 10167206 10 12113901701 비하. 1 100019416 0212 바 2131\2 01 078 17801006 10 21291 바라: 00000 90000 00709416 0845 3090. ㅠ .50801189 501 00000108060 9351729

## POAP Dynamic Breakout

Beginning with Cisco NX-OS Release 7.0(3)I4(1), POAP dynamically breaks out ports in an effort to detect a DHCP server behind one of the broken-out ports. Previously, the DHCP server used for POAP had to be directly connected to a normal cable because breakout cables were not supported.

POAP determines which breakout map (for example, 10gx4, 50gx2, 25gx4, or 10gx2) will bring up the link connected to the DHCP server. If breakout is not supported on any of the ports, POAP skips the dynamic breakout process. After the breakout loop completes, POAP proceeds with the DHCP discovery phase as normal.

<

For more information on dynamic breakout, see the interfaces configuration guide for your device.

- Note

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

41

뜰

## Using PowerOn Auto Provisioning

| |

## Script Execution Phase

## Script Execution Phase

After the device bootstraps itself using the information in the DHCP acknowledgement, the script file is downloaded from the TFTP server.

The switch runs the configuration script, which downloads and installs the software image and downloads a switch-specific configuration file.

However, the configuration file is not applied to the switch at this point, because the software image that currently runs on the switch might not support all of the commands in the configuration file. After the switch reboots, it begins running the new software image, if an image was installed. At that point, the configuration is applied to the switch.

<

> **NOTE**
> Note

- If the switch loses connectivity, the script stops, and the switch reloads its original software images and bootup variables.

## Post-Installation Reload Phase

The switch restarts and applies (replays) the configuration on the upgraded software image. Afterward, the switch copies the running configuration to the startup configuration.

## POAPv3

PowerOn Auto Provisioning version 3 (POAPv3) is introduced in Cisco NX-OS Release 9.3(5). With this feature you can install license, RPM, and certificate through POAP.

Perform the following steps to install license or RPM or certificate through POAP.

1. Create a folder on the POAP server with serial number of the box as the name.

2. Create .yaml or .yml file with files to be installed. Make sure the file name is in <serial-number>.yaml or <serial-number>.yml format.

3. Create MD5 checksum for the .yaml or .yml file.

4. Make sure the format of the .yaml file should be similar to the below format:

Version : 1

Target-image : nxos.9.3.4.bin Description : Yaml for box XYZ12345 poap provisioning. N9k Leaf mode box License : [license1.lic, XYZ12345/license2.lic, folder1/license3.lic] RPM :

- - rpm1.rpm

- - patches/reload/rpm2-reload.rpm

- - rpm3.rpm

Certificate : [ssh1.pub, XYZ12345/ssh2key.pub]

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

42

ㅣ

|!

## Using PowerOn Auto Provisioning

## POAPv3

Trustpoint :

CA1 :

cert_1.p12 : password1 (priv_key_passphrase)

XYZ12345/CA1/cert_2.pfx : password2

CA2 :

CA2/XYZ12345/cert_3.p12 : password3

5. Note that the yaml keywords must match the format shown in above example.

6. Place all files in appropriate path.

7. Update the POAP script with install_path variable as the path where folder with the serial number as name is placed.

The following list provides the guidelines and limitations related to POAPv3:

- • YAML is a human friendly data serialization standard for all programming languages. YAML stands forYAMLAin'tMarkupLanguage,andthisfileformattechnologyisusedindocuments.Thesedocuments are saved in plain text format and are appended with the . yml extension. YAML is the file format and .yml is the file extension.

- • YAML is a superset of JSON and the YAML parser understands JSON. YAML file formats are used for configuration management because it is easy to read and comments are useful.

- • The Target_image mentioned in yaml should be kept only in the target_system_image path mentioned within POAP script. Relative path is not supported for the Target_image in yaml file.

- • Both.yamland.ymlextensionsaresupported.Youhaveanoptiontochoosetouseanyoftheseextensions. If you don’t choose any option, the <serial>.yamlextensionwill be tried first and if it fails the <serial>.yml is considered.

- • The MD5 files of yaml/yml is required similar to the configuration file. But if the disable_md5 is ‘True’ then the MD5 files of yaml/yml are not required.

- • Although 'install_path' is set in the POAP script file if no yaml file for device is found, then POAP workflowwillproceedwiththelegacypath,i.e.,withoutanyinstallationofRPMs,licensesandcertificates.

- • Install reset is highly preferred over write erase if PoAP with RPM installation is done in scenarios apart from Day-0.

- • ISSU is the new default for moving to new image via PoAP. Note that you need to use "use_nxos_boot": True, if legacy boot nxos <> is required.

- • The Filetype checks for .pfx,.p12 in trustpoints; .lic in license; and .rpm in rpms and aborts the current POAP if the checks/fileformats are not honoured.

- • In case of .rpm, you need to provide the original file name in the yaml file.

For example: if you renamed customCliGoApp-1.0-1.7.5.x86_64.rpm to custom.rpm then PoAP will bail out indicating the name mismatch.

To get the original name of rpm:

bash-4.3$ rpm -qp --qf '%{NAME}-%{VERSION}-%{RELEASE}.%{ARCH}.rpm' custom.rpm customCliGoApp-1.0-1.7.5.x86_64.rpm bash-4.3$

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

43

빼

## Using PowerOn Auto Provisioning

| |

## Guidelines and Limitations for POAP

- • Once ISSU via POAP begins, abort of PoAP will be blocked. If ISSU fails for some reason, then abort capability will be re-enabled.

## Guidelines and Limitations for POAP

POAP configuration guidelines and limitations are as follows:

- • The bootflash:poap_retry_debugs.log is a file populated by POAP-PNP for internal purposes only. This file has no relevance in case of any POAP failures.

- • Due to limitations in Syslog, securePOAP pem file name characters length is limited to 230 characters, though secure POAP supports 256 characters length for a pem file name.

- • The switch software image must support POAP for this feature to function.

- • POAP does not support provisioning of the switch after it has been configured and is operational. Only auto-provisioning of a switch with no startup configuration is supported.

- • The https_ignore_certificate option should be turned on to use the ignore-certificate keyword with https protocol in POAP. This would enable you to successfully perform HTTPS transfer in the POAP script and without this option https as protocol cannot work with POAP.

- • ForthosewhousesHTTP/HTTPSserversforDay0provisioning,provisioninginstructionswillbegiven based on the MAC information and other related details in the HTTP header. POAP uses these details from HTTP GET headers so that the correct provisioning script is identified and used. This was available for other vendors (and other Cisco OSs).These additional information will be available in HTTP get headers from Cisco NX-OS Release 10.2(1) for Cisco Nexus 9000. This feature will be available by default for POAP and non-POAP HTTP get operations.

- • When you use copy http/https GET commands, the following fields are shared as part of the HTTP header:

Host: IP address User-Agent: cisco-nxos X-Vendor-SystemMAC: System MAC X-Vendor-ModelName: Switch-Model X-Vendor-Serial: Serial_Num X-Vendor-HardwareVersion: Hardwareversion X-Vendor-SoftwareVersion: sw_version X-Vendor-Architecture: Architecture

- • If you use POAP to bootstrap a Cisco Nexus device that is a part of a virtual port channel (vPC) pair using static port channels on the vPC links, the Cisco Nexus device activates all of its links when POAP starts up. The dually connected device at the end of the vPC links might start sending some or all of its traffic to the port-channel member links that are connected to the Cisco Nexus device, which causes traffic to get lost.

To work around this issue, you can configure Link Aggregation Control Protocol (LACP) on the vPC links so that the links do not incorrectly start forwarding traffic to the Cisco Nexus device that is being bootstrapped using POAP.

- • If you use POAP to bootstrap a Cisco Nexus device that is connected downstream to a Cisco Nexus 9000 Series switch through a LACP port channel, the Cisco Nexus 9000 Series switch defaults to suspend its member port if it cannot bundle it as a part of a port channel. To work around this issue, configure the

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

44

ㅣ

|!

## Using PowerOn Auto Provisioning

## Guidelines and Limitations for POAP

CiscoNexus 9000 Seriesswitchto not suspend itsmemberports by using theno lacp suspend-individual command from interface configuration mode.

- • Important POAP updates are logged in the syslog and are available from the serial console.

• Critical POAP errors are logged to the bootflash. The filename format is

- date-time_poap_PID_[init,1,2].log, where date-time is in the YYYYMMDD_hhmmss format and PID is the process ID.

- • You can bypass the password and the basic POAP configuration by using the skip option at the POAP prompt. When you use the skip option, no password is configured for the admin user. The copy running-config startup-config command is blocked until a valid password is set for the admin user.

- • If the boot poap enable command (perpetual POAP) is enabled on the switch, on a reload, a POAP boot is triggered even if there is a startup configurationpresent. If you do not want to use POAP in this scenario, remove the boot poap enable configuration by using the no boot poap enable command.

- • Script logs are saved in the bootflash directory. The filename format is date-time_poap_PID_script.log, where date-time is in the YYYYMMDD_hhmmss format and PID is the process ID.

You can configure the format of the script log file. Script file log formats are specified in the script. The template of the script log file has a default format; however, you can choose a different format for the script execution log file.

- • The POAP feature does not require a license and is enabled by default. However for the POAP feature to function, appropriate licenses must be installed on the devices in the network before the deployment of the network.

- • POAP DHCP transaction may fail if the device receives high traffic rate. This issue happens when POAP uses a front panel. To avoid this issue, make sure POAP uses a management port.

- • Beginning with NX-OS 7.0(3)I7(4), RFC 3004 (User Class Option for DHCP) is supported. This enables POAP to support user-class option 77 for DHCPv4 and user-class option 15 for DHCPv6. The text displayed for the user class option for both DHCPv4 and DHCPv6 is "Cisco-POAP".

- • With RFC 3004 (User Class Option for DHCP) support, POAP over IPv6 is supported on Nexus 9000 switches.

- • Beginning with NX-OS 9.2(2), POAP over IPv6 is supported on Nexus 9504 and Nexus 9508 switches with –R line cards.

The POAP over IPv6 feature enables the POAP process to use IPv6 when IPv4 fails. The feature is designed to cycle between IPv4 and IPv6 protocols when a connection failure occurs.

- • For secure POAP, ensure that DHCP snooping is enabled.

- • To support POAP, set firewall rules to block unintended or malicious DHCP servers.

- • To maintain system security and make POAP more secure, configure the following:

- • Enable DHCP snooping.

- • Set firewall rules to block unintended or malicious DHCP servers.

- • POAP is supported on both MGMT ports and in-band ports.

- • Beginning with Cisco NX-OS Release 10.2(3)F, the Hardware SUDI for POAP/HTTPS feature provides an option to securely download the POAP script.

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

45

| |

## Using PowerOn Auto Provisioning

| |

## Setting Up the Network Environment to Use POAP

- • To collect the debugging information on POAP, use the show tech-support poap command, post abort of POAP.

- • Beginning with Cisco NX-OS Release 10.3(1)F, POAP is supported on Cisco Nexus X9836DM-A line card of the Cisco Nexus 9808 platform switches.

- • Beginning with Cisco NX-OS Release 10.4(1)F, POAP is supported on Cisco Nexus X98900CD-A line card of Cisco Nexus 9808 switches.

- • Beginning with Cisco NX-OS Release 10.4(1)F, POAP is supported on Cisco Nexus 9804 platform switches, and Cisco Nexus X98900CD-A and X9836DM-A line cards.

- • BeginningwithCiscoNX-OS Release10.4(3)F, for thesecurityenhancements,theskipoptionisdisabled. You must enter a valid password to access the box irrespective of whether the POAP process is stopped or not.

- • Beginning with Cisco NX-OS Release 10.6(1)F, POAP is supported on Cisco N9336C-SE1 switch.

## Setting Up the Network Environment to Use POAP

## Procedure

Step 1

- Modify the basic configuration script provided by Cisco or create your own script. For information, see the Python Scripting and API Configuration Guide.

- Step 2 Every time you make a change to the configuration script, ensure that you recalculate the MD5 checksum by running # f=poap_nexus_script.py ; cat $f | sed '/^#md5sum/d' > $f.md5 ; sed -i "s/^#md5sum=.*/#md5sum=\"$(md5sum $f.md5 | sed 's/ .*//')\"/" $f using a bash shell. For more information, see the Python API Reference Guide.

Step 3

- (Optional) Put the POAP script and any other desired software image and switch configuration files on a USB device accessible to the switch.

Step 4

- Deploy a DHCP server and configure it with the interface, gateway, and TFTP server IP addresses and a bootfile with the path and name of the configuration script file. (This information is provided to the switch when it first boots.) You do not need to deploy a DHCP server if all software image and switch configuration files are on the USB device.

Step 5

- Deploy a TFTP or HTTP server to host the configuration script. In order to trigger the HTTP request to the server, prefix HTTP:// to the TFTP server name. HTTPS is not supported.

- Add the URL portion into the TFTP script name to show correct path to the file name.

Step 6

- Deploy one or more servers to host the software images and configuration files.

## Configuring a Switch Using POAP

## Before you begin

Make sure that the network environment is set up to use POAP.

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

46

ㅣ

|!

## Using PowerOn Auto Provisioning

## Creating md5 Files

## Procedure

- Step 1 Install the switch in the network.

- Step 2 Power on the switch.

If no configuration file is found, the switch boots in POAP mode and displays a prompt that asks if you want to abort POAP and continue with a normal setup.

No entry is required to continue to boot in POAP mode.

Step 3

(Optional) If you want to exit POAP mode and enter the normal interactive setup script, enter y (yes).

The switch boots, and the POAP process begins.

## What to do next

Verify the configuration.

## Creating md5 Files

Every time you make a change to the configuration script, ensure that you recalculate the MD5 checksum by running # f=poap_fabric.py ; cat $f | sed '/^#md5sum/d' > $f.md5 ; sed -i "s/^#md5sum=.*/#md5sum=\"$(md5sum $f.md5 | sed 's/ .*//')\"/" $f using a bash shell.

This procedure replaces md5sum in poap_fabric.py with a new value if there was any change in that file.

<

- Note Steps 1-4 and 7-8 are needed only if you are using the BASH shell. If you have access to any other Linux server, these steps are not required.

## Before you begin

Access to the BASH shell.

Procedure

|  | 600001800 0726000 | 『00 ㅁ 056 |
|---|---|---|
| 1601 | ㅇ 0008406 (60001021 6801016: 3016010# 007 ㅁ 5*1094 ㅠ 6 ㄴ 62 ㅋ 0 ㅁ 17 ㅁ 21 으 1606 (6020 조 10) 부 | 트 마 666 인 06861 00011841780070 20006. |
| 160 2 | 168041610851-58401 6801016: | 08616 82561 91611 1680476. |

Step 1

Step 2

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

47

| |

## Using PowerOn Auto Provisioning

| |

## Creating md5 Files

Command or Action

Purpose

|  | 30100 (0002?10) + -626 ㅁ 026 1 ㅁ 5298-5156611 |  |
|---|---|---|
| 5660 3 5160 4 | 60 | 211 000118478000 20006. |
| 60801016: |  |
| 을까 (60201) 푸 @ 포 11 470 0251 | 0060 11048 89. |
| 5660 5 | 3160156#3 200 1529 프 10056410 /000601251740305.70/0096 77707706/.010 > /000608917/0305.70/0056 77707706/.010.0005 60801016: 1023610-4 .29 10 ㅁ 0586100 /5 ㅁ 600 ㄴ 『125616/ ㅁ ×05.7.0 . 3. 16 . 1 .51 ㅁ /5600 561 ㅁ | (2068665 20059410 107 0416 .1517 ㅁ 116. |
| 5160 6 | 20554107/600601251/0020. 어 용 > /000001291/00280.018.0 ㅁ 05 60801016: 10851-4.25 0 ㅁ 05600 /1 ㅁ 00 ㄴ 『1268/ ㅁ 026 .0『9 > /500 ㅇ ㄴ *1288/ ㅁ 022 .02209 . ㅁ 05 | | ((768166 2 ㅁ 40594100 107 416 . ㅇㅁㅇ 116. |
| 5160 7 | 6 60801016: 을까 (60201) 푸 @ 포 11 | 0011 0406 8 ㅅ 91 94611. |
| 8 | 0 1.005 | 121920187 0416 .0005 11168. 01060 01611166 10 416 (0020118478000 800 5011\8176 56776 ㄷ |
| 5160 5160 9 | | |
| 60801016: 803160# 632 | 1 .005 65 0040 09 12138148 2017 |
| ㅁ ※6086.7.0.3.16.1.1610.0 ㅁ 05 54 040 09 12139:136 2017 ㅁ 08206.0 ㅇ [0 . ㅁ 05 67299 040 09 12:148158 2017 ㅁ 6086.27.0 ㅁ 05 0007 0001012514:00200. 아 8.0005 500://7272 0007655/ |
|  | 60801016: ㅇ 0289 ㅁ 00 ㄴ 1261: ㅁ 0220 .09 . ㅁ 05 500: //10.1.100 .3/' 보 0 느 6 노 지 노 든 (1 오 ㅁ 6 10046 이 000272672 는 922 0 !06 세 2041 16 ㅇ 07 ㅁ 8106 ㅠ 6 ㅎ 60) : ㅠ ㅁ 82 ㅁ 6 ㅎ 06 ㅇ 062 ㄴ 프 6 느 6 포 0456672020061 000 트 006010.1.100.3'18 |  |
| 08550: 2 ㅁ 082 . ㅇ 9 005 54 0.188/8 06067 0 ㅇ 00 ㅁ ㅁ 616 ㄴ ㅎㅇ. 100 00:00 |

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

48

ㅣ

|!

## Using PowerOn Auto Provisioning

## Verifying the Device Configuration

## Verifying the Device Configuration

To verify the configuration, use one of the following commands:

| 600001800 | 『00056 |
|---|---|
| 9410\ 0000108-00008 | [6 도 이 40 이 00720720720 | [580102001] | 1219018575 0416 6006(60[6 01 016 041760015 20400108 60001184178000 07 8 9410661 01 0386 0001184080000,.466 016 940\7000108-60104 용 000101800 10 0416 80000700 ㅁ 816 200006@. * ㆍ 60406: (0000081) 6 이 4068 8 60601116 00721184080070 17010 0416 0162018 11066 016 6406 165\070 10110\60 67 8 0077277107/70 8784006001 10 6%01406 8 90601116 600011847801070 17010 016 016018. * ㆍ 60002071470: (0000081) 1219218575 0217 8 91016 0000021800 07 8 540866 0[ 06000048008 8781186616 40067 8 506011160 600004800 201006@. ㆍ 58010200: (070007081) 1016018575 8 598011200 00011841780070 107 5816 0190011641100 800 808157519. 268100108 \101 (21600 페 -056 《616856 10.3(2), 54010200 165\010 18 540000060 070 (21900 페 6%348 9000 862166 5\1661168. |
| 9410\ 56420410-000108 | 1219018575 016 61800042 600118478007. 띠 066 18760 3 68660 1680176 00701184180005 876 01680160 10 016 20070108-007118. 016 540\ 5617600410-060011 용 600104800 00665 ㅁ 01 01920167 01622. 10\676, 0416 06001184000006 17601810 10080 10 0416 6680002 0255, 4001 016 60003 70070108 5630000 000001800 16 060000060. |
| 940\ 0046-562000 1047070108- ㅇ 07018 1256-0020860 | 1219018575 016 11066[84022 \1160 016 0100108 0001184180 ㅁ 070 \88 1891 01180860. |

The following example shows sample output of show running-config command with the sanitized keyword. The sanitized configuration is used to share a configuration without exposing some configuration details.

This option masks the sensitive words in running configuration output with <removed> keyword.

```cisco-ios
switch# show running-config sanitized
```

!Command: show running-config sanitized !Running configuration last done at: Wed Oct 12 09:14:54 2022 !Time: Wed Oct 12 13:52:55 2022 version 10.3(2) Bios:version 07.69 username admin password 5 <removed> role network-admin copp profile strict snmp-server user admin network-admin auth md5 <removed> priv aes-128 <removed> localizedV2key rmon event 1 log trap <removed> description FATAL(1) owner PMON@FATAL rmon event 2 log trap <removed> description CRITICAL(2) owner PMON@CRITICAL rmon event 3 log trap <removed> description ERROR(3) owner PMON@ERROR

username admin password 5 <removed> role network-admin

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

49

| |

## Using PowerOn Auto Provisioning

| |

## Troubleshooting for POAP

rmon event 4 log trap <removed> description WARNING(4) owner PMON@WARNING rmon event 5 log trap <removed> description INFORMATION(5) owner PMON@INFO --More--

## Troubleshooting for POAP

The following is a list of known issues and suggestions while using POAP:

- • Issue: POAP script execution fails immediately with no syslogs or output except for a "Script execution failed" statement.

Suggestion: Use the python script-name command on the server and make sure there are no syntax errors. The options dictionary is a Python dictionary so each entry must be comma separated and have the key or option and the value separated by a colon.

- • Issue: A TypeError exception occurs at various places depending on the incorrectly used option.

Suggestion: Some options use integers (for example, timeouts and other numeric values). Check the options dictionary for numeric values that are enclosed in quotes. Refer to the options list for the correct usage.

- • Issue: POAP over USB is not finding the files that are present.

Suggestion: Some devices have two USB slots. If you are using USB slot 2, you need to specify that as an option.

- • Issue: Any issue with POAP.

Suggestion: Abort POAP, and when the system boots up, run the show tech-support poap command, which displays POAP status and configuration.

## Managing the POAP Personality

## POAP Personality

The POAP personality feature, which is introduced in Cisco NX-OS Release 7.0(3)I4(1), enables user data, Cisco NX-OS and third-party patches, and configuration files to be backed up and restored. In previous releases, POAP can restore only the configuration.

The POAP personality is defined by tracked files on the switch. The configuration and package list in the

personality file are ASCII files.

Binary versions are recorded in the personalityfile, but the actualbinary files are not included. Becausebinary files are typically large, they are accessed from a specified repository.

The personality file is a .tar file, which would typically be extracted into a temporary folder. Here is an example:

## switch# dir bootflash: 042516182843personality # timestamp name

46985 Dec 06 23:12:56 2015 running-config Same as “show running-configuration” command. 20512 Dec 06 23:12:56 2015 host-package-list Package/Patches list 58056 Dec 06 23:12:56 2015 data.tar User Data 25 Dec 06 23:12:56 2015 IMAGEFILE Tracked image metadata

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

50

ㅣ

|!

## Using PowerOn Auto Provisioning

## Backing Up the POAP Personality

## Backing Up the POAP Personality

You can create a backup of the POAP personality either locally on the switch or remotely on the server. The personality backup taken from the switch should be restored only on a switch of the same model.

%

- Note If you are using the Cisco scheduler feature for backups, you can configure it to also back up the POAP personality, as shown in the following example. For more information on the scheduler, see the Cisco Nexus 9000 Series NX-OS System Management Configuration Guide.

```cisco-ios
switch(config)# scheduler schedule name weeklybkup switch(config-schedule)# time weekly mon:07:00 switch(config-schedule)# job name personalitybkup switch(config-schedule)# exit switch(config)# scheduler job name personalitybkup switch(config-job)# personality backup bootflash:/personality-file ; copy bootflash:/personality-file tftp://10.1.1.1/ vrf management
```

## SUMMARY STEPS

1. personality backup [bootflash:uri | scp:uri]

## DETAILED STEPS

Procedure

|  | 600001800 0726000 | 『00 ㅁ 056 |
|---|---|---|
| 51601 | 복 6041760: 06650001165 028 이 0040 [000002911777 | 56011071] 6801016: 3160150# ㅁ 668500211 ㄴ 7 1620102 16000 ㄴ 『12616106 ㅁ 800 ㅁ 211 ㄴ 71 . 12~ 6801016: 3160150# ㅁ 668500211 ㄴ 7 1620102 80086:// ㅋ 00602.1.1.1/7282/116/ ㄴ ㄷ 60600 ㄴ 62006. ㄴ 2~ | (2768666 8 6800040 01 046. 02(0 ㅅ 0 ㅁ 6060081165. |

## Configuring the POAP Personality

You can specify whether the POAP personality should be derived from the running state of the system or the committed (startup) state.

## SUMMARY STEPS

1. configure terminal

2. personality

3.

track [running-state | startup-state | data local-directories-or-files]

4. binary-location source-uri-folder

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

51

| |

## Using PowerOn Auto Provisioning

| |

## Configuring the POAP Personality

## DETAILED STEPS

## Procedure

Purpose

Command or Action

| 80 1 | 복 6041760: 600008466@ (60001421 60801016: 38 뒤 1601# ㅇ 002 ㅁ 5,19456 ㄴ 6501 ㅁ 21 으 1606 (6020 조 10) 부 | 트 마 666 인 06861 00011841780070 20006. |
|---|---|---|
| 30 2 | 복 6041760: 06050021165 60801016: 으 듀 1 느 00# 0 66 네 5072 끄 167 81606 (60722,19- ㅁ 66556002 그 3167) 추 | 트 마 606 26060081167 000118418000 00006. |
| 30 3 | 복 6041760: 6080 [0 ㅁ 0070108-5666 | 5640000-56266 | 0212 70007-0776000776%-07-77769] | 306011166 40\ 016 『20 ㅅ 2 ㅁ 6090081157 15 06060. 1116 10110\108 000005 876 878118616: |
|  | 60801016: 38160 (602 ㅁ 2,19- ㅁ 66 ㅁ 500 ㅁ 2117) # ㄴ ㄴ 20 02 ㄴ 2 1600『1265610 ㅁ 71161 60801016: 38160 (602 ㅁ 2,19- ㅁ 66 ㅁ 500 ㅁ 2117) # ㄴ ㄴ 20 02 ㄴ 2 156006『12616104662 50212656/^0 | *1747070108-56366--('82001768 0416 10110\10 을 101000081107: 1466 240010 을 6000118478000 (89 510\10 10 1016 540\ 1407010 용 -60011 용 6000201800), 80076 (21600 찌 ×-08 72860068 800 01100-08267 28 아 86865 10 016 1081 5756(620, 800 016 4270886 ㅁ 81046 (895 5910\10 10 016 9040\ 60910 06010004800). 11116 16 016 00613416( 00007. |
|  | 60801016: 38160 (602 ㅁ 2,19- ㅁ 66 ㅁ 500 ㅁ 2117) # ㄴ ㄴ 20 02 ㄴ 2 1600 ㄴ ㄷ 1281:626601 ㄴ ㅁ /*/1201040_02 ㄴ 2 | 568160410-56866--('80041768 016 10110\108 101070018007: 1466 96800042 600118478007 (05 5940\1 10 016 540\ 568600- ㅇ 00018 000002800), 000210010660 (21600 찌 ×-(08 72860068 800 01100-08267 28 아 86865 10 016 1081 5756(620, 800 016 4270886 ㅁ 81046 (895 5910\10 10 016 9040\ 60910 000000800). 0868 70007-077607077069-07-7776$--976011165 8 010606075 07 116 10 66 680660 042. 704 680 60667 0116 600002840 10416216 00068 (0 68042 204101216 01276010066 800 11168. 니 제 1%-667016 \1106870 01187801676 8176 940001[60. 10 016 68104216, 006 10106 800 60070 01260602066 876 506011160. 띠 066 100 201 456 10116 600000840 (0 68 이 0472 61081 1166 10 046 160010894 800 00 201 00101 (0 0416 60076 6001101891. |

Step 1

Step 2

Step 3

Guest Shell packages are not tracked.

## Note

Signed RPMs (which require a key) are not supported. The POAPpersonalityfeaturedoesnotworkwithsignedRPMs.

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

52

ㅣ

|!

## Using PowerOn Auto Provisioning

## Restoring the POAP Personality

| 51660 4 | 복 6041760: 0108650-1008004 9070<6-2077-70706/" | 306011166 0416 10081 07 7600016 01760[07 17010 \11011 10 210 |
|---|---|---|
|  | 6801016: 31606 (6022,19- ㅁ 6652600 ㅁ 2117) 165102 ㄴ 7-10 ㅇ 2 ㄴ 1 ㅇ ㅁ 806:// ㄴ 6040 ㄴ 6-01 ㅁ 1/ ㅁ ×05 ㅁ 08 ㄴ ㅇ ㅁ 65 7 | 1402 01087 11166 \1160 016 020 ㅅ [ ㅁ ㅁ 6060081167 16 769[01760. 04 080 6066 0116 6000008600 00416216 02068 (10 02067 01 20 ㅁ 02150) 10 9060115 204107016 10080 ㅁ 0708. |

## Restoring the POAP Personality

During the POAP script execution phase, the personality module in the script restores the POAP personality, provided that the currently booted switch image is Cisco NX-OS Release 7.0(3)I4(1) or later. If necessary, upgrade the switch to the correct software image.

<

> **NOTE**
> Note

- A personality restore is done with the same software image used for the personality backup. Upgrading to a newer image is not supported through the POAP personality feature. To upgrade to a newer image, use the regular POAP script.

<

> **NOTE**
> Note

- If the personality script fails to execute for any reason (such as not enough space in the bootflash or a script execution failure), the POAP process returns to the DHCP discovery phase.

The restore process performs the following actions:

1. Untars and unzips the personality file in the bootflash.

2. Validates the personality file.

3. Reads the configuration and package list files from the personality file to make a list of the binaries to be downloaded.

4.

- If the current image or patches are not the same as specified in the personality file, downloads the binaries to the bootflash (if not present) and reboots with the correct image and then applies the packages or patches.

5. Unzips or untars the user data files relative to "/".

6. Copies the configuration file in the POAP personality to the startup configuration.

7. Reboots the switch.

## POAP Personality Sample Script

The following sample POAP script (poap.py) includes the personality feature:

#md5sum="b00a7fffb305d13a1e02cd0d342afca3"

# The above is the (embedded) md5sum of this file taken without this line, # can be # created this way:

- # f=poap.py ; cat $f | sed '/^#md5sum/d' > $f.md5 ; sed -i "s/^#md5sum=.*/#md5sum=$(md5sum $f.md5 | sed 's/ .*//')/" $f # This way this script's integrity can be checked in case you do not trust # tftp's ip checksum. This integrity check is done by /isan/bin/poap.bin). # The integrity of the files downloaded later (images, config) is checked # by downloading

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

53

| |

## Using PowerOn Auto Provisioning

107

## POAP Personality Sample Script

the corresponding file with the .md5 extension and is # done by this script itself.

from poap.personality import POAPPersonality import os # Location to download system image files, checksums, etc. download_path = "/var/lib/tftpboot" # The path to the personality tarball used for restoration personality_tarball = "/var/lib/tftpboot/foo.tar" # The protocol to use to download images/config protocol = "scp" # The username to download images, the personality tarball, and the # patches and RPMs during restoration username = "root" # The password for the above username password = "passwd754" # The hostname or IP address of the file server server = "2.1.1.1" # The VRF to use for downloading and restoration vrf = "default" if os.environ.has_key('POAP_VRF'): vrf = os.environ['POAP_VRF'] # Initialize housekeeping stuff (logs, temp dirs, etc.) p = POAPPersonality(download_path, personality_tarball, protocol, username, password, server, vrf) p.get_personality() p.apply_personality() sys.exit(0)

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

54

5

C H A P T E R 5

## Using Network Plug and Play

This chapter contains these sections:

- • About Network Plug and Play, on page 55

- • Troubleshooting Examples for Network Plug and Play, on page 63

## About Network Plug and Play

Network Plug and Play (PnP) is a software application that runs on a Cisco Nexus 9500 Series Switch (specifically, N9K-C9504, N9K-C9508, and N9K-C9516). The PnP feature provides a simple, secure, unified, and integrated offering to make a new branch or campus rollouts much easier, or for provisioning updates to an existing or a new network. This feature provides a unified approach to provision networks comprising multiple devices with a near-zero-touch deployment experience.

Simplifieddeploymentreducesthecostandcomplexityandincreasesthespeedandsecurityofthedeployments. The PnP feature helps simplify the deployment of any Cisco device by automating the following deployment-related operational tasks:

- • Establishing initial network connectivity for a device.

- • Delivering device configuration to the controller.

- • Delivering software and firmware images to the controller.

- • Provisioning local credentials of a switch.

- • Notifying other management systems about deployment-related events.

The PnP is a client-server based model. The client (agent) runs on a Cisco Nexus 9500 Series Switch and the server (controller) runs on the Cisco DNA Controller.

PnP uses a secure connection to communicate between the agent and the controller. This communication is encrypted.

For information on configuring and managing the needed security certificate(s) for PnP functionality, see the Cisco Digital Network Architecture Center Security Best Practices Guide.

The PnP agent converge solutions that exist in a network into a unified agent and adds additional functionality toenhancethecurrentsolutions.ThemainobjectivesofthePnPagentistoprovideconsistentDay0deployment solution for all the deployment scenarios.

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

55

| |

## Using Network Plug and Play

## About Network Plug and Play

## Features Provided by the Network Plug and Play (PnP) Agent

## Day 0 Provisioning

Day 0 bootstrapping includes the configuration, image, and other files. When a device is powered on for the first time, the PnP discovery process, which is embedded in the device, gets enabled in the absence of a startup configuration file and attempts to discover the address of the PnP controller or server. The PnP agent uses methods such as DHCP, Domain Name System (DNS), and others to acquire the desired IP address of the PnP server.

When the PnP agent successfully acquires the IP address, it initiates a long-term, bidirectional Layer 3 connection with the server and waits for a message from the server. The PnP server application sends messages to the corresponding agent, requesting for information about the devices and the services to be performed on the device.

The agent running on the Cisco Nexus 9500 Series switch then configures the IP address on receiving the DHCP acknowledgment and establishes a secure channel with the controller to provision the configurations. The switch then upgrades the image and applies the configurations.

## Discovery Methods

A PnP agent discovers the PnP controller or server using one of the following methods:

- • DHCP-based discovery

• DNS-based discovery

• PnP connect

After the discovery, the PnP agent writes the discoveredinformationinto a file, which is then used to handshake with the PnP server (DNA controller/DNA-C).

The following tasks are carried out by the agent in the PnP discovery phase:

- • Brings up all the interfaces.

- • Sends a DHCP request in parallel for all the interfaces.

- • On receiving a DHCP reply, configures the IP address and mask, default route, DNS server, domain name, and writes the PnP server IP in a lease-parsing file. Note that there is no DHCP client in Cisco Nexus Switches and static configuration is required.

• Brings down all the interfaces.

%

> **NOTE**
> Note

- POAP is the first order of choice for Day 0 provisioning. Only when there is no valid POAP offer, PnP discovery is attempted. Also, PnP is supported only on Cisco Nexus 9000 EoR models N9K-C9504, N9K-C9508, and N9K-C9516. PnP is not supported on Cisco Nexus 9000 ToRs.

## DHCP-Based Discovery

When the switch is powered on and if there is no startup configuration, the PnP starts with DHCP discovery. DHCP discovery obtains the PnP server connectivity details.

The PnP agent configures the following:

- • IP address

• Netmask

• Default gateway

• DNS server

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

56

|

|

## Using Network Plug and Play

## About Network Plug and Play

• Domain name

If the agent configuration fails, you should manually intervene and configure the switch.

DHCP discovery has the following flow:

- • Power on the switch.

- • Switch will boot up, the PnP process will be started, as there is no configuration present.

- • Start DHCP discovery.

- • DHCP Server replies with the PnP server configuration.

- • PnP agent handshakes with the PnP server.

- • Download the image, install, and reload.

- • Download and apply the configuration from the controller.

A device with no startup configuration in the NV-RAM triggers the day 0 provisioning and goes through the POAP process (as detailed in m_using_poweron_auto_provisioning_92x.ditamap#id_70221). When there is no valid POAP offer, the PnP agent is initiated. The DHCP server can be configured to insert additional information using vendor-specific Option 43. Upon receiving Option 60 from the device with the string (cisco pnp), to pass on the IP address or hostname of the PnP server to the requesting device. When the DHCP responseis receivedby thedevice,thePnP agentextractstheOption43 from theresponseto gettheIP address or the hostname of the PnP server. The PnP agent then uses this IP address or hostname to communicate with the PnP server.

Figure8:DHCPDiscoveryProcessforPnPServer

60 06106 16 00\6「60 00. 0 ㅁ 6106 6185 마 10『 16006 66006 1『10 00100 43 8009 \ 따 06466 『 6\ 061066 661801161166 00006 10 『000 56006『 @ @ 마 310 66006『「 (66000056 \ 마 00 391499

## DNS-Based Discovery

When the DHCP discovery fails to get the PnP server, the agent falls back to DNS-based discovery. To start the DNS-based discovery, the following information is required from DHCP:

• IP address and netmask

• Default gateway

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

57

빼

'

## Using Network Plug and Play

## About Network Plug and Play

- • DNS server IP

• Domain name

The agent obtains the domain name of the customer network from the DHCP response and constructs the fully qualified domain name (FQDN). The following FQDN is constructed by the PnP agent using a preset deployment server name and the domain name information for the DHCP response. The agent then looks up the local name server and tries to resolve the IP address for the above FQDN.

Figure9:DNSLookupforpnpserver.[domainname].com

얄 띠 6\0 06106 16 00\6「60 00. 0 ㅁ 6106 61815 마 10 이 600160 (20 마 10 66006「 「(6500006 \ 따 1 0606 1『, 0070810 08016 800 02046 66006『 @ 0 ㅁ 6106 (6806 0010810 08006 800 아 68166 0「6060060『 마 66106 08106 (000560/6「.01600.0001) 300 「6501066 10「1『0 30016656 [4] 띠 6\ 061066 661801161166 00006 이 6 10 『0 마 0 56706『 391501

<

- Note The device reads domain name and creates predefined PnP server name as pnpserver.[domain name].com, for example; pnpserver.cisco.com.

## Plug and Play Connect

When the DHCP and the DNS discovery fail, the PnP agent discovers and communicates with Cisco Cloud-based deployment service for initial deployment. The PnP agent directly opens an HTTPS channel using the Python library, which internally invokes OpenSSL to talk with cloud for configuration.

## Cisco Power On Auto Provisioning

Cisco Power On Auto Provisioning (PoAP) communicates with the DHCP and TFTP servers to download the image and configurations. With the introduction of the PnP feature, PnP and PoAP coexist together in a Cisco Nexus 9500 Series Switch. PoAP and PnP interworking has the following processes:

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

58

|

|!

## Using Network Plug and Play

## About Network Plug and Play

- • PoAP starts first when no start-up configuration is present in the system.

• PnP starts later if PoAP does not get provisioned.

- • PoAP and PnP discover the controller alternatively.

- • The controller discovery process continues until a controller or until the admin aborts auto provision.

- • The process (POAP or PnP) that finds the controller continues provisioning and the other process that does not find the controller is notified and eventually terminated.

## Services and Capabilities of the Network Plug and Play Agent

The PnP agent performs the following tasks:

- • Backoff

• Capability

• CLI execution

• Configuration upgrade

• Device information

• Certificate install

• Image install

- • Redirection

<

- Note The PnP controller or server provides an optional checksum tag to be used in the image installation and configuration upgrade service requests by the PnP agent. When the checksum is provided in a request, the image install process compares the checksum against the current running image checksum.

If the checksums are same, the image being installed or upgraded is the same as the current image running on the device. The image install process will not perform any other operation in this scenario.

If the checksums are not the same, the new image will be copied to the local file system, and the checksum will be calculated again and compared with the checksum provided in the request. If they are the same, the image install process continues to install the new image or upgrade the device to the new image. If the checksums are not the same, the process exits with an error.

## Backoff

A Cisco NX-OS device that supports PnP protocol, which uses HTTP transport, requires the PnP agent to send the work request to the PnP server continuously. If the PnP server does not have any scheduled or outstanding PnP service for the PnP agent to execute, the continuous no-operation work requests exhaust both the network bandwidth and the device resources. This PnP backoff service allows the PnP server to inform the PnP agent to rest for the specified time and call back later.

## Capability

Capability service request is sent by the PnP server to the PnP agent on a device to query the supported services by the agent. The server then sends an inventory service request to query the device's inventory information; and then sends an image installation request to download an image and install it. After getting the response from the agent, the list of supported PnP services and features are enlisted and returned back to the Server.

## CLI Execution

Cisco NX-OS supports two modes of command execution, privileged EXEC mode and global configuration mode. Most of the EXEC commands are one-time commands, such as show commands, which show the current configuration status, and clear commands, which clear counters or interfaces. The EXEC commands

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

59

| |

| |

## Using Network Plug and Play

## About Network Plug and Play

arenot savedwhen a devicereboots.Configurationmodecommandsallowuser to makechangesto therunning configuration. If you save the configuration, these commands are saved when a device reboots.

## Configuration Upgrade

Two types of configuration upgrades takes place in a Cisco device—copying new configuration files to the startup configuration and copying new configuration files to the running configuration.

Copying new configuration files to the startup configuration—A new configuration file is copied from the file server to the device using the copy command, and the file check task is performed to check the validity of the file. If the file is valid, the file is copied to the startup configuration. The previous configuration file is backed up if enough disk space is available. The new configuration comes into effect when the device reloads again.

Copying new configuration files to the running configuration—A new configuration file is copied from the file server to the device using the copy command or configure replace command. Replace and rollback of configuration files may leave the system in an unstable state if rollback is performed inefficiently. Therefore, configuration upgrade by copying the files is preferred.

## Device Information

The PnP agent provides the capability to extract device inventory and other important information to the PnP server on request. The following device-profile request types are supported:

- • all—Returns complete inventory information, which includes unique device identifier (UDI), image, hardware, and file system inventory data.

- • filesystem—Returns file system inventory information, which includes file system name and type, local size (in bytes), free size (in bytes), read flag, and write flag.

- • hardware—Returns hardware inventory information, which includes hostname, vendor string, platform name, processor type, hardware revision, main memory size, I/O memory size, board ID, board rework ID, processor revision, mid-plane revision, and location.

- • image—Returnsimage inventory information, which includes version string, image name, boot variable, return to ROMMON reason, bootloader variable, configuration register, configuration register on next boot, and configuration variables.

• UDI—Returns the device UDI.

## Certificate Install

Certificate install is a security service through which a PnP server requests the PnP agent on a device for trust pool or trust point certificate installation or uninstallation. This service also specifies the agent about the primaryandbackupserversforreconnection.Thefollowingprerequisitesarerequiredforasuccessfulcertificate installation:

- • The server from which the certificate or trust pool bundle needs to be downloaded should be reachable.

- • There should not be any permission issues to download the certificate or the bundle.

- • The PKI API should be available and accessible for the PnP agent so that the agent could call to download and install the certificate or the bundle.

- • There is enough memory on the device to save the downloaded certificate or bundle.

## PnP Agent

The PnP agent is an embedded software component that is present in all Cisco network devices that support simplified deployment architecture. The PnP agent understands and interacts only with a PnP server. The PnP agent first tries to discover a PnP server, with which it can communicate.After a server is found and connection established, the agent performs deployment-related activities such as configuration, image and file updates

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

60

|

|

## Using Network Plug and Play

## About Network Plug and Play

by communicating with the server. It also notifies the server of all interesting deployment-related events such as out-of-band configuration changes and new device connections on an interface.

## PnP Server

The PnP server is a central server that encodes the logic of managing and distributing deployment information (images, configurations, files, and licenses) for the devices being deployed. The server communicates with the agent on the device that supports the simplified deployment process using a specific deployment protocol.

Figure10:SimplifiedDeploymentServer

626. 50516075 …---- _ 퀴 트 6009 |4- | 00160 51916006 6 아어 56006 | [| 055/855 91492

The PnP server also communicates with proxy servers such as deployment applications on smart phones and PCs, or other PnP agents acting as Neighbor Assisted Provisioning Protocol (NAPP) servers, and other types of proxy deployment servers such as VPN gateways.

The PnP server can redirect the PnP agent to another deployment server. A common example of redirection is a PnP server redirecting a device to communicate with it directly after sending the bootstrap configuration through a NAPP server. A PnP server can be hosted by an enterprise. This solution allows for a cloud-based deployment service provided by Cisco. In this case, a device discovers and communicates with Cisco cloud-based deployment service for initial deployment. After that, it can be redirected to the customer's deployment server.

In addition to communicating with the devices, the server interfaces with a variety of external systems such as authentication, authorizing, and accounting (AAA) systems, provisioning systems, and other management applications.

## PnP Agent Deployment

The following steps indicate the PnP agent deployment procedure on Cisco devices:

1. A Cisco device with a PnP agent contacts the PnP server, requesting for a task, that is, the PnP agent sends UDI along with a request for work.

2.

- If the PnP server has a task for the device, for example, image installation, configuration, upgrade, and so on, it sends a work request.

3. After the PnP agent receives the work request, it executes the task and sends back a reply to the PnP server about the task status, that is whether it is successful or if an error has occurred, and the corresponding information that is requested.

## PnP Agent Network Topology

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

61

빼

## Using Network Plug and Play

| |

## Guidelines and Limitations for Network Plug and Play

## Figure11:NetworkTopologyofCiscoPnPAgentDeployment

마 0 ~ 56006「 고기. 개 00 「 고 [ 버 터 6 { 경 56008「 ｌ 6700 56008「56009 , 톡 ^ 60465 10 아노 0619100 061000080000 뜨 즈 책 개 0" 01010088000 미 56706「 2 10000 | 064661010666 00 ( 는 800 (66000061\0 따 0 0689160「 | 101000708800006070 | 18049 솔 = 수 2 르스 건 으르 91494

## PnP Agent Initialization

The PnP agent is enabled by default, but can be initiated on a device when the startup configuration is not

available.

## Absence of Startup Configuration

New Cisco devices are shipped to customers with no startup configuration file in the NVRAM of the devices. When a new device is connected to a network and powered on, the absence of a startup configuration file on the device automatically triggers the PnP agent to discover the PnP server IP address.

## CLI Configuration for the PnP Agent

PnP supports devices that are using VLAN 1 by default.

## Guidelines and Limitations for Network Plug and Play

Network Plug and Play (PnP) guidelines and limitations are as follows:

- • Beginning with NX-OS 9.2(3), PnP is supported on the management port of Cisco Nexus 9500 platform switches.

- • PnP runs on both the in-band and the management interfaces. In-band is supported only on FX-series line cards (specifically N9K-X9736C-FX for PnP).

- • The PnP deployment method depends on the discovery process that is required for finding the PnP controller or server.

- • The discovery mechanism must be deployed, either as a DHCP server discovery process or a Domain Name Server (DNS) discovery process, before launching PnP.

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

62

|

|!

## Using Network Plug and Play

## Troubleshooting Examples for Network Plug and Play

- • Configure the DHCP server or the DNS server before deploying PnP.

• The PnP server must communicate with the PnP agent.

- • PnP connect does not require a DHCP or DNS configuration.

- • IPv6 support for PnP is not available for Cisco Nexus 9500 Series devices.

## Cisco DNA Center Support

The following guidelines and limitations are specific for PnP connectivity to the Cisco DNA Center:

- • Cisco DNA Center supports the following functionality on the Cisco Nexus 9504, Cisco Nexus 9508, and Cisco Nexus 9516 switches:

- • Discovery

- • Inventory

- • Topology

- • Template Programmer

『

- • Software Image Management

- • Basic Monitoring

- • The following PnP guidelines and limitationsare only for the Cisco DNA Center version 1.2.6 and earlier:

- • The startup configuration that is provided during plug and play must ensure that the connectivity for the interface that is connected to the Cisco DNA Center remains intact.

- • The system image .bin and startup configuration must be uploaded to the Cisco DNA Center.

- • The bootflash must have enough space to download the image and configurations from the Cisco DNA Center.

Click here for the user documentation for the Cisco DNA Center.

## Troubleshooting Examples for Network Plug and Play

## Example: Troubleshooting PnP

The following examples shows the PnP troubleshooting command outputs:

```cisco-ios
Switch# show pnp status PnP Agent is running server-connection status: Success time: 08:41:26 Jan 11 interface-info status: Success time: 08:34:00 Jan 11 device-info status: Success time: 08:33:46 Jan 11 config-upgrade status: Success
```

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

63

| |

| |

## Using Network Plug and Play

## Troubleshooting Examples for Network Plug and Play

time: 08:31:36 Jan 11 capability status: Success time: 08:33:50 Jan 11 backoff status: Success time: 08:41:26 Jan 11 topology status: Success time: 08:33:54 Jan 11

```cisco-ios
Switch# show pnp version PnP Agent Version Summary
```

PnP Agent: 1.6.0 Platform Name: nxos PnP Platform: 1.5.0.rc2

```cisco-ios
Switch# show pnp profiles Created by UDI DHCP Discovery PID:N9K-C9504,VID:V01,SN:FOX1813GCZ8
```

Primary transport: https Address: 10.105.194.248 Port: 443 CA file: /etc/pnp/certs/trustpoint/pnplabel

Work-Request Tracking:

Pending-WR: Correlator=

Cisco-PnP-POSIX-nxos-1.6.0-21-589a466a-0d88-427b-a17e-69afb7d0a226-1

Last-WR:

Correlator=

Cisco-PnP-POSIX-nxos-1.6.0-20-ab225de4-b0ef-46c5-9c4f-e3bd9f7c6b87-1

PnP Response Tracking:

Last-PR:

Correlator=

Cisco-PnP-POSIX-nxos-1.6.0-20-ab225de4-b0ef-46c5-9c4f-e3bd9f7c6b87-1

```cisco-ios
Switch# show pnp lease
```

"lease": { "uptime": "Fri Jan 11 05:32:17 2019", "intf": "Vlan1", "ip_addr": "10.77.143.239", "mask": "255.255.255.0", "gw": "10.77.143.1", "domain": "", "opt_43": "5A1D;B2;K4;I10.105.194.248;J80", "lease": "3600", "server": "10.77.143.231", "vrf": "1" }

{

}

## Switch# show pnp internal trace

- 1) Event:E_DEBUG, length:49, at 907122 usecs after Fri Jan 11 08:30:44 2019 [104] pnp_ascii_gen: ascii gen completed rcode[0]

- 2) Event:E_DEBUG, length:16, at 907094 usecs after Fri Jan 11 08:30:44 2019 [104] pss type: 5

- 3) Event:E_DEBUG, length:31, at 907069 usecs after Fri Jan 11 08:30:44 2019 [104] Entering pnp_ascii_gen_cfg

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

64

|

|

## Using Network Plug and Play

## Troubleshooting Examples for Network Plug and Play

- 4) Event:E_DEBUG, length:22, at 907061 usecs after Fri Jan 11 08:30:44 2019 [104] Calling Ascii gen

- 5) Event:E_DEBUG, length:16, at 907051 usecs after Fri Jan 11 08:30:44 2019 [104] pss type: 2

- 6) Event:E_DEBUG, length:49, at 907018 usecs after Fri Jan 11 08:30:44 2019 [104] pnp_ascii_gen: fu_num_acfg_pss_entries[0x2]

- 7) Event:E_DEBUG, length:49, at 973813 usecs after Fri Jan 11 08:29:51 2019 [104] pnp_ascii_gen: ascii gen completed rcode[0]

- 8) Event:E_DEBUG, length:16, at 973787 usecs after Fri Jan 11 08:29:51 2019 [104] pss type: 5

- 9) Event:E_DEBUG, length:31, at 973760 usecs after Fri Jan 11 08:29:51 2019 [104] Entering pnp_ascii_gen_cfg

- 10) Event:E_DEBUG, length:22, at 973751 usecs after Fri Jan 11 08:29:51 2019 [104] Calling Ascii gen

- 11) Event:E_DEBUG, length:16, at 973742 usecs after Fri Jan 11 08:29:51 2019 [104] pss type: 2

- 12) Event:E_DEBUG, length:49, at 973707 usecs after Fri Jan 11 08:29:51 2019 [104] pnp_ascii_gen: fu_num_acfg_pss_entries[0x2]

- 13) Event:E_DEBUG, length:35, at 535794 usecs after Fri Jan 11 08:04:15 2019 [104] pnp_pi_spawn_finalize pid 690

- 14) Event:E_DEBUG, length:41, at 228291 usecs after Fri Jan 11 08:04:13 2019 [104] + pnp_pi_spawn child_pid: 0xdd526da0

- 15) Event:E_DEBUG, length:76, at 132853 usecs after Fri Jan 11 08:03:26 2019 [104] Rx: Direction: PnP PI -> PnP PD, Type: Device Provisioned, Cfg: Present

- 16) Event:E_DEBUG, length:35, at 440380 usecs after Fri Jan 11 08:03:18 2019 [104] !!! ACKED Unconfigure Ret:1!!!

- 17) Event:E_DEBUG, length:61, at 440347 usecs after Fri Jan 11 08:03:18 2019 [104] Tx: Direction: Max, Type: DHCP Unconfigure Done, Len: 16

- 18) Event:E_DEBUG, length:35, at 440331 usecs after Fri Jan 11 08:03:18 2019 [102] Unknown timer cancel requested

- 19) Event:E_DEBUG, length:35, at 440311 usecs after Fri Jan 11 08:03:18 2019 [104] pnp_pss_runtime_commit success

- 20) Event:E_DEBUG, length:57, at 440103 usecs after Fri Jan 11 08:03:18 2019 [104] pnp_pss_runtime_commit: Stored values in runtime PSS

- 21) Event:E_DEBUG, length:23, at 440051 usecs after Fri Jan 11 08:03:18 2019 [104] - pnp_vsh_halt:206

- 22) Event:E_DEBUG, length:17, at 950291 usecs after Fri Jan 11 08:03:15 2019 [104] Adding "end"

- 23) Event:E_DEBUG, length:58, at 950269 usecs after Fri Jan 11 08:03:15 2019 [104] Adding "configure terminal ; no clock protocol none "

- 24) Event:E_DEBUG, length:33, at 945994 usecs after Fri Jan 11 08:03:15 2019 [104] - pnp_vsh_config_l3_intf:788

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

## 65

| |

| |

## Using Network Plug and Play

## Troubleshooting Examples for Network Plug and Play

- 25) Event:E_DEBUG, length:29, at 945979 usecs after Fri Jan 11 08:03:15 2019 [104] + pnp_vsh_config_l3_intf

- 26) Event:E_DEBUG, length:39, at 945963 usecs after Fri Jan 11 08:03:15 2019 [104] Adding "no feature interface-vlan"

- 27) Event:E_DEBUG, length:32, at 945932 usecs after Fri Jan 11 08:03:15 2019 [104] Adding "configure terminal"

- 28) Event:E_DEBUG, length:40, at 945886 usecs after Fri Jan 11 08:03:15 2019 [104] Got Semaphore, vsh halt continue...

- 29) Event:E_DEBUG, length:46, at 945870 usecs after Fri Jan 11 08:03:15 2019 [104] sem_timedwait Success, Start VSH clean up

- 30) Event:E_DEBUG, length:19, at 945843 usecs after Fri Jan 11 08:03:15 2019 [104] + pnp_vsh_halt

- 31) Event:E_DEBUG, length:35, at 945831 usecs after Fri Jan 11 08:03:15 2019 [104] pnp_pss_runtime_commit success

- 32) Event:E_DEBUG, length:57, at 945643 usecs after Fri Jan 11 08:03:15 2019 [104] pnp_pss_runtime_commit: Stored values in runtime PSS

- 33) Event:E_DEBUG, length:33, at 945607 usecs after Fri Jan 11 08:03:15 2019 [104] !!! Received Unconfigure !!!

- 34) Event:E_DEBUG, length:74, at 945578 usecs after Fri Jan 11 08:03:15 2019 [104] Rx: Direction: PnP PI -> PnP PD, Type: DHCP Unconfigure, Cfg: Present

- 35) Event:E_DEBUG, length:49, at 789616 usecs after Fri Jan 11 08:01:52 2019 [104] pnp_ascii_gen: ascii gen completed rcode[0]

- 36) Event:E_DEBUG, length:16, at 789579 usecs after Fri Jan 11 08:01:52 2019 [104] pss type: 5

- 37) Event:E_DEBUG, length:31, at 789522 usecs after Fri Jan 11 08:01:52 2019 [104] Entering pnp_ascii_gen_cfg

- 38) Event:E_DEBUG, length:22, at 789514 usecs after Fri Jan 11 08:01:52 2019 [104] Calling Ascii gen

- 39) Event:E_DEBUG, length:16, at 789506 usecs after Fri Jan 11 08:01:52 2019 [104] pss type: 2

- 40) Event:E_DEBUG, length:49, at 789489 usecs after Fri Jan 11 08:01:52 2019 [104] pnp_ascii_gen: fu_num_acfg_pss_entries[0x2]

- 41) Event:E_DEBUG, length:35, at 789365 usecs after Fri Jan 11 08:01:52 2019 [104] pnp_pss_runtime_commit success

- 42) Event:E_DEBUG, length:57, at 789135 usecs after Fri Jan 11 08:01:52 2019 [104] pnp_pss_runtime_commit: Stored values in runtime PSS

- 43) Event:E_DEBUG, length:26, at 789096 usecs after Fri Jan 11 08:01:52 2019 [104] Phase Init -> Monitor

- 44) Event:E_DEBUG, length:35, at 788967 usecs after Fri Jan 11 08:01:52 2019 [104] pnp_pi_spawn_finalize pid 1c9

- 45) Event:E_DEBUG, length:41, at 831561 usecs after Fri Jan 11 08:01:49 2019 [104] + pnp_pi_spawn child_pid: 0xffff7e28

- 46) Event:E_DEBUG, length:45, at 831550 usecs after Fri Jan 11 08:01:49 2019

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

66

|

|

## Using Network Plug and Play

## Troubleshooting Examples for Network Plug and Play

- [104] Have startup config, Starting PnP PI....

- 47) Event:E_DEBUG, length:40, at 831538 usecs after Fri Jan 11 08:01:49 2019 [104] Posix log directory creation failed

- 48) Event:E_DEBUG, length:50, at 831479 usecs after Fri Jan 11 08:01:49 2019 [104] pnp_fire_event: PNP_EVENT_HAVE_STARTUP_CONFIG

- 49) Event:E_DEBUG, length:35, at 831465 usecs after Fri Jan 11 08:01:49 2019 [104] Inside : pnp_other_msg_handler

- 50) Event:E_DEBUG, length:80, at 831437 usecs after Fri Jan 11 08:01:49 2019 [104] pnp_get_data_from_queue: dequeued event 0x1102e0cc 25/cat 11 from pending Q

- 51) Event:E_DEBUG, length:50, at 831368 usecs after Fri Jan 11 08:01:49 2019 [104] Injecting Event PNP_EVENT_HAVE_STARTUP_CONFIG

- 52) Event:E_DEBUG, length:59, at 831303 usecs after Fri Jan 11 08:01:49 2019 [104] Have Startup Config, move the process state to monitor

- 53) Event:E_DEBUG, length:57, at 799379 usecs after Fri Jan 11 08:01:49 2019 [104] Accelerating PnP, Break Point: Break Point PoAP Init

- 54) Event:E_DEBUG, length:35, at 799334 usecs after Fri Jan 11 08:01:49 2019 [104] pnp_pss_runtime_commit success

- 55) Event:E_DEBUG, length:57, at 799239 usecs after Fri Jan 11 08:01:49 2019 [104] pnp_pss_runtime_commit: Stored values in runtime PSS

- 56) Event:E_DEBUG, length:23, at 799226 usecs after Fri Jan 11 08:01:49 2019 [104] Phase None -> Init

- 57) Event:E_DEBUG, length:53, at 799200 usecs after Fri Jan 11 08:01:49 2019 [104] Initilizing PnP-agent State machine curr_state 3

- 58) Event:E_DEBUG, length:35, at 799188 usecs after Fri Jan 11 08:01:49 2019 [104] pnp_pss_runtime_commit success

- 59) Event:E_DEBUG, length:57, at 799070 usecs after Fri Jan 11 08:01:49 2019 [104] pnp_pss_runtime_commit: Stored values in runtime PSS

- 60) Event:E_DEBUG, length:26, at 798965 usecs after Fri Jan 11 08:01:49 2019 [104] !!! Box is Online !!!

- 61) Event:E_DEBUG, length:35, at 798954 usecs after Fri Jan 11 08:01:49 2019 [104] pnp_pss_runtime_commit success

- 62) Event:E_DEBUG, length:57, at 798770 usecs after Fri Jan 11 08:01:49 2019 [104] pnp_pss_runtime_commit: Stored values in runtime PSS

- 63) Event:E_DEBUG, length:70, at 370297 usecs after Fri Jan 11 07:55:41 2019 [102] pnp_demux_mts(463): (Warning) unexpected mts msg (opcode - 7655)

- 64) Event:E_DEBUG, length:41, at 092701 usecs after Fri Jan 11 07:55:33 2019 [104] PnP Init Internal subsystem, Done!!!

- 65) Event:E_DEBUG, length:32, at 089920 usecs after Fri Jan 11 07:55:33 2019 [104] PnP Init Internal subsystem

## Switch# show pnp posix_pi configs

/isan/etc/pnp/platform_config.cfg:

/isan/etc/pnp/file_paths.cfg:

## Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

67

| |

| |

## Troubleshooting Examples for Network Plug and Play

/isan/etc/pnp/pnp_config.cfg: /isan/etc/pnp/policy_discovery.conf: /isan/etc/pnp/certs/platform.json: /isan/etc/pnp/certs/pnp_status.json: /isan/etc/pnp/certs/job_status.json:

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

68

## Using Network Plug and Play

|

6

C H A P T E R 6

## Understanding the Command-Line Interface

This chapter contains these sections:

- • About the CLI Prompt, on page 69

- • Command Modes, on page 70

- • Special Characters, on page 74

- • Keystroke Shortcuts, on page 75

- • Abbreviating Commands, on page 78

- • Completing a Partial Command Name, on page 78

- • Identifying Your Location in the Command Hierarchy, on page 79

- • Using the no Form of a Command, on page 79

- • Configuring CLI Variables, on page 80

- • Command Aliases, on page 82

- • Command Scripts, on page 85

- • Context-Sensitive Help, on page 87

- • Understanding Regular Expressions, on page 88

- • Searching and Filtering show Command Output, on page 89

- • Searching and Filtering from the --More-- Prompt, on page 94

- • Using the Command History, on page 95

- • Enabling or Disabling the CLI Confirmation Prompts, on page 97

- • Setting CLI Display Colors, on page 97

- • Sending Commands to Modules, on page 98

- • Sending Command Output in Email, on page 99

- • BIOS Loader Prompt, on page 101

- • Examples Using the CLI, on page 101

## About the CLI Prompt

Once you have successfully accessed the device, the CLI prompt displays in the terminal window of your console port or remote workstation as shown in the following example:

User Access Verification login: admin Password:<password> Cisco Nexus Operating System (NX-OS) Software TAC support: http://www.cisco.com/tac

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

69

## Understanding the Command-Line Interface

| |

## Command Modes

Copyright (c) 2002-2013, Cisco Systems, Inc. All rights reserved. The copyrights to certain works contained in this software are owned by other third parties and used and distributed under license. Certain components of this software are licensed under the GNU General Public License (GPL) version 2.0 or the GNU Lesser General Public License (LGPL) Version 2.1. A copy of each such license is available at http://www.opensource.org/licenses/gpl-2.0.php and http://www.opensource.org/licenses/lgpl-2.1.php switch#

You can change the default device hostname.

From the CLI prompt, you can do the following:

- • Use CLI commands for configuring features

- • Access the command history

- • Use command parsing functions

<

> **NOTE**
> Note

- In normal operation, usernames are case sensitive. However, when you are connected to the device through its console port, you can enter a login username in all uppercase letters regardless of how the username was defined. As long as you provide the correct password, the device logs you in.

## Command Modes

This section describes command modes in the Cisco NX-OS CLI.

## EXEC Command Mode

When you first log in, the Cisco NX-OS software places you in EXEC mode. The commands available in EXEC mode include the show commands that display the device status and configuration information, the clear commands, and other commands that perform actions that you do not save in the device configuration.

## Global Configuration Command Mode

Global configuration mode provides access to the broadest range of commands. The term indicates characteristics or features that affect the device as a whole. You can enter commands in global configuration mode to configure your device globally or to enter more specific configuration modes to configure specific elements such as interfaces or protocols.

## SUMMARY STEPS

1. configure terminal

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

70

ㅣ

|!

## Understanding the Command-Line Interface

## Interface Configuration Command Mode

## DETAILED STEPS

Procedure

|  | 600001800 0726000 | 『00 ㅁ 056 |
|---|---|---|
| 51601 | 000841@ 6(60001021 | 트 마 666 인 06861 00011841780070 20006. |
|  | 606801016: 9\1608# 00021961456 ㄴ 6501061 81606 (600【319) 츄 | 티 06 7116 (21.1170000006(0080868 (0 140108[6 4186 104 876 10 10681 0600118418000 00006. |

## Interface Configuration Command Mode

One example of a specific configuration mode that you enter from global configuration mode is interface configuration mode. To configure interfaces on your device, you must specify the interface and enter interface configuration mode.

Youmustenablemanyfeaturesonaper-interfacebasis.Interfaceconfigurationcommandsmodifytheoperation of the interfaces on the device, such as Ethernet interfaces or management interfaces (mgmt 0).

For more information about configuring interfaces, see the Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide.

## SUMMARY STEPS

1. configure terminal

2.

interface type number

## DETAILED STEPS

Procedure

|  | 600001800 0726000 | 『00 ㅁ 056 |
|---|---|---|
| 51601 | 000841@ 6(60001021 6801016: 38 뒤 1601# ㅇ 002 ㅁ 5,19456 ㄴ 6501 ㅁ 21 으 1606 (6020 조 10) 부 | 트 마 666 인 06861 00011841780070 20006. |
| 5160 2 | 1066 타 060 71276 72707706/" | 306011166 0416 1016 다 306 0186 104 \810[ 10 0070118416@. |
| 6801016: 81600 (602 ㅁ 죄 190) 부 10 ㄴ 622206 66206 | 7116 (1.1 216068 704 1010 10160806 0001184780070 20006 107 1446 606011160 1066 다 306. |
| 요다 (60208,106-1 조 ) 부 | 띠 066 |
|  | 7116 (21.1 0700021 00180866 10 10010686(6 04481 704 876 10 10660806 0070118418000 00006. |

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

71

| |

## Understanding the Command-Line Interface

| |

## Subinterface Configuration Command Mode

## Subinterface Configuration Command Mode

From global configuration mode, you can access a configuration submode for configuring VLAN interfaces called subinterfaces. In subinterface configuration mode, you can configure multiple virtual interfaces on a single physical interface. Subinterfaces appear to a protocol as distinct physical interfaces.

Subinterfaces also allow multiple encapsulations for a protocol on a single interface. For example, you can configure IEEE 802.1Q encapsulation to associate a subinterface with a VLAN.

For more information about configuring subinterfaces, see the Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide.

## SUMMARY STEPS

1. configure terminal

2.

interface type number.subint

## DETAILED STEPS

Procedure

|  | 600007800 0726000 | 『00 ㅁ 056 |
|---|---|---|
| 5160 1 | 000847@ 6(60001021 60801016: 38 뒤 1601# ㅇ 002 ㅁ 5,19456 ㄴ 6501 ㅁ 21 으 1606 (6020 조 10) 부 | 트 마 666 인 06861 00011841780070 20006. |
| 6160 2 | 1066 타 2060 77276 727007706/.51007777 60801016: 81606 (602 ㅁ 219) 뷰 10 ㄴ 622206 66206 2/72.1 81600 (6020 ㅁ 8,196-5401 조 ) 부 | 306011166 016 누 스지 10[(60406 10 66 00201184160. 7116 21.1218068 704 1060 8 5416106(60800 00011841800000006@ 107 016 50601060 스티 1066 다 306. 띠 066 7116 (21.1 0700021 00180866 10 10010686(6 04481 704 876 10 9461016 다 306 6001184780070 20006. |

Step 1

Step 2

## Saving and Restoring a Command Mode

The Cisco NX-OS software allows you to save the current command mode, configure a feature, and then restore the previous command mode. The push command saves the command mode, and the pop command restores the command mode.

The following example shows how to save and restore a command mode:

```cisco-ios
switch# configure terminal
switch(config)# event manager applet test switch(config-applet)# push switch(config-applet)# configure terminal switch(config)# username testuser password newtest switch(config)# pop switch(config-applet)#
```

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

72

ㅣ

|!

## Understanding the Command-Line Interface

## Exiting a Configuration Command Mode

## Exiting a Configuration Command Mode

## SUMMARY STEPS

1. exit

2. end

- (Optional) Ctrl-Z

## DETAILED STEPS

Procedure

|  | 600001800 0726000 | 『00 ㅁ 056 |
|---|---|---|
| 56601 | 60 6801016: 으 뒤 프 00 (6020 조 196-1 조 ) 퓨 611 으 1606 (6020 조 10) 부 | 뜨 16 0010 016 04060 600118418000 000000800 0 ㅁ 006 800 1604709 (0 016 276\1045 6070118418000 600001800 22006. |
| 5660 2 | 600 6801016: 81600 (602052196-12) 뷰 620 5\101# | 뜨 16 0010 016 04060 600118418000 000000800 0 ㅁ 006 800 1604009 60 80: 24006. |
| 5160 3 | (00002081) 002 6801016: 31606 (602 ㅁ 5,19-1<) 우스 5\101# | 트 찌 (9 016 0410606(60701184180010 000004800 21006 800 76[04708 10 608: 2006. 684000 1704 00665 ( 그 디 -2, 41 416 600 01 8 000000600 1146 10 \11101 88110 6000021800 1185 0660 67060, 0416 (:1.1 8008 016 0600004800 (0 016200010108 6000118478007 1116. 10 2208 08968, 304 9910410 611 8 602011846780000000614810 응 0416 6511 07 600 0600004800. |

## Command Mode Summary

This table summarizes information about the main command modes.

Table4:CommandModeSummary

| 01006 | 66655 1064100 | 『10040 | 60「00460100 |
|---|---|---|---|
| 68 | 7000 016 10810 270100206 0016 1047 466008006 800 0859\070. | 으 위그노 | 70 6611 10 016 10810 2701001. 486 046 6 60020002800. |
| (31061 000108408000 | 7000 600: 2006, 456 016 | 0000840@ (60011 0600000800. | 901600 (002519) 총 | 10 6011 10 80 2 ㅁ 006. 466 016 600 07 61 000001800 07 27659 002. |

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

73

| |

## Understanding the Command-Line Interface

| |

## Special Characters

| 01006 | 66655 1064100 | 『10040 | 60「00460100 |
|---|---|---|---|
| 10660806 0001184780070 | 700 인 06861 0020118478002 10006, 9060117 80 10160806 1\0101 30 1066 타 466 000000840. | 31056 (6028,19-1<) 푸 | 70 6011 10 인 00861 002118478002 10006, 456 10416 61 000004800. 10 6011 10 80 2 ㅁ 006. 466 016 6 600001800 07 27655 ( 기 01-2.. |
| 옵 40106(6 다 306 0001184780070 | 700 인 06861 0020118478002 10006, 9060117 8 54610160806 1\0101 30 1066 타 466 000000840. | 30100 (00205,106- ㄱ 51401) 취 | 70 6011 10 인 00861 002118478002 10006, 456 10416 61 000004800. 10 6011 10 80 2 ㅁ 006. 466 016 600 600001800 07 27655 ( 기 디 -2.. |
| 재 0001184780070 | 700 인 06861 0020118478002 10006, 456 016 다 0010002800 300 906011/ 8704108 20010001. | 81056 (6072 조 19-976 호 ) 퓨 | 70 6011 10 인 00861 002118478002 10006, 456 10416 61 000004800. 10 6011 10 80 2 ㅁ 006. 466 016 600 600001800 07 27655 ( 기 디 -2.. |
| 80: 1078 70006[3416 자 | 7000 600: 2006, 456 016 104008-60066 되 쿠 【 0020101800 300 69060117 8 70 | 316010- ㄴ 60 | 710 61110 016 0613416 자 456 06 701460108-6010166 되 지다 0012416 06010000800. |

## Special Characters

This table lists the characters that have special meaning in Cisco NX-OS text strings and should be used only in regular expressions or other special contexts.

Table5:SpecialCharacters

| 아 18100 | | 065000000 |
|---|---|
| % | 60060 |
| # | 20400, 48914. 07 7 ㅁ 40206 |
|  | 트 110518 |
|  | 투 6001081 687 |
| <> | 트 696 0180 07 2068660 04182 |
| [] | 278016666 |
| {} | 278068 |

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

74

ㅣ

|!

## Understanding the Command-Line Interface

## Keystroke Shortcuts

## Keystroke Shortcuts

This table lists command key combinations that can be used in both EXEC and configuration modes.

Table6:KeystrokeShortcuts

| (615601668 | 066000000 |
|---|---|
| 1- 스 | 40769 0416 007607 10 016 66810010 을 01 016 1106. |
| 20-8 | 40769 0416 047607 006 이 181000667 10 016 1616. \160 704 60167 8 600002800 018 6×(6008 66040 3910 인 61106,704 080 ㅁ 1727669 0161.61 ㅅ ㅁ 00\ 07 ( 가 다 -0 675 76006816017 (0 567011 680 10\810 1446 9796600 200000206 800 60117 0416 668100108 01 416 60020202800 6005, 07 704 080 0668 016 1 피 - 스 67 0002061080072. |
| 20 | (2800616 0416 600000800 800 7604706 10 016 600002800 070100206 ㄴ |
| 20-2 | 10616668 0446 0118608016『 81 0416 04760 |
| 20 | 40769 016 000907 10 016 600 01 016 1106. |
| ( 어 내 비 이 | 40769 0416 000607 006 0118780167 10 046 22141. |
| 20-6 | 『%1[6 10 016 07671046 60100104800 22006 \101041[ 76100 416 6010001800 60408. |
| 20 | 12616668 811 아 1808001679 17010 0416 047607 10 016 600 01 0416 600000800 1106. |
| ( 어 내 빈 비 | \601921879 0416 04060 000001800 1106. |
| 1- 지 | 121601879 0416 46 000002800 10 016 600000800 1116107%. |
| 200-0 | (16876 016 (60001081 507662. |
| ( 어 내 비 이 | 12160189 0416 206\1048 60104008100 10 10416 6000048100 1116607. |
| 03 | \601921879 0416 04060 000001800 1106. |
| (아내 레보 | 77806900566 016 011828 이 67 40067 0416 00476907 \101 0416 이 187806(67 10086(60 10 016 피임 01 016 0041760. 1116 04760 19 0160 20060 10 1016 2 ㅁ 011 006 이 18086. |
| 20-0 | 12616669 311 01187801679 17010 1016 041607 10 0416 668100108 01 0416 600000800 1106. |
| 20 | \602069 807 5060181 2468010 을 107 0416 10110\10 응 659060166. 07 68200216, 27055 ( 가 디 - 투 1661076 6016008 8 44660070 2084 (?) 10 87084187 0%1017655107. |
| 20-\ | 12616668 0416 \0170 10 016 161 01 0416 00760. |
| 20, 브 | [1969 0416 1116601 01 0000028008 704 1186 60[6760. |
| \1160 45108 0119 667 60006010811070, 20696 800 7616866 016 (그 300 초 6575 10860167 66016 72065910 은 뻐 . |
| 0- 호 | \608116 0416 24096 76000[ 600 10 016 6041167 (07665 6575 5101411606014815). |

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

75

| |

| |

## Keystroke Shortcuts

|

|

76

## Understanding the Command-Line Interface

| 002 | 009 8 6001184780070 5666100, 800 7604705 104 10 (1 22006. \1160 4660 8[ 0416 600 01 8 600000800 11046 10 \114011 8 78110 6070001800 1186 66610 67060, 016 |
|---|---|
|  | 16941008 60001184000070 16 11761 80060 (0 0416 20100108 60001184180 ㅁ 07 1116. |
| 00 000\ 67 | |101601679 0446 206\1048 6010400800 10 0416 60004048100 1116607. |
| 120\0 80001\ 6? | 1219018575 016 06 600001800 10 016 600004800 1116607%. |
| 때인 8000\ 665 트 61 800\ 665 | | 5410766 70417 007907 4170411 416 600001800 60718, 61016 102\0810 07 68 이 00810, 8110\14 을 04 10 6011 016 0410601 6000008200. |
| ? | 1219018575 8 119 01 878118616 6000018008. |

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

ㅣ

|!

## Understanding the Command-Line Interface

## Keystroke Shortcuts

Keystrokes Tab Description Completes the word for you after you enter the first characters of the word and then press the Tab key. All options that match are presented. Use tabs to complete the following items: • Command names • Scheme names in the file system • Server names in the file system • Filenames in the file system Example: switch(config)# xm<Tab> switch(config)# xml<Tab> switch(config)# xml server Example: switch(config)# c<Tab> callhome class-map clock cdp cli control-plane switch(config)# cl<Tab> class-map cli clock switch(config)# cla<Tab> switch(config)# class-map Example: switch# cd bootflash:<Tab> bootflash:/// bootflash://sup-1/ bootflash://sup-active/ bootflash://sup-local/ bootflash://module-27/ bootflash://module-28/ Example: switch# cd bootflash://mo<Tab> bootflash://module-27/ bootflash://module-28/

```cisco-ios
switch# cd bootflash://module-2
```

> **NOTE**
> Note

You cannot access remote machines using the cd command. If you are on slot 27 and enter the cd bootflash://module-28 command, the following message appears: "Changing directory to a non-local server is not allowed."

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

77

| |

## Understanding the Command-Line Interface

| |

## Abbreviating Commands

## Abbreviating Commands

You can abbreviate commands and keywords by entering the first few characters of a command. The abbreviation must include sufficient characters to make it unique from other commands or keywords. If you are having trouble entering a command, check the system prompt and enter the question mark (?) for a list of available commands. You might be in the wrong command mode or using incorrect syntax.

This table lists examples of command abbreviations.

Table7:ExamplesofCommandAbbreviations

| 600001800 | 씨 0016 바 8000 |
|---|---|
| 00108466@ 6(60001021 | 00011 |
| 005 2000108-000108 5600040-000108 | | 60025 2020 나 |
| 1066 다 200 00160006[ 172 | 1060 172 |
| 9410\ 170070108-007011 을 | 541 707 |

## Completing a Partial Command Name

If you cannot remember a complete command name or if you want to reduce the amount of typing you have to perform, enter the first few letters of the command, and then press the Tab key. The command line parser will complete the command if the string entered is unique to the command mode. If your keyboard does not have a Tab key, press Ctrl-I instead.

The CLI recognizes a command once you have entered enough characters to make the command unique. For example, if you enter conf in EXEC mode, the CLI will be able to associate your entry with the configure command, because only the configure command begins with conf.

In the following example, the CLI recognizes the unique string for conf in EXEC mode when you press the Tab key:

```cisco-ios
switch# conf<Tab> switch# configure
```

When you use the command completion feature, the CLI displays the full command name. The CLI does not executethe commanduntilyou press the Return or Enter key. This featureallowsyou to modify the command if the full command was not what you intended by the abbreviation. If you enter a set of characters that could indicate more than one command, a list of matching commands displays.

For example, entering co<Tab> lists all commands available in EXEC mode beginning with co:

```cisco-ios
switch# co<Tab> configure copy switch# co
```

> **NOTE**
> Note that the characters you entered appear at the prompt again to allow you to complete the command entry.

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

78

ㅣ

|!

## Understanding the Command-Line Interface

## Identifying Your Location in the Command Hierarchy

## Identifying Your Location in the Command Hierarchy

Some features have a configuration submode hierarchy nested more than one level. In these cases, you can display information about your present working context (PWC).

## SUMMARY STEPS

1. where detail

## DETAILED STEPS

Procedure

| 51601 | \1666 06634 |  | 121901875 016 2\(:. |
|---|---|---|---|
| 6801016: |  |  |
| 38 뒤 1601# ㅇ 002 ㅁ 5,19456 ㄴ | 6501 ㅁ 21 |  |
| 31605 (60722,19) 유 10 ㄴ | 6652306 피 90 ㅁ ㄴ 0 |  |
| 으 뒤 포 00 (6072 ㅁ 죄 106-1<) 뷰 | 626 06211 |  |
| 피 0061 | 002 |  |
|  | 1066 ㅋ =3266 2 ㅁ 9760 |  |
| 146620 ㅁ 08006: | 2000127 |  |
| 포 0046109-0 ㅇ 02068 다 | 062 2016 |  |

## Using the no Form of a Command

Almost every configuration command has a no form that can be used to disable a feature, revert to a default value, or remove a configuration.

This example shows how to disable a feature:

```cisco-ios
switch# configure terminal switch(config)# feature tacacs+ switch(config)# no feature tacacs+
```

This example shows how to revert to the default value for a feature:

```cisco-ios
switch# configure terminal switch(config)# banner motd #Welcome to the switch# switch(config)# show banner motd Welcome to the switch
switch(config)# no banner motd switch(config)# show banner motd User Access Verification
```

This example shows how to remove the configuration for a feature:

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

79

| |

## Understanding the Command-Line Interface

| |

## Configuring CLI Variables

```cisco-ios
switch# configure terminal switch(config)# radius-server host 10.10.2.2 switch(config)# show radius-server retransmission count:0 timeout value:1 deadtime value:1 total number of servers:1 following RADIUS servers are configured: 10.10.1.1: available for authentication on port:1812 available for accounting on port:1813 10.10.2.2: available for authentication on port:1812 available for accounting on port:1813
switch(config)# no radius-server host 10.10.2.2
switch(config)# show radius-server
```

retransmission count:0

timeout value:1

deadtime value:1

total number of servers:1

following RADIUS servers are configured: 10.10.1.1: available for authentication on port:1812 available for accounting on port:1813

This example shows how to use the no form of a command in EXEC mode:

```cisco-ios
switch# cli var name testinterface ethernet1/2 switch# show cli variables SWITCHNAME="switch" TIMESTAMP="2013-05-12-13.43.13" testinterface="ethernet1/2"
switch# cli no var name testinterface switch# show cli variables SWITCHNAME="switch" TIMESTAMP="2013-05-12-13.43.13"
```

## Configuring CLI Variables

This section describes CLI variables in the Cisco NX-OS CLI.

## About CLI Variables

The Cisco NX-OS software supports the definition and use of variables in CLI commands.

You can refer to CLI variables in the following ways:

- • Entered directly on the command line.

- • Passed to a script initiated using the run-script command. The variables defined in the parent shell are available for use in the child run-script command process.

CLI variables have the following characteristics:

- • Cannot have nested references through another variable

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

80

ㅣ

|!

## Understanding the Command-Line Interface

## Configuring CLI Session-Only Variables

- • Can persist across switch reloads or exist only for the current session

Cisco NX-OS supports one predefined variable: TIMESTAMP. This variable refers to the current time when the command executes in the format YYYY-MM-DD-HH.MM.SS.

<

- Note

The TIMESTAMP variable name is case sensitive. All letters must be uppercase.

## Configuring CLI Session-Only Variables

You can define CLI session variables to persist only for the duration of your CLI session. These variables are useful for scripts that you execute periodically. You can reference the variable by enclosing the name in parentheses and preceding it with a dollar sign ($), for example $(variable-name).

## SUMMARY STEPS

1. cli var name variable-name variable-text

2.

(Optional) show cli variables

## DETAILED STEPS

Procedure

|  | 6801016: 8 뒤 1600# | 611 | 78 | ㅁ 206 ㄴ 656 ㄴ 1 ㅁ ㄴ 6 ㄴ | 2206 66206 271 @684100006[15 108%104410 @68400606[15 95108069, 800 1189 띠 066 268107010 을 \101 82086169 6870 |  | 8120118041046010, 0866 560510 ㅋ 6, 800 1185 8 1608041 01 31 01182801669. 1116 2077070/6-200 810118041046016, 0856 56091076, 6080 007206810 8 018×100410 16001 01 200 이 13280(668. (21600 씨 -058 티 6856 7.0(3)14(1). 1001406 1157011605 (-) 8300 40067900765 (_ ). |
|---|---|---|---|---|---|---|---|
| 5160 2 | (0000081) 6801016: 316010# | 5980 510 | 011 011 | 디 다 30165 572881216168 | 1219218575 016 |  | (01.1 782 ㅁ 86016 60701184780 ㅁ 07. |

## Configuring Persistent CLI Variables

You can configure CLI variables that persist across CLI sessions and device reloads.

## SUMMARY STEPS

1. configure terminal

2. cli var name variable-name variable-text

3. exit

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

81

| |

## Understanding the Command-Line Interface

| |

## Command Aliases

- (Optional) show cli variables

- (Optional) copy running-config startup-config

## DETAILED STEPS

Procedure

|  | 600007800 0726000 | 『00 ㅁ 056 |
|---|---|---|
| 51601 | 000847@ 6(60001021 60801016: 38 뒤 1601# ㅇ 002 ㅁ 5,19456 ㄴ 6501 ㅁ 21 으 1606 (6020 조 10) 부 | 트 마 666 인 06861 00011841780070 20006. |
| 5160 2 | 위 1 지레 22026 907707070-7207770 70770/070-760 터 3 보 미 6 미하 으 디 1600 (0020 네 190) 뷰 011 72 ㅁ 806 ㄴ 68 ㄴ 2/1 | (2001184168 016 (:1.1 0615166(60[ 782 ㅁ 8616. 1116 780 ㅁ 8016 ㅁ 0810 19 8 0896-960910176, 61011804146016 50108 800 00491 6610 \14| 320 810086606 08006. 1116 016%101410 160801 16 31 162 티 17806 ㆍ 띠 066 268107010 을 \101 (21600 피 -056 16856 7.0(3)14(1). 82086169 6870 1001406 1157011605 (-) 8300 40067900765 (_ ). |
| 5160 3 | 603 60801016: 을 (6020 조 16) # 681 느 8 뒤 103 | 2069 인 0081 000118478000 00006. |
| 5160 4 | (0000081) 5980 듀 011 디 다 30165 60801016: 3 뒤 1601# 610 011 781216168 | 1219218575 016 (01.1 782 ㅁ 86016 60701184780 ㅁ 07. |
| 5160 5 | (0000081) 0005 『0070108-0070118 5640260010-6001 60801016: 81600 (0072219) 00072 120001 ㅁ 9- ㅇ 01 ㅁ | (200166 0416 210010 용 00011841780070 (0 016 618002 의 060011841800270. |

Configures the CLI persistent variable. The variable name

is a case-sensitive,alphanumericstring and must begin with

## Command Aliases

This section provides information about command aliases.

## About Command Aliases

You can define command aliases to replace frequently used commands. The command aliases can represent all or part of the command syntax.

Command alias support has the following characteristics:

- • Command aliases are global for all user sessions.

82

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

ㅣ

|!

## Understanding the Command-Line Interface

## Defining Command Aliases

- • Command aliases persist across reboots if you save them to the startup configuration.

- • Command alias translation always takes precedence over any keyword in any configuration mode or submode.

- • Command alias configuration takes effect for other user sessions immediately.

- • The Cisco NX-OS software provides one default alias, alias, which is the equivalent to the show cli alias command that displays all user-defined aliases.

- • You cannot delete or change the default command alias alias.

- • You can nest aliases to a maximum depth of 1. One command alias can refer to another command alias that must refer to a valid command, not to another command alias.

- • A command alias always replaces the first command keyword on the command line.

- • You can define command aliases for commands in any command mode.

- • If you reference a CLI variable in a command alias, the current value of the variable appears in the alias, not the variable reference.

- • You can use command aliases for show command searching and filtering.

<

> **NOTE**
> Note

- When using the cli alias name command, few keywords are reserved and cannot be used. To view the list of reserved keywords, type the show cli internal keywords common command. The reserved keywords match either partially or fully. For instance, in the cli alias name i show version command, i is a partial match. To prevent the use of reserved keywords, enable strict checking using the cli alias check strict command. This command is not enabled by default. After enabling the command, if a user attempts to use any reserved keywords, the switch displays an error.

## Defining Command Aliases

You can define command aliases for commonly used commands.

## SUMMARY STEPS

1. configure terminal

2. cli alias name alias-name alias-text

3. exit

4. (Optional) alias

5.

(Optional) copy running-config startup-config

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

83

| |

## Understanding the Command-Line Interface

| |

## Configuring Command Aliases for a User Session

## DETAILED STEPS

## Procedure

|  | 600007800 0726000 |  | 『00 ㅁ 056 |
|---|---|---|---|
| 51601 | 000847@ 6(60001021 60801016: 38 뒤 1601# ㅇ 002 ㅁ 5,19456 ㄴ 6501 ㅁ 21 으 1606 (6020 조 10) 부 |  | 트 마 666 인 06861 00011841780070 20006. |
| 5160 2 | 01 31185 08106 07/705-7207776 07205-760 60801016: 3801600 (60010) 011 21125 7 ㅁ 206 666206 느 | 10 ㄴ 622 206 | (2001184168 016 600001800 81189. 1116 81189 ㅁ 81006 18 82 히 218041006016 9000 용 448[(1600(6856 660510176 800 00456 66810 : : : : \101 80 6101866606 이 18180666. 1116 018×1171410 16001 16 30 17869. |
| 5160 3 | 603 60801016: 을 (6020 조 16) # 681 느 |  | 2069 인 0081 000118478000 00006. |
| 5160 4 | 8 뒤 103 (06000081) 31185 60801016: |  | 1219218575 016 000002800 81185 6001184180 ㅁ 07. |
| 5160 5 | 58\1601# 21125 (0000081) 0005 『0070108-0070118 | 5640260010-6001 을 | (200166 0416 210010 용 00011841780070 (0 016 618002 060011841800270. |
|  | 60801016: 38 뒤 160150# 60209 12400109- ㅇ 012 ㅁ 619 | ~6000-002 ㅁ 519 |  |

## Configuring Command Aliases for a User Session

You can create a command alias for the current user session that is not available to any other user on the Cisco NX-OS device. You can also save the command alias for future use by the current user account.

## SUMMARY STEPS

terminal alias [persist] alias-name command-string

## DETAILED STEPS

Procedure

|  | 600007800 0726000 | 『00 ㅁ 056 |
|---|---|---|
|  | 501600# ㄴ 6201021 21125 51010 50609 1066522206 55216 | 1446 0496 80001406. 되 티 066 |

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

84

ㅣ

|!

## Understanding the Command-Line Interface

## Command Scripts

| 100 201 80676 ㅋ 1866 016 065156[ 65\070. |
|---|

## Command Scripts

This section describes how you can create scripts of commands to perform multiple tasks.

## Running a Command Script

You can create a list of commands in a file and execute them from the CLI. You can use CLI variables in the command script.

<

- Note You cannot create the script files at the CLI prompt. You can create the script file on a remote device and copy it to the bootflash: or volatile: directory on the Cisco NX-OS device.

## SUMMARY STEPS

1. run-script [bootflash: | volatile:] filename

## DETAILED STEPS

Procedure

|  | 600001800 0726000 |  | 『00 ㅁ 056 |
|---|---|---|---|
| 1601 | 140-5001061000108911: | | 01210161] /7/0070776 | 표지 66066 016 6000018008 10 016 1116 070 016 0613416 012606075. |
| 6801016: |  |  |
| 3816056# 0200-50 ㅋ 16 | ㄴ 66 ㄴ 5116 |  |

Step 1

## Echoing Information to the Terminal

You can echo information to the terminal, which is particularly useful from a command script. You can reference CLI variables and use formatting options in the echoed text.

This table lists the formatting options that you can insert in the text.

Table8:FormattingOptionsfortheechoCommand

| 『00080109 00000 | 06501100400 |
|---|---|
| 6 | 10669 680 9708068. |
| 6 | 복 6200766 0160 ㅁ 6\ 11046 01181780167 86 416 600 01 016 16%[ 50018. |

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

85

| |

## Understanding the Command-Line Interface

| |

## Delaying Command Action

| 00000 | 0650110000 |
|---|---|
| 낸 | 10566 8 10070 1660 01180806@ ㅠ |
| 2 | 10560 8.06\ 1106 0118028066 ㅁ . |
| 뇨 | 복 604209 (0 016 66810010 을 01 016 (6 1166. |
| 나 | 10560 8 4020200181 186 0118080 이 6 |
| \ | 10566 8 ㅋ 6001681 606 001808006 ㄷ |
|  | 1216218579 8 08 이 66518911 011828 이 66. |
| 02202 | 101601859 0416 600 ㅠ 6500700108 811 00181 00828006 ㄷ |

## SUMMARY STEPS

1. echo [backslash-interpret] [text]

## DETAILED STEPS

Procedure

|  | 600007800 | 0726000 | 『00 ㅁ 056 |
|---|---|---|---|
| 0160 1 | 6000 [02 | 51511-106(6001761] [760] | 7116 08016510511-1066001661665\070 14010686(69 018 416 16 |
|  | 60801016: 3\16010# 모 118 18 | 60106 띠 118 18 28 ㄴ ㄷ 68 ㄴ ㄴ ㄴ 68 ㄴ ㄴㄴ | 50010 6000686106 1007086008 000008. 1116 7607 878410006 15 히 218041006016, 0856 96091076, 800 680 60701810 01806. 1116 108%100410 16001 16 200 01180800(678. 1116 061341116 8 61810 1106. |

Step 1

## Delaying Command Action

You can delay a command action for a period of time, which is particularly useful within a command script.

## SUMMARY STEPS

1. sleep seconds

## DETAILED STEPS

Procedure

|  | 600007800 0726000 | 『00 ㅁ 056 |
|---|---|---|
| 51601 | 위 660 56007705 | (284568 8 00137 1078 2 ㅁ 40006 01 5600008. 1116 78086 16 12070 010 2147483647. |

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

86

ㅣ

|!

## Understanding the Command-Line Interface

## Context-Sensitive Help

## Context-Sensitive Help

The Cisco NX-OS software provides context-sensitive help in the CLI. You can use a question mark (?) at any point in a command to list the valid input options.

CLI uses the caret (^) symbol to isolate input errors. The ^ symbol appears at the point in the command string where you have entered an incorrect command, keyword, or argument.

This table shows example outputs of context sensitive help.

Table9:Context-SensitiveHelpExample

| 3016056# 36 3\16058# | 61606? 0208 10041 68 016 ㅇ < |  | 602260 ㄴ 모 106 | 1216218579 0416 600001800 57018 107 0416 0100 06000041800 10 8: 2006. 7116 5\16011 04041 9140\86 1418 016 566 165\010 18 16041760 10『14610 을 0416 010 6020001800. |
|---|---|---|---|---|
| 3\16056# 뒤 080 | 01660 38104; | 96 ? | 60207672 | 또 106 | 121621859 0416 600001800 97018 1017 56100 416 02006. |
| 3\16056# | 01060 | 56 566 | ㅁ 0 |  | 7116106120 04104 910\9 018 0416 0410606[ 10006 18 16041760 107 5660208 016 이 00 800 10\ (0 10008 016 11006. |
| 3016056# 응 100006016\ | 01060 ㄴ ㅎㅇ 0 ㅇ | 56 00027 | 13132: | 00<08> | 스 006 016 00410 ㅁ 0606 10206. |
| 5\101# |  |  |  |  | 7116 (01.1 10401686(66 0416 600001800 16 14001072166(6. |
| 3016056# | <06601-2> |  |  |  | 121601859 0416 2001048 6010004800 04181 704 6066060. |
| 35\16080# | 0100 | 56 | 13132100 |  |  |
| 5\16050# | 01060 0100 | 56 2287 0, 56 | 13132100 ㄴ 6 13132100 | ? 20250 | 1216016579 0416 80010107081 8184006066 107 0416 0100 566 0600004800. |
|  |  |  |  | 0416 80010107081 107 0416 0100 566 |
| <1-31> 35\16080# 3\16010# 26211 즈 040498 2 ㅁ 60 ㅇ 6006 보 662428 느 크 프 느 르 노 르포 00406 02208 2 기 607600006@ 060 ㄴ 6066- 3626 ㄴ 3\16010# | 01060 떠 는 떠 떠 포 두 떠 우 떠 떠 떠 떠 떠 떠 떠 6000062 0 0160 | 56 62061 62061 62061 62061 62061 62061 62061 62061 62061 62061 62061 200 트 56 | 13132100 6 66 6 66 6 66 6 66 6 66 6 66 6 66 6 66 6 66 6 66 6 66 0 66 13132100 | 18 ? 762 ㅁ 762 ㅁ 762 ㅁ 762 ㅁ 762 ㅁ 762 ㅁ 762 ㅁ 762 ㅁ 762 ㅁ 762 ㅁ 762 ㅁ 7626 18 | 1216016579 8184006066 0600004800. 스 0068 0416 0816 (0 016 이 006 56600 음 . |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |
| 01066 56 13132100 18 2065211 13<08> 1004 06 ㄴ ㄷ 60 ㅇ ㄴ 60 2 ㄴ ^! 패 82665. |  |
| 301600# 은 10732110 | 7116 (01.1100108166 80 60007 \101 416 68766 85006001 (^) 8113. |

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

87

| |

## Understanding the Command-Line Interface

| |

## Understanding Regular Expressions

| 6680010!16 | 0400015 |  |  | 065000000 |
|---|---|---|---|---|
| 3 뒤 160150# <2000-2030> 38 퀴 160156# | 6166 6166 | 56 표 ㅁ ㄴ 56 | 13132100 6 트 6 76285 13132100 | 121621859 0416 60060 8784101601[8 107 0416 768 ㄷ |
| 3 퀴 16056# 5\101# | 61066 | 56 | 13132100 | 뜨 26669 416 00260 57018 1070416 0100 56[( 60020201840. |

## Understanding Regular Expressions

The Cisco NX-OS software supports regular expressions for searching and filtering in CLI output, such as the show commands. Regular expressions are case sensitive and allow for complex matching requirements.

## Special Characters

You can also use other keyboard characters (such as ! or ~) as single-character patterns, but certain keyboard characters have special meanings when used in regular expressions.

This table lists the keyboard characters that have special meanings.

Table10:SpecialCharacterswithSpecialMeaning

|  | 16600168 80 910 은 16 이 1808 이 66, 10014010 을 \11116 50866. |
|---|---|
|  | 16600168 0 0720076 560460065 01 0416 08062. |
| + | 1660166 1 07720076 560460065 01 0416 08062. |
| ? | 16600168 0 071 00041060065 01016 08062. |
| ^ $ | 16601168 016 668107010 을 01 016 50008. 1860168 0416 600 01 016 |
| - (04006760076) | 60008. 16600166 8 00200008 (,), 161 60806 ({), 프 이 60406 (} ), 161 20000016615 ( ( ), 2 ㅁ 8111 08760 016916 |
| |( ) ), 446 668100108 01 016 60408, 016 600 01 016 50708. 07 8 50806. 이 016 |
| 711614006790076 16 0017 ㅁ ㅠ 68160 85 8 7084187 6%07069100 107 8(3[-7618160 00000218008 |

To use these special characters as single-character patterns, remove the special meaning by preceding each character with a backslash (\). This example contains single-character patterns that match a dollar sign ($), an underscore (_), and a plus sign (+), respectively:

- \$ \_ \+

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

ㅠㅠ

88

ㅣ

|!

## Understanding the Command-Line Interface

## Multiple-Character Patterns

## Multiple-Character Patterns

You can also specify a pattern that contains multiple characters by joining letters, digits, or keyboard characters that do not have special meanings. For example, a4% is a multiple-character regular expression.

With multiple-character patterns, the order is important. The regular expression a4% matches the character a followed by a 4 followed by a percent sign (%). If the string does not have a4%, in that order, pattern matching fails. The multiple-character regular expression a. (the character a followed by a period) uses the special meaning of the period character to match the letter a followed by any single character. With this example, the strings ab, a!, or a2 are all valid matches for the regular expression.

You can remove the special meaning of a special character by inserting a backslash before it. For example, when the expression a\. is used in the command syntax, only the string a. will be matched.

## Anchoring

You can match a regular expression pattern against the beginning or the end of the string by anchoring these regular expressions to a portion of the string using the special characters.

This table lists the special characters that you can use for anchoring.

Table11:SpecialCharactersUsedforAnchoring

| 다 1808 더 다 | 066000000 |
|---|---|
| ^ | 166010168 016 66810010 을 01 0416 50018. |
|  | 18601166 016 600 01 016 9001 음 . |

For example, the regular expression ^con matches any string that starts with con, and sole$ matches any string that ends with sole.

<

- Note The ^ symbol can also be used to indicate the logical function "not" when used in a bracketed range. For example, the expression [^abcd] indicates a range that matches any single letter, as long as it is not a, b, c, or d.

## Searching and Filtering show Command Output

Often,theoutputfromshowcommandscanbelengthyandcumbersome.TheCiscoNX-OSsoftwareprovides the means to search and filter the output so that you can easily locate information. The searching and filtering options follow a pipe character (|) at the end of the show command. You can display the options using the CLI context-sensitive help facility:

```cisco-ios
switch# show running-config | ?
```

cut Print selected parts of lines. diff Show difference between current and previous invocation (creates temp files: remove them with 'diff-clean' command and don't use it on commands with big outputs, like 'show tech'!) egrep Egrep - print lines matching a pattern grep Grep - print lines matching a pattern head Display first lines

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

89

| |

## Understanding the Command-Line Interface

| |

## Filtering and Searching Keywords

human Output in human format last Display last lines less Filter for paging no-more Turn-off pagination for command output perl Use perl script to filter output section Show lines that include the pattern as well as the subsequent lines that are more indented than matching line sed Stream Editor sort Stream Sorter sscp Stream SCP (secure copy) tr Translate, squeeze, and/or delete characters uniq Discard all but one of successive identical lines vsh The shell that understands cli command wc Count words, lines, characters xml Output in xml format (according to .xsd definitions) begin Begin with the line that matches count Count number of lines end End with the line that matches exclude Exclude lines that match include Include lines that match

## Filtering and Searching Keywords

The Cisco NX-OS CLI provides a set of keywords that you can use with the show commands to search and filter the command output.

This table lists the keywords for filtering and searching the CLI output.

Table12:FilteringandSearchingKeywords

| (61\00010 51018× 10@010 57177778 초 200016: |  | 066000000 옴 타 5 01901857120 을 81 416 1146 04181 00068108 1416 1(6% 038 1081(01169 016 56870 50008. 1116 5687011 50108 16 0856 86091[16. |
|---|---|---|
| 5180\ 76 ㅋ 510 ㅁ | ㅁ 6910 ㅁ 82 ㄴ ㅁ 00\22 ㅋ 6 |
| 0101 |  |  | 1019018575 0416 0400667 01 11468 10 016 6000021800 04104. |
| 초 200016: |
| 3530 ~972712 ㅁ 09- ㅇ ㅇ 프 19 | ㅇ ㅇ 4 ㅁ 프 |
| 0046[-0 0007007000] {-0 | | | -<< | [| - 아 | 121601875 0017 280 01016 041041 11468. 004 680 0190185 80400667 01 65669 (-0), 0180006266 (-~70041 [-0 |
| 초 200016: 000700700] {-0 | -<| 그 | -9} ), 07 8 이 06 (1). 00 080 |
| 53830 호 116 ㄴ 656 ㄴ ㅇ | 46045 | | 0045 -5 1-10 | 히 90 496 016 -0 65\070 (0 061106 8 1610 061124166 00167 04480 016 1808 00118080 이 60 061341[. 1116 -5 665\010 9400069966 0416 0192018 01416 1446 0418[( 0068 20 0021810 066 0611020160 |
| 600 .5777778 |  |  | 101901855 811 12066 472 (0 0416 1861 0004176006 01 016 |
| 초 200016: 5681011 96041 을 . |
| 5380 2-<940010 ㅁ 09- ㅇ 02219 | ㅣ | 6700 10 ㅁ ㄴ ㄷ 6 ㄴ 【 ㄷ 206 |  |

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

90

ㅣ

|!

## Understanding the Command-Line Interface

## diff Utility

| (6100010 51018× | 066000000 1216018575 811 11468 04181 00 ㅁ 401 1001406 016 68101 9071 응 . 7116 66870 90708 16 0896 56051056. |
|---|---|
| 60406 5777778 |  |  |  |
| 초 200016: |
| 85 ㅁ 80\ 17 ㅁ ㄴ 6 ㄴ 【『3206 15~ ㅁ 16 ㅣ ㅇ × ㅇ 1 ㅁ 06 0 ㅇ 0 디 ㅁ |
| 14680 [11069 72777651 |  |  |  | 1019018575 016 668100108 01 0446 041041 107 0416 ㅁ 4006062 |
| 초 200016: |  |  |  | 이 11469 506011160. 1116 0613416(00400666 01 11468 16 10. |
| 5180\ 109910 ㅁ 09 1095*116 | 1 | ㅁ 620 | 11065 | 50 |  |
| 100020 |  |  |  | 1019018575 016 04004 10 ㅁ 070081 10028 11 704 1186 |
| 초 200016: 206\104917 566 0416 04104 10028 10 11. 46108 016 101001021 04046 3041 600001800. |
| 8560 76251 ㅇ ㅁ ㅣ 20022 |
| 10 이 406 5777778 |  |  |  | 121901855 811 1120466 0181 1001406 016 5687011 60748. 1116 95681011 9041 응 15 6896 560816016. |
| 5160 170 ㅁ ㄴ 6 ㄴ 2206 5216 조 | ㅇ | 100 11006 | 102 |  |
| 1256 [72765] |  |  |  | 1019018575 016 600 01 416 04041 10746 0 ㅁ 40006 01 11068 |
| 초 200016: 5180\ | 126 | 50 |  | 906011160. 1116 06341 ㅁ 4101667 01 11468 16 10. |
| 109910 ㅁ 09 1096116 프 0-00016@ |  |  |  | 1019018575 811 416 041041\101041[66000108 86046 600 01 |
| 초 200016: 5160 17 ㅁ ㄴ ㄷ 6 ㄴ 206 155216 조 | ㅁ ㅇ - 패 0 ㄴ | ㅠ ㅎ |  | 46 9070060 \101 016 --146 ㅁ 6 ㅇ 6-- 0000006 ㄴ |
| 590] .5.577-0077770077077-7707770 초 200016: 560\ 776 ㅋ 510 ㅁ | 55058 5160 576 ㅋ 51 ㅇ ㅁ ㅇ ㅁ \ ㄴ 24 | 900 ㅁ ㅁ 6 ㅇ ㄴ | 77700207770 ㄷ 1 ㅇ | ㅁ | 복 60126069 0416 04124 46108 510681010 응 560416 00172? (5902) (0 8080060 881 00006010107. 04 080 07086 0446 58 80060 600060101020 4610 0416 5504 ㅁ 8104@ 0601000800. |
| \ ㅇ 6 [05665 | 4065 | \0005] 초 200016: 580 ,116 ㄴ 65 ㄴ ㅇ 46046 ㅣ 21 | \ ㅇ | 57568 |  | 1219018576 00409 01 01187801666, 14466, 07 \01708. 1116 061341[ 19 (0 0160185 0446 ㅁ 41021667 01 11068. \0208, 800 이 180806669. 1019018575 016 04041 10 5011. 10008. |
| 초 200016: |  |
| 350 765516 ㅇ ㅁ | 2001 |  |  |  |

## diff Utility

You can compare the output from a show command with the output from the previous invocation of that command.

diff-clean [all-sessions] [all-users]

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

91

때

## Understanding the Command-Line Interface

| |

## grep and egrep Utilities

This table describes the keywords for the diff utility.

| 211-66951005 | 복 6000 ㅋ 65 011 (6000078177 11169 12000 811 56961009 (0851 200 0066606(96691005) 01 016 041060[ 456. |
|---|---|
| 211-05669 | 복 6000 ㅋ 65 011 (6000078177 11169 12000 811 56961009 (0851 300 0065606[966610705) 01 311 48618. |

The Cisco NX-OS software creates temporary files for the most current output for a show command for all current and previous users sessions. You can remove these temporary files using the diff-clean command.

## diff-clean [all-sessions | all-users]

By default, the diff-clean command removes the temporary files for the current user's active session. The all-sessions keyword removes temporary files for all past and present sessions for the current user. The all-users keyword removes temporary files for all past and present sessions for the all users.

## grep and egrep Utilities

You can use the Global Regular Expression Print (grep) and Extended grep (egrep) command-line utilities to filter the show command output.

The grep and egrep syntax is as follows:

{grep | egrep} [count] [ignore-case] [invert-match] [line-exp] [line-number] [next lines] [prev lines] [word-exp] expression}]

This table lists the grep and egrep parameters.

Table13:grepandegrepParameters

| 0101 | 10192018575 0017 016 (0601 00401 01 208(01160 11468. |
|---|---|
| 180016-085@ | 옵 06011169 10 180076 016 6856 0111606006@ 10 20081(01160 11068. |
| 1056@06-028601 | 1019018575 11066 04181 00 ㅁ 006 20801 016 6%07655107. |
| 1106-650 | 1019218575 0017 11468 0186 20081011 8 0010020166(6 11406. |
| 11066- ㅁ 0402006 ㅠ | 옵 06011169 10 0192018 0416 1146 ㅁ 41000667 661076 68011 208(0160 1146. |
| 26 777765 | 옵 06011169 416 ㅁ 402667 01 11068 10 0182187 81666 8 018101160 11046. 1116 0613141616 0. 1116 78086 18 18000 1 (0 999. |
| 216? 727765 | 옵 06011169 0416 0 ㅁ 401067 01 11465 (0 0192018 66076 8 008101160 1106. 1116 001341(16 0. 1116 78086 1 18000 1 (0 999. |
| \000-650 | 1019218575 02017 11468 0181 20801 8 0020001666 \070. |
| 0002765597077 | 오 06011169 8 7684181 6%076961070 107 56870110 응 416 041241. |

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

92

ㅣ

|!

## Understanding the Command-Line Interface

## less Utility

## less Utility

You can use the less utility to display the contents of the show command output one screen at a time. You can enter less commands at the : prompt. To display all less commands you can use, enter h at the : prompt.

## Mini AWK Utility

AWK is a simple but powerful utility to summarize text output. You can use this utility after a pipe (|) to further process the text output of a command. Cisco NX-OS supports a mini AWK, which takes an inline program as an argument.

This example shows how the mini AWK utility can be used to summarize the text output of the show ip route summary vrf all command:

```cisco-ios
switch# show ip route summary vrf all | grep "Total number of routes" Total number of routes: 3 Total number of routes: 10
switch# show ip route summary vrf all | grep "Total number of routes" | awk '{ x = x + $5} END { print x }'
```

13

## sed Utility

You can use the Stream Editor (sed) utility to filter and manipulate the show command output as follows:

sed command

The command argument contains sed utility commands.

## sort Utility

You can use the sort utility to filter show command output.

The sort utility syntax is as follows:

sort [-M] [-b] [-d] [-f] [-g] [-i] [-k field-number[.char-position][ordering]] [-n] [-r] [-t delimiter] [-u]

This table describes the sort utiliity parameters.

## Table14:sortUtilityParameters

| 『8『80166 | 066000000 |
|---|---|
| -1 | 옴 0066 6 20070. |
| -0 | 18007661680108 01806 (60806 이 181806676). 1116 06341 50 10014066 0416 168010 을 61820166. |
| -0 | 옴 0069 6 0010008008 02017 01606 800 81201180412606 이 180806669. 1116 06341 602 104014068 811 이 180801668. |
| + | 0109 10\6606896 01181780[679 10160 400670896 01180280[678 |
|  | 옥 0069 6 000008008 8 8606681 ㅁ 4104606 ? ㅋ 8146. |

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

93

때

## Understanding the Command-Line Interface

| |

## Searching and Filtering from the --More-- Prompt

| 그 | 옴 0066 02017 4510 을 20018616 이 18086 이 666. 1116 061341[ 502 104014068 ㅁ 014000[8616 이 18280(6678. |
|---|---|
| 6 770/0-72707206/1.00707-20577071][070607279] | 옴 005 80007010 용 10 8665 8146. 111676 16 00 0613411166 두 78106. |
|  | 옴 0065 80007010 응 10 8.4400461016 9011 을 8146. |
| < | 복 6760666 00067 01 016 502 769416. 1116 061341[ 602 04104 16 10 860600108 00067. |
| -[ 06/2777767" | 옴 026914910 응 8 506011160 06110411(60. 1116 06[3416(0611211162 19 0416 50806 0118080016 ㄷ |
|  | 복 6000769 047011086(6 14466 17010 0416 6027 66416. 1116 502 04104 0162018575 016 00721108[6 11068. |

## Searching and Filtering from the --More-- Prompt

You can search and filter output from --More–- prompts in the show command output.

This table describes the --More–- prompt commands.

Table15:--More--PromptCommands

| [/2765]<60806> | 1016218579 04604 11468 107 010167 416 606011160 0 ㅁ 40066 01 11068 07 0416 04176 507601 9126. |
|---|---|
| 1/076912 | 1016218579 04604 11468 107 010167 416 606011160 0 ㅁ 40066 01 11068 07 0416 04176 507601 9126. 1 704 466 016 77776$ 8784100606, 0186[?8146 66000068 0416 ㅁ 6\ 061341[ 602000 9126. |
| [/2765]< ㅠ 60400> | 1021621856 04104 11066 107 010167 0416 606011160 ㅁ 4100061 01 11068 07 0416 041700[ 0613411 7404667 01 11468. 1116 01481 061341616 1 1166. 11 704 466 0416 000 ㅁ 0081 77769 87840060Ｌ. 1468[ ㅋ 8104666000068 016706\ 061341[70 ㅁ 40166 01 11468 (0 016018 107 0116 6010004810., |
| 1/27659]10 0 ㅠ [/076 위 (00+69111 나 ㅁ | 옥 60119 41704 인 1 04104 11468 107 61016『 0416 606011160 ㅁ 4101667 01 11466 07 0416 04161 061341[0400667 01 11468. 1116 1010481 061341[16 11 11468. 11 704 486 0416 07 ㅁ 0781 /77765 @08404606, 418[ ㅋ 81046 660020066 0416 0 ㅁ 6\ 06[34160 ㅁ 40166 01 11466 10 0190185 107 0115 0600004800. |
| 94000 62 00- | 319 016 --14626-- 2000006 |
| [/276515 | 우 106 102\7810 10 016 041041 107 010167 0416 606011160 ㅁ 4121667 01 11066 07 016 04706 061341(00400666 01 11468 800 01690185785 8 507660 01 11068. 1116 0613411[ 16 1 1106. |

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

94

ㅣ

|!

## Understanding the Command-Line Interface

## Using the Command History

| [70769 | 오 106 107\0810 10 0416 04104 107 01416 416 506011160 ㅁ 4102667 01 5076609 07 016 0410606[ 0613416(0401667 01 6006605 800 016018575 8 507060 01 11468. 1116 061341[ 18 1 80660. |
|---|---|
|  | 1216218579 0416 04061 1146 2 ㅁ 41206. |
| [001077]/60276557077 | 오 106 (0 016 1146 04181 208601169 416 7684187 6%1076561070 800 01901875 8 507660 01 046004111068. 086 016 0000081 007077 878404606( 10 56801 107 11068 \101 204101216 000410060068 01 0416 6×%07655107. 11116 0002101800 56(9 016 041700[ 76814181 6×%[07095100 14681 704 080 486 10 00167 0000028408. |
| [00102 | 오 106 (0 0416 06 11046 016[(248101166 016 04107606[7684187 6%1076561070 800 0190185785 8 500660 01 04104 11468. 066 016 02000081 00077 878400606[ 10 91012 2861 218101168. |
| 섬 | 딕 [59/76//-00770] } | 60469 016 600002800 9[06011160 10 016 5/76/7-0770 3784100006[10 8 541651611. |
|  | 복 606866 016 276\1048 600001840. |

## Using the Command History

The Cisco NX-OS software CLI allows you to access the command history for the current user session. You can recall and reissue commands, with or without modification. You can also clear the command history.

## Recalling a Command

You can recall a command in the command history to optionally modify and enter again.

This example shows how to recall a command and reenter it:

```cisco-ios
switch(config)# show cli history
```

0 11:04:07 configure terminal 1 11:04:28 show interface ethernet 2/24 2 11:04:39 interface ethernet 2/24 3 11:05:13 no shutdown 4 11:05:19 exit 5 11:05:25 show cli history switch(config)# !1 switch(config)# show interface ethernet 2/24

You can also use the Ctrl-P and Ctrl-N keystroke shortcuts to recall commands.

## Controlling CLI History Recall

You can control the commands that you recall from the CLI history using the Ctrl-P and Ctrl-N keystroke shortcuts.CiscoNX-OSsoftwarerecallsallcommandsfromthecurrentcommandmodeandhighercommand modes. For example, if you are working in global configuration mode, the command recall keystroke shortcuts recall both EXEC mode and global configuration mode commands.

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

95

| |

## Understanding the Command-Line Interface

| |

## Configuring the CLI Edit Mode

## Configuring the CLI Edit Mode

You can recall commands from the CLI history using the Ctrl-P and Ctrl-N keystroke shortcuts and edit them before reissuing them. The default edit mode is emacs. You can change the edit mode to vi.

## SUMMARY STEPS

- [no] terminal edit-mode vi [persist]

## DETAILED STEPS

Procedure

|  | 0726000 | 『00 ㅁ 056 |
|---|---|---|

Step 1

## Displaying the Command History

You can display the command history using the show cli history command.

The show cli history command has the following syntax:

show cli history [lines] [config-mode | exec-mode | this-mode-only] [unformatted]

By default, the number of lines displayed is 12 and the output includes the command number and timestamp.

This example shows how to display the default number of lines of the command history:

```cisco-ios
switch# show cli history
```

This example shows how to display 20 lines of the command history:

```cisco-ios
switch# show cli history 20
```

This example shows how to display only the configuration commands in the command history:

- One of the parametersavailablefor the show cli history config-mode command is Number of lines to display (from end). The line number here is dependent on the show cli list line numbers (from end) and not on show cli history config-mode output line number. This parameter is mainly intended to be used with the show cli history command.

> **NOTE**
> Note

```cisco-ios
switch(config)# show cli history config-mode
```

This example shows how to display only the EXEC commands in the command history:

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

96

ㅣ

|!

## Understanding the Command-Line Interface

## Enabling or Disabling the CLI Confirmation Prompts

```cisco-ios
switch(config)# show cli history exec-mode
```

This example shows how to display only the commands in the command history for the current command mode:

```cisco-ios
switch(config-if)# show cli history this-mode-only
```

Thisexampleshowshowtodisplayonlythecommandsinthecommandhistorywithoutthecommandnumber and timestamp:

```cisco-ios
switch(config)# show cli history unformatted
```

## Enabling or Disabling the CLI Confirmation Prompts

For many features, the Cisco NX-OS software displays prompts on the CLI that ask for confirmation before continuing. You can enable or disable these prompts. The default is enabled.

## SUMMARY STEPS

1.

[no] terminal dont-ask [persist]

## DETAILED STEPS

Procedure

|  | 0726000 | 『00 ㅁ 056 |
|---|---|---|
|  | (62010 ㅁ 21 00085 | 066 0416.40 10000 0 0416 60002104800 (0 6086016 0416 (011 0600110208000 2000006. |

## Setting CLI Display Colors

You can change the CLI colors to display as follows:

- • The prompt displays in green if the previous command succeeded.

- • The prompt displays in red of the previous command failed.

• The user input displays in blue.

- • The command output displays in the default color.

The default colors are sent by the terminal emulator software.

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

97

| |

## Understanding the Command-Line Interface

| |

## Sending Commands to Modules

## SUMMARY STEPS

## terminal color [evening] [persist]

## DETAILED STEPS

Procedure

|  | 0726000 | 『00 ㅁ 056 |
|---|---|---|
| 0160 1 | 0010 |[6760108] [0665150] | 옥 669 0416 (-1.1 016018 01076 107 0416 (60001081 5656107. 1116 @6014 용 65\000 16 54000060. 1116 066.5156( <65\020 |

Step 1

## Sending Commands to Modules

You can send commands directly to modules from the supervisor module session using the slot command.

The slot has the following syntax:

slot slot-number [quoted] command-string

By default, the keyword and arguments in the command-string argument are separated by a space. To send more than one command to a module, separate the commands with a space character, a semicolon character (;), and a space character.

The quoted keyword indicates that the command string begins and ends with double quotation marks ("). Use this keyword when you want to redirect the module command output to a filtering utility, such as diff, that is supported only on the supervisor module session.

This example shows how to display and filter module information:

## switch# slot 27 show version | grep lc

This example shows how to filter module information on the supervisor module session:

```cisco-ios
switch# slot 27 quoted "show version" | diff switch# slot 28 quoted "show version" | diff -c *** /volatile/vsh_diff_1_root_8430_slot__quoted_show_version.old 2013 --- - Wed Apr 29 20:10:41 2013 *************** *** 1,5 **** ! RAM 1036860 kB ! lc27 Software BIOS: version 6.20 system: version 6.1(2)I1(1) [build 6.1(2)] --- 1,5 ---- ! RAM 516692 kB ! lc28 Software BIOS: version 6.20 system: version 6.1(2)I1(1) [build 6.1(2)]
```

Wed Apr 29 20:10:41

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

98

ㅣ

## Understanding the Command-Line Interface

## Sending Command Output in Email

*************** *** 12,16 **** Hardware bootflash: 0 blocks (block size 512b) ! uptime is 0 days 1 hours 45 minute(s) 34 second(s) --- 12,16 ---- Hardware bootflash: 0 blocks (block size 512b) ! uptime is 0 days 1 hours 45 minute(s) 42 second(s)

## Sending Command Output in Email

You can use the CLI to send the output of a show command to an email address using the pipe operator (|).

<

- Note

The email configuration remains persistent for all show command output until it is reconfigured.

When you upgrade from a release before Cisco NX-OS Release 9.3(3) to Cisco NX-OS Release 9.3(3) or later releases, email configuration will be missing. This is due to enabling DME functionality for this feature. To resolve this, you need to execute "no email" and reapply the entire email configuration.

## SUMMARY STEPS

1. configure terminal

2. email

3.

smtp-host ip-address smtp-port port

4.

vrf management

4. 0 2200880020006

5.

from email-address

6.

ㅠ

reply-to email-address

7. exit

8. exit

9. show email

10.

show-command | email subject subject email-address

## DETAILED STEPS

Procedure

|  | 600001800 0746000 | 『400056 |
|---|---|---|
| 51601 | <00108466 (60001021 608001016: 음 데 호 00# 002 ㅁ <19456 ㄴ 6501 ㅁ 021 을 뒤 프 01 (6020 노 16) 푸 | 01665 인 0681 0001184780020 24006. |

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

99

| |

## Understanding the Command-Line Interface

| |

## Sending Command Output in Email

|  | 600001800 0746000 | 『00 ㅁ 056 |
|---|---|---|
| 5160 2 | 00034 608001016: 으 다 1600 (60201210) # ㅎ 60211 으 듀 프 06 (060201,2190-6 ㅇ 60211) 퓨 | 26666 604811 00201184780 ㅁ 070 20006. |
| 5160 3 | 50460-005[777-0007695 50060- ㅁ 006 72077 608001016: 으 다 프 01 (00205,219- ㄱ 60211) 퓨 5260- ㅁ 605 1982.51 2100.71 30 ㅁ 60- ㅁ 05 25 | 306011166 016 55411 7 11061 10 43007695 800 016 55411 72 00 ㅁ 7204100660. |
| 5160 4 | 다 22002886021606 608001016: 을 듀 프 01 (060205,219-6 ㅇ 60211) 2 패 20 ㅁ 2060062 ㄴ | 요 06011166 8 짜 자: 107 016 60081] [ ㅠ 8 ㅁ 600166107. |
| 5160 5 | 0010 0077077-0007659 608001016: 을 데 프 020 (002 ㅁ 1,19- ㄱ 60211) ,60 ㅁ 4 200100107 ㅇ 00 ㅁ 02207 ㅇ ㅇ ㅁ | 306011165 0416 56006116 60081] 8007689. |
| 5160 6 | 16015-60 007707/-0007655 608001016: 81600 (002519- ㄱ 60211) 26617- ㄴ ㅇ 2001000000 ㅇ 00 ㅁ ㅁ 21 ㅁ 7, 00 | 306011166 0416 760101601'5 60081] 800176889. |
| 5160 7 | 6 608001016: 을 뒤 프 01 (20201,219 ㄱ 60211) 611 을 뒤 프 01 (6020 노 16) 푸 | 0119 60081 0020118478000 00006. |
| 5160 8 | 6 608001016: 으 뒤 프 06 (602052190) # 61 는 을 뭐 1 는 213 뷰 | 0169 인 0681 00201184780070 20006. |
| 5160 9 | 5060\ 00004 608001016: 8 뒤 11601# 8106 60211 | 1216218579 0416 60081 6001184780 ㅁ 070. |
| 5160 10 | 5/20-0077770770 | 60281 5410]001 572//07007 077077-0007655 608001016: 음 디 1 느 010# 810 10662『206 16216, ㅣ 60811 840760 ㄴ 38060-17 ㅁ ㄴ 6 ㄴ 2066 20010 ㅁ 01900 ㅇ 00 ㅁ 0207 ㅇ 0 ㅁ | 10669 01670106 0200080607(|) 10 56600 0416 04004 01016 5006011160 59940\ 6020001800 \101 8 5460160[ (0 80 60081 8007688. |

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

100

ㅣ

|!

## Understanding the Command-Line Interface

## BIOS Loader Prompt

## BIOS Loader Prompt

When the supervisor modules power up, a specialized BIOS image automatically loads and tries to locate a valid nx-os image for booting the system. If a valid nx-os image is not found, the following BIOS loader prompt displays:

```cisco-ios
loader>
```

For information on how to load the Cisco NX-OS software from the loader> prompt, see the Cisco Nexus 9000 Series NX-OS Troubleshooting Guide.

## Examples Using the CLI

This section includes examples of using the CLI.

## Using the System-Defined Timestamp Variable

This example uses $(TIMESTAMP) when redirecting show command output to a file:

```cisco-ios
switch# show running-config > rcfg.$(TIMESTAMP)
```

Preparing to copy....done switch# dir 12667 May 01 12:27:59 2013 rcfg.2013-05-01-12.27.59 Usage for bootflash://sup-local 8192 bytes used 20963328 bytes free 20971520 bytes total

## Using CLI Session Variables

You can reference a variable using the syntax $(variable-name).

This example shows how to reference a user-defined CLI session variable:

## switch# show interface $(testinterface)

Ethernet2/1 is down (Administratively down) Hardware is 10/100/1000 Ethernet, address is 0000.0000.0000 (bia 0019.076c.4dac) MTU 1500 bytes, BW 1000000 Kbit, DLY 10 usec, reliability 255/255, txload 1/255, rxload 1/255 Encapsulation ARPA auto-duplex, auto-speed Beacon is turned off Auto-Negotiation is turned on Input flow-control is off, output flow-control is off Auto-mdix is turned on Switchport monitor is off Last clearing of "show interface" counters never 5 minute input rate 0 bytes/sec, 0 packets/sec 5 minute output rate 0 bytes/sec, 0 packets/sec L3 in Switched:

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

101

| |

## Understanding the Command-Line Interface

| |

## Defining Command Aliases

ucast: 0 pkts, 0 bytes - mcast: 0 pkts, 0 bytes L3 out Switched: ucast: 0 pkts, 0 bytes - mcast: 0 pkts, 0 bytes Rx 0 input packets 0 unicast packets 0 multicast packets 0 broadcast packets 0 jumbo packets 0 storm suppression packets 0 bytes Tx 0 output packets 0 multicast packets 0 broadcast packets 0 jumbo packets 0 bytes 0 input error 0 short frame 0 watchdog 0 no buffer 0 runt 0 CRC 0 ecc 0 overrun 0 underrun 0 ignored 0 bad etype drop 0 bad proto drop 0 if down drop 0 input with dribble 0 input discard 0 output error 0 collision 0 deferred 0 late collision 0 lost carrier 0 no carrier 0 babble 0 Rx pause 0 Tx pause 0 reset

## Defining Command Aliases

This example shows how to define command aliases:

cli alias name ethint interface ethernet cli alias name shintbr show interface brief cli alias name shintupbr shintbr | include up | include ethernet

This example shows how to use a command alias:

```cisco-ios
switch# configure terminal switch(config)# ethint 2/3 switch(config-if)#
```

## Running a Command Script

This example displays the CLI commands specified in the script file:

```cisco-ios
switch# show file testfile configure terminal interface ethernet 2/1 no shutdown end show interface ethernet 2/1
```

This example displays the run-script command execution output:

```cisco-ios
switch# run-script testfile `configure terminal` `interface ethernet 2/1` `no shutdown` `end` `show interface ethernet 2/1 ` Ethernet2/1 is down (Link not connected)
```

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

102

ㅣ

|!

## Understanding the Command-Line Interface

## Sending Command Output in Email

Hardware is 10/100/1000 Ethernet, address is 0019.076c.4dac (bia 0019.076c.4dac) MTU 1500 bytes, BW 1000000 Kbit, DLY 10 usec, reliability 255/255, txload 1/255, rxload 1/255 Encapsulation ARPA Port mode is trunk auto-duplex, auto-speed Beacon is turned off Auto-Negotiation is turned on Input flow-control is off, output flow-control is off Auto-mdix is turned on Switchport monitor is off Last clearing of "show interface" counters 1d26.2uh 5 minute input rate 0 bytes/sec, 0 packets/sec 5 minute output rate 0 bytes/sec, 0 packets/sec Rx 0 input packets 0 unicast packets 0 multicast packets 0 broadcast packets 0 jumbo packets 0 storm suppression packets 0 bytes Tx 0 output packets 0 multicast packets 0 broadcast packets 0 jumbo packets 0 bytes 0 input error 0 short frame 0 watchdog 0 no buffer 0 runt 0 CRC 0 ecc 0 overrun 0 underrun 0 ignored 0 bad etype drop 0 bad proto drop 0 if down drop 0 input with dribble 0 input discard 0 output error 0 collision 0 deferred 0 late collision 0 lost carrier 0 no carrier 0 babble 0 Rx pause 0 Tx pause 0 reset

## Sending Command Output in Email

This example shows how to send the output of the show interface brief command to an email address using

the pipe operator (|):

switch<config># email switch(config-email)# smtp-host 198.51.100.1 smtp-port 25 switch(config-email)# vrf management switch(config-email)# from admin@Mycompany.com switch(config-email)# reply-to admin@Mycompany.com switch(config-email)# exit switch(config)# exit switch# show email SMTP host: 198.51.100.1 SMTP port: 25 Reply to: admin@Mycompany.com From: admin@Mycompany.com VRF: management switch# show interface brief | email subject show-interface admin@Mycompany.com

Email sent

Theemailsenttoadmin@Mycompany.comwiththesubject"show-interface"showstheoutputofthecommand:

<snip>

---------------------------------------------------------------------

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

103

| |

| |

## Understanding the Command-Line Interface

## Sending Command Output in Email

| 뷰 튼 16206 10 ㄴ 6 ㅁ ㅁ 206 | 924 | 또 706 | 4606 | 3 ㄴ 62 ㄴ ㅁ ㅁ 8 |  | 8625807 ㅁ |  |  | 86660 | 2021 |
|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  | 08 |
| 교 타 21/1 | -- | 66 | 0 60200 |  | ㅁ 010 ㅁ | ㅎㅇ |  |  | 106 (2) | =- |
| 교 타 1/2 | -- | 6 타 0 | 204660 | 02 00\2 ㅁ | 410 | ㅁ | 0 ㄴ | 002 ㅁ 0060 ㄴ 60 | 23 ㅎ 460 (02) | =- |
| 고 타 21273 | -- | 6 타 0 | 204660 |  | ㅁ 010 ㅁ | ㅎㅇ |  |  | 106 (2) | =- |
|  | -- |  |  | 02 |  |  |  |  |  | =- |
| 교 타 21/4 |  | 6 타 0 | 204660 | 00\2 ㅁ | 410 | ㅁ | 0 ㄴ | 002 ㅁ 0060 ㄴ 60 | 28460 (2) |  |
| 교 탄 212/75 | -- | 6 타 0 | 204660 | 00\2 ㅁ | 410 | ㅁ | 0 ㄴ | 002 ㅁ 0060 ㄴ 60 | 28460 (2) | =- |
| 고 타 212/76 | -- | 6 타 0 | 204660 | 00\2 ㅁ | 410 | ㅁ | 0 ㄴ | 002 ㅁ 0060 ㄴ 60 | 28460 (2) | =- |
| 교 탄 21/7 | -- | 6 타 0 | 204660 | 00\2 ㅁ | 410 | ㅁ | 0 ㄴ | 002 ㅁ 0060 ㄴ 60 | 28460 (2) | =- |
| 교 타 1/8 | -- | 6 타 0 | 204660 | 00\2 ㅁ | 410 | ㅁ | 0 ㄴ | 002 ㅁ 0060 ㄴ 60 | 28460 (2) | =- |
| 교 탄 21/9 | -- | 6 타 0 | 204660 | 00\2 ㅁ | 410 | ㅁ | 0 ㄴ | 002 ㅁ 0060 ㄴ 60 | 28460 (2) | =- |
| 워 타 21710 | -- | 665 0 | 20466 | 00 ㅁ | 110 | ㅁ | 0\ ㄴ | 000060 ㄴ 60 | 2 ㅎ ㅁㄴㅇ ( |  |

<snip>

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

104

ㅣ

7

C H A P T E R 7

## Configuring Terminal Settings and Sessions

This chapter contains these sections:

- • About Terminal Settings and Sessions, on page 105

- • Default Settings for File System Parameters, on page 106

- • Configuring the Console Port, on page 106

- • Configuring Virtual Terminals, on page 108

- • Clearing Terminal Sessions, on page 110

- • Displaying Terminal and Session Information, on page 110

## About Terminal Settings and Sessions

This section includes information about terminal settings and sessions.

## Terminal Session Settings

The Cisco NX-OS software features allow you to manage the following characteristics of terminals:

## Terminal type

Name used by Telnet when communicating with remote hosts

Length

Number of lines of command output displayed before pausing

## Width

Number of characters displayed before wrapping the line

Inactive session timeout

Number of minutes that a session remains inactive before the device terminates it

## Console Port

The console port is an asynchronous serial port that allows you to connect to the device for initial configuration through a standard RS-232 port with an RJ-45 connector. Any device connected to this port must be capable of asynchronous transmission. You can configure the following parameters for the console port:

## Data bits

Specifies the number of bits in an 8-bit byte that is used for data.

Inactive session timeout

Specifies the number of minutes a session can be inactive before it is terminated.

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

105

## Configuring Terminal Settings and Sessions

| |

## Virtual Terminals

## Parity

Specifies the odd or even parity for error detection.

Speed

Specifies the transmission speed for the connection.

## Stop bits

Specifies the stop bits for an asynchronous line.

Configure your terminal emulator with 9600 baud, 8 data bits, 1 stop bit, and no parity.

## Virtual Terminals

You can use virtual terminal lines to connect to your device. Secure Shell (SSH) and Telnet create virtual terminal sessions. You can configure an inactive session timeout and a maximum sessions limit for virtual terminals.

## Default Settings for File System Parameters

This table lists the default settings for the file system parameters.

Table16:DefaultFileSystemSettings

| 『8『801616[5 | 06841 |
|---|---|
| 1061341[1116876[600 | | 6000018911: |

## Configuring the Console Port

You can set the following characteristics for the console port:

- • Data bits

- • Inactive session timeout

- • Parity

• Speed

- • Stop bits

## Before you begin

Log in to the console port.

## SUMMARY STEPS

1.

- configure terminal

2.

line console

이온 08

- 1106 0070501@

3. databits bits

4.

exec-timeout minutes

5.

parity {even | none | odd}

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

106

ㅣ

|!

## Configuring Terminal Settings and Sessions

## Configuring the Console Port

- speed {300 | 1200 | 2400 | 4800 | 9600 | 38400 | 57600 | 115200}

7. stopbits {1 | 2}

8. exit

0

9. (Optional) show line console

- (Optional) copy running-config startup-config

## DETAILED STEPS

Procedure

|  | 600001800 0746000 | 『400056 |
|---|---|---|
| 51601 | <00108466 (60001021 608001016: 음 데 호 00# 002 ㅁ <19456 ㄴ 6501 ㅁ 021 을 뒤 프 01 (6020 노 16) 푸 | 01665 인 0681 0001184780020 24006. |
| 5660 2 | 1106 0005016 608001016: 8 듀 1600 1106 0 ㅇ 00 ㅁ 5016 81010 (0020119-0 ㅇ 0 ㅁ 5016) 퓨 | 06669 0005016 0001184178000 00006. |
| 5160 3 | 026210165 70275 608001016: 81010 (00205,219-000 ㅁ 5016) 02 ㄴ 21016 7 | 20011841768 0446 0 ㅁ 4401667 01 0818 0115 266 6516. 1116 78086 18 10000 5 10 8. 1116 061841616 8. |
| 5160 4 | @66-010060146 7727722/769 터 3 머 끼 8: 미하 81010 (00205219-000 ㅁ 58016) 6×60- ㄴ 10 ㅁ 6014 30 | 2001184768 016 010604[ 107 80 10801146 5689107. 1116 70086 16 00000 0 (0 525600 220104166 (8760 10478). 스 81046 01 0 720104666 0168160168 0416 5666100 0046041. 1116 061841616 30 10104168. |
| 5160 5 | 28060 {16660 | ㅁ 2000| 000} 608001016: 으 데프 (0020119- ㅇ 0 ㅁ 5016) 유 0219 69762 | 2001184768 016 08206. 1116 061341616 ㅁ 006@. |
| 5160 6 | 50600 {1300 |1200|2400|4800|9600|38400|57600| ㅣ | 115200} 608001016: 81010 (0001109-000 ㅁ 5016) 50660 115200 | |(0001084768 0446 0 ㅁ 80600 800 7606176 60660. 1116 061341[ 18 9600. |
| 5160 7 | 56000166 {11 | 2} 608001016: 81010 (00205, ㅋ 19-000 ㅁ 5016) 8 ㄴ 0001656 그 | 20011841708 016 6602 016. 1116 0613411 16 1. |
| 5660 8 | 6 608001016: 요도 (00205,219-000 ㅁ 5016) 유 6811 | 119 0005016 000118478000 00006. |

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

107

| |

## Configuring Terminal Settings and Sessions

| |

## Configuring Virtual Terminals

| 5660 9 | (0000081) 940\ 1106 0005016@ 608001016: 으 뒤 프 01 (0020 네 190) 5106 1106 00 ㅁ 5016@ | 1216018579 0416 6005016 66101088. |
|---|---|---|
| 51660 10 | (06000081) 0005 2000108-00018 564060410-6070108 608001016: 8 바 1600 (6020 네 19) 00092 1204001 ㅁ 9- ㅇ 01 ㅁ 5190 8 ㄴ 2 ㄴ ㄴ ㅁ 060- ㅇ 02 ㅁ 21 의 | 200169 016 2000108 6001184780070 10 016 618002 000118478007. 너 |

## Configuring Virtual Terminals

This section describes how to configure virtual terminals on Cisco NX-OS devices.

## Configuring the Inactive Session Timeout

You can configure a timeout for inactive virtual terminal sessions on the device.

## SUMMARY STEPS

1. configure terminal

2. line vty

3. exec-timeout minutes

4. exit

5.

(Optional) show running-config all | begin vty

6.

(Optional) copy running-config startup-config

## DETAILED STEPS

Procedure

| 51601 | 000847@ 6(60001021 60801016: | 트 마 666 인 06861 00011841780070 20006. |
|---|---|---|
|  | 38 뒤 1601# ㅇ 002 ㅁ 5,19456 ㄴ 6501 ㅁ 21 으 1606 (6020 조 10) 부 |  |
| 5160 2 | 1106 뒤 두 60801016: 8 뒤 1 는 00# 01106 꼬 는 도 81606 (602 ㅁ 219-1106) 츄 | 트 마 666 1146 0020118478000 04006. |
| 5160 3 | @66-6010060141 77777770/65 60801016: 31600 (6020219- ㄱ 1106) 6860-\ | (2001184169 0416 10800176 5699100 11460141. 1116 78086 16 12020 010 525600 270104168 (8760 10478). 스 78146 01 0 20104166 01986169 016 010046041. 1116 061341[78106 16 30. |

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

108

ㅣ

|!

## Configuring Terminal Settings and Sessions

## Configuring the Session Limit

| 5160 4 | @[ |  | 표지 1146 0001184780070 20006. |
|---|---|---|---|
|  | 6801016: 81605 (6072219-1106) * 으 1606 (6020 조 10) 부 | 6※1 는 |  |
| 5160 5 | (0000081) 940\ 0007 ㅁ 6801016: 81606 (6072219) 6566 까 느 까 | 0108-607018 2411 | 66810 뒤 도 <2000109- ㅇ 02 ㅁ 5, ㅋ 19 211 | 15691 | 1219218575 016 10481 (60001081 60701184780 ㅁ 070. |
| 5160 6 | (0000081) 000 ㅁ 000108-607018 6801016: | 564060010-0 ㅇ 00108 | (200166 0416 210010 용 00011841780070 (0 016 618002 060011841800270. |
|  | 81600 (0072219) 00072 | 120001 ㅁ 9- ㅇ 01 ㅁ [ ㅋ 19 5 ㄴ 256 ㅁ 00- ㅇ 0252 1 의 |  |

## Configuring the Session Limit

You can limit the number of virtual terminal sessions on your device.

## SUMMARY STEPS

1. configure terminal

2. line vty

3. session-limit sessions

4. exit

5.

(Optional) show running-config all | begin vty

6.

(Optional) copy running-config startup-config

## DETAILED STEPS

Procedure

|  | 600001800 0726000 | 『00 ㅁ 056 |
|---|---|---|
| 51601 | 000841@ 6(60001021 6801016: 38 뒤 1601# ㅇ 002 ㅁ 5,19456 ㄴ 6501 ㅁ 21 으 1606 (6020 조 10) 부 | 트 마 666 인 06861 00011841780070 20006. |
| 5160 2 | 1106 뒤 두 6801016: 8 뒤 1 는 00# 01106 꼬 는 도 81606 (602 ㅁ 219-1106) 츄 | 트 마 666 1146 0020118478000 04006. |
| 5160 3 | 5@551040-11021[ 569670775 6801016: | (20201184168 016 008%1041410 0 ㅁ 41021667 01 10481 56691006 107 37047 060\166. 1116 70086 16 12000 1 (0 64. 1116 001341[16 32. |

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

109

| |

## Configuring Terminal Settings and Sessions

| |

## Clearing Terminal Sessions

|  | 31600 (6020219-1106)#* | 5658100- ㄱ 1101 10 |  |
|---|---|---|---|
| 51660 4 | @[ |  | 표지 1146 0001184780070 20006. |
| 60801016: 81605 (6072219-1106) * 으 1606 (6020 조 10) 부 | 6※1 는 |  |
| 5660 5 | (0000081) 940\ 0007 ㅁ 60801016: 81606 (6072219) 6566 까 느 까 | 0108-607018 2411 | 66810 뒤 도 <2000109- ㅇ 02 ㅁ 5, ㅋ 19 211 | 15691 | 1219218575 016 뉘 다 481 (60001081 00721184780 ㅁ 070. |
| 51660 6 | (0000081) 000 ㅁ 0070108-607018 60801016: 81600 (0072219) 00072 | 56406010-0 ㅇ 00108 120001 ㅁ 9- ㅇ 01 ㅁ [ ㅋ 19 5 ㄴ 256 ㅁ 00- ㅇ 0252 1 의 | (200166 0416 210010 용 00011841780070 (0 016 618002 060011841800270. |

Step 4

Step 5

Step 6

## Clearing Terminal Sessions

You can clear terminal sessions on your device.

## SUMMARY STEPS

- (Optional) show users

2. clear line name

## DETAILED STEPS

Procedure

|  | 600007800 0726000 |  | 『00 ㅁ 056 |
|---|---|---|---|
| 51601 | (0000081) 59040\ 60801016: 35\16010# 6108 | 45665 5626 | 1219218575 016 4667 56661008 07 016 06166. |
| 5660 2 | 이 680 1106 72070 60801016: 3\16056# 01628 | 1106 26870 | (16815 8 160001081 5695100 00 8 50601116 1446. 1116 1106 ㅁ 8106 19 6856 5606101576. |

## Displaying Terminal and Session Information

To display terminal and session information, perform one of the following tasks:

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

110

ㅣ

|!

## Configuring Terminal Settings and Sessions

## Displaying Terminal and Session Information

| 600001800 | 『 바 0056 |
|---|---|
| 9810\ 1(60001021 | 101901856 (60001081 66[[1088. |
| 980\ 1106 | 1019018575 016 (00411 300 0008016 0005 5660085. |
| 9410\ 45615 | 121901855 100481 (60001081 566910208. |
| 9410\ 7041070108-00018 [2411] | | 216218786 046 4860 8000401 600201184780070 10 016 20400108 600011841780070. 1116 411 노 65\070 0162018575 016 061341[ ㅋ 81068 107 0416 4567 80004069. |

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

111

| |

| |

## Displaying Terminal and Session Information

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

112

## Configuring Terminal Settings and Sessions

ㅣ

8

C H A P T E R 8

## Basic Device Management

This chapter contains these sections:

- • About Basic Device Management, on page 113

- • Default Settings for Basic Device Parameters, on page 114

- • Changing the Device Hostname, on page 114

- • Configuring the MOTD Banner, on page 115

- • Configuring the Time Zone, on page 117

- • Configuring Summer Time (Daylight Saving Time), on page 117

- • Manually Setting the Device Clock, on page 119

- • Setting the Clock Manager, on page 119

- • Managing Users, on page 120

- • Verifying the Device Configuration, on page 121

## About Basic Device Management

This section provides information about basic device management.

## Device Hostname

You can change the device hostname displayed in the command prompt from the default (switch) to another character string. When you give the device a unique hostname, you can easily identify the device from the command-line interface (CLI) prompt.

## Message-of-the-Day Banner

The message-of-the-day (MOTD) banner displays before the user login prompt on the device. This message can contain any information that you want to display for users of the device.

## Device Clock

If you do not synchronize your device with a valid outside timing mechanism, such as an NTP clock source, you can manually set the clock time when your device boots.

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

113

## Basic Device Management

| |

## Clock Manager

## Clock Manager

The Cisco NX-OS device might contain clocks of different types that might need to be synchronized. These clocks are a part of various components (such as the supervisor, line card processors, or line cards), and each might be using a different protocol.

The clock manager provides a way to synchronize these different clocks.

## Time Zone and Summer Time (Daylight Saving Time)

You can configure the time zone and summer time (daylight saving time) setting for your device. These values offset the clock time from Coordinated Universal Time (UTC). UTC is International Atomic Time (TAI) with leap seconds added periodically to compensate for the Earth's slowing rotation. UTC was formerly called Greenwich Mean Time (GMT).

## User Sessions

You can display the active user session on your device. You can also send messages to the user sessions. For more informationabout managinguser sessions and accounts,see the Cisco Nexus 9000 Series NX-OS Security Configuration Guide.

## Default Settings for Basic Device Parameters

This table lists the default settings for basic device parameters.

Table17:DefaultBasicDeviceParameters

| 『8『801616[5 | ㅁ 0618 비 |
|---|---|
| 10112 680067 16 | 0667 스 00689 \60111680020 |
| 21066 10206 2006 | 046 |

## Changing the Device Hostname

You can change the device hostname displayed in the command prompt from the default (switch) to another character string.

## SUMMARY STEPS

1. configure terminal

2. {hostname | switchname} name

3. exit

4.

(Optional) copy running-config startup-config

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

114

ㅣ

|!

## Basic Device Management

## Configuring the MOTD Banner

## DETAILED STEPS

Procedure

| 51601 | 000841@ 6(60001021 6801016: 38 뒤 1601# ㅇ 002 ㅁ 5,19456 ㄴ 6501 ㅁ 21 으 1606 (6020 조 10) 부 | 트 마 666 인 06861 00011841780070 20006. |
|---|---|---|
| 5160 2 | 10560200@ | 5\601020060} 77070 6801016: 10614 을 416 406608104@ 0002104800: 51608 (60019) ※ 1005 ㄴ ㅁ 806 180 ㅁ 910661 909106611091 (000519) 개 10910 을 0416 5\1[0104800@ 000001800: 피 0 ㅁ 91066 ㅋ 1091 (00725,10) 8 티 16000 ㅁ 206 209010 피 0 ㅁ 91066210 ㅁ 92 (00722,19) 퓨 | (1180866 016 06106 109078146. 1116 7707776 8784106106[ 15 히 21804006016 800 0896 5609106. 1116 06341 19 5\16011. 0066 , . 116 9\160008046 0002102800 06[01019 0416 58006 140011070 858 1446 460560081046 0010002800. 26810010 을 \101 (21900 피 %-08 표 인 6856 7.0(3)17(3), 3 2 ㅁ 8×100410 160801 01 63 이 1828 이 666 107 016 6\1008146 19 54000060. |
| 5160 3 | 6 6801016: 피 0 ㅁ 91066 ㅋ 1092 (00722,19) 뷰 6811 피 0 ㅁ 91066810 ㅁ 92 퓨 | 2069 인 0081 000118478000 00006. |
| 5160 4 | (0000081) 0005 『700701408-0070118 5640260010-6001 6801016: 피 0 ㅁ 91066 ㅋ 10 ㅁ 92# 6009 ~2400109- ㅇ 0219 | (200166 0416 210010 용 00011841780070 (0 016 618002 56000-0 5219 060011841800270. |

## Configuring the MOTD Banner

You can configure the MOTD to display before the login prompt on the terminal when a user logs in. The MOTD banner has the following characteristics:

- • Maximum of 255 characters per line

- • Maximum of 40 lines

## SUMMARY STEPS

1. configure terminal

2. banner motd delimiting-character message delimiting-character

3. exit

4.

(Optional) show banner motd

5.

(Optional) copy running-config startup-config

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

115

| |

## Basic Device Management

| |

## Configuring the MOTD Banner

## DETAILED STEPS

## Procedure

| 000847@ 6(60001021 60801016: 38 뒤 1601# ㅇ 002 ㅁ 5,19456 ㄴ 6501 ㅁ 21 으 1606 (6020 조 10) 부 | 트 마 666 인 06861 00011841780070 20006. |
|---|---|
| 162006@ 20060 076/777777779-0/7070076/'777659086 ㅇ 06/77277778-0007007607" | (2001184168 016 5407112) 68006. 100 ㅁ 01 486 016 06/707277778-00070076/' 02 06 77695086 165. |
| 60801016: 81600 (602 ㅁ 【<19)#* 152006 ㅋ 피 0 ㄴ 0 #\\610 ㅇ 006 ㄴㅇ 트 6 501 느 08 쥐 51608 (60019) | 티 06 120 006 0866 00 % 86 8 061100100 용 008080660 05416 0081 \1160 704 47081806 10 1181167 70168966 107 016 1101118000 01 14019 1680476. 미 06 268100108 17010 (61900 피 -05 61686 10.1(×), 016 10110\108 5060181 01808001629 (", %, >, <, ' ', (50806), 800 스 8(11 0180806666 ~ 015) 376 1078110 85 0 이 120100 음 이 1808 이 669. 1 80 63160248 54101 12 680067 \101 01666 461121104 을 01180006(606 16 60160 07 8 17691 080067 15 80060 \101 01656 061124104 을 이 18080(666, 0416 68006 16 201 0001184160 (0 016 20000108 00201184080027. \1160 704 4080606 17010 80 0801167 76168961.6, 661076 10. 16168566 (0 80 10. 01606 15 20 02 |
|  | 61502 76168566, 12008 1446 6001184178000 10 016 (:01.1 340 016 60701184780070 \)111 66 1446 68046 10 016 200010 용 00201184780 ㅁ 07. |
| 603 60801016: 을 (6020 조 16) # 681 느 8 뒤 103 | 트 30169 인 0081 000118478000 00006. |
| (0000081) 9440\ 00006 22010 60801016: 3160150# 6100 152006 ㄴ ㅇㅇ | 1219018575 016 0001184760 54101 12 68006 |
| (0000081) 0005 『0070108-0070118 5640260010-6001 을 60801016: | (200166 0416 210010 용 00011841780070 (0 016 618002 060011841800270. |

Step 1

Step 2

Step 3

Step 4

Step 5

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

116

ㅣ

|!

## Basic Device Management

## Configuring the Time Zone

## Configuring the Time Zone

You can configure the time zone to offset the device clock time from UTC.

## SUMMARY STEPS

1. configure terminal

2. clock timezone zone-name offset-hours offset-minutes

3. exit

4.

(Optional) show clock

5.

(Optional) copy running-config startup-config

## DETAILED STEPS

Procedure

|  | 600001800 0726000 |  |  | 『00 ㅁ 056 |
|---|---|---|---|---|
| 51601 | ㅇ 0008406 (60001021 6801016: 38 뒤 1601# ㅇ 002 ㅁ 5,19456 ㄴ 6501 ㅁ 21 으 1606 (6020 조 10) 부 |  |  | 트 마 666 인 06861 00011841780070 20006. |
| 5160 2 | 이 00 0006200@ 2=0770-7707776 07/7567-/70705 터 3 머 만: 미하 9\1600 (000519)* 0100 ㄴ 1062006 | 06 또 -5 | 0//567-7777770/65 0 | (2001184169 016 01006 2006. 1116 20770-7707776 878410001 16 8 3- 아 80006 90408 107 016 0006 2006 80000 (107 6800216, 2671 07 6917). 1116 07/7967-/707075 878401601 16 0416 01561 17020 1466 074'(@〉 300 016 18086 16 010 -23 10 23 10016. 1116 20086 107 016 077967-77777//69$ 878410060[ 19 17010 0 10 59 100104168. |
| 5160 3 | 603 6801016: 을 (6020 조 16) # 681 느 8 뒤 103 |  |  | 2069 인 0081 000118478000 00006. |
| 5160 4 | (0000081) 59040\ 000 6801016: 58 뒤 1601# 6100 ㅇ 16 ㅇ < |  |  | 1219218575 016 0106 800 1106 2006. |
| 5160 5 | (0000081) 0005 『700701408-0070118 6801016: 38 뒤 160150# 60209 12400109- ㅇ 012 ㅁ 619 | 5640260010-6001 ㄴ ~6000-002 | 을 ㅁ 519 | (200166 0416 210010 용 00011841780070 (0 016 618002 060011841800270. |

## Configuring Summer Time (Daylight Saving Time)

You can configure when summer time, or daylight saving time, is in effect for the device and the offset in minutes.

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

117

| |

## Basic Device Management

| |

## Configuring Summer Time (Daylight Saving Time)

## SUMMARY STEPS

1. configure terminal

2. clock summer-time zone-namestart-weekstart-daystart-monthstart-timeend-weekend-dayend-month end-time offset-minutes

3. exit

4.

(Optional) show clock detail

- (Optional) copy running-config startup-config

## DETAILED STEPS

## Procedure

|  | 600007800 0726000 | 『00 ㅁ 056 |
|---|---|---|
| 51660 1 | 000847@ 6(60001021 60801016: 38 뒤 1601# ㅇ 002 ㅁ 5,19456 ㄴ 6501 ㅁ 21 으 1606 (6020 조 10) 부 | 트 마 666 인 06861 00011841780070 20006. |
| 5160 2 5160 3 | 이 0065000046-61046 =0770-7707776 57077-766 57077-007 57077-77707777/2 57077-77770 07/70-1\71066 07070-0011 0070-7770777/ 00070 07907 00 때 ： | (20201184169 9414046 01006 07 0801 음 11 5814 음 4146. 뽀 ; ; 16 20776-7707770 878410001 19 8 01766 0118780167 5000 음 107 016 106 2006 800020520 (107 6800016, 251 4300 6577). |
| 60801016: ㅁ 591600 (0602219)* 010 ㅇ < 6140006<- ㄴ 06 ㅁ 0 모 그 80002 46200 02100 1 80002 36760062 02:00 60 | 위 16 81466 107 0416 57077-001" 800 6/20-001' 87841000[5 876 10005. 06502, \60065025. 11104190285. 60025. 58604608, 800 50002. |
|  | 116 81466 107 0416 57077-770777/7 300 07/20-770777/1 3724720016 306 440004877.0000277., 51401. 011. 5145. 4406. 4415. 스 08456, 5606(6020060. 006006@0,. 390760106. 400 196600010@0. |
|  | 7116 81046 107 016 51077-77776 800 07/70-77776 8784100065 87610 46 1000081 7/2/217270. |
|  | 71161808610710416 0/75607-77771065 878410000116 12021 0 10 1440 10104168. |
| 6 60801016: 을 (6020 조 16) # 681 느 8 뒤 103 | 2069 인 0081 000118478000 00006. |
| 5160 4 | (0000081) 59860\ 0006 06634 60801016: 81600 (6020210)# 81600 0100 06211 | 1219018575 016 0001184760 54101 12 68006 |
| 5660 5 | (0000081) 000 ㅁ 0070108-607018 56406010-0 ㅇ 00108 60801016: 38 뒤 160150# 60209 12400109- ㅇ 012 ㅁ 619 8 ㄴ 2 ㄴ ~6000-002 ㅁ 519 | (200166 0416 210010 용 00011841780070 (0 016 618002 060011841800270. |

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

118

ㅣ

|!

## Basic Device Management

## Manually Setting the Device Clock

## Manually Setting the Device Clock

You can set the clock manually if your device cannot access a remote time source.

## Before you begin

Configure the time zone.

## SUMMARY STEPS

1. clock set time day month year

2.

(Optional) show clock

## DETAILED STEPS

Procedure

|  | 600001800 | 『00 ㅁ 056 |
|---|---|---|
| 51601 | 이 00 566 | (2001184168 016 06\06 01006. |
| 606801016: | 7116 10008[ 107 016 77776 8784100601 15 /2/217277155. |
| 501600# 포 되 1 462 | 7116 18086 107 016 00) 4648400606 16 6000 1 10 31. 7116 ㅋ 81466 107 10167770777/72 878400601 876 48042757.460010215. 12100. 011. 5145. 4406.441?. 08456, 56066001066. 006006『, 제 0 ㅋ 60106. 400 10600000606. 7116 70086 107 10416 7700/' 8784100001 16 10000 2000 10 2030. |
| 5160 2 | (0000081) 6801016: 을 라 포 00 | 1219018575 016 04060 0100 ㅋ 8106. |

## Setting the Clock Manager

You can configure the clock manager to synchronize all the clocks of the components in the Cisco Nexus device.

## SUMMARY STEPS

1. clock protocol protocol

2.

(Optional) show run clock_manager

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

119

| |

## Basic Device Management

| |

## Managing Users

## DETAILED STEPS

Procedure

| 601 | 이 006000600601 | 727070007 | (2001184168 016 이 006 2080886 ㄷ . |
|---|---|---|---|
| 002 | (0000081) 60801016: 5\16010# | ㅁ 040 0006 2 ㅁ 802866 010 < | 1219201875 016 0001184086000 01 016 01006 28088. |

Step 1

Step 2

## Managing Users

You can display information about users logged into the device and send messages to those users.

## Displaying Information about the User Sessions

You can display information about the user session on the device.

## SUMMARY STEPS

1. show users

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

120

ㅣ

|!

## Basic Device Management

## Sending a Message to Users

## DETAILED STEPS

Procedure

|  | 0726000 | 『00 ㅁ 056 |
|---|---|---|
| 51601 | ㅁ ㄴ 5626 | 1219018575 016 4867 56661005. |

## Sending a Message to Users

You can send a message to active users currently using the device CLI.

## SUMMARY STEPS

1.

(Optional) show users

2. send [session line] message-text

## DETAILED STEPS

Procedure

| 51601 | (0000081) 5900\ 45666 6801016: 35\16010# 6108 ㅁ ㄴ 5626 | 1219018575 016 801146 4667 56961019. |
|---|---|---|
|  | 6801016: 53\1 ㄴ 010# 5600 861020100 + ㄴ 1 ㅁ 6 067106 15 10 | 7116006565886 080 06142 (0 80 310118904016016 01187801675 800 : 00 19 68956 560616156. |

## Verifying the Device Configuration

To verify the configuration, use one of the following commands:

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

121

| |

| |

## Basic Device Management

## Verifying the Device Configuration

| 600001800 | 『00056 |
|---|---|
|  | 808157519. 268100108 \101 (21600 페 -056 《616856 10.3(2), 54010200 165\010 18 540000060 070 (21900 페 6%348 9000 862166 5\1661168. |
| 9410\ 56420410-000108 | 1219018575 016 61800042 600118478007. 띠 066 18760 3 68660 1680176 00701184180005 876 01680160 10 016 20070108-007118. 016 540\ 5617600410-060011 용 600104800 00665 ㅁ 01 01920167 01622. 10\676, 0416 06001184000006 17601810 10080 10 0416 6680002 0255, 4001 016 60003 70070108 5630000 000001800 16 060000060. |
| 940\ 0046-562000 14070108-0 ㅇ 00118 1256-0020860 | 1219018575 016 11066[84022 \1160 016 0100108 0001184180 ㅁ 070 \88 1891 01180860. |

The following example shows sample output of show running-config command with the sanitized keyword. The sanitized configuration is used to share a configuration without exposing some configuration details.

This option masks the sensitive words in running configuration output with <removed> keyword.

```cisco-ios
switch# show running-config sanitized
```

!Command: show running-config sanitized !Running configuration last done at: Wed Oct 12 09:14:54 2022 !Time: Wed Oct 12 13:52:55 2022 version 10.3(2) Bios:version 07.69 username admin password 5 <removed> role network-admin copp profile strict snmp-server user admin network-admin auth md5 <removed> priv aes-128 <removed> localizedV2key rmon event 1 log trap <removed> description FATAL(1) owner PMON@FATAL rmon event 2 log trap <removed> description CRITICAL(2) owner PMON@CRITICAL rmon event 3 log trap <removed> description ERROR(3) owner PMON@ERROR rmon event 4 log trap <removed> description WARNING(4) owner PMON@WARNING rmon event 5 log trap <removed> description INFORMATION(5) owner PMON@INFO

version 10.3(2) Bios:version 07.69

username admin password 5 <removed> role network-admin

--More--

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

122

ㅣ

9

C H A P T E R 9

## Using the Device File Systems, Directories, and

Files

This chapter contains these sections:

- • About the Device File Systems, Directories, and Files, on page 123

- • Guidelines and Limitations, on page 125

- • Default Settings for File System Parameters, on page 125

- • Configuring the FTP, HTTP, or TFTP Source Interface, on page 125

- • Working with Directories, on page 126

- • Working with Files, on page 129

- • Working with Archive Files, on page 136

- • SSD Re-partitioning, on page 139

- • Enable or Disable Tech-Support Command, on page 141

- • Displaying Tech-support Blocked CLIs, on page 141

- • Examples of Using the File System, on page 142

## About the Device File Systems, Directories, and Files

This section describes file systems, directories, and files on the Cisco NX-OS device.

## File Systems

The syntax for specifying a local file system is filesystem:[//modules/].

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

123

| |

## Directories

## Directories

## Files

|

|

124

## Using the Device File Systems, Directories, and Files

This table describes file systems that you can reference on your device.

Table18:FileSystemSyntaxComponents

| 터 116 5156601 88076 | 0100416 | 066000000 |
|---|---|---|
| 1600108918 | 9410-801176 940-10081 | 10660081 (00200080 따 16911 21600075 10068160 00 0446 80106 5406071507 1000141614660 10『6600108 120886 1168, 060011846780070 11168, 800 0016 20166611806048 11168. 1116 1010481 0613411 017606077 16 60010891. |
| 9410-968001057 8410-『600016 | 10660081 (00200080 따 16911 21600075 10068160 00 046 56800165 54106071607 100041614660 107810008 120886 11168, 060011846780070 11168, 800 0016 20160611806048 11168. |
| ㅠ 018016 |  | 투 018016 70900010-800688 20610015 (51) 1008660 00 ㅁ 8 9406771507 1000416 4860 107 160200781750 0 ㅠ 7260010 을 01180868. |
| 108 |  | 1600017 020 016 8001176 5470617190 ㅠ 481 660766 108810 은 116 96608068. |
| 89660 |  | 1600077 020 8 54706001607 2100416 14960 107 66000 0416 70400108-000118478000 116. |
| 06604 음 |  | 1600077 020 8 54706001607 2100416 14960 107 06104 1085. |

You can create directories on bootflash: and external flash memory (usb1: and usb2:). You can navigate through these directories and use them for files.

You create and access files on bootflash:, volatile:, usb1:, and usb2: filesystems. You can only access files on the system: filesystem. You can use the log: filesystem for debug log files.

You can download files, such as the nx-os image file, from remote servers using FTP, Secure Copy (SCP), Secure Shell FTP (SFTP), and TFTP. You can also copy files from an external server to the device, because the device can act as an SCP server.

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

ㅣ

|!

## Using the Device File Systems, Directories, and Files

## Guidelines and Limitations

## Guidelines and Limitations

Guidelines and limitations for device file systems, directories, and files are as follows:

- • The show tech-support details command cannot be terminated using Ctrl+Z. Instead, use Ctrl+C to terminate the command.

- • Utilize a user with the "network-admin" role to make changes to files in the bootflash.

- • Starting with Release 10.5(1), you can automatically detect SSD partition size on the Nexus 9000 to match the expected configured size. An information syslog is seen during bootup in the show logging log or show logging nvram commands to indicate the NX-OS Nexus 9000 booted with an unexpected SSD partitioning size.

%PLATFORM-2-SSD_PARTITION_CHECK: Incorrect <device> partition size detected - please contact Cisco TAC for additional information

## Default Settings for File System Parameters

This table lists the default settings for the file system parameters.

Table19:DefaultFileSystemSettings

| 『8『801616[5 | 06841 |
|---|---|
| 1061341[1116876[600 | | 6000018911: |

## Configuring the FTP, HTTP, or TFTP Source Interface

You can configure the source interface for the File Transfer Protocol (FTP), Hypertext Transfer Protocol (HTTP),orTrivialFileTransferProtocol(TFTP).ThisconfigurationallowsyoutousetheIPaddressassociated with the configured source interface when copy packets are transferred.

## SUMMARY STEPS

1. configure terminal

- [no] ip {ftp | http | tftp} source-interface {ethernet slot/port | loopback number}

3.

(Optional) copy running-config startup-config

## DETAILED STEPS

Procedure

| 51601 | ㅇ 0008406 (60001021 | 트 마 666 인 06861 00011841780070 20006. |
|---|---|---|
| 6801016: |  |

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

125

| |

## Using the Device File Systems, Directories, and Files

| |

## Working with Directories

|  | 600007800 0726000 | 『00 ㅁ 056 |
|---|---|---|
|  | 38 뒤 1601# ㅇ 002 ㅁ 5,19456 ㄴ 6501 ㅁ 으 1606 (6020 조 10) 부 |  |
| 0160 2 | 120] 12 116 | 402 | 00 504706-10660206 5/07722077 | 10000 77707706/ | (2001184169 416 604706101600806107811+ 102 11702 00 17 72806669. |
| 60801016: 31606 (60219) 유 16 606 2/1 |  |
| 0160 3 | (0000081) 0005 『0070108-0070118 60801016: 81600 (0072219) 00072 120001 | (200166 0416 210010 용 00011841780070 (0 016 618002 060011841800270. |

Step 2

Step 3

## Working with Directories

This section describes how to work with directories on the Cisco NX-OS device.

## Identifying the Current Directory

You can display the directory name of your current directory.

## SUMMARY STEPS

1. pwd

## DETAILED STEPS

Procedure

|  | 600007800 0726000 | 『00 ㅁ 056 |
|---|---|---|
| 5160 1 | 2\0 | 1219018575 016 08006 01 047 0410601 01260607. |
|  | 60801016: 8 뒤 1601# 5 |  |

## Changing the Current Directory

You can change the current directory for file system operations. The initial default directory is bootflash:.

## SUMMARY STEPS

1. (Optional) pwd

2. cd {directory | filesystem:[//module/][directory]}

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

126

ㅣ

|!

## Using the Device File Systems, Directories, and Files

## Creating a Directory

## DETAILED STEPS

Procedure

|  | 600001800 0726000 | 『00 ㅁ 056 |
|---|---|---|
| 51601 | (0000081) 0\0 6801016: 8 뒤 1601# 5 | 1219218575 016 28006 01 7047 0416610[ 0613416 01260607%. |
| 5160 2 | 60 {077600077|./7/6571576011[//7700700/6/][477600072] } 6801016: 3816016# 60 05161: | (1180866 (0 820\ 04601 01760607. 1116 116 8796(610, 04004416, 300 0176060177 2 ㅁ 80066 876 0896 56091056. |

## Creating a Directory

You can create directories in the bootflash: and flash device file systems.

## SUMMARY STEPS

1. (Optional) pwd

- (Optional) cd {directory | filesystem:[//module/][directory]}

3. mkdir [filesystem:[//module/]]directory

## DETAILED STEPS

Procedure

|  | 600001800 0726000 | 『00 ㅁ 056 |
|---|---|---|
| 51601 | (0000081) 0\0 6801016: 8 뒤 1601# 5 | 1219218579 0416. 08026 01 7047 04160 061341[ 01760607%. |
| 5160 2 | (060002081) 00 {027760707711777/69115760211//770070076/][47760700771]} 6801016: 58160156# 60 51601 | | <011800805 (0 8420\ 04000 01000601%. 1116 116 6791600, 0 ㅁ 001416, 300 0176060177 2 ㅁ 80066 876 0896 56091056. |
| 5160 3 | 11606 [7276511570071[//77007//6/]]277607077 6801016: 5\16056# 2018 6 ㄴ 68 느 | (27686 82 ㅁ 6\ 01260607. 1116 7/7/6511576077 87841020101 16 0856 56091076. 1116 0776007077' 0784100006[ 19 8101180410061010, 0856 56091076, 800 1189 8 0186×100410 01 64 011878016678. |

## Displaying Directory Contents

You can display the contents of a directory.

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

127

| |

## Using the Device File Systems, Directories, and Files

| |

## Deleting a Directory

## SUMMARY STEPS

1. dir [directory | filesystem:[//module/][directory]]

## DETAILED STEPS

## Procedure

|  | 600007800 0726000 |  | 『00 ㅁ 056 |
|---|---|---|---|
| 5660 1 | 0 [077607077 60801016: 3\16056# 0182 600 ㄴ ㅁ 12811 ㄴ 568 는 | |./7/76511576071[//771001076/][407600774]] | 12192018575 016 01760607/ 607016066. 1116 001341616 0416 04060 \0200010 응 012601079. 1116 116 69160 800 012601017 ㅁ 810008 8176 6896 96091056. |

Step 1

## Deleting a Directory

You can remove directories from the file systems on your device.

## Before you begin

Ensure that the directory is empty before you try to delete it.

## SUMMARY STEPS

1. (Optional) pwd

- (Optional) dir [filesystem :[//module/][directory]]

3. rmdir [filesystem :[//module/]]directory

## DETAILED STEPS

Procedure

|  | 600007800 0726000 | 『00 ㅁ 056 |
|---|---|---|
| 51601 | (0000081) 0\0 60801016: 8 뒤 1601# 5 | 1219218579 0416 08026 01 7047 04160 0613416 01760607%. |
| 5160 2 | (0000081) 04 [7/727651576077 디 //770070//6/][477600074]] 60801016: 90110 81 는 566 는 13981 69 는 | 121921875 016 00016019 01 0416 04060 01260[07%. 1116 116 95796604, 2400416, 800 01260[017 ㅁ 81468 876 6896 560910156. 타 따 6 010606077 16 001 60006. 704 20481 066 811 016 1168 1661076 704 0870 00166 0416 01260[07%. |
| 5160 3 | 1000 [77/65157002 리 //772007//6/]]477007077 60801016: 35\16056# 20018 ㄴ 68 트 | 26166 8 01060607. 1116 116 5796(600 800 01760[077 ㅁ 81026 876 0896 96091056. |

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

128

ㅣ

|!

## Using the Device File Systems, Directories, and Files

## Accessing Directories on the Standby Supervisor Module

## Accessing Directories on the Standby Supervisor Module

You can access all file systems on the standby supervisor module (remote) from a session on the active supervisor module. This feature is useful when copying files to the active supervisor modules requires similar files to exist on the standby supervisor module. To access the file systems on the standby supervisor module from a session on the active supervisor module, you specify the standby supervisor module in the path to the file using either filesystem://sup-remote/ or filesystem://sup-standby/.

## Working with Files

This section describes how to work with files on the Cisco NX-OS device.

## Moving Files

You can move a file from one directory to another directory.

^

> **CAUTION**
> Caution

- If a file with the same name already exists in the destination directory, that file is overwritten by the moved file.

You can use the move command to rename a file by moving the file within the same directory.

## SUMMARY STEPS

1. (Optional) pwd

- (Optional) dir [filesystem:[//module/][directory]]

3. move [filesystem:[//module/][directory /] | directory/]source-filename {{filesystem:[//module/][directory /] | directory/}[target-filename] | target-filename}

## DETAILED STEPS

Procedure

|  | 600001800 0726000 | 『00 ㅁ 056 |
|---|---|---|
| 51601 | (0000081) 0\0 6801016: 8 뒤 1601# 5 | 1219218575 016 28006 01 7047 0416610[ 0613416 01260607%. |
| 5160 2 | (0000081) 0 [7/27651576071[//7700700/6/][477600774]] 8 배 기 0: 316056# 018 50012 | 121921875 016 00016019 01 0416 04060 01260[07%. 1116 116 95796604 800 010606(077 ㅁ 8006 876 6896 560910156. |
| 5160 3 | 1006 [/776511576021[//77007/7/6/][477600077 /] | | 40766 8 116. |
| 07076070737]90106060-77/0020776 음 7276577576011[//77007//6/][477600077 /] | 0277/00707717} |7072607-77/00707770| | 727207-/7/07/227770} | 7116 116 679660, 2 ㅁ 00416, 800 012760[07/ ㅁ 810468 876 0856 5610916076. |

directory/}[target-filename] | target-filename}

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

129

| |

## Using the Device File Systems, Directories, and Files

| |

## Copying Files

| 60801016: 3\16010# ㅁ | 076 | 656 | 010 ㄴ 65 ㄴ 56/ ㄴ 681 | 116 707807-77/07707710 8784100001 16 81011804106110, 0850 56051076, 800 1188 8 0186×1004104 01 64 01187801668. 1 016 7079807-77/60707710 878400001[16 201 500011160, 016 11160 ㅁ 8106 06[34166 (0 016 50706-77760207776 878400606[ 81046. |
|---|---|---|---|---|

## Copying Files

You can make copies of files, either within the same directory or on another directory. For more information, see the Cisco Nexus 9000 Series NX-OS Troubleshooting Guide.

%

- Note Use the dir command to ensure that enough space is available in the target file system. If enough space is not available, use the delete command to remove unneeded files.

## SUMMARY STEPS

1. (Optional) pwd

- (Optional) dir [filesystem:[//module/][directory]]

3. copy [filesystem:[//module/][directory/] | directory/]source-filename | {filesystem:[//module/][directory/] | directory/}[target-filename]

## DETAILED STEPS

Procedure

|  | 600007800 0726000 | 『00 ㅁ 056 |
|---|---|---|
| 51601 | (0000081) 0\0 60801016: 8 뒤 1601# 5 | 1219218575 016 08046 01 047 04167610[ 0613416 01260607%. |
| 5160 2 | (00002081) 06 [/77/6511576007[//77007/7/6/][477600774]] 8 배 10: 316056# 018 50012 | 121921875 016 00016019 01 0416 04060 01260[07%. 1116 116 59660 800 010606(077 0 ㅁ 81006 876 6896 560911156. |
| 5160 3 | 003 [/7/6511576011[//720070//6/][4776000727] | 07276070737]9010660-77/0020770 | {/77/6511576021//720070//6/][4770000727] | 07076070737}[747907-7770070770] 60801016: | (000166 81416. 1116 1416 6791602,22001416, 800 01260[077 ㅁ 810068 2606 0896 560911176. 1116 507/7/06-77/677077706 8784006001 15 히 2118041006016, 0896 96091096, 800 1189 8 018×1004104 01 64 이 1808 이 669. 11 016 707907-77(00707710 87840000[ 16 ㅁ 40 506011160, 446 1116081006 0 아 34166 (0 0416.502/7/06-777607207776 878400601[ 81046. |
| 81600# 60069 ㄴ 65 ㄴ 010 ㄴ 66 ㄴ 5/ ㄴ 66 |  |

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

130

ㅣ

|!

## Using the Device File Systems, Directories, and Files

## Copying Files Using HTTP or HTTPS

## Copying Files Using HTTP or HTTPS

You can make copies of files from remote server to local device using HTTP or HTTPS.

<

> **NOTE**
> Note

- Beginning with Cisco NX-OS Release 10.4(3)F, the copy http or copy https command supports TLS version 1.3 and 1.2 on Cisco Nexus switches.

## SUMMARY STEPS

1. (Optional) pwd

- (Optional) dir [filesystem:[//module/][directory]]

3. copy https:// username:password@directory/filename bootflash: vrf management

4. copy http:// directory/filename bootflash: vrf management

## DETAILED STEPS

Procedure

|  | 600001800 0726000 | 『00 ㅁ 056 |
|---|---|---|
| 51601 | (0000081) 0\0 6801016: 8 뒤 1601# 5 | 1219218575 016 28006 01 7047 0416610[ 0613416 01260607%. |
| 5160 2 | (0000081) 0 [7/27651576071[//7700700/6/][477600774]] 6801016: 316056# 018 50012 | 121921875 016 00016019 01 0416 04060 01260[07%. 1116 116 95796604 800 010606(077 ㅁ 8006 876 6896 560910156. |
| 5160 3 | 60053 466070581// 2<596077707701:2705517070(000776070771777/60020776 1600100254: 1 2 ㅁ 8028002001 6801016: 81606 (6072 제 19) 0020? 60661; //456208061100010192.168.0.1/ ㄴ ㄷ 68 느 1600 ㄴ 『129161 ㅁㅁ 때 2 ㅁ 60600672 ㄴ | (200165 016 906011160 11166 10000 76020016 660067 10 10081 06106 46108 46600 00007. |
| 5160 4 | 005 4600:// 7760000731777/674716000010914: \[2 ㅁ 8088601601(| 6801016: 81606 (600219) 뷰 0002 6601/7/192.168.0.1/66 느 나 1600 ㄴ 『129161 ㅁㅁ 때 2 ㅁ 60600672 ㄴ | (』】072166 0416 60601060 11168 17011 7602016 56746 10 10081 06\106 46108 46600 00007. |

## Deleting Files

You can delete a file from a directory.

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

131

| |

## Using the Device File Systems, Directories, and Files

| |

## Displaying File Contents

## SUMMARY STEPS

- (Optional) dir [filesystem:[//module/][directory]]

2. delete {filesystem:[//module/][directory/] | directory/}filename

## DETAILED STEPS

## Procedure

|  | 600007800 0726000 | 『00 ㅁ 056 |
|---|---|---|
| 51660 1 | (0000081) 0 [7/27651576071[//7700700/6/][477600774]] 태미: 3160156# 018 600 ㄴ ㄷ 12810 1 | 121921875 016 00016019 01 0416 04060 01260[07%. 1116 116 59660 800 010606(077 0 ㅁ 81006 876 6896 560911156. |
| 5160 2 | 00666 {/7765175976011[//72001076/][4/76000707] | 072760070737}77/60707760 | 26669 8 416. 1116 116 6766600, 0400416, 800 01760[0797 ㅁ 8100056 266 6896 56091176. 1116 507/7/06-77/607707770 878400001 16 0856 561091076. |
| 60801016: 53\1\ ㄴ 010#* 06166 1 ㅁ 00 ㄴ 12810: 010 000 ㅁ [109 09 | 684000 1704 9060117 8 01060107, 0416 0 이 66 6000001800 06166(66 016 60016 010606077 800 811 115 60066018. |

## Displaying File Contents

You can display the contents of a file.

## SUMMARY STEPS

- show file [filesystem:[//module/]][directory/]filename

## DETAILED STEPS

Procedure

|  | 600007800 0726000 |  | 『00 ㅁ 056 |
|---|---|---|---|
| 51601 | 910\ 1116 | [/7765115700/[//72007//6/]][0776070777]77/00207776 | 1219018578 016 1116 607016018. |

## Displaying File Checksums

You can display checksums to check the file integrity.

## SUMMARY STEPS

- show file [filesystem:[//module/]][directory/]filename {cksum | md5sum}

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

132

ㅣ

|!

## Using the Device File Systems, Directories, and Files

## Compressing and Uncompressing Files

## DETAILED STEPS

Procedure

|  | 600001800 0726000 |  |  | 『00 ㅁ 056 |
|---|---|---|---|---|
| 51601 | 910\ 1116 16650 | 20550440 | [/7765115700/[//72007/76/]][0776070777]77700207776 | |  | 121901855 016 0116069410 07 1401205 01160166410 01 016 116. |
| 6801016: 3160150# 6100 | ,116 15600 ㄴ ㅁ 12611 ㄴ 50062. 020 ㅇ | 05140 |

## Compressing and Uncompressing Files

You can compress and uncompress files on your device using Lempel-Ziv 1977 (LZ77) coding.

## SUMMARY STEPS

- (Optional) dir [filesystem:[//module/]directory]]

2. gzip [filesystem:[//module/][directory/] | directory/]filename

3. gunzip [filesystem:[//module/][directory/] | directory/]filename .gz

## DETAILED STEPS

Procedure

| 51601 | (0000081) 0 [7/27651576071[//77007//6/]4776000774]] 0110: 3160156# 018 600 ㄴ ㄷ 12810 1 | 121921875 016 00016019 01 0416 04060 01260[07%. 1116 116 95796604 800 010606(077 ㅁ 8006 876 6896 560910156. |
|---|---|---|
| 5160 2 | 용 20 [7/2/6511576021[//77000/7/6/][4776000777] | 076000737]/7/6070776 6801016: 3\16050# 0216 8160 ㄴ 6 ㅇ 01 | | 00200705565 8 1416. [67 0416 116 16 0022707685060, 1 185 8 .22 51186. |
|  | 5\16010# 040216 ㅁ 0 51000 ㄴ 6 ㅇ 0101.92 |  |

## Displaying the Last Lines in a File

You can display the last lines of a file.

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

133

| |

## Using the Device File Systems, Directories, and Files

| |

## Redirecting show Command Output to a File

## SUMMARY STEPS

tail [filesystem:[//module/]][directory/]filename [lines]

## DETAILED STEPS

Procedure

|  | 600007800 | 0726000 | 『00 ㅁ 056 |
|---|---|---|---|
| 160 1 | 1811 | [/77/6511570011[//772007/7/0/]][07700700777]77/007047760 |/776 이 | 121921875 0416 1891110468 01 8 116. 1116 06184117 ㅁ 0402667 01 11068 |
| 60801016: 8 뒤 160150# | 6211 6562,-6 노 00 프 도 | 16 10. 1116 70086 16 10010 0 10 80 11068. |

Step 1

## Redirecting show Command Output to a File

You can redirect show command output to a file on bootflash:, volatile:, or a remote server. You can also specify the format for the command output.

## SUMMARY STEPS

- (Optional) terminal redirection-mode {ascii | zipped}

2. show-command > [filesystem:[//module/][directory] | [directory /]]filename

## DETAILED STEPS

Procedure

|  | 600007800 0726000 |  | 『00 ㅁ 056 |
|---|---|---|---|
| 51601 | (0000081) (660001031 7601760000-000@ {13504 | 60801016: 53\16016# ㄴ 612 ㅋ 01021 <601260 ㄴ ㄷ 10 ㅁ - 패 006 2102060 ㅇ | 20060} | | 5066 016 76012601100 ㅁ 20006 107 0416 940\ 6010002800 04124 107 016 4667 56991070. 1116 0013416(270006 16 85011. |
| 5160 2 | 5/20-00777770770 > [/7/6511570071[//77007076/][47700707001 [010606077 /]]77/0070770 60801016: | | | 표 60106065 0416 041041 17010 8 540\ 000001800 10 8 1116. |
| 8916010# 51105 ㄴ 600-5404000 ㄴ ㄴㄴ > 6500 ㄴ 125616 1 | 16001 ㅁ 【 ㅇ |  |

## Finding Files

You can find the files in the current working directory and its subdirectories that have names that begin with a specific character string.

## SUMMARY STEPS

1. (Optional) pwd

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

134

ㅣ

|!

## Using the Device File Systems, Directories, and Files

## Formatting the Bootflash

- (Optional) cd {filesystem:[//module/][directory] | directory}

3.

find filename-prefix

## DETAILED STEPS

Procedure

|  | 600001800 0726000 | 『00 ㅁ 056 |
|---|---|---|
| 51601 | (0000081) 0\0 6801016: 8 뒤 1601# 5 | 1219218575 016 28006 01 7047 0416610[ 0613416 01260607%. |
| 5160 2 | (0000081) 60 {/77/65119700/1[//770070076/][4776000771] | 0/760707 까 6801016: 8\1010# 00 1600\ ㄴ 125101 ㄴ 66 50105 | | 01180865 0446 0013416 01760107%. |
| 5160 3 | 1100 .777/0070770-227607 6801016: 5016056# <100 1696 .50512 느 | 1008 811 016080068 10 016 0613411( 0126060797 800 10 168 9460176060068 66810010 을 \101 0416 11608146 27611%. 1116 116081006 27011 16 6896 5609111596. |

## Formatting the Bootflash

Use the format bootflash: CLI command to format the onboard flash memory (bootflash:). If the command errorsoutduetotheDeactivate all virtual-services and try againerrormessage,destroy the Guest Shell using the guestshell destroy CLI command and rerun the format bootflash: command, for example,

```cisco-ios
switch# sh virtual-service list Virtual Service List:
```

Name

Status

Package Name

-----------------------------------------------------------------------

guestshell+

Activated

guestshell.ova

```cisco-ios
switch#
switch# guestshell destroy
```

You are about to destroy the guest shell and all of its contents. Be sure to save your work. Are you sure you want to continue? (y/n) [n] y

```cisco-ios
switch# 2018 Jan 17 18:42:24 switch %$ VDC-1 %$ %VMAN-2-ACTIVATION_STATE: Deactivating virtual service 'guestshell+'
switch#format bootflash:
```

## Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

135

| |

## Using the Device File Systems, Directories, and Files

| |

## Working with Archive Files

## Working with Archive Files

The Cisco NX-OS software supports archive files. You can create an archive file, append files to an existing archive file, extract files from an archive file, and list the files in an archive file.

## Creating an Archive File

You can create an archive file and add files to it. You can specify the following compression types:

- • bzip2

- • gzip

- • Uncompressed

The default is gzip.

## SUMMARY STEPS

1.

- tar create {bootflash: | volatile:}archive-filename [absolute] [bz2-compress] [gz-compress] [remove] [uncompressed] [verbose] filename-list

## DETAILED STEPS

Procedure

| 01 | 187 00816 100501416] 14000000165560] | {1001085911: | ?018016 을 47077776-77760207776 [022-000001655] [82-000201655] [『602006] [ ㅋ 600056] 7/77607207776-/797 | (2768666 80 8700176 1416 800 8008 1168 10 11. 1116 1116081006 18 히 2180400606, 406 6896 660510176, 400 1189 8 4018%×1044100 16080 이 240 011808 이 669. |
|---|---|---|---|
|  |  |  | 711610000\61665\010 606011166 04181 416 (01900 피 %-08 5011\816 940410 06166(6 0416 1169 12010 016 1116 6796(600 8166 |

Step 1

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

136

ㅣ

|!

## Using the Device File Systems, Directories, and Files

## Appending Files to an Archive File

| 20010 01620 10 0476 8701176. 8 0613416 0416 1168 8726 206 0616660. |
|---|
| 7116 5@ 타 0056 165\010 506011166 0186[ 0416 (21900 피 -(0)8 501[\816 940410 116[ 016 11166 89 416 876 80060 10 0416 8601196. 27 0613416 026 1168 876 1166(60 86 0165 876 80060. |

## Appending Files to an Archive File

You can append files to an existing archive file on your device.

## Before you begin

You have created an archive file on your device.

## SUMMARY STEPS

1.

tar append {bootflash: | volatile:}archive-filename [absolute] [remove] [verbose] filename-list

## DETAILED STEPS

Procedure

| 51601 | 18 800000 {150060128 외 1: | ?012016 을 2/<772776-77/60707776 18050104166] [00006] [60056] 7/7/0770770-7757 | 스 006 11166 10 30 651600 을 8701476 116. 1116 87016 111608106 16 00 0896 560910156. |
|---|---|---|

## Example

This example shows how to append a file to an existing archive file:

```cisco-ios
switch# tar append bootflash:config-archive.tar.gz bootflash:new-config
```

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

137

| |

## Using the Device File Systems, Directories, and Files

| |

## Extracting Files from an Archive File

## Extracting Files from an Archive File

You can extract files to an existing archive file on your device.

## Before you begin

You have created an archive file on your device.

## SUMMARY STEPS

1. tar extract {bootflash: | volatile:}archive-filename [keep-old] [screen] [to {bootflash: | volatile:}[/directory-name]] [verbose]

## DETAILED STEPS

Procedure

|  | 600007800 | 0726000 | 『00 ㅁ 056 |
|---|---|---|---|
| 601 | 18 06801 16600-010] 을 | 000012911: | ㅋ 0141416 을 470/2776-77767020776 [566600] [66 1600100251: | 012016 [/2776070772-70770]] [+6000501 | 08065 11686 17010 80 6×1901 을 67011176 1116. 1116 8701196 116081026 19 00 0896 560911196. 1116600-010 165\0170 14010686(69 0418 016 (21600 페 ×-(08 |
|  |  | 7116 5@00056165\010 506011166 0186[ 0416 (21900 피 -(0)8 5011\816 940410 01620187 016 ㅁ 810468 01 0416 11165 86 0416 816 6080660. |

Step 1

## Displaying the Filenames in an Archive File

You can display the names of the files in an archive files using the tar list command.

tar list {bootflash: | volatile:}archive-filename

The archive filename is not case sensitive.

```cisco-ios
switch# tar list bootflash:config-archive.tar.gz config-file new-config
```

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

138

ㅣ

|!

## Using the Device File Systems, Directories, and Files

## SSD Re-partitioning

## SSD Re-partitioning

You can configure SSD re-partitioning to increase the configuration storage space. This also increases the size of logflash storage. This configuration takes effect after a system reload, and the additional cfg and logflash storage space may decrease the size of the bootflash.

We recommendthatyou perform a backup of allthe softwareimages,configurations,and personaldatabefore performing the SSD re-partitioning.

Starting with Release 10.5(1), you can automatically detect SSD partition size on the switch to match the expected configured size. An information syslog is seen during bootup in the show logging log or show logging nvram commands to indicate the switch booted with an unexpected SSD partitioning size.

%PLATFORM-2-SSD_PARTITION_CHECK: Incorrect <device> partition size detected - please contact

Cisco TAC for additional information

Extended partitioning scheme is not support for platforms with a 64GB SSD.

## SUMMARY STEPS

1.

system flash sda resize

## DETAILED STEPS

Procedure

| 5660 1 | 55660 11851 502 705120 | 봉 66126 267919660[ 5607886 10 ㅁ 6\ 50116046. |
|---|---|---|
|  | 6801016: |  |  |
|  | 69604 <08> | ㅅ |  |
|  | ㅇ ※× ㄴ 60060 0 ㅇ 【 ㅋ 0= ㅋ | 100『1281=3902 |  |
|  | 58 ㄴ 2002 ㅁ 0 0 ㅇ 【?0= ㅋ 64143, | 1001,1286180=4 | 80628 |  |

Step 1

## Example

Following is an example for standard resize:

```cisco-ios
switch# system flash sda resize standard
```

!!!! WARNING !!!!

Attempts will be made to preserve drive contents during the resize operation, but risk of data loss does exist. Backing up of bootflash, logflash, and running configuration is recommended prior to proceeding.

!!!! WARNING !!!!

current scheme is

## Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

139

| |

650

## SSD Re-partitioning

|

|

140

## Using the Device File Systems, Directories, and Files

sda

8:0

0 119.2G 0 disk

|-sda1 8:1 0 512M 0 part |-sda2 8:2 0 32M 0 part /mnt/plog |-sda3 8:3 0 128M 0 part /mnt/pss |-sda4 8:4 0 114.5G 0 part /isan/vdc_1/virtual-instance/guestshell+/rootfs/bootflash |-sda5 8:5 0 64M 0 part /mnt/cfg/0 |-sda6 8:6 0 64M 0 part /mnt/cfg/1 `-sda7 8:7 0 4G 0 part /logflash target scheme is sda 8:0 0 64G|120GB|250GB 0 disk |-sda1 8:1 0 512M 0 part |-sda2 8:2 0 32M 0 part /mnt/plog |-sda3 8:3 0 128M 0 part /mnt/pss |-sda4 8:4 0 110.5G 0 part /bootflash |-sda5 8:5 0 64M 0 part /mnt/cfg/0 |-sda6 8:6 0 64M 0 part /mnt/cfg/1 |_sda7 8:7 0 8G 0 part /logflash

Continue? (y/n) [n] y

A module reload is required for the resize operation to proceed Please, do not power off the module during this process.

Following is an example for extended resize:

```cisco-ios
switch# system flash sda resize extended
```

!!!! WARNING !!!!

Attempts will be made to preserve drive contents during the resize operation, but risk of data loss does exist. Backing up of bootflash, logflash, and running configuration is recommended prior to proceeding.

!!!! WARNING !!!!

current scheme is sda 8:0 0 119.2G 0 disk |-sda1 8:1 0 512M 0 part |-sda2 8:2 0 32M 0 part /mnt/plog |-sda3 8:3 0 128M 0 part /mnt/pss |-sda4 8:4 0 110.5G 0 part /bootflash |-sda5 8:5 0 64M 0 part /mnt/cfg/0 |-sda6 8:6 0 64M 0 part /mnt/cfg/1 `-sda7 8:7 0 8G 0 part /logflash target scheme is sda 8:0 0 120GB|250GB 0 disk |-sda1 8:1 0 512M 0 part |-sda2 8:2 0 32M 0 part /mnt/plog |-sda3 8:3 0 128M 0 part /mnt/pss |-sda4 8:4 0 rem 0 part /bootflash |-sda5 8:5 0 1.0G 0 part /mnt/cfg/0 |-sda6 8:6 0 1.0G 0 part /mnt/cfg/1 |_sda7 8:7 0 39G 0 part /logflash Continue? (y/n) [n] y A module reload is required for the resize operation to proceed

A module reload is required for the resize operation to proceed Please, do not power off the module during this process.

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

ㅣ

|!

## Using the Device File Systems, Directories, and Files

## Enable or Disable Tech-Support Command

## Enable or Disable Tech-Support Command

Follow the steps to enable or disable tech-support command.

## SUMMARY STEPS

- system tech-support blocked-commands sample_list

2. clear system tech-support blocked-commands

## DETAILED STEPS

Procedure

|  | 600001800 0726000 | ㅁ | 『00 056 |
|---|---|---|---|
| 51601 | 5556(601 (6080-50100006 010 606801016: 6016014# 66660 5200616 1151 90400656814117 600210160 118 트 | 이 60-0000008005 581001016 1156 | 71016 66080-5146060 ㄴ 161001<60-0000 ㅎ ㅁ 006 11660 ㄴ 6010-540001 ㄴ ㄴ ㅁ 10 ㅇ (60 ㅇ 0000227 의 0 \ | 8080165 (6011-64000 60100460 60000418008 1196. 600001800 6100166 0416 6×6041100 01 9410\ 0010008008 10 5800016 115[ 17020 5940\1(6080-50000 타 00(0115 [0006- 0004001200].9040\1600-50000 다 311 [0006- 0000412001]. 300 10600-50000 타 ㅇ 6010022008. 1116 11960 6010108008 \04107 ㅁ 01166 6604660 800 91010060 107 0416 8006 9110\-[6011 06000008009. |
|  |  |  |
| 5160 2 | 이 55660 66011-5000006 6801016: | 010 이 60-00100008009 | (16876 (600 -54000 601006660 600200218008 116. |
| 30100 06162 67860 \ | ㄴ 600-5146801 ㄴ ㄴ 16 ㅁ 1 ㅇ ㅇ 60-000 ㅁ 0 ㅁ 270 ㅇ 희 |  |
| 38000658+71411 ㅠ 0162 ㅁ 60 118 느 | ㄴ 6010-54000 ㄴ ㅁㄴ 1 ㅁ 10060 000 ㅁ 0270 희 |  |

## Displaying Tech-support Blocked CLIs

You can find the status of tech support blocked-commands list using the following commands.

## SUMMARY STEPS

- show system tech-support blocked-commands status

2. run bash cat /bootflash/sample_list

## DETAILED STEPS

Procedure

|  | 600001800 0726000 | 『00 ㅁ 056 |
|---|---|---|
| 51601 | 이 10\ 55660 (6004-5000006 010060-0010000005 56314 | 1219218575 016 968048 01 (6011 64000 010060 60100018006 118 |
| 6801016: | 타 따 6 6000000800 1161 15 60860160, 11 940\5 0416 1116 ㅁ 8026 |

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

141

| |

## Using the Device File Systems, Directories, and Files

| |

## Examples of Using the File System

|  | 600007800 0726000 |  | 『00 ㅁ 056 |
|---|---|---|---|
|  | 3\1601# 610 87864 8 ㄴ 28\ ㄴ ㅁㅁ | ㄴ 6 ㅇ 10-51402800 ㄴ ㄴ 1 ㅁ 1 ㅇ ㅇ 60- ㅇ 00 ㅠ ㅁ 27 ㅁ ㅇ 의 |  |
|  | ?601-5104000 ㄴ \ ㄴ 1 ㅁ 10060 | 000020058 116 56 ㄴ 2 ㄴ ㅁ ㅁ 8: ㅁ 1521016 | 예 |
| 160 2 | 1040 08580 | 086(/000608517/5804016 115 | 1219018575 016 60100660-00100048408 1116. |
| 60801016: 5\1 ㄴ 056# 240 62861 5100 7625102 ㅁ 300 1209760 ㅁ ㄴ 606 두 3100 ㅁ 00 ㅁ 16 ㅎ 3100 ㄴ 600-514000 | /600 ㄴ 『165186/520016 118 는 52000 | 7116 0208×1004100 160801 01 446 116 080 ㅁ 206 128. * ㆍ 7146 16 6380: 2006 000000800 641 016 110060-00000480061\0410 66 6116610176 88 1070 을 89 016 116 16 6606 86/000707745//, 800 \0410 0006166 807055 811 1446 7610808. |
|  |  | * 7116 116 ㅁ 6608 7680 06000165107. |

Step 2

## Examples of Using the File System

This section includes examples of how to use the file system on the Cisco NX-OS device.

## Accessing Directories on Standby Supervisor Modules

This example shows how to list the files on the standby supervisor module:

```cisco-ios
switch# dir bootflash://sup-remote
```

4096 Oct 03 23:55:55 2013 .patch/ ... 16384 Jan 01 13:23:30 2011 lost+found/ 297054208 Oct 21 18:55:36 2013 n9000-dk9.6.1.2.I1.1.bin ... Usage for bootflash://sup-remote 1903616000 bytes used 19234234368 bytes free 21137850368 bytes total

This example shows how to delete a file on the standby supervisor module:

```cisco-ios
switch# delete bootflash://sup-remote/aOldConfig.txt
```

## Moving Files

This example shows how to move a file on an external flash device:

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

142

ㅣ

|!

## Using the Device File Systems, Directories, and Files

## Copying Files

## switch# move usb1:samplefile usb1:mystorage/samplefile

This example shows how to move a file in the default file system:

## switch# move samplefile mystorage/samplefile

## Copying Files

This example shows how to copy the file called samplefile from the root directory of the usb1: file system to the mystorage directory:

```cisco-ios
switch# copy usb1:samplefile usb1:mystorage/samplefile
```

This example shows how to copy a file from the current directory level:

## switch# copy samplefile mystorage/samplefile

This example shows how to copy a file from the active supervisor module bootflash to the standby supervisor module bootflash:

```cisco-ios
switch# copy bootflash:nx-os-image bootflash://sup-2/nx-os-image
```

This example shows how to overwrite the contents of an existing configuration in NVRAM:

## switch# copy nvram:snapshot-config nvram:startup-config

> **WARNING**
> Warning: this command is going to overwrite your current startup-config: Do you wish to continue? {y/n} [y] y

You can also use the copy command to upload and download files from the bootflash: file system to or from a FTP, TFTP, SFTP, or SCP server.

## Deleting a Directory

You can remove directories from the file systems on your device.

## Before you begin

Ensure that the directory is empty before you try to delete it.

## SUMMARY STEPS

1. (Optional) pwd

- (Optional) dir [filesystem :[//module/][directory]]

3. rmdir [filesystem :[//module/]]directory

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

143

| |

## Using the Device File Systems, Directories, and Files

| |

## Displaying File Contents

## DETAILED STEPS

Procedure

|  | 600007800 0726000 | 『00 ㅁ 056 |
|---|---|---|
| 51660 1 | (0000081) 0\0 60801016: 8 뒤 1601# 5 | 1219218575 016 08046 01 047 04167610[ 0613416 01260607%. |
| 5160 2 | (00002081) 06 [/7765157007 :[//77007076/][40760007001] 태미: 8016089# 615 566 는 1396 169 는 | 121921875 016 00016019 01 0416 04060 01260[07%. 1116 116 95796604, 2400416, 800 01260[017 ㅁ 81468 876 6896 560910156. 타 따 6 010606077 16 001 60006. 704 20481 066 811 016 1168 1661076 704 0870 00166 0416 01260[07%. |
| 5160 3 | 1000 [77/65157002 리 //772007//6/]]477007077 60801016: 35\16056# 20018 ㄴ 68 트 | 26166 8 01060607. 1116 116 5796(600 800 01760[077 ㅁ 81026 876 0896 96091056. |

## Displaying File Contents

This example shows how to display the contents of a file on an external flash device:

```cisco-ios
switch# show file usb1:test configure terminal interface ethernet 1/1 no shutdown end show interface ethernet 1/1
```

This example shows how to display the contents of a file that resides in the current directory:

```cisco-ios
switch# show file myfile
```

## Displaying File Checksums

This example shows how to display the checksum of a file:

```cisco-ios
switch# show file bootflash:trunks2.cfg cksum 583547619
```

This example shows how to display the MD5 checksum of a file:

```cisco-ios
switch# show file bootflash:trunks2.cfg md5sum 3b94707198aabefcf46459de10c9281c
```

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

144

ㅣ

|!

## Using the Device File Systems, Directories, and Files

## Compressing and Uncompressing Files

## Compressing and Uncompressing Files

This example shows how to compress a file:

```cisco-ios
switch# dir 1525859 Jul 04 00:51:03 2013 Samplefile ... switch# gzip volatile:Samplefile switch# dir 266069 Jul 04 00:51:03 2013 Samplefile.gz ...
```

This example shows how to uncompress a compressed file:

```cisco-ios
switch# dir 266069 Jul 04 00:51:03 2013 Samplefile.gz ... switch# gunzip samplefile switch# dir 1525859 Jul 04 00:51:03 2013 Samplefile
```

...

## Redirecting show Command Output

This example shows how to direct the output to a file on the bootflash: file system:

```cisco-ios
switch# show interface > bootflash:switch1-intf.cfg
```

This example shows how to direct the output to a file on external flash memory:

```cisco-ios
switch# show interface > usb1:switch-intf.cfg
```

This example shows how to direct the output to a file on a TFTP server:

```cisco-ios
switch# show interface > tftp://10.10.1.1/home/configs/switch-intf.cfg Preparing to copy...done
```

This example shows how to direct the output of the show tech-support command to a file:

```cisco-ios
switch# show tech-support > Samplefile Building Configuration ... switch# dir 1525859 Jul 04 00:51:03 2013 Samplefile Usage for volatile:// 1527808 bytes used 19443712 bytes free 20971520 bytes total
```

## Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

145

| |

\'

## Finding Files

## Finding Files

|

|

146

## Using the Device File Systems, Directories, and Files

This example shows how to find a file in the current default directory:

```cisco-ios
switch# find smm_shm.cfg
```

/usr/bin/find: ./lost+found: Permission denied ./smm_shm.cfg ./newer-fs/isan/etc/routing-sw/smm_shm.cfg ./newer-fs/isan/etc/smm_shm.cfg

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

ㅣ

1 0

C H A P T E R 10

## Working with Configuration Files

This chapter contains these sections:

- • About Configuration Files, on page 147

- • Guidelines and Limitations for Configuration Files, on page 148

- • Managing Configuration Files, on page 148

- • Configuration Archive and Configuration Log, on page 159

- • Verifying the Device Configuration, on page 163

- • Examples of Working with Configuration Files, on page 165

## About Configuration Files

Configuration files contain the Cisco NX-OS software commands used to configure the features on a Cisco NX-OS device. Commands are parsed (translated and executed) by the Cisco NX-OS software when the system is booted (from the startup-config file) or when you enter commands at the CLI in a configuration

mode.

To change the startup configuration file, you can either save the running-configuration file to the startup configuration using the copy running-config startup-config command or copy a configuration file from a file server to the startup configuration.

## Types of Configuration Files

TheCiscoNX-OSsoftwarehastwotypesofconfigurationfiles,runningconfigurationandstartupconfiguration. The device uses the startup configuration (startup-config) during device startup to configure the software features. The running configuration (running-config) contains the current changes that you make to the startup-configuration file. The two configuration files can be different. You might want to change the device configuration for a short time period rather than permanently. In this case, you would change the running configuration by using commands in global configuration mode but not save the changes to the startup configuration.

To change the running configuration, use the configure terminal command to enter global configuration mode. As you use the Cisco NX-OS configuration modes, commands generally are executed immediately and are saved to the running configuration file either immediately after you enter them or when you exit a configuration mode.

To change the startup-configuration file, you can either save the running configuration file to the startup configuration or download a configuration file from a file server to the startup configuration.

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

147

## Working with Configuration Files

| |

## Guidelines and Limitations for Configuration Files

## Related Topics

Saving the Running Configuration to the Startup Configuration, on page 148 Downloading the Startup Configuration From a Remote Server, on page 150

## Guidelines and Limitations for Configuration Files

Configuration file guidelines and limitations are as follows:

- • Beginning with NX-OS 7.0(3)I7(4), the reload timer command is supported to enable a reboot after a delay of 5 -60 seconds.

## Managing Configuration Files

This section describes how to manage configuration files.

## Saving the Running Configuration to the Startup Configuration

You can save the running configuration to the startup configuration to save your changes for the next time you that reload the device.

## SUMMARY STEPS

1.

(Optional) show running-config

2. copy running-config startup-config

## DETAILED STEPS

Procedure

| 160 1 | (0000081) 940\ 60801016: 으 듀오 00# 610 2000109- ㅇ ㅇㅁㅇ | 00070108-6070108 | 1219218575 016 20400108 0001184780 ㅁ 07. |
|---|---|---|---|
|  | 60801016: 38 뒤 160150# 60209 12400109- ㅇ 012 ㅁ | 619 8 ㄴ 2 ㄴ ~6000-002 ㅁ 519 | 84! |

Step 1

Step 2

## Copying a Configuration File to a Remote Server

You can copy a configuration file stored in the internal memory to a remote server as a backup or to use for configuring other Cisco NX-OS devices.

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

148

ㅣ

|!

## Working with Configuration Files

## Downloading the Running Configuration From a Remote Server

## SUMMARY STEPS

1. copy running-config scheme://server/[url /]filename

2. copy startup-config scheme://server/[url /]filename

## DETAILED STEPS

Procedure

| 51601 | 6003 70707010 용 -600 을 50/76776:1//9677677[207 /]/77/0020776 | (200166 0416 20100108-000118418007 116 10 8 7000016 56006 ㄷ . |
|---|---|---|
|  | 6801016: 8 뒤 1606# ㅇ 062 우 120400109- ㅇ 0 ㅇ 5 ㅋ 19 느 6061//10.10.1.1/5601-2040-000 ㅁ 219 .08 노 | 07006 50076016 878401001, 04 080 60167 00: 1001. 500: 00 90001. 1116 567776/' 87840460[ 16 416 8007666 0『77 ㅁ 81046 01 016 1600016 56776, 400 0416 707 817840060618 0416 08041 10 016 04706 116 00 016 7600016 56006. 116 56776, 107, 300 77/00207776 87241001065 876 0896 560510156. |
|  |  | 116 56776, 107, 300 77/00207776 87241001065 876 0896 560510156. |

## Example

This example shows how to copy the configuration file to a remote server:

```cisco-ios
switch# copy running-config tftp://10.10.1.1/sw1-run-config.bak switch# copy startup-config tftp://10.10.1.1/sw1-start-config.bak
```

## Downloading the Running Configuration From a Remote Server

You can configure your Cisco NX-OS device by using configuration files that you created on another Cisco NX-OS device and uploaded to a remote server. You then download the file from the remote server to your device using TFTP, FTP, Secure Copy (SCP), or Secure Shell FTP (SFTP) to the running configuration.

## Before you begin

Ensure that the configuration file that you want to download is in the correct directory on the remote server.

Ensure that the permissions on the file are set correctly. Permissions on the file should be set to world-read.

Ensure that your device has a route to the remote server. Your device and the remote server must be in the same subnetwork if you do not have a router or a default gateway to route traffic between subnets.

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

149

| |

## Working with Configuration Files

| |

## Downloading the Startup Configuration From a Remote Server

Check connectivity to the remote server using the ping or ping6 command.

## SUMMARY STEPS

1. copy scheme://server/[url/]filename running-config

- (Optional) show running-config

- (Optional) copy running-config startup-config

- (Optional) show startup-config

## DETAILED STEPS

Procedure

| 51601 | 005 560/767761//9677677[107/]/7700707167000108-607018 | 100\1410808 016 200100108-000118418007 1116 12010 8 7002016@ |
|---|---|---|
|  | 60801016: 5016056# 0002 6501//10.10. 1. 17 ㅁ 9-00 포 400 ㅁ 1 ㅁ 9- ㅇ 0 ㅁ 519 | 56196. 보 00 016. 90/06076 868400606 704 680 60666 06001, 001 500 을 00 90001. 1116 567776/' 878404100[ 16 0416 8007666 077 ㅁ 81046 01 06 1600016 56776, 400 0416 707 878400601 19 0416 08041 10 016 6014706 116 00 016 7600016 56006. 116 567776/, 107, 300 77/00707776 87241001065 876 0896 5605110156 |
| 5160 2 | (0000081) 5940\ 7007010 용 -60701 을 60801016: 으 듀오 00# 610 2000109- ㅇ ㅇㅁㅇ | 1219218575 016 20400108 0001184780 ㅁ 07. |
| 5160 3 | (0000081) 000 ㅁ 0070108-607018 56406010-0 60801016: 38 뒤 160150# 60209 12400109- ㅇ 012 ㅁ 619 8 ㄴ 2 ㄴ ~6000-002 | (200166 0416 210010 용 00011841780070 (0 016 618002 060011841800270. |
| 5160 4 | (0000081) 9440\ 56026000-0 ㅇ 00108 60801016: 3816010# 610 8 ㄴ 226000- ㅇ 02 ㅁ 519 | 1219218575 016 61800042 0070118478007. |

## Related Topics

Copying Files, on page 143

## Downloading the Startup Configuration From a Remote Server

You can configure your Cisco NX-OS device by using configuration files that you created on another Cisco NX-OS device and uploaded to a remote server. You then download the file from the remote server to your device using TFTP, FTP, Secure Copy (SCP), or Secure Shell FTP (SFTP) to the startup configuration.

^

- Caution

This procedure disrupts all traffic on the Cisco NX-OS device.

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

150

ㅣ

|!

## Working with Configuration Files

## Downloading the Startup Configuration From a Remote Server

## Before you begin

Log in to a session on the console port.

Ensure that the configuration file that you want to download is in the correct directory on the remote server.

Ensure that the permissions on the file are set correctly. Permissions on the file should be set to world-read.

Ensure that your device has a route to the remote server. Your device and the remote server must be in the same subnetwork if you do not have a router or a default gateway to route traffic between subnets.

Check connectivity to the remote server using the ping or ping6 command.

## SUMMARY STEPS

1. write erase

2. reload

3. copy scheme://server/[url /]filename running-config

4. copy running-config startup-config

5.

(Optional) show startup-config

## DETAILED STEPS

Procedure

|  | 600001800 0726000 | 『00 ㅁ 056 |
|---|---|---|
| 51601 | \216(6 00056 6801016: 3\16010# 216 62566 | 트 086968 016 618000420 0001184080007 11416. |
| 5160 2 5160 3 | 101020 60801016: 5\16010# ㅜ 610080 모 116 60000827 ㅁ 0 111 61660 ㄴㄴ 57866. 꼬 표 0668 66 2 ㅁ 25880 < 20012"; 06206【120 ㅁ 6 ㅁ 08550 082 "20012"; 뭐 00410 04 1116 6 60662 타 6 1652616 212109 (768/2 ㅁ 0): 2 ㅁ | 표 인 0808 016 (21600 페 즈 -08 06106. 띠 066 100 201 466 0416 56042 401167 10 600118476 016 06106. |
| 5\101# 003 50/076776://9677677[107 /]/7/624776 2000108- | 100\14010808 016 20010010 을 6000118478007 1116 12010 8 70100016 |

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

151

| |

## Working with Configuration Files

| |

## Copying Configuration Files to an External Flash Memory Device

|  | 600007800 0726000 | 『00 ㅁ 056 |
|---|---|---|
| 6160 4 | 6003 7000108-60018 56『060040-607018 60801016: 8 뒤 1606# ㅇ 062 우 120400109- ㅇ 0 ㅇ 5 ㅋ 19 8 ㄴ 622600- ㅇ 0 ㅁ 【 ㅁ 19 | 옹 3 ㅋ 66 016 2040010 을 0001184000070 116 10 016 98002 06001184180070 116. |
| 6160 5 | (0000081) 940\ 568『00040-0070108 60801016: 3816010# 610 8 ㄴ 226000- ㅇ 02 ㅁ 519 | 1219218575 016 20400108 0001184780 ㅁ 07. |

Step 4

Step 5

## Related Topics

Copying Files, on page 143

## Copying Configuration Files to an External Flash Memory Device

You can copy configuration files to an external flash memory device as a backup for later use.

## Before you begin

Insert the external Flash memory device into the active supervisor module.

## SUMMARY STEPS

- (Optional) dir {usb1: | usb2:}[directory/]

2. copy running-config {usb1: | usb2:}[directory/]filename

3. copy startup-config {usb1: | usb2:}[directory/]filename

## DETAILED STEPS

Procedure

|  | 600007800 0726000 | 『00 ㅁ 056 |
|---|---|---|
| 51601 | (0000081) 0 14501: |45021}[07760000707] 60801016: 8 뒤 160156# 0 218 06161 』 | 1219201875 016 1166 00 016 6%(60081 11891 20600077 06166. |
| 5160 2 | 6003 2000108-60018 14501: | 45021}[0776070777]77/6070776 60801016: 8 뒤 1606# ㅇ 062 우 120400109- ㅇ 0 ㅇ 5 ㅋ 19 48161 1080- ㄴ 00010090-0 ㅇ 0 ㅁ [10 . ㅇ 090 | | 002165 016 0100108 000118418000 (0 80 6%160081 11898 106100077 06106. 1116 .7/7/767707770 8784100001[ 16 0896 5606101576. - |
| 5160 3 | 60053 56000040-00018 14501: | 45021} [4776070777]/7/0070776 60801016: 3816050# 6009 8 ㄴ 2 ㄴ 56 ㅁ 00- ㅇ 0 ㅁ 5 ㅋ 19 1481 61:080-8 ㄴ 2 ㄴ \ ㄴ ㄷ ㄴ ㅁ 06-00 ㅁ [10 . 020 | |(002165 016 9680002 000118418000 (0 80 6%160081 18911 0060001% 06166. 1116.7/77607070776 878402601[ 19 6896 5606106. |

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

152

ㅣ

|!

## Working with Configuration Files

## Copying the Running Configuration from an External Flash Memory Device

## Related Topics

Copying Files, on page 143

## Copying the Running Configuration from an External Flash Memory Device

You can configure your device by copying configuration files created on another Cisco NX-OS device and saved to an external flash memory device.

## Before you begin

Insert the external flash memory device into the active supervisor module.

## SUMMARY STEPS

1.

(Optional) dir {usb1: | usb2:}[directory/]

2. copy {usb1: | usb2:}[directory/]filename running-config

3.

(Optional) show running-config

4.

(Optional) copy running-config startup-config

5.

(Optional) show startup-config

## DETAILED STEPS

Procedure

| 51601 | (0000081) 004 {14901 | 45021 }[4770000707] 6801016: 8 뒤 160156# 0 218 06161 』 |  | 1219201875 016 1166 00 016 6%(60081 11891 20600077 06166. |
|---|---|---|---|
| 5160 2 | 000 10901; | 6801016: 38160156# ㅇ 600869 ㅁ 4515611096 ㅁ -0 ㅇ 012 ㅁ [,190, ㅇ 29 | 49021[0776070777]777/607077600070108-0010118 ~400109- ㅇ 0 ㅇ ㅁ 5 ㅋ 19 | | 02165 0416 2400108 0001184180010 10000 80 6%167081 11898 1061000757 06106. 1116 .7/7/767707770 8784100001[ 16 0856 5606101576. - |
| 5160 3 | (0000081) 5940\ 7007010 용 -60701 을 6801016: 으 듀오 00# 610 2000109- ㅇ ㅇㅁㅇ |  | 1219218575 016 20400108 0001184780 ㅁ 07. |
| 5160 4 | (0000081) 000 ㅁ 000108-607018 6801016: 38 뒤 160150# 60209 12400109- ㅇ 012 ㅁ 619 8 ㄴ 2 ㄴ | 564060010-0 ㅇ 00108 ~6000-002 ㅁ 519 | (200166 0416 210010 용 00011841780070 (0 016 618002 060011841800270. |
| 5160 5 | (0000081) 9440\ 56026000-0 ㅇ 00108 6801016: |  | 1219218575 016 61800042 0070118478007. |
|  | 3816010# 610 8 ㄴ 226000- ㅇ 02 ㅁ 519 |  |  |

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

153

| |

## Working with Configuration Files

| |

## Copying the Startup Configuration From an External Flash Memory Device

## Related Topics

Copying Files, on page 143

## Copying the Startup Configuration From an External Flash Memory Device

You can recover the startup configuration on your device by downloading a new startup configuration file saved on an external flash memory device.

## Before you begin

Insert the external flash memory device into the active supervisor module.

## SUMMARY STEPS

- (Optional) dir {usb1: | usb2:}[directory/]

2. copy {usb1: | usb2:}[directory /]filename startup-config

3.

(Optional) show startup-config

## DETAILED STEPS

Procedure

|  | 600007800 0726000 | 『00 ㅁ 056 |
|---|---|---|
| 51601 | (0000081) 04 10501: | 4502 으 [4776000777] 60801016: 8 뒤 160156# 0 218 06161 』 | 1219201875 016 1166 00 016 6%(60081 11891 20600077 06166. |
| 5160 2 | 000 14901: | 49021} [0776070077'/]/7/070776 60801016: 3\0160150# 0009 ㅁ 4561106 ㅁ -0010 ㅁ [10.0 ㅇ 29 | | 02165 0416 51800472 0001184180070 10010 80 6×%(60081 01894 106100077 06106. 1116 .7/7/767707770 8784100001[ 16 0896 5606101576. - |
| 5160 3 | (0000081) 9440\ 56026000-0 ㅇ 00108 60801016: 3816010# 610 8 ㄴ 226000- ㅇ 02 ㅁ 519 | 1219218575 016 61800042 0070118478007. |

## Related Topics

Copying Files, on page 143

## Copying Configuration Files to an Internal File System

You can copy configuration files to the internal memory as a backup for later use.

## SUMMARY STEPS

1. copy running-config [filesystem:][directory/] | [directory/]filename

2. copy startup-config [filesystem:][directory/] | [directory/]filename

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

154

ㅣ

|!

## Working with Configuration Files

## Rolling Back to a Previous Configuration

## DETAILED STEPS

Procedure

|  | 600001800 0726000 | 『00 ㅁ 056 |
|---|---|---|
| 51601 | 003 70070108-000118 [/776515760071][4776000727] | 07276070737]77/602077760 「 4 | (200166 0416 2400108-06001184178007 1116 10 10160081 0061007%. , 그 800 |
| 6801016: 8 뒤 1606# ㅇ 062 우 120400109- ㅇ 0 ㅇ 5 ㅋ 19 1600 ㄴ 『 ㄷ 1286161 501- ㄴ ㅋ 00-007 ㅁ ㅋ 10 5626 | 116.7/77651157007, 077007077, 7/1/00707776 8784100015 876 0856 5610916076. |
| 5160 2 | 60053 564060040-007118 [/77/651576021][4776000727] | | (200166 0416 56020000-00701184180070 1116 (0 10[60081 02610007%. |
| [00276070737]77/60707760 6801016: 3816050# 6009 8 ㄴ 2 ㄴ 56 ㅁ 00- ㅇ 0 ㅁ 5 ㅋ 19 1000 ㄴ 『12810:8\01-582 ㄴ ㄴ -00 ㅁ [10502 | 그 116.7/77651157007, 077007077, 800 7/1/00707776 8784100015 876 0856 5610916076. |

## Related Topics

Copying Files, on page 130

## Rolling Back to a Previous Configuration

Problems, such as memory corruption, can occur that make it necessary for you to recover your configuration from a backed up version.

<

- Note Each time that you enter a copy running-config startup-config command, a binary file is created and the ASCII file is updated. A valid binary configuration file reduces the overall boot time significantly. A binary file cannot be uploaded, but its contents can be used to overwrite the existing startup configuration. The write erase command clears the binary file.

## SUMMARY STEPS

1. write erase

2. reload

3. copy configuration-file running-configuration

4. copy running-config startup-config

## DETAILED STEPS

Procedure

|  | 600001800 0726000 | 『00 ㅁ 056 |
|---|---|---|
| 51601 | \216(6 00056 | (16876 016 0410 ㅠ 606[ 60201184180070 01 016 5\16041. |
| 6801016: |  |

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

155

| |

## Working with Configuration Files

| |

## Removing the Configuration for a Missing Module

|  | 3\16010# | 216 62566 |  |  |
|---|---|---|---|---|
| 3160 2 | 10100 |  |  | 봉 6616069 016 06166. 704 \111 66 0001000160 10 200\106 82 |
| 0160 3 | 00 ㅇ 60801016: 38\160150# 노 40 ㅁ 1 ㅁ 9- | 072778100707707-777/6 0009 16500 ㄴ 12510: ㅁ 5 ㅋ 190 ㅇ 0 ㅁ 【<1942261 ㅇ ㅁ | -2000108-000108468007 5255-00 .52 노 | (200166 8276\1046917 58760 6001184178007 1116 10 0416 2107010 음 060011841800270. 티 06 . 때 7116 007277810077077-7776 416081006 818400601 18 0856 9605106@. |
|  |  |  |  |  |
| 0160 4 | 003 60801016: | 70070108-000118 564『0410-607018 |  | (200166 0416 201207010 용 0001184178007 (0 016 51002-02 060011841800270. |
|  | 38 뒤 160150# | 60209 12400109- ㅇ 012 ㅁ 619 8 ㄴ 2 ㄴ | ~6000-002 ㅁ 519 |  |

Step 2

Step 3

Step 4

## Removing the Configuration for a Missing Module

When you remove an I/O module from the chassis, you can also remove the configuration for that module from the running configuration.

<

- Note

You can only remove the configuration for an empty slot in the chassis.

## Before you begin

Remove the I/O module from the chassis.

## SUMMARY STEPS

1.

(Optional) show hardware

2. purge module slot running-config

3.

(Optional) copy running-config startup-config

## DETAILED STEPS

Procedure

|  | 600007800 0726000 | 『00 ㅁ 056 |
|---|---|---|
| 51601 | (0000081) 59410\ 6200\276 60801016: 3\1601# 610 122 ㅋ 0\226 | 1219218575 016 109681160 11870\816 107 0416 06106. |
| 5160 2 | 24686 2200416 5707 『0070108- ㅇ 07018 60801016: | 폭 6000 ㅋ 68 016 60201184180010 107 8 20196108 20200416 17010 046 170400108 600011847800272. |

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

156

ㅣ

|!

## Working with Configuration Files

## Erasing a Configuration

|  | 316010# | ㅁ 6045296 | 패 00016 3 ~<040010 ㅁ 9- ㅇ 0 ㅁ [ㄴㅇ |  |
|---|---|---|---|---|
| 03 | (0000081) | 000 | ㅁ 000108-607018 564060010-0 ㅇ 00108 | (200166 0416 210010 용 00011841780070 (0 016 618002 |
| 6801016: |  |  | 060011841800270. |
| 38 뒤 160150# | 60209 | 12400109- ㅇ 012 ㅁ 619 8 ㄴ 2 ㄴ ~6000-002 ㅁ 519 |  |

Step 3

## Erasing a Configuration

You can erase the configuration on your device to return to the configuration defaults. "Configuration" refers to the startup configuration as seen in 'show startup'. No other internal application or process states are cleared.

Erase configuration feature is supported on the Nexus 9200-X, Nexus 9300-FX, -FX2, -FX3, and Nexus 9500 series switches.

You can erase the following configuration files saved in the persistent memory on the device:

- • Startup

- • Boot

- • Debug

The write erase command erases the entire startup configuration, except for the following:

- • Boot variable definitions

- • The IPv4 and IPv6 configuration on the mgmt0 interface, including the following:

- • Address

- • Subnet mask

- • Default Gateway/Route in the management VRF

To remove the boot variabledefinitionsand the IPv4/IPv6 configurationon the mgmt0 interface,use the write erase boot command. To remove all application persistency files such as patch rpms, third party rpms, application configuration in /etc directory other than configuration, use 'install reset'. This command was added as of the 7.0(3)I6(1) release.

%

> **NOTE**
> Note

- When there are multiple IPv6 default routes present in the management VRF, the default route that is displayed first in the show ipv6 static-route command for the management VRF just before using ‘copy r s’ gets restored after the write erase and reload.

- Note After you enter the write erase command, you must reload the ASCII configuration twice to apply the breakout configuration.

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

157

| |

## Working with Configuration Files

| |

## Clearing Inactive Configurations

## SUMMARY STEPS

## 1. write erase [boot | debug]

## DETAILED STEPS

Procedure

| 1601 | \216(6 60856 | [60061 00008] |  |  |  | 트 |  | 086968 007011847800108 10 026679166610[ 2161001%. 1116 0613141[ |
|---|---|---|---|---|---|---|---|---|
|  | 60801016: |  |  |  |  | 7116 |  | 20000 608968 016 60800020 000118408007. 00016 02000 008666 0416 6001 ㅋ 80 ㅁ 8016 061101110085 800 |
|  | 3\16010# 216 뭐 32010 ㅁ 0901 또 218 ㅇ | 62566 000600 | 0111 | 62256 | ㄴㅇ | 1446 |  | 10274 0001184780070 070 016 04800160 10[60806. |
|  | 36226000-002 ㅁ 206 704 01616 6 | 【1942286102 ㅁ . ㅁ 200 ㅇ 660 | 20579087?2 | 0 | ㅁ ) | (?/2 [21] 꼬 7116 띠 066 |  | 00048 00000 600965 016 000088108 60001184780 ㅁ 07. |
|  |  |  |  |  |  | 7116 |  | 20000108-0001184180070 1116 16 001 81[60160 65 0218 0600004800. |

Step 1

## Clearing Inactive Configurations

You can clear inactive QoS and/or ACL configurations.

## SUMMARY STEPS

1.

(Optional) show running-config type inactive-if-config

2. clear inactive-config policy

3.

(Optional) show inactive-if-config log

## DETAILED STEPS

Procedure

|  | 600007800 0726000 |  | 『00 ㅁ 056 |
|---|---|---|---|
| 51601 | (0000081) 9410\ 070070108-607011 60801016: | 을 70276 108060156-11-007011 을 | 121921875 807 1080076 80066 600001 119[ ( 스 (11.) 07 04811 0 6600106 (0008) 60201184780008. |
| 퓨 51606 데 <040010 ㅁ 9-0 ㅇ 010 ㅁ 219 | 10005 1020 ㄴ 1576-1-00 ㅁ [ ㅋ 19 | 7116 81466 107 0416 70276 8784100601 876 80100 800 10005. ㆍ 8 이 00 으 -12160186579 805 10801106 60701184180008 107 80120 |

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

158

ㅣ

|!

## Working with Configuration Files

## Configuration Archive and Configuration Log

|  |  |  | * ㆍ 10008--12192185785 807 10480076 00701184180008 107 0406006. |
|---|---|---|---|
| 5160 2 | 이 10266196-60018 /70/707 |  | (16876 108001046 6001184780 ㅁ 10708. |
| 6801016: |  | 7116 81466 107 016 77077011 8<8410001 876 0405 800 801. |
| * 0162 ㄴ 10206106 ㄱ 00019 005 ㅇ 0162 ㄴ 005 1020\ ㄴ 1176 00010 |  | 7116 10110\108 0660171068 016 81466: |
| 1020\ ㄴ 176 1, 00010 10 0098 0 ㅁ 26/6006 ㄴ ㅁ 20176 1 | 8202806 ㄴ 15 52760 1286186/0605._10 000219 0529 <0 ㅁ 1700 | ㆍ 009--(:16875 108611\6 008 06001184680008. |
| 0628142 7014 020 666 \ ㄴ 1 ㅁ 6 109 +116 0 109 | 61600 1020 ㄴ 176-1『-000 ㅁ [1 이 | *801-(216879 148006 (1. 0001184080008. * ㆍ 8 이 409--(16875 10480076 (11. 00011840800205 800 1080601976 (0008 60011841800108. |
| 5160 3 | (0000081) 5060\1080056-1-007018 6801016: | 10 음 | 1219018575 0416 6000018008 018[ \676 46560 [0 01687 016 10800 06001184180008. |
|  | # 51608 1020 ㄴ 176-1-000 ㅁ 5190 | 109 |  |

Displays the commands that were used to clear the inactive

## Configuration Archive and Configuration Log

This section contains information on configuration archive and configuration log.

## Information About Configuration Archive

The configuration archive is intended to provide a mechanism to store, organize, and manage an archive of the configuration files to enhance the configuration rollback capability provided by the configure replace command. Before configuration archiving was introduced, you could save copies of the running configuration usingthecopyrunning-configdestination-urlcommand,storingthereplacementfileeitherlocallyorremotely. However, this method lacked any automated file management. The configuration replace and configuration rollback provides the capability to automatically save copies of the running configuration to the configuration archive. These archived files serve as checkpoint configuration references and can be used by the configure replace command to revert to the previous configuration states.

The archive config command allows you to save configurations in the configuration archive using a standard location and filename prefix that is automatically appended with an incremental version number (and optional timestamp) as each consecutive file is saved. This functionality provides a means for consistent identification of saved configuration files. You can specify how many versions of the running configuration are kept in the archive. After the maximum number of files are saved in the archive, the oldest file is automatically deleted when the next, most recent file is saved. The show archive command displays information for all configuration files saved in the configuration archive.

Theconfigurationarchive,whereintheconfigurationfilesarestoredandareavailableforusewiththeconfigure replace command, can be located on the following file systems: bootflash, FTP, and TFTP.

%

- Note

The TFTP and FTP for this feature use VRF management.

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

159

| |

## Working with Configuration Files

| |

## Configuring the Characteristics of the Configuration Archive

## Configuring the Characteristics of the Configuration Archive

Before using the archive config command, the configuration archive must be configured. Complete the following steps to configure the characteristics of the configuration archive:

## SUMMARY STEPS

1. configure terminal

2. archive

3. path url

4. maximum number

5.

time-period minutes

6. write-memory

7. archive config

8.

(Optional) show archive log config all

## DETAILED STEPS

Procedure

| 6160 1 | 000847@ | 6(60001021 |  |  | 느 26(666 016 인 01681 0020118478000 20006. |
|---|---|---|---|---|---|
| 6160 2 |  |  |  |  | 뜨 26666 016 8101476 000118478000 24006. |
|  | 60801016: 3016010# 2670115@ 60801016: 81600 | 007 ㅁ 5*1094 ㅠ 6 ㄴ 62 ㅋ 0 (60021) | ㅁ 17 ㅁ 22080176@ |  | 티 06 71119 000002800 0068 001 80215 10 (01600 페 6%045 9300-×., 2200 - 벡 옵 60169 9\1601168. |
| 6160 3 | 2801 707 60801016: |  |  |  | 306011166 016 10080070 800 0416 11608146 27611 107 0416 11168 10 016 600118478000 80116. 00 11870\8176 416 08016 01 |
| (0020 | 31600 ㅁ 219-22 ㅋ 00176) | * | 5600 ㄴ ㄷ 1251: ㅁ 7 ㅇ 0 프 219 | *1260600108 5047 201600402000, 7047 1116 6756600 080 66 01466606[ 04180 016 006 018218760 10 016 68100016. 띠 066 1 8 00606077 19 506011160 10 016 0801 1061680 01 0416 116, 016 010606077 ㅁ 8006 20496 66 10110\60 67 8 107\08170 918911 89 10110\8: 0601 118911:/0776070777. 1116 10700870 918911 15 2001 760699817 81667 8 11608100 11 15 ㅁ 0606668177 02017 \1160 90601157108 8 01260[07%. |

Step 1

Step 2

Step 3

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

160

ㅣ

|!

## Working with Configuration Files

## Information About Configuration Log

|  | 600001800 0726000 | 『00 ㅁ 056 |
|---|---|---|
| 61660 4 | 083004410 77707706/" 606801016: 81600 (6020219-22050176) # 02×1000 14 | (0600602081) 56(6 016 0086×100410 0 ㅁ 41166 01 70146 1168 0 1446 2400108 000118418000 (0 66 58760 10 016 0001184780027 : 00196. |
| 6660 5 | 14006-060100 77277770/68 | * 7116 727070206/'19 0446 008×100404 0 ㅁ 40066 01 0416 87016 1166 01 416 0000108 60001184178000 016[( 080 ㅁ 66 58760 10 14466 600118418000 87016. 1116 70086 19 1 10 14. 1116 061341[16 10. 띠 066 26【076 49108 0116 6000028600, 704 00481 60020118476 016 080 10 9060115 0446 10080070 800 1141608146 07611 107 416 1168 10 1446 60011841801070 870116. (060007081) 5616 0416 04046 1040[61006046[10784602028008117 58710 음 |
|  | 606801016: 31606 (0020219-2 ㅋ 01501476) * ㄴ 《106- ㅁ 62100 10 | 30 86701176 116 01 0416 04060[7000108 60201184780070 10 046 ' : 000118418000 87016. 1116. 777777/769 878400601( 6906011166 10\ 01160, 10 00104168, 10 84100080068117 5876 80 87016 1116 01 016 04060 70400108 60001184786000 10 0416 60011841780010 87016. 띠 066 26【076 49108 0116 6000028600, 704 00481 60020118476 016 080 0600004800 [0 9060117 0416 1008000 800 111608106 21611 10 ㅠ 1446 1166 10 016 00701184180070 87011196. |
| 6660 6 | \2166-00002015 606801016: 81606 (6020219-22010176) + 듀 노 166- 때 6006? | 트 0860166 016 600001800. 1119 01686160 67 0618416. 041600 음 4019 600004800 684966 80 8701176 (0 00047 1\160 016 : 0600000800 60055 16 060000060. |
| 61660 7 | 26010176 00008 606801016: 31606 (002 ㅁ 219-22 ㅋ 0101976) * 22001176 ㅇ 02 ㅁ 219 | 옥 8 ㅋ 69 0416 6417606[70040010 용 0001184178007 1116 (0 416 ㅇ 00118418000 8701146. 티 016 . 쪼 004.00469[ 6020118466 016 08144 66106 4810 0416 8701115@ ㅇ 0010 응 6000200800. |
| 6660 8 | (0000081) 910\ 70116 108 00008 2011 6801016: | 1219218575 016 000118408007 10 음 60100166 107 811 0416 49678. |

Step 4

Step 5

Step 6

Step 7

Step 8

## Information About Configuration Log

The configuration change logging tracks the changes that are made to the running configuration by using the data in the accounting log. This configuration log tracks the changes that are initiated only through the CLI. Only complete commands that result in the invocation of action routines are logged. The following types of entries are not logged:

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

161

| |

## Working with Configuration Files

| |

## Displaying Configuration Log Entries

- • Commands that result in a syntax error message

- • Partial commands that invoke the device help system

The configuration log tracks the changes that are initiated only through the CLI. For each configuration command that is executed, the following information is logged:

- • A configuration change sequence number

- • The line from which the command was executed

- • The name of the user that executed the command

- • The command that was executed

You can display the information from the configuration log by using the show archive log config all command

For each configuration command that is executed, the following information is logged:

- • The command that was executed

- • The name of the user that executed the command

- • A configuration change sequence number

You can display the information from the configuration log by using the show archive log config command.

## Displaying Configuration Log Entries

To display the configuration log entries, the configuration change logging provides the show archive log config all command.

## SUMMARY STEPS

1.

```cisco-ios
switch# show archive log config all
```

2. switch# show archive log config user username

3. switch# show archive log config user username first-index start-number [last-index end-number ]

## DETAILED STEPS

## Procedure

## Step 1 switch# show archive log config all

Displays the configuration log entries for all users

## Example:

```cisco-ios
switch# show archive log config all
```

INDEX LINE USER LOGGED COMMAND 1 console0 user01 | logging console 1 2 console0 user01 | logging monitor 2 3 console0 user02 | system default switchport shutdown

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

162

ㅣ

|!

## Working with Configuration Files

## Verifying the Device Configuration

| ㅇ 0 ㅁ 60160 | 1486 ㅁ 02 | | |  | 106682『206 피 9060 |
|---|---|---|---|---|
| ㅇ 0 ㅁ 80160 | 1486 ㅋ 02 | | | ㅁ ㅇ | 8 끄 46086 미 ㅁ |

4

console0

user02

| interface mgmt0

## Step 2 switch# show archive log config user username

Displays the configuration log entries for the specified username.

## Example:

The following example displays the configuration log entries for a specified username.

```cisco-ios
switch# show archive log config user user02 INDEX LINE USER LOGGED COMMAND 3 console0 user02 | system default switchport shutdown 4 console0 user02 | interface mgmt0 5 console0 user02 | no shutdown
```

- Step 3 switch# show archive log config user username first-index start-number [last-index end-number ]

Displays the configuration log entries by the index numbers. If you specify a number for the optional last-index, all the log entries with the index numbers in the range from the value entered for the start-number through the end-number for the specified user are displayed.

## Example:

The following example displays the configuration log entry numbers 4 and 5 for a user with the username, user02. The range for the first-index and last-index is 1 to 2000000000.

```cisco-ios
switch# show archive log config user user02 first-index 4 last-index 5 Last Log cleared/wrapped time is : Wed Oct 19 00:53:08 2016
```

INDEX

LINE

USER

LOGGED COMMAND

| 140808※ 4 | ㅇ 0 ㅁ 80160 | 1486 ㅋ 02 | ㅁ 0 12066522206 패 9060 |
|---|---|---|---|
| 5 | ㅇ 0 ㅁ 5016 ㅎ 0 | 1486.02 | ㅁ ㅇ 3884600 뒤 ㅁ |

## Verifying the Device Configuration

To verify the configuration, use one of the following commands:

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

163

| |

| |

## Working with Configuration Files

## Verifying the Device Configuration

| 600001800 | 『00056 |
|---|---|
|  | 808157519. 268100108 \101 (21600 페 -056 《616856 10.3(2), 54010200 165\010 18 540000060 070 (21900 페 6%348 9000 862166 5\1661168. |
| 9410\ 56420410-000108 | 1219018575 016 61800042 600118478007. 띠 066 18760 3 68660 1680176 00701184180005 876 01680160 10 016 20070108-007118. 016 540\ 5617600410-060011 용 600104800 00665 ㅁ 01 01920167 01622. 10\676, 0416 06001184000006 17601810 10080 10 0416 6680002 0255, 4001 016 60003 70070108 5630000 000001800 16 060000060. |
| 940\ 0046-562000 14070108-0 ㅇ 00118 1256-0020860 | 1219018575 016 11066[84022 \1160 016 0100108 0001184180 ㅁ 070 \88 1891 01180860. |

The following example shows sample output of show running-config command with the sanitized keyword. The sanitized configuration is used to share a configuration without exposing some configuration details.

This option masks the sensitive words in running configuration output with <removed> keyword.

```cisco-ios
switch# show running-config sanitized
```

!Command: show running-config sanitized !Running configuration last done at: Wed Oct 12 09:14:54 2022 !Time: Wed Oct 12 13:52:55 2022 version 10.3(2) Bios:version 07.69 username admin password 5 <removed> role network-admin copp profile strict snmp-server user admin network-admin auth md5 <removed> priv aes-128 <removed> localizedV2key rmon event 1 log trap <removed> description FATAL(1) owner PMON@FATAL rmon event 2 log trap <removed> description CRITICAL(2) owner PMON@CRITICAL rmon event 3 log trap <removed> description ERROR(3) owner PMON@ERROR rmon event 4 log trap <removed> description WARNING(4) owner PMON@WARNING rmon event 5 log trap <removed> description INFORMATION(5) owner PMON@INFO

version 10.3(2) Bios:version 07.69

username admin password 5 <removed> role network-admin

--More--

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

164

ㅣ

|!

## Working with Configuration Files

## Examples of Working with Configuration Files

## Examples of Working with Configuration Files

This section includes examples of working with configuration files.

## Copying Configuration Files

This example shows how to overwrite the contents of an existing configuration in NVRAM:

## switch# copy nvram:snapshot-config nvram:startup-config

> **WARNING**
> Warning: this command is going to overwrite your current startup-config. Do you wish to continue? {y/n} [y] y

This example shows how to copy a running configuration to the bootflash: file system:

```cisco-ios
switch# copy system:running-config bootflash:my-config
```

## Backing Up Configuration Files

This example shows how to back up the startup configuration to the bootflash: file system (ASCII file):

```cisco-ios
switch# copy startup-config bootflash:my-config
```

This example shows how to back up the startup configuration to the TFTP server (ASCII file):

```cisco-ios
switch# copy startup-config tftp://172.16.10.100/my-config
```

This example shows how to back up the running configuration to the bootflash: file system (ASCII file):

```cisco-ios
switch# copy running-config bootflash:my-config
```

## Rolling Back to a Previous Configuration

To roll back your configuration to a snapshot copy of a previously saved configuration, you need to perform the following steps:

1. Clear the current running image with the write erase command.

2. Restart the device with the reload command.

3. Copy the previously saved configuration file to the running configuration with the copy configuration-file running-configuration command.

4. Copy the running configuration to the start-up configuration with the copy running-config startup-config command.

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

165

| |

| |

## Rolling Back to a Previous Configuration

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

166

## Working with Configuration Files

ㅣ

1 1

C H A P T E R 11

## Nexus Switch Intersight Device Connector

This chapter contains these sections:

- • Nexus Switch Intersight Device Connector Overview, on page 167

- • Guidelines and Limitations, on page 168

- • Configuring Nexus Switch to Intersight, on page 168

- • Verifying NXDC configuration and status, on page 170

- • Claiming Nexus Switches in Intersight, on page 171

## Nexus Switch Intersight Device Connector Overview

Devices are connected to the Cisco Intersight portal through a Nexus Switch Intersight Device Connector (NXDC) that is embedded in the Cisco NX-OS image of each system.

Beginning with Cisco NX-OS Release 10.2(3)F, the Device Connector on NX-OS feature is supported which provides a secure way for the connected devices to send information and receive control instructions from the Cisco Intersight portal, using a secure Internet connection.

The NXDC is enabled by default on all Cisco Nexus series switches and it starts at boot by default, and attemptstoconnecttothecloudservice.Onceasecureconnectionhasbeenestablishedandthedeviceconnector is registered with the Intersight service, the device connector collects detailed inventory, health status and sends the adoption telemetry data to the Intersight database. Inventory is refreshed once in a day.

The NXDC supports the AutoUpdate feature where it gets automatically updated to the latest version through a refresh by the Intersight service when you connect to Intersight.

TheNXDCalsosupports theConnectedTAC featureto collecttech-supportdatafrom devicesthatareclaimed.

The NXDC feature integration was done to resolve the standalone Nexus switches with the following

capabilities:

- • It provides fast and quick solution to gather basic data from standalone Nexus switches.

- • It stores and manages private data securely in the cloud.

- • It is flexible for future capabilities and enables the ability to upgrade NXDC.

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

167

## Nexus Switch Intersight Device Connector

| |

## Guidelines and Limitations

76160061 『【16077016 5110\ 020-0601800 ^400186160 & (000000800 76 아 -540000 7607-640001 ^081/106 068080110 (060116 예 100 (060116 예 00 @ 16046 0 ㅁ 6106 (60006 여 아

## Guidelines and Limitations

NXDC has the following guidelines and limitations:

- • You must configure DNS.

- • You must ensure svc.intersight.com gets resolved and allow outbound initiated HTTPS connections on port 443.

If a proxy is required for an HTTPS connection to svc.intersight.com, the proxy can be configured in the NXDC user interface. For proxy configuration, see Configuring NXDC.

## Configuring Nexus Switch to Intersight

By default the Nexus switch attempts to connect to Cisco's Intersight. If your Nexus device does not have the ability to reach Intersight, a specific proxy for Intersight must be configured.

%

- Note

By default the Intersight feature (also known as Nexus Device Connector) is enabled.

To configure the optional parameters for the Intersight feature, follow the below steps:

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

168

ㅣ

|!

## Nexus Switch Intersight Device Connector

## Configuring Nexus Switch to Intersight

## SUMMARY STEPS

1. configure terminal

2.

(Optional) intersight proxy <proxy-name> port <proxy-port>

3.

(Optional) intersight use-vrf <vrf-name>

4.

(Optional) intersight trustpoint <trustpoint-label> [host-name]

5.

(Optional) intersight source-interface <interface>

6.

(Optional) no feature intersight

## DETAILED STEPS

Procedure

|  | 600001800 0726000 | 『00 ㅁ 056 |
|---|---|---|
| 51601 | ㅇ 0008406 (60001021 606801016: 38 뒤 1601# ㅇ 002 ㅁ 5,19456 ㄴ 6501 ㅁ 21 으 1606 (6020 조 10) 부 | 트 마 666 인 06861 00011841780070 20006. |
| 5160 2 | (0000081) 10660518106( 07035 7270301-770770> 000 < -22077= 27030200: 6801016: 81606 (60722,19) 유 10 ㄴ 662561918 250: 아 200 _ 이 이 오 . 매 아다 8080 떠 | (2001184169 016 20037 56776 107 101[67918111 6000 ㅁ 601107. ㆍ 7270301-770776: 1074 07176 3007698 07 12445 28016 01 2007 56006 ㄷ . . , * ㆍ 227030-22077: 20087 0200 740066. 1116 72008618 1-65535. 7116 061841678106 16 8080. 띠 066 12007 19 60860160 \101 0416 50182 1106096 007118478000 020 (21900 피 6×49 5\1[01169, 016 찌 츠 1)() 101160169 14118 0600118400000 800 866600066 10 0000601 \101 (21600 1016791211[ 21000. |
| 5160 3 | (0000081) 1066『518116 456- 디 다 07-770770=> 6801016: 8106 (6072219) \ 10 ㄴ 666261916 튼 466-57 뉴 5146 | 40011169 016 재 ' 0 제 츠 121, 7 0000601191[7 19 01704811 0416 50601160 0 티 016 2 061341610667918111 15 518060 10 008088614610[ 티 카 708102660806. |
| 5160 4 | (0000081) 106(66918116 1704560 ㅁ 00106 7776577707777-/000/=> /050- /4090000/ 606801016: 81606 (000219)* 10660619466 6546600106 는 6666 666 는 | (2001184169 0611011168168 107 1066761811[ 000 ㅁ 60107. , 277657207777-7/406/: (67700 08 0 ㅁ 04900101[ 18001. 07 20016 101010008000 16167 10 (77900 24609 9000 567/769 205 이 00070 000080000700 00006. |
| 5160 5 | (00002081) 10666918106( 504166-106601866 ~77770/70060=> 6801016: 31606 (60722,19) \ 10 ㄴ 66251910 ㄴ 5040206-10 ㄴ 65306 2941 ㄴ 0 | (2001184169 016 504706 106(60806 107 0000014010680 ㅁ 027. |

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

169

| |

## Nexus Switch Intersight Device Connector

| |

## Verifying NXDC configuration and status

| 06 | (0000081) 20 10004101010『518116 |  | 1216816166 016 10660919111 0000685 800 76020066 811 떼 ×12(' |
|---|---|---|---|
|  | 81660 (60722,19) ㅁ ㅇ | <602 0026 120 ㅁ ㄴ 625192 는 |  |

Step 6

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

## Nexus Switch Intersight Device Connector

## Claiming Nexus Switches in Intersight

## Claiming Nexus Switches in Intersight

To get started with using the features and functionality, you must claim the switch in an Intersight User Interface (UI).

To claim the switch in Intersight UI, use the following procedure:

- • Claim Nexus switches using Intersight UI.

To claim the connected devices in Intersight, follow the process as described in Target Claim.

- • Claim multiple Nexus switches with Ansible playbook.

To claimmultipleNexusswitchesin an automatedmannerusing Ansible,checkthedetailsin theAnsible playbook.

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

171

| |

| |

## Claiming Nexus Switches in Intersight

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

172

## Nexus Switch Intersight Device Connector

ㅣ

I N D E X

## A

alias 83–84

copy system 165 copy tftp 150–151 copy usb1 | usb2 153

## B

## D

banner motd 115–116 binary-location 51, 53 bootflash 124

## C

cd 126–127, 135 clear inactive-config 158–159 clear line 110 cli alias name cli var name 83–84 81–82 clock 87 clock protocol none 119–120 clock protocol ntp 119–120 clock protocol ptp 119–120 clock set 87, 119–120 clock summer-time 118 clock timezone 117 configure 78 configuring devices 25 using POAP 25 copy 130, 151, 155–156 copy {usb1 | usb2} 154 copy ftp 150–151 copy nvram 165 copy running-config 154–155 copy running-config {usb1 | usb2} copy running-config ftp 149 copy running-config scp 149 copy running-config sftp 149 copy running-config tftp 149 copy scp 150–151 copy sftp 150–151 copy startup-config 154–155 copy startup-config {usb1 | usb2} copy startup-config ftp 149 copy startup-config scp 149 copy startup-config sftp 149

152

152

databits 106–107 debug 124 diff-clean 91 diff-clean all-sessions 92 diff-clean all-users dir 129–130, 133 92 dir usb1 152–154 dir usb2 152–154

## E

echo 86 echo backslash-interpret 86 egrep 92 email 99–100 end 73 exec-timeout 106–108

## F

find 135 from 99–100

## G

grep 92 gunzip 133 gzip 133

## H

hostname 114–115

## I

interface

71–72

ip {ftp | http | tftp} source-interface {ethernet | loopback}

copy startup-config tftp 149

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

|

|

IN-1

ㅣ

## INDEX

## L

less 93 line console 106–107 line vty 108–109 log 124

## M

mkdir

127

move

129

## P

parity {even | none | odd} persist 97 personality 51–52 personality backup 51 ping 150–151 106–107 ping6 150–151 POAP 25, 46 setting up the network environment 46 pop 72 provisioning devices 25 using POAP 25 purge module 156 push 72 pwd 126–127, 130–131, 134–135

## R

reload 151, 155–156, 165 reply-to 99–100 rmdir 128, 143–144 run-script 85

show inactive-if-config log 158–159 show interface brief 103 show line 111 show line console 107–108 show run clock_manager 119–120 show running-config 148, 150, 153, 158 show startup-config 49, 122, 151–154, 164 show terminal show users 111 110–111, 120–121 sleep 86 slot 98 smtp-host 99–100 smtp-port sort 93 99–100 speed 107 ssh name 91 stopbits 107 switchname system 124 114–115

## T

## tail 134

tar append bootflash 137 tar append volatile 137 tar create bootflash 136 tar create volatile 136 tar extract {bootflash | volatile} 138 tar list bootflash 138 tar list volatile terminal alias 138 84 terminal color 98 terminal dont-ask 97 terminal edit-mode vi 96 terminal output xml 91 terminal redirection-mode ascii 134 terminal redirection-mode zipped 134 track 51–52

## S

sed 93 send 121 session-limit 109 set 87 show 88–89, 91, 93–94, 101 show banner motd 115–116 show cli history 95–96 show cli variables 81–82 show clock 117, 119 show clock detail 118 show email 99–100 show file 132–133 show hardware 156

## V

volatile 124 vrf management 99–100

## W

where detail 79 write erase 151, 155, 157, 165 write erase boot 158 write erase debug 158

|

|

Cisco Nexus 9000 Series NX-OS Fundamentals Configuration Guide, Release 10.6(x)

IN-2