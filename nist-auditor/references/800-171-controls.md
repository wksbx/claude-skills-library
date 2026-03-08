# NIST SP 800-171 Rev 2 — CUI Protection Controls Reference

## Overview

SP 800-171 provides requirements for protecting Controlled Unclassified Information (CUI) in non-federal systems and organizations. It contains **110 security requirements** organized into **14 families**. All requirements are mandatory for systems handling CUI — there is no baseline tailoring.

800-171 requirements are derived from NIST SP 800-53 Moderate baseline controls, adapted for non-federal environments.

## Control Families

### 3.1 — Access Control (22 requirements)

| ID | Requirement |
|----|-------------|
| 3.1.1 | Limit system access to authorized users, processes, and devices |
| 3.1.2 | Limit system access to authorized transaction types and functions |
| 3.1.3 | Control CUI flow in accordance with approved authorizations |
| 3.1.4 | Separate duties of individuals to reduce risk of malicious activity |
| 3.1.5 | Employ principle of least privilege, including for specific security functions and privileged accounts |
| 3.1.6 | Use non-privileged accounts when accessing nonsecurity functions |
| 3.1.7 | Prevent non-privileged users from executing privileged functions; audit execution |
| 3.1.8 | Limit unsuccessful logon attempts |
| 3.1.9 | Provide privacy and security notices consistent with applicable CUI rules |
| 3.1.10 | Use session lock with pattern-hiding displays |
| 3.1.11 | Terminate user sessions automatically after defined conditions |
| 3.1.12 | Monitor and control remote access sessions |
| 3.1.13 | Employ cryptographic mechanisms to protect confidentiality of remote access sessions |
| 3.1.14 | Route remote access via managed access control points |
| 3.1.15 | Authorize remote execution of privileged commands and access to security-relevant info |
| 3.1.16 | Authorize wireless access prior to allowing connections |
| 3.1.17 | Protect wireless access using authentication and encryption |
| 3.1.18 | Control connection of mobile devices |
| 3.1.19 | Encrypt CUI on mobile devices and mobile computing platforms |
| 3.1.20 | Verify and control/limit connections to and use of external systems |
| 3.1.21 | Limit use of portable storage devices on external systems |
| 3.1.22 | Control CUI posted or processed on publicly accessible systems |

### 3.2 — Awareness and Training (3 requirements)

| ID | Requirement |
|----|-------------|
| 3.2.1 | Ensure managers, systems administrators, and users are aware of security risks and applicable policies |
| 3.2.2 | Ensure personnel are trained to carry out assigned information security-related duties |
| 3.2.3 | Provide security awareness training on recognizing and reporting potential indicators of insider threat |

### 3.3 — Audit and Accountability (9 requirements)

| ID | Requirement |
|----|-------------|
| 3.3.1 | Create and retain system audit logs and records |
| 3.3.2 | Ensure actions of individual users can be uniquely traced for accountability |
| 3.3.3 | Review and update logged events |
| 3.3.4 | Alert on audit logging process failures |
| 3.3.5 | Correlate audit record review, analysis, and reporting for investigation and response |
| 3.3.6 | Provide audit record reduction and report generation to support analysis |
| 3.3.7 | Provide system capability to compare and synchronize internal clocks |
| 3.3.8 | Protect audit information and audit logging tools from unauthorized access, modification, and deletion |
| 3.3.9 | Limit management of audit logging functionality to a subset of privileged users |

### 3.4 — Configuration Management (9 requirements)

| ID | Requirement |
|----|-------------|
| 3.4.1 | Establish and maintain baseline configurations and inventories of systems |
| 3.4.2 | Establish and enforce security configuration settings |
| 3.4.3 | Track, review, approve/disapprove, and log changes to systems |
| 3.4.4 | Analyze security impact of changes prior to implementation |
| 3.4.5 | Define, document, approve, and enforce physical and logical access restrictions |
| 3.4.6 | Employ principle of least functionality by configuring systems to provide only essential capabilities |
| 3.4.7 | Restrict, disable, or prevent use of nonessential programs, functions, ports, protocols, and services |
| 3.4.8 | Apply deny-by-exception (blacklisting) policy to prevent use of unauthorized software; or employ allow-by-exception (whitelisting) to allow execution of authorized software |
| 3.4.9 | Control and monitor user-installed software |

### 3.5 — Identification and Authentication (11 requirements)

| ID | Requirement |
|----|-------------|
| 3.5.1 | Identify system users, processes acting on behalf of users, and devices |
| 3.5.2 | Authenticate identities of users, processes, and devices as a prerequisite to access |
| 3.5.3 | Use multifactor authentication for local and network access to privileged accounts and for network access to non-privileged accounts |
| 3.5.4 | Employ replay-resistant authentication mechanisms for network access to privileged and non-privileged accounts |
| 3.5.5 | Prevent reuse of identifiers for a defined period |
| 3.5.6 | Disable identifiers after a defined period of inactivity |
| 3.5.7 | Enforce minimum password complexity and change of characters when new passwords are created |
| 3.5.8 | Prohibit password reuse for a specified number of generations |
| 3.5.9 | Allow temporary password use for system logons with immediate change to permanent password |
| 3.5.10 | Store and transmit only cryptographically-protected passwords |
| 3.5.11 | Obscure feedback of authentication information |

### 3.6 — Incident Response (3 requirements)

| ID | Requirement |
|----|-------------|
| 3.6.1 | Establish operational incident-handling capability including preparation, detection, analysis, containment, recovery, and user response |
| 3.6.2 | Track, document, and report incidents to designated officials and/or authorities |
| 3.6.3 | Test the organizational incident response capability |

### 3.7 — Maintenance (6 requirements)

