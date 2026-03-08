# Assessment Procedures Reference (SP 800-53A Rev 5)

## Overview

SP 800-53A provides a methodology for assessing the implementation and effectiveness of security and privacy controls. It defines assessment objectives, methods, and objects for each control in SP 800-53.

## Assessment Methods

Three methods are used, often in combination:

### Examine
Review, inspect, observe, study, or analyze assessment objects (specifications, mechanisms, activities).

**Specification objects:** Policies, procedures, plans, system security plans, system design documentation, configuration settings, rules of behavior, service level agreements, contracts, memoranda of understanding.

**Mechanism objects:** Hardware, software, firmware — access control lists, firewall rules, encryption implementations, audit log configurations, IDS/IPS settings, authentication mechanisms.

**Activity objects:** System operations, administration, management, exercises — backup procedures, account management processes, configuration change processes, contingency plan exercises.

### Interview
Conduct discussions with individuals or groups to facilitate understanding, achieve clarification, or obtain evidence.

**Typical interview subjects by control family:**

| Family | Interview Subjects |
|--------|--------------------|
| AC | System administrators, security officers, account managers |
| AT | Training managers, supervisors, end users |
| AU | System administrators, SIEM operators, security analysts |
| CA | Authorizing officials, assessors, system owners |
| CM | Configuration managers, change control board members, system administrators |
| CP | Contingency plan coordinators, system owners, backup administrators |
| IA | Identity management administrators, PKI administrators |
| IR | Incident response team leads, SOC analysts, CISO |
| MA | Maintenance personnel, facility managers |
| MP | Media custodians, records managers |
| PE | Facility security officers, physical security staff |
| PL | System owners, security planners, architects |
| PM | CISO, risk management officers, program managers |
| PS | HR managers, security officers, supervisors |
| PT | Privacy officers, data stewards, legal counsel |
| RA | Risk analysts, vulnerability management staff, threat intelligence analysts |
| SA | Acquisition/procurement officers, developers, architects |
| SC | Network engineers, cryptographic administrators, security architects |
| SI | Patch management staff, AV/EDR administrators, security monitoring analysts |
| SR | Supply chain risk managers, vendor management, procurement officers |

### Test
Exercise assessment objects under specified conditions to compare actual with expected behavior.

**Common test activities by control family:**

| Family | Test Activities |
|--------|----------------|
| AC | Attempt unauthorized access, verify account lockout, test session timeout, validate role-based access |
| AU | Verify log generation, confirm log protection, test log alerting, review log content completeness |
| CM | Compare configurations against baselines, verify change control process, test least functionality |
| CP | Restore from backup, exercise contingency plan, test failover, verify recovery time objectives |
| IA | Test MFA enforcement, verify password complexity, attempt credential replay, test identity proofing |
| IR | Conduct tabletop exercise, test incident detection, verify reporting procedures, test containment procedures |
| RA | Run vulnerability scans, review scan results handling, verify remediation timelines |
| SC | Test encryption implementation, verify boundary protection, conduct network segmentation tests |
| SI | Verify patching compliance, test malware detection, confirm monitoring effectiveness |

## Evidence Collection Matrix Template

For each control being assessed, document:

```
Control ID: [e.g., AC-2]
Control Title: [e.g., Account Management]
Assessment Objective: [from 800-53A]

Examine:
  - [ ] Policy document: [name, version, date]
  - [ ] Procedure document: [name, version, date]
  - [ ] System configuration: [screenshot/export]
  - [ ] Audit logs: [sample period]

Interview:
  - [ ] [Role]: [Name] — [Key questions]
  - [ ] [Role]: [Name] — [Key questions]

Test:
  - [ ] [Test description]: [Expected result] → [Actual result]
  - [ ] [Test description]: [Expected result] → [Actual result]

Finding:
  Status: [Implemented | Partially Implemented | Planned | Alternative | Not Implemented]
  Evidence: [Summary of evidence reviewed]
  Gaps: [Deficiencies identified]
  Risk: [Likelihood x Impact = Score]
  Notes: [Auditor observations]
```

## Assessment Depth and Coverage

### Depth
How thoroughly each assessment object is examined, interviewed, or tested.

| Depth | Description | When to Use |
|-------|-------------|-------------|
| Basic | Focused review, limited sampling, high-level interviews | Low-impact systems, initial assessments |
| Focused | Detailed review, representative sampling, specific interviews | Moderate-impact systems, periodic assessments |
| Comprehensive | Exhaustive review, complete coverage, in-depth interviews | High-impact systems, authorization assessments |

### Coverage
How many assessment objects are included.

| Coverage | Description | When to Use |
|----------|-------------|-------------|
| Basic | Review representative sample of objects | Low-impact systems |
| Focused | Review larger sample, include key objects | Moderate-impact systems |
| Comprehensive | Review all or nearly all objects | High-impact systems, critical controls |

## Control Assessment Workflow

1. **Prepare** — Gather prior assessment results, SSP, POA&M, and system documentation
2. **Conduct** — Execute examination, interview, and test procedures for each control
3. **Document** — Record findings using the evidence collection matrix
4. **Determine** — Make a finding for each assessment objective (Satisfied or Other Than Satisfied)
5. **Report** — Compile assessment results into the Security Assessment Report (SAR)
6. **Recommend** — Provide recommendations for remediating findings rated Other Than Satisfied

## Assessment Objectives Structure

Each control has assessment objectives structured as:

**Determine if the organization:**
- [a] Defines [parameter] as required by the control
- [b] Documents [artifact] in accordance with the control
- [c] Implements [mechanism] as specified
- [d] [Action] is performed at the organization-defined frequency

For parameterized controls (those with organization-defined values), verify:
1. The organization has defined the parameter value
2. The parameter value is reasonable and documented
3. The control is implemented using the defined parameter value
