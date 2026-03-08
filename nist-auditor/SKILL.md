---
name: nist-auditor
description: "Comprehensive NIST cybersecurity audit skill for conducting structured assessments against NIST frameworks. Use when Claude needs to: (1) Conduct NIST 800-53 control assessments, (2) Perform NIST CSF gap analyses, (3) Assess NIST 800-171 CUI compliance, (4) Evaluate NIST AI RMF alignment, (5) Generate System Security Plans (SSPs), Plans of Action & Milestones (POA&Ms), or audit report decks, (6) Map controls across NIST frameworks and to ISO 27001 or CMMC, (7) Determine FIPS 199 impact levels, (8) Tailor control baselines, or any NIST compliance and audit tasks. Triggers on keywords: NIST audit, NIST assessment, 800-53, 800-171, NIST CSF, cybersecurity framework, control assessment, FIPS 199, FedRAMP, FISMA, system security plan, SSP, POA&M, plan of action, NIST compliance, security controls, control baseline, AI RMF, CMMC mapping, NIST gap analysis, RMF, risk management framework."
---

# NIST Auditor Skill

## Overview

Conducts structured cybersecurity audits against NIST frameworks. Guides through scoping, control selection, evidence planning, assessment, risk scoring, cross-framework mapping, and deliverable generation.

This skill covers four NIST frameworks:
- **SP 800-53 Rev 5** — Security and privacy controls (20 families, 1000+ controls)
- **SP 800-171 Rev 2** — Protecting CUI in non-federal systems (14 families, 110 controls)
- **NIST CSF 2.0** — Cybersecurity Framework (6 functions, 22 categories)
- **NIST AI RMF** — AI Risk Management Framework (4 functions, 19 categories)

## Workflow

### Step 1: Framework Selection

Ask: **"Which NIST framework should this audit assess against?"**

Present options:
- SP 800-53 Rev 5 (federal systems, FedRAMP, FISMA)
- SP 800-171 Rev 2 (defense contractors, CUI protection, CMMC)
- NIST CSF 2.0 (voluntary, industry-agnostic cybersecurity posture)
- NIST AI RMF (AI system governance and trustworthiness)
- Multiple / Cross-framework (map across frameworks)

If the user is unsure, ask about their context:
- Federal agency or contractor? → 800-53 or 800-171
- Private sector improving security posture? → CSF
- Building or deploying AI systems? → AI RMF
- Defense supply chain? → 800-171 + CMMC mapping

Load the relevant reference file from `references/`:
- 800-53 → [references/800-53-controls.md](references/800-53-controls.md)
- 800-171 → [references/800-171-controls.md](references/800-171-controls.md)
- CSF → [references/csf-functions.md](references/csf-functions.md)
- AI RMF → [references/ai-rmf.md](references/ai-rmf.md)

### Step 2: Scope Definition

Gather the following:

**Entity identification:**
- Organization or system name
- System type (general support system, major application, cloud service, AI system)
- System boundary description (what's in scope, what's inherited, what's out of scope)

**Impact classification (for 800-53 audits):**

Use FIPS 199 to determine impact level across three security objectives:

| Objective | Low | Moderate | High |
|---|---|---|---|
| **Confidentiality** | Limited adverse effect | Serious adverse effect | Severe/catastrophic effect |
| **Integrity** | Limited adverse effect | Serious adverse effect | Severe/catastrophic effect |
| **Availability** | Limited adverse effect | Serious adverse effect | Severe/catastrophic effect |

The overall system impact level = the HIGH WATER MARK (highest rating across all three objectives).

This determines the baseline: Low (155 controls), Moderate (325 controls), or High (421 controls).

Ask: **"What is the FIPS 199 categorization for this system? If unknown, describe the data types processed and I'll help determine the appropriate impact level."**

**For 800-171:** Scope is any non-federal system that processes, stores, or transmits CUI.
**For CSF:** Scope is the organizational cybersecurity program or a defined business unit.
**For AI RMF:** Scope is a specific AI system or the organization's AI governance program.

### Step 3: Control Baseline & Tailoring

**For 800-53:** Select the appropriate baseline (Low/Moderate/High) per SP 800-53B. Then apply tailoring:
- **Common controls** — Inherited from the organization or shared infrastructure
- **System-specific controls** — Implemented by the system owner
- **Hybrid controls** — Partially inherited, partially system-specific
- **Compensating controls** — Alternative controls that achieve equivalent protection
- **Scoping exclusions** — Controls not applicable due to system characteristics

Ask: **"Are there any controls you know are inherited from shared infrastructure, or any control families you want to exclude from scope? Do you have an existing SSP or prior audit results I can reference?"**

**For 800-171:** All 110 controls apply to any system handling CUI. No tailoring is permitted, but organizations can document compensating controls via POA&Ms.

**For CSF and AI RMF:** All categories are assessed. The organization sets its own target maturity per category.

### Step 4: Evidence Collection Planning

For each in-scope control family, generate an evidence request matrix. See [references/assessment-procedures.md](references/assessment-procedures.md) for the 800-53A assessment methodology.

Evidence types by method:
- **Examine** — Policies, procedures, plans, system documentation, configurations, logs, diagrams
- **Interview** — System owners, administrators, security officers, users, developers
- **Test** — Vulnerability scans, penetration tests, configuration checks, access reviews, backup restoration

Present the evidence request list organized by control family. For each family, specify:
1. Required documents (policies, procedures, plans)
2. Technical evidence (configurations, logs, scan results)
3. Interview subjects and key questions
4. Tests to perform or observe

Ask: **"Would you like me to generate the full evidence request matrix, or focus on specific control families?"**

### Step 5: Control Assessment

Walk through each control systematically. For each control, capture:

**Implementation status:**
| Status | Definition |
|---|---|
| **Implemented** | Fully in place and operating as intended |
| **Partially Implemented** | Some aspects in place, gaps remain |
| **Planned** | Not yet implemented, scheduled for future |
| **Alternative** | Compensating control in place |
| **Not Implemented** | No implementation, no plan |

**Assessment dimensions:**
- **Implementation** — Is the control documented and deployed?
- **Effectiveness** — Does the control achieve its security objective? Evidence of testing?
- **Maturity** — Is the control repeatable, measured, and continuously improved?

**Maturity scale (for CSF and general use):**

| Level | Description |
|---|---|
| 1 - Initial | Ad hoc, reactive, undocumented |
| 2 - Repeatable | Documented but inconsistently followed |
| 3 - Defined | Standardized, consistently implemented |
| 4 - Managed | Measured, monitored, reviewed periodically |
| 5 - Optimized | Continuously improved based on metrics |

For each finding, record: Control ID, title, status, evidence reviewed, gaps identified, and auditor notes.

Ask: **"Shall I walk through controls one family at a time, or would you prefer to provide your assessment data in bulk (e.g., from a spreadsheet or existing SSP)?"**

### Step 6: Risk Scoring

For each gap or deficiency identified in Step 5, score the risk.

If the risk-assessment skill is available, invoke it for 5x5 matrix scoring of inherent and residual risk per finding. If not, apply this simplified scoring:

**Likelihood (1-5):**
1. Rare — Requires significant effort/resources to exploit
2. Unlikely — Possible but not expected under normal conditions
3. Possible — Could occur during the assessment period
4. Likely — Expected to occur without remediation
5. Almost Certain — Actively exploited or trivially exploitable

**Impact (1-5):**
1. Negligible — Minimal effect on operations
2. Minor — Limited degradation of capability
3. Moderate — Significant degradation, partial loss of mission
4. Major — Major damage to organizational operations or assets
5. Critical — Complete loss of confidentiality, integrity, or availability

**Risk Score** = Likelihood × Impact

| Score Range | Risk Level | Response |
|---|---|---|
| 1-4 | Low | Accept or monitor |
| 5-9 | Medium | Mitigate within 180 days |
| 10-15 | High | Mitigate within 90 days |
| 16-25 | Critical | Immediate action required |

### Step 7: Cross-Framework Mapping

If the user needs multi-framework alignment, consult [references/crosswalks.md](references/crosswalks.md).

Common mapping scenarios:
- **800-53 ↔ CSF** — Map specific controls to CSF functions/categories
- **800-53 ↔ ISO 27001** — For organizations with dual compliance needs
- **800-171 ↔ CMMC** — Map CUI controls to CMMC levels
- **800-53 ↔ AI RMF** — Map AI-specific controls using NIST's AI overlay

Ask: **"Do you need findings mapped to any additional frameworks (ISO 27001, CMMC, SOC 2, HIPAA)?"**

### Step 8: Deliverable Generation

Always produce deliverables based on the audit scope. Offer the following:

**Core deliverables (always generate):**
1. **Audit Summary Report** — Executive summary, methodology, key findings, risk scores
2. **Control Assessment Worksheet** — Detailed per-control findings (xlsx)
3. **POA&M** — Plan of Action & Milestones for all open findings (xlsx)

**Extended deliverables (offer based on context):**
4. **Executive Presentation** — Audit findings deck (pptx) — use the pptx skill
5. **System Security Plan (SSP)** — Full or updated SSP (docx) — use the docx skill
6. **Risk Heat Map** — Visual 5x5 matrix with findings plotted

**Presentation structure** (when generating a deck):
1. Title — Audit name, entity, framework, date
2. Executive Summary — Overall posture, critical findings count, risk distribution
3. Scope & Methodology — System boundary, impact level, assessment approach
4. Findings by Control Family — Grouped findings with status and risk
5. Risk Matrix — 5x5 heat map with finding placement
6. POA&M Summary — Top priority items, owners, timelines
7. Cross-Framework Mapping — If applicable
8. Recommendations — Prioritized remediation roadmap
9. Next Steps — Timeline, responsibilities, reassessment schedule

Ask: **"Which deliverables should I generate? I'll always produce the assessment worksheet and POA&M. Would you also like an executive presentation or SSP?"**

### Step 9: Publication & Sharing

Ask: **"Should any deliverables be shared via connected services?"**

If connectors are enabled, offer: Google Drive, Notion, Slack, email distribution.
Otherwise: save locally and provide download links.

## Assessment Tips

- When assessing inherited controls, verify the inheritance chain — don't assume parent organization controls are effective without evidence
- For cloud systems, distinguish between provider responsibilities (IaaS/PaaS/SaaS) and customer responsibilities
- Document compensating controls thoroughly — they must achieve equivalent protection to the original control
- POA&M items need realistic milestones — don't set 30-day remediation for controls requiring procurement or architecture changes
- For 800-171 assessments, track compliance against the 110 controls using the NIST SP 800-171A assessment procedures
- For AI systems, consider both the AI-specific risks (bias, transparency, robustness) and the underlying IT infrastructure controls