| ID | Requirement |
|----|-------------|
| 3.7.1 | Perform maintenance on organizational systems |
| 3.7.2 | Provide controls on tools, techniques, mechanisms, and personnel for maintenance |
| 3.7.3 | Ensure equipment removed for off-site maintenance is sanitized |
| 3.7.4 | Check media containing diagnostic and test programs for malicious code |
| 3.7.5 | Require multifactor authentication for remote maintenance sessions and terminate when complete |
| 3.7.6 | Supervise maintenance activities of personnel without required access authorization |

### 3.8 — Media Protection (9 requirements)

| ID | Requirement |
|----|-------------|
| 3.8.1 | Protect (control access to, mark, store) system media containing CUI, both paper and digital |
| 3.8.2 | Limit access to CUI on system media to authorized users |
| 3.8.3 | Sanitize or destroy system media containing CUI before disposal or release for reuse |
| 3.8.4 | Mark media with necessary CUI markings and distribution limitations |
| 3.8.5 | Control access to media containing CUI and maintain accountability during transport |
| 3.8.6 | Implement cryptographic mechanisms to protect confidentiality of CUI stored on digital media during transport |
| 3.8.7 | Control use of removable media on system components |
| 3.8.8 | Prohibit use of portable storage devices when such devices have no identifiable owner |
| 3.8.9 | Protect confidentiality of backup CUI at storage locations |

### 3.9 — Personnel Security (2 requirements)

| ID | Requirement |
|----|-------------|
| 3.9.1 | Screen individuals prior to authorizing access to systems containing CUI |
| 3.9.2 | Ensure CUI and systems containing CUI are protected during and after personnel actions such as terminations and transfers |

### 3.10 — Physical Protection (6 requirements)

| ID | Requirement |
|----|-------------|
| 3.10.1 | Limit physical access to systems, equipment, and operating environments to authorized individuals |
| 3.10.2 | Protect and monitor the physical facility and support infrastructure |
| 3.10.3 | Escort visitors and monitor visitor activity |
| 3.10.4 | Maintain audit logs of physical access |
| 3.10.5 | Control and manage physical access devices |
| 3.10.6 | Enforce safeguarding measures for CUI at alternate work sites |

### 3.11 — Risk Assessment (3 requirements)

| ID | Requirement |
|----|-------------|
| 3.11.1 | Periodically assess risk to organizational operations, assets, and individuals |
| 3.11.2 | Scan for vulnerabilities in systems and applications periodically and when new vulnerabilities are identified |
| 3.11.3 | Remediate vulnerabilities in accordance with risk assessments |

### 3.12 — Security Assessment (4 requirements)

| ID | Requirement |
|----|-------------|
| 3.12.1 | Periodically assess security controls to determine if controls are effective |
| 3.12.2 | Develop and implement plans of action to correct deficiencies and reduce/eliminate vulnerabilities |
| 3.12.3 | Monitor security controls on an ongoing basis |
| 3.12.4 | Develop, document, and periodically update system security plans |

### 3.13 — System and Communications Protection (16 requirements)

| ID | Requirement |
|----|-------------|
| 3.13.1 | Monitor, control, and protect communications at external boundaries and key internal boundaries |
| 3.13.2 | Employ architectural designs, software development techniques, and systems engineering principles that promote effective information security |
| 3.13.3 | Separate user functionality from system management functionality |
| 3.13.4 | Prevent unauthorized and unintended information transfer via shared system resources |
| 3.13.5 | Implement subnetworks for publicly accessible system components physically or logically separated from internal networks |
| 3.13.6 | Deny network communications traffic by default; allow by exception (deny all, permit by exception) |
| 3.13.7 | Prevent remote devices from simultaneously establishing non-remote connections (split tunneling) |
| 3.13.8 | Implement cryptographic mechanisms to prevent unauthorized disclosure of CUI during transmission |
| 3.13.9 | Terminate network connections at end of sessions or after defined period of inactivity |
| 3.13.10 | Establish and manage cryptographic keys for cryptography employed |
| 3.13.11 | Employ FIPS-validated cryptography when used to protect confidentiality of CUI |
| 3.13.12 | Prohibit remote activation of collaborative computing devices; provide indication of devices in use |
| 3.13.13 | Control and monitor the use of mobile code |
| 3.13.14 | Control and monitor the use of Voice over Internet Protocol (VoIP) technologies |
| 3.13.15 | Protect authenticity of communications sessions |
| 3.13.16 | Protect confidentiality of CUI at rest |

### 3.14 — System and Information Integrity (7 requirements)

| ID | Requirement |
|----|-------------|
| 3.14.1 | Identify, report, and correct system flaws in a timely manner |
| 3.14.2 | Provide protection from malicious code at designated locations within systems |
| 3.14.3 | Monitor system security alerts and advisories and take action in response |
| 3.14.4 | Update malicious code protection mechanisms when new releases are available |
| 3.14.5 | Perform periodic scans and real-time scans of files from external sources |
| 3.14.6 | Monitor systems including inbound and outbound communications traffic |
| 3.14.7 | Identify unauthorized use of systems |

## 800-171 to CMMC Mapping

800-171 requirements map directly to CMMC Level 2 practices. CMMC Level 2 requires implementation of all 110 800-171 requirements. CMMC Level 1 covers a subset (17 practices) for Federal Contract Information (FCI) only.

## 800-171 to 800-53 Traceability

Each 800-171 requirement traces back to one or more 800-53 Moderate baseline controls. For example:
- 3.1.1 (Limit system access) ← AC-2, AC-3, AC-17
- 3.5.3 (MFA) ← IA-2(1), IA-2(2)
- 3.13.8 (Encryption in transit) ← SC-8, SC-8(1)
