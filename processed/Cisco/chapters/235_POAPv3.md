---
title: "POAPv3"
page_start: 59
page_end: 59
level: 2
---

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