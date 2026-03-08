# NIST Cybersecurity Framework (CSF) 2.0 — Functions Reference

## Overview

NIST CSF 2.0 (released February 2024) provides a high-level, outcome-based framework for managing cybersecurity risk. It is organized into **6 Functions**, **22 Categories**, and **106 Subcategories**. CSF 2.0 added the Govern function and expanded applicability beyond critical infrastructure to all organizations.

## Functions and Categories

### GV — GOVERN (new in 2.0)

Establishes and monitors the organization's cybersecurity risk management strategy, expectations, and policy. Cross-cutting function that informs all other functions.

| Category | ID | Description |
|----------|----|-------------|
| Organizational Context | GV.OC | The circumstances (mission, stakeholder expectations, dependencies, legal/regulatory/contractual requirements) surrounding the organization's cybersecurity risk management decisions are understood |
| Risk Management Strategy | GV.RM | The organization's priorities, constraints, risk tolerance, and assumptions are established, communicated, and used to support operational risk decisions |
| Roles, Responsibilities, and Authorities | GV.RR | Cybersecurity roles, responsibilities, and authorities are established and communicated to foster accountability, performance assessment, and continuous improvement |
| Policy | GV.PO | Organizational cybersecurity policy is established, communicated, and enforced |
| Oversight | GV.OV | Results of organization-wide cybersecurity risk management activities and performance are used to inform, improve, and adjust the risk management strategy |
| Cybersecurity Supply Chain Risk Management | GV.SC | Cyber supply chain risk management processes are identified, established, managed, monitored, and improved |

### ID — IDENTIFY

Develop an organizational understanding to manage cybersecurity risk to systems, people, assets, data, and capabilities.

| Category | ID | Description |
|----------|----|-------------|
| Asset Management | ID.AM | Assets (data, hardware, software, systems, facilities, services, people) that enable the organization to achieve business purposes are identified and managed consistent with their relative importance to organizational objectives and risk strategy |
| Risk Assessment | ID.RA | The organization understands the cybersecurity risk to the organization, assets, and individuals |
| Improvement | ID.IM | Improvements to organizational cybersecurity risk management processes, procedures, and activities are identified across all CSF Functions |

### PR — PROTECT

Develop and implement appropriate safeguards to ensure delivery of critical services.

| Category | ID | Description |
|----------|----|-------------|
| Identity Management, Authentication, and Access Control | PR.AA | Access to physical and logical assets is limited to authorized users, services, and hardware and managed commensurate with the assessed risk |
| Awareness and Training | PR.AT | The organization's personnel are provided cybersecurity awareness and training |
| Data Security | PR.DS | Data are managed consistent with the organization's risk strategy to protect the confidentiality, integrity, and availability of information |
| Platform Security | PR.PS | The hardware, software, and services of physical and virtual platforms are managed consistent with the organization's risk strategy |
| Technology Infrastructure Resilience | PR.IR | Security architectures are managed with the organization's risk strategy to protect asset confidentiality, integrity, and availability and organizational resilience |

### DE — DETECT

Develop and implement appropriate activities to identify the occurrence of a cybersecurity event.

| Category | ID | Description |
|----------|----|-------------|
| Continuous Monitoring | DE.CM | Assets are monitored to find anomalies, indicators of compromise, and other potentially adverse events |
| Adverse Event Analysis | DE.AE | Anomalies, indicators of compromise, and other potentially adverse events are analyzed to characterize the events and detect cybersecurity incidents |

### RS — RESPOND

Develop and implement appropriate activities to take action regarding a detected cybersecurity incident.

| Category | ID | Description |
|----------|----|-------------|
| Incident Management | RS.MA | Responses to detected cybersecurity incidents are managed |
| Incident Analysis | RS.AN | Investigations are conducted to ensure effective response and support forensics and recovery activities |
| Incident Response Reporting and Communication | RS.CO | Response activities are coordinated with internal and external stakeholders as required by laws, regulations, or policies |
| Incident Mitigation | RS.MI | Activities are performed to prevent expansion of an event and mitigate its effects |

### RC — RECOVER

Develop and implement appropriate activities to maintain plans for resilience and to restore any capabilities or services that were impaired due to a cybersecurity incident.

| Category | ID | Description |
|----------|----|-------------|
| Incident Recovery Plan Execution | RC.RP | Restoration activities are performed to ensure operational availability of systems and services |
| Incident Recovery Communication | RC.CO | Restoration activities are coordinated with internal and external parties |

## Assessment Approach

### Maturity Tiers (Current and Target Profile)

CSF uses Implementation Tiers to describe the degree of rigor:

| Tier | Name | Description |
|------|------|-------------|
| Tier 1 | Partial | Risk management is ad hoc. Limited awareness of cybersecurity risk. |
| Tier 2 | Risk Informed | Risk management practices approved by management but may not be organization-wide. Some external collaboration. |
| Tier 3 | Repeatable | Organization-wide risk management practices are formally approved and expressed as policy. Regular updates based on changes in risk landscape. |
| Tier 4 | Adaptive | Organization adapts cybersecurity practices based on lessons learned and predictive indicators. Continuous improvement with advanced technologies and practices. |

### Profile-Based Assessment

1. **Create Current Profile** — Assess current state across all categories/subcategories
2. **Create Target Profile** — Define desired state based on risk appetite, regulatory requirements, and business objectives
3. **Perform Gap Analysis** — Compare current vs. target to identify improvement areas
4. **Prioritize Actions** — Rank gaps by risk impact and create implementation roadmap

### CSF to 800-53 Mapping

Each CSF subcategory maps to specific 800-53 controls. Key mappings:

| CSF Category | Primary 800-53 Families |
|---|---|
| GV.OC | PM, PL, RA |
| GV.RM | PM, RA |
| GV.SC | SR, SA |
| ID.AM | CM, PM |
| ID.RA | RA, CA |
| PR.AA | AC, IA |
| PR.AT | AT |
| PR.DS | SC, MP |
| PR.PS | CM, SI |
| DE.CM | AU, SI, CA |
| DE.AE | IR, SI |
| RS.MA | IR |
| RS.AN | IR |
| RC.RP | CP |
