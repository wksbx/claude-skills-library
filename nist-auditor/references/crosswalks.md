# Cross-Framework Mapping Reference

## Overview

Organizations often need to demonstrate compliance across multiple frameworks simultaneously. This reference provides key mappings between NIST frameworks and commonly paired standards.

## NIST 800-53 ↔ NIST CSF 2.0

| CSF Function | CSF Category | Primary 800-53 Control Families |
|---|---|---|
| **GOVERN** | GV.OC Organizational Context | PM-1, PM-7, PM-8, PM-11, PL-1, PL-2 |
| | GV.RM Risk Management Strategy | PM-9, PM-28, RA-1, RA-3 |
| | GV.RR Roles and Responsibilities | PM-2, PM-10, PM-13, PS-7 |
| | GV.PO Policy | *-1 (all family policy controls), PL-4 |
| | GV.OV Oversight | PM-6, PM-14, CA-2, CA-7 |
| | GV.SC Supply Chain RM | SR-1, SR-2, SR-3, SR-5, SR-6, SA-9, SA-12 |
| **IDENTIFY** | ID.AM Asset Management | CM-8, CM-12, PM-5, RA-2 |
| | ID.RA Risk Assessment | RA-2, RA-3, RA-5, RA-9, PM-16 |
| | ID.IM Improvement | CA-2, CA-5, CA-7, PM-4, PM-14 |
| **PROTECT** | PR.AA Access Control | AC-1 through AC-22, IA-1 through IA-12 |
| | PR.AT Awareness & Training | AT-1 through AT-4 |
| | PR.DS Data Security | SC-8, SC-13, SC-28, MP-1 through MP-7 |
| | PR.PS Platform Security | CM-1 through CM-12, SI-2, SI-7, SI-16 |
| | PR.IR Infrastructure Resilience | CP-1 through CP-13, SC-5, SC-6, SC-7 |
| **DETECT** | DE.CM Continuous Monitoring | AU-2, AU-6, AU-12, SI-4, CA-7 |
| | DE.AE Adverse Event Analysis | IR-4, IR-5, SI-4, AU-6 |
| **RESPOND** | RS.MA Incident Management | IR-1, IR-4, IR-7, IR-8 |
| | RS.AN Incident Analysis | IR-4, IR-5, AU-6, AU-7 |
| | RS.CO Communications | IR-6, IR-7 |
| | RS.MI Mitigation | IR-4, IR-5 |
| **RECOVER** | RC.RP Recovery Execution | CP-2, CP-4, CP-10 |
| | RC.CO Recovery Communication | CP-2, IR-6 |

## NIST 800-53 ↔ ISO/IEC 27001:2022

| ISO 27001 Annex A Control | NIST 800-53 Control(s) |
|---|---|
| A.5.1 Policies for information security | *-1 (all policy controls), PL-1 |
| A.5.2 Information security roles | PM-2, PM-10, PM-13 |
| A.5.3 Segregation of duties | AC-5 |
| A.5.7 Threat intelligence | PM-16, RA-3, SI-5 |
| A.5.8 Information security in project management | SA-3, SA-8, PM-7 |
| A.5.9 Inventory of information | CM-8, PM-5 |
| A.5.15 Access control | AC-1, AC-2, AC-3, AC-6 |
| A.5.16 Identity management | IA-4 |
| A.5.17 Authentication information | IA-5 |
| A.5.23 Information security for cloud services | SA-9, SC-7 |
| A.5.24 Incident management planning | IR-1, IR-8 |
| A.5.25 Assessment and decision on events | IR-4, IR-5 |
| A.5.26 Response to incidents | IR-4, IR-6 |
| A.5.27 Learning from incidents | IR-4(4) |
| A.5.28 Collection of evidence | AU-3, AU-9, AU-11 |
| A.5.29 Disruption planning | CP-1, CP-2 |
| A.5.30 ICT readiness for business continuity | CP-7, CP-8, CP-9 |
| A.5.34 Privacy and protection of PII | PT-1 through PT-8 |
| A.5.36 Compliance with policies | CA-2, PM-14 |
| A.6.1 Screening | PS-3 |
| A.6.5 Responsibilities after termination | PS-4, PS-5 |
| A.7.1 Physical security perimeters | PE-3 |
| A.7.2 Physical entry | PE-2, PE-3 |
| A.7.4 Physical security monitoring | PE-6 |
| A.8.1 User endpoint devices | AC-19, SC-28 |
| A.8.2 Privileged access rights | AC-6 |
| A.8.3 Information access restriction | AC-3, AC-4 |
| A.8.5 Secure authentication | IA-2, IA-8 |
| A.8.7 Protection against malware | SI-3 |
| A.8.8 Management of technical vulnerabilities | RA-5, SI-2 |
| A.8.9 Configuration management | CM-2, CM-6, CM-7 |
| A.8.12 Data leakage prevention | AC-4, SC-7 |
| A.8.15 Logging | AU-2, AU-3, AU-12 |
| A.8.16 Monitoring activities | SI-4, AU-6, CA-7 |
| A.8.20 Networks security | SC-7 |
| A.8.24 Use of cryptography | SC-12, SC-13 |
| A.8.25 Secure development lifecycle | SA-3, SA-11 |
| A.8.28 Secure coding | SA-11, SI-10 |
| A.8.31 Separation of environments | CM-4, SC-2 |
| A.8.32 Change management | CM-3, CM-4 |
| A.8.34 Protection during audit testing | CA-2 |

