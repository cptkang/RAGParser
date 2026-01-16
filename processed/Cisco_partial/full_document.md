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