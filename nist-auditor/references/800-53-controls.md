# NIST SP 800-53 Rev 5 — Control Families Reference

## Table of Contents
1. [Control Family Overview](#control-family-overview)
2. [Baseline Allocations](#baseline-allocations)
3. [Control Details by Family](#control-details-by-family)

## Control Family Overview

SP 800-53 Rev 5 contains **20 control families** with over 1,000 controls and enhancements.

| ID | Family | Controls | Focus |
|----|--------|----------|-------|
| AC | Access Control | 25 + enhancements | User permissions, authentication, session management |
| AT | Awareness and Training | 6 + enhancements | Security training, role-based awareness |
| AU | Audit and Accountability | 16 + enhancements | Event logging, audit review, retention |
| CA | Assessment, Authorization and Monitoring | 9 + enhancements | Security assessments, system authorization, continuous monitoring |
| CM | Configuration Management | 14 + enhancements | Baseline configs, change control, least functionality |
| CP | Contingency Planning | 13 + enhancements | Backup, recovery, continuity of operations |
| IA | Identification and Authentication | 12 + enhancements | Identity proofing, authenticator management, MFA |
| IR | Incident Response | 10 + enhancements | Detection, reporting, response procedures |
| MA | Maintenance | 7 + enhancements | System maintenance, remote maintenance controls |
| MP | Media Protection | 8 + enhancements | Media access, marking, sanitization, transport |
| PE | Physical and Environmental Protection | 23 + enhancements | Facility access, environmental controls, power |
| PL | Planning | 11 + enhancements | Security plans, rules of behavior, architecture |
| PM | Program Management | 32 + enhancements | Enterprise-wide security program management |
| PS | Personnel Security | 9 + enhancements | Screening, termination, transfers, agreements |
| PT | PII Processing and Transparency | 8 + enhancements | Privacy notices, consent, data minimization |
| RA | Risk Assessment | 10 + enhancements | Risk analysis, vulnerability scanning, threat assessment |
| SA | System and Services Acquisition | 23 + enhancements | SDLC, supply chain, developer security |
| SC | System and Communications Protection | 51 + enhancements | Boundary protection, encryption, network segmentation |
| SI | System and Information Integrity | 23 + enhancements | Flaw remediation, malware protection, monitoring |
| SR | Supply Chain Risk Management | 12 + enhancements | Supply chain controls, provenance, integrity |

## Baseline Allocations

SP 800-53B defines three baselines. The system's FIPS 199 impact level determines which baseline applies.

### Low Baseline (~155 controls)
Minimum controls for systems where loss would have **limited** adverse effect.
Key families emphasized: AC, AT, AU, CA, CM, CP, IA, IR, MA, MP, PE, PL, PS, RA, SA, SC, SI

### Moderate Baseline (~325 controls)
Controls for systems where loss would have **serious** adverse effect. Adds significant enhancements to Low baseline.
Additional emphasis: Enhanced logging (AU), stronger authentication (IA), incident response capabilities (IR), supply chain (SR)

### High Baseline (~421 controls)
Controls for systems where loss would have **severe or catastrophic** effect.
Additional emphasis: Advanced access controls (AC), redundancy (CP), penetration testing (CA), covert channel analysis (SC)

## Control Details by Family

### AC — Access Control

**AC-1: Policy and Procedures**
Develop, document, and disseminate access control policy and procedures. Review and update at organization-defined frequency.
- Low ✓ | Moderate ✓ | High ✓

**AC-2: Account Management**
Define and manage information system accounts. Includes: account types, conditions for group/role membership, authorization, monitoring, disabling.
- Low ✓ | Moderate ✓ (+ enhancements 1-5, 11-13) | High ✓ (+ enhancements 1-6, 11-13)
- Key enhancements: (1) Automated account management, (2) Automated temporary/emergency accounts, (3) Disable accounts, (4) Automated audit actions, (5) Inactivity logout

**AC-3: Access Enforcement**
Enforce approved authorizations for logical access. System enforces assigned privileges.
- Low ✓ | Moderate ✓ | High ✓

**AC-4: Information Flow Enforcement**
Enforce approved authorizations for controlling information flows within and between systems.
- Moderate ✓ | High ✓ (+ enhancements)

**AC-5: Separation of Duties**
Define and enforce separation of duties through assigned access authorizations.
- Moderate ✓ | High ✓

**AC-6: Least Privilege**
Employ the principle of least privilege. Allow only authorized access needed for assigned tasks.
- Moderate ✓ (+ enhancements 1-2, 5, 7, 9-10) | High ✓ (+ enhancements 1-5, 7, 9-10)

**AC-7: Unsuccessful Logon Attempts**
Enforce limit on consecutive invalid logon attempts. Automatically lock account or delay next attempt.
- Low ✓ | Moderate ✓ | High ✓

**AC-8: System Use Notification**
Display approved system use notification message before granting access.
- Low ✓ | Moderate ✓ | High ✓

**AC-11: Device Lock**
Prevent access by initiating device lock after organization-defined time period of inactivity.
- Moderate ✓ (+ enhancement 1) | High ✓ (+ enhancement 1)

**AC-12: Session Termination**
Automatically terminate user session after organization-defined conditions or trigger events.
- Moderate ✓ | High ✓

**AC-14: Permitted Actions Without Identification or Authentication**
Identify specific user actions permitted without identification or authentication.
- Low ✓ | Moderate ✓ | High ✓

**AC-17: Remote Access**
Establish, document, authorize, monitor, and control remote access methods.
- Low ✓ | Moderate ✓ (+ enhancements 1-4) | High ✓ (+ enhancements 1-4)

**AC-18: Wireless Access**
Establish, document, authorize, monitor, and control wireless access.
- Low ✓ | Moderate ✓ (+ enhancement 1) | High ✓ (+ enhancements 1, 4-5)

**AC-19: Access Control for Mobile Devices**
Establish usage restrictions, configuration requirements, and implementation guidance for mobile devices.
- Low ✓ | Moderate ✓ (+ enhancement 5) | High ✓ (+ enhancement 5)

**AC-20: Use of External Systems**
Establish terms and conditions for authorized use of external systems.
- Low ✓ | Moderate ✓ (+ enhancements 1-2) | High ✓ (+ enhancements 1-2)

**AC-22: Publicly Accessible Content**
Designate individuals authorized to post publicly accessible content. Review content for nonpublic information.
- Low ✓ | Moderate ✓ | High ✓

### AT — Awareness and Training

**AT-1: Policy and Procedures** — Low ✓ | Moderate ✓ | High ✓
**AT-2: Literacy Training and Awareness** — Low ✓ | Moderate ✓ (+ enhancements 2-3) | High ✓ (+ enhancements 2-3)
**AT-3: Role-Based Training** — Low ✓ | Moderate ✓ | High ✓
**AT-4: Training Records** — Low ✓ | Moderate ✓ | High ✓

### AU — Audit and Accountability

**AU-1: Policy and Procedures** — Low ✓ | Moderate ✓ | High ✓
**AU-2: Event Logging** — Low ✓ | Moderate ✓ | High ✓
Define auditable events: logon/logoff, access to objects, privilege use, security-relevant changes.
**AU-3: Content of Audit Records** — Low ✓ | Moderate ✓ (+ enhancement 1) | High ✓ (+ enhancements 1-2)
Records must contain: what, when, where, source, outcome, identity.
**AU-4: Audit Log Storage Capacity** — Low ✓ | Moderate ✓ | High ✓
**AU-5: Response to Audit Logging Process Failures** — Low ✓ | Moderate ✓ | High ✓ (+ enhancements 1-2)
**AU-6: Audit Record Review, Analysis, and Reporting** — Low ✓ | Moderate ✓ (+ enhancements 1, 3) | High ✓ (+ enhancements 1, 3, 5-6)
**AU-7: Audit Record Reduction and Report Generation** — Moderate ✓ (+ enhancement 1) | High ✓ (+ enhancement 1)
**AU-8: Time Stamps** — Low ✓ | Moderate ✓ | High ✓
**AU-9: Protection of Audit Information** — Low ✓ | Moderate ✓ (+ enhancement 4) | High ✓ (+ enhancements 2-4)
**AU-11: Audit Record Retention** — Low ✓ | Moderate ✓ | High ✓
**AU-12: Audit Record Generation** — Low ✓ | Moderate ✓ | High ✓ (+ enhancements 1, 3)

### CA — Assessment, Authorization and Monitoring

**CA-1: Policy and Procedures** — Low ✓ | Moderate ✓ | High ✓
**CA-2: Control Assessments** — Low ✓ | Moderate ✓ (+ enhancement 1) | High ✓ (+ enhancements 1-2)
**CA-3: Information Exchange** — Low ✓ | Moderate ✓ | High ✓ (+ enhancement 6)
**CA-5: Plan of Action and Milestones** — Low ✓ | Moderate ✓ | High ✓
**CA-6: Authorization** — Low ✓ | Moderate ✓ | High ✓
**CA-7: Continuous Monitoring** — Low ✓ | Moderate ✓ (+ enhancement 4) | High ✓ (+ enhancement 4)
**CA-8: Penetration Testing** — High ✓
**CA-9: Internal System Connections** — Low ✓ | Moderate ✓ | High ✓

### CM — Configuration Management

**CM-1: Policy and Procedures** — Low ✓ | Moderate ✓ | High ✓
**CM-2: Baseline Configuration** — Low ✓ | Moderate ✓ (+ enhancements 2, 7) | High ✓ (+ enhancements 2, 7)
**CM-3: Configuration Change Control** — Moderate ✓ (+ enhancements 1-2, 4, 6) | High ✓ (+ enhancements 1-2, 4, 6)
**CM-4: Impact Analyses** — Low ✓ | Moderate ✓ | High ✓ (+ enhancements 1-2)
**CM-5: Access Restrictions for Change** — Moderate ✓ | High ✓
**CM-6: Configuration Settings** — Low ✓ | Moderate ✓ | High ✓ (+ enhancements 1-2)
**CM-7: Least Functionality** — Low ✓ | Moderate ✓ (+ enhancements 1-2) | High ✓ (+ enhancements 1-2, 5)
**CM-8: System Component Inventory** — Low ✓ | Moderate ✓ (+ enhancements 1, 3) | High ✓ (+ enhancements 1-5)
**CM-9: Configuration Management Plan** — Moderate ✓ | High ✓
**CM-10: Software Usage Restrictions** — Low ✓ | Moderate ✓ | High ✓
**CM-11: User-Installed Software** — Low ✓ | Moderate ✓ | High ✓
**CM-12: Information Location** — Moderate ✓ | High ✓

### CP — Contingency Planning

**CP-1: Policy and Procedures** — Low ✓ | Moderate ✓ | High ✓
**CP-2: Contingency Plan** — Low ✓ | Moderate ✓ (+ enhancements 1, 3, 8) | High ✓ (+ enhancements 1-5, 8)
**CP-3: Contingency Training** — Low ✓ | Moderate ✓ (+ enhancement 1) | High ✓ (+ enhancements 1-2)
**CP-4: Contingency Plan Testing** — Low ✓ | Moderate ✓ (+ enhancement 1) | High ✓ (+ enhancements 1-2)
**CP-6: Alternate Storage Site** — Moderate ✓ (+ enhancements 1, 3) | High ✓ (+ enhancements 1-3)
**CP-7: Alternate Processing Site** — Moderate ✓ (+ enhancements 1-3) | High ✓ (+ enhancements 1-4, 6)
**CP-8: Telecommunications Services** — Moderate ✓ (+ enhancements 1-2) | High ✓ (+ enhancements 1-4)
**CP-9: System Backup** — Low ✓ | Moderate ✓ (+ enhancement 1) | High ✓ (+ enhancements 1, 5, 8)
**CP-10: System Recovery and Reconstitution** — Low ✓ | Moderate ✓ (+ enhancement 2) | High ✓ (+ enhancements 2, 4)

### IA — Identification and Authentication

**IA-1: Policy and Procedures** — Low ✓ | Moderate ✓ | High ✓
**IA-2: Identification and Authentication (Organizational Users)** — Low ✓ | Moderate ✓ (+ enhancements 1-2, 8, 12) | High ✓ (+ enhancements 1-2, 5-6, 8, 12)
Enhancement 1: Multi-factor authentication to privileged accounts
Enhancement 2: Multi-factor authentication to non-privileged accounts
**IA-3: Device Identification and Authentication** — Moderate ✓ | High ✓
**IA-4: Identifier Management** — Low ✓ | Moderate ✓ (+ enhancement 4) | High ✓ (+ enhancement 4)
**IA-5: Authenticator Management** — Low ✓ | Moderate ✓ (+ enhancements 1-2, 6) | High ✓ (+ enhancements 1-2, 6)
**IA-6: Authentication Feedback** — Low ✓ | Moderate ✓ | High ✓
**IA-7: Cryptographic Module Authentication** — Low ✓ | Moderate ✓ | High ✓
**IA-8: Identification and Authentication (Non-Organizational Users)** — Low ✓ | Moderate ✓ (+ enhancements 1-2, 4) | High ✓ (+ enhancements 1-2, 4)
**IA-11: Re-authentication** — Low ✓ | Moderate ✓ | High ✓
**IA-12: Identity Proofing** — Moderate ✓ (+ enhancements 2-3, 5) | High ✓ (+ enhancements 2-3, 5)

### IR — Incident Response

**IR-1: Policy and Procedures** — Low ✓ | Moderate ✓ | High ✓
**IR-2: Incident Response Training** — Low ✓ | Moderate ✓ | High ✓ (+ enhancements 1-2)
**IR-3: Incident Response Testing** — Moderate ✓ (+ enhancement 2) | High ✓ (+ enhancements 2-3)
**IR-4: Incident Handling** — Low ✓ | Moderate ✓ (+ enhancement 1) | High ✓ (+ enhancements 1, 4, 11)
**IR-5: Incident Monitoring** — Low ✓ | Moderate ✓ (+ enhancement 1) | High ✓ (+ enhancement 1)
**IR-6: Incident Reporting** — Low ✓ | Moderate ✓ (+ enhancement 1) | High ✓ (+ enhancements 1, 3)
**IR-7: Incident Response Assistance** — Low ✓ | Moderate ✓ (+ enhancement 1) | High ✓ (+ enhancement 1)
**IR-8: Incident Response Plan** — Low ✓ | Moderate ✓ | High ✓

### MA — Maintenance

**MA-1: Policy and Procedures** — Low ✓ | Moderate ✓ | High ✓
**MA-2: Controlled Maintenance** — Low ✓ | Moderate ✓ | High ✓ (+ enhancement 2)
**MA-3: Maintenance Tools** — Moderate ✓ (+ enhancements 1-2) | High ✓ (+ enhancements 1-3)
**MA-4: Nonlocal Maintenance** — Low ✓ | Moderate ✓ | High ✓ (+ enhancements 1, 3)
**MA-5: Maintenance Personnel** — Low ✓ | Moderate ✓ | High ✓ (+ enhancement 1)

### MP — Media Protection

**MP-1: Policy and Procedures** — Low ✓ | Moderate ✓ | High ✓
**MP-2: Media Access** — Low ✓ | Moderate ✓ | High ✓
**MP-3: Media Marking** — Moderate ✓ | High ✓
**MP-4: Media Storage** — Moderate ✓ | High ✓
**MP-5: Media Transport** — Moderate ✓ | High ✓ (+ enhancement 4)
**MP-6: Media Sanitization** — Low ✓ | Moderate ✓ | High ✓ (+ enhancements 1-3)
**MP-7: Media Use** — Low ✓ | Moderate ✓ (+ enhancement 1) | High ✓ (+ enhancement 1)

### PE — Physical and Environmental Protection

**PE-1 through PE-23** — Physical access controls, visitor management, environmental protections (temperature, humidity, water, fire), power supply, emergency shutoff, delivery/removal controls.
Key controls: PE-2 (Physical Access Authorizations), PE-3 (Physical Access Control), PE-6 (Monitoring Physical Access), PE-8 (Visitor Access Records), PE-13 (Fire Protection), PE-14 (Environmental Controls)

### PL — Planning

**PL-1: Policy and Procedures** — Low ✓ | Moderate ✓ | High ✓
**PL-2: System Security and Privacy Plans** — Low ✓ | Moderate ✓ | High ✓
**PL-4: Rules of Behavior** — Low ✓ | Moderate ✓ (+ enhancement 1) | High ✓ (+ enhancement 1)
**PL-10: Baseline Selection** — Low ✓ | Moderate ✓ | High ✓
**PL-11: Baseline Tailoring** — Low ✓ | Moderate ✓ | High ✓

### PM — Program Management

**PM-1 through PM-32** — Organization-wide program management controls. Not allocated to baselines (these are organizational-level). Includes: PM-1 (Information Security Program Plan), PM-2 (Information Security Program Leadership Role), PM-9 (Risk Management Strategy), PM-10 (Authorization Process), PM-11 (Mission/Business Process Definition), PM-14 (Testing, Training, and Monitoring), PM-30 (Supply Chain Risk Management Strategy).

### PS — Personnel Security

**PS-1 through PS-9** — Personnel screening, termination, transfers, access agreements, third-party personnel.
All in Low, Moderate, and High baselines.

### PT — PII Processing and Transparency

**PT-1 through PT-8** — Privacy notices, consent, purpose specification, data minimization, use limitation, quality, data integrity.
Moderate: PT-1 through PT-4 | High: PT-1 through PT-4

### RA — Risk Assessment

**RA-1: Policy and Procedures** — Low ✓ | Moderate ✓ | High ✓
**RA-2: Security Categorization** — Low ✓ | Moderate ✓ | High ✓
**RA-3: Risk Assessment** — Low ✓ | Moderate ✓ (+ enhancement 1) | High ✓ (+ enhancement 1)
**RA-5: Vulnerability Monitoring and Scanning** — Low ✓ | Moderate ✓ (+ enhancements 2, 5, 11) | High ✓ (+ enhancements 2-4, 5, 11)
**RA-7: Risk Response** — Low ✓ | Moderate ✓ | High ✓
**RA-9: Criticality Analysis** — High ✓

### SA — System and Services Acquisition

Key controls: SA-2 (Resource Allocation), SA-3 (System Development Life Cycle), SA-4 (Acquisition Process — security requirements in contracts), SA-5 (System Documentation), SA-8 (Security and Privacy Engineering Principles), SA-9 (External System Services), SA-10 (Developer Configuration Management), SA-11 (Developer Testing and Evaluation), SA-22 (Unsupported System Components)

### SC — System and Communications Protection

Key controls: SC-1 (Policy), SC-2 (Separation of System and User Functionality), SC-4 (Information in Shared System Resources), SC-5 (Denial-of-Service Protection), SC-7 (Boundary Protection — firewalls, DMZ, proxies), SC-8 (Transmission Confidentiality and Integrity — encryption in transit), SC-10 (Network Disconnect), SC-12 (Cryptographic Key Establishment and Management), SC-13 (Cryptographic Protection), SC-15 (Collaborative Computing Devices), SC-17 (PKI Certificates), SC-18 (Mobile Code), SC-20 (Secure Name/Address Resolution — DNSSEC), SC-23 (Session Authenticity), SC-28 (Protection of Information at Rest)

### SI — System and Information Integrity

Key controls: SI-1 (Policy), SI-2 (Flaw Remediation — patching), SI-3 (Malicious Code Protection — AV/EDR), SI-4 (System Monitoring — IDS/IPS, SIEM), SI-5 (Security Alerts, Advisories, and Directives), SI-7 (Software, Firmware, and Information Integrity — integrity verification), SI-10 (Information Input Validation), SI-12 (Information Management and Retention)

### SR — Supply Chain Risk Management

Key controls: SR-1 (Policy), SR-2 (Supply Chain Risk Management Plan), SR-3 (Supply Chain Controls and Processes), SR-5 (Acquisition Strategies, Tools, and Methods), SR-6 (Supplier Assessments and Reviews), SR-8 (Notification Agreements), SR-11 (Component Authenticity)
- Moderate ✓ (SR-1 through SR-3, SR-5, SR-6, SR-8, SR-11) | High ✓ (same + enhancements)