## NIST 800-171 ↔ CMMC Level 2

CMMC Level 2 practices map 1:1 with 800-171 requirements. The CMMC domain structure mirrors 800-171 families:

| CMMC Domain | 800-171 Family | Practice Count |
|---|---|---|
| Access Control (AC) | 3.1 Access Control | 22 |
| Awareness & Training (AT) | 3.2 Awareness & Training | 3 |
| Audit & Accountability (AU) | 3.3 Audit & Accountability | 9 |
| Configuration Management (CM) | 3.4 Configuration Management | 9 |
| Identification & Authentication (IA) | 3.5 Identification & Authentication | 11 |
| Incident Response (IR) | 3.6 Incident Response | 3 |
| Maintenance (MA) | 3.7 Maintenance | 6 |
| Media Protection (MP) | 3.8 Media Protection | 9 |
| Personnel Security (PS) | 3.9 Personnel Security | 2 |
| Physical Protection (PE) | 3.10 Physical Protection | 6 |
| Risk Assessment (RA) | 3.11 Risk Assessment | 3 |
| Security Assessment (CA) | 3.12 Security Assessment | 4 |
| System & Communications Protection (SC) | 3.13 System & Comms Protection | 16 |
| System & Information Integrity (SI) | 3.14 System & Info Integrity | 7 |
| **Total** | | **110** |

CMMC Level 1 requires 17 practices (subset of Level 2) for FCI-only systems.
CMMC Level 3 adds 24 additional practices from 800-172 for high-value assets.

## NIST 800-53 ↔ SOC 2 Trust Services Criteria

| SOC 2 Category | Primary 800-53 Control Families |
|---|---|
| Security (Common Criteria) | AC, AU, CC, CM, IA, IR, RA, SC, SI |
| Availability | CP, PE, SC-5 |
| Processing Integrity | SI-10, SI-7, AU |
| Confidentiality | AC-3, AC-4, MP, SC-8, SC-28 |
| Privacy | PT, UL, IP, AR |

## NIST 800-53 ↔ HIPAA Security Rule

| HIPAA Safeguard | Primary 800-53 Control Families |
|---|---|
| Administrative Safeguards | PM, AT, RA, IR, CA, PS |
| Physical Safeguards | PE, MP |
| Technical Safeguards | AC, AU, IA, SC, SI |

## Using Crosswalks in Audits

When conducting a multi-framework audit:

1. **Identify the primary framework** — Usually the one driving regulatory compliance
2. **Map controls across frameworks** — Use this reference to identify overlapping requirements
3. **Assess once, report multiple** — Evaluate the control once, then map the finding to all applicable frameworks
4. **Document framework-specific gaps** — Some frameworks have unique requirements not covered by others
5. **Present unified findings** — Show stakeholders a consolidated view with framework-specific annotations

This approach significantly reduces audit fatigue and ensures consistency across compliance programs.
