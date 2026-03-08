# NIST Auditor

A Claude Code skill for conducting structured cybersecurity audits against NIST frameworks. Guides through scoping, control selection, evidence planning, assessment, risk scoring, cross-framework mapping, and deliverable generation.

## Supported Frameworks

| Framework | Scope | Controls |
|---|---|---|
| **SP 800-53 Rev 5** | Security & privacy controls for federal systems (FISMA, FedRAMP) | 20 families, 1000+ controls |
| **SP 800-171 Rev 2** | Protecting CUI in non-federal systems (CMMC, defense contractors) | 14 families, 110 controls |
| **NIST CSF 2.0** | Cybersecurity posture (voluntary, industry-agnostic) | 6 functions, 22 categories |
| **NIST AI RMF 1.0** | AI system governance and trustworthiness | 4 functions, 19 categories |

## Audit Workflow

1. **Framework Selection** — Choose the appropriate NIST framework based on organizational context
2. **Scope Definition** — Identify the system boundary, data types, and FIPS 199 impact level
3. **Control Baseline & Tailoring** — Select the baseline (Low/Moderate/High for 800-53) and apply tailoring (inherited, compensating, excluded controls)
4. **Evidence Collection Planning** — Generate an evidence request matrix organized by control family (Examine, Interview, Test)
5. **Control Assessment** — Walk through each control capturing implementation status, effectiveness, and maturity
6. **Risk Scoring** — Score each gap using a 5x5 likelihood × impact matrix with inherent and residual risk calculations
7. **Cross-Framework Mapping** — Map findings across frameworks (800-53 ↔ CSF, 800-171 ↔ CMMC, 800-53 ↔ ISO 27001, etc.)
8. **Deliverable Generation** — Produce audit reports, assessment worksheets, and POA&Ms
9. **Publication & Sharing** — Export deliverables locally or share via connected services

## Deliverables

**Core (always generated):**
- Audit Summary Report (`.docx`)
- Control Assessment Worksheet (`.xlsx`)
- Plan of Action & Milestones / POA&M (`.xlsx`)

**Extended (offered based on context):**
- Executive Presentation (`.pptx`)
- System Security Plan / SSP (`.docx`)
- Risk Heat Map (5×5 visual matrix)

## Scripts

Helper scripts in `scripts/` for generating formatted deliverables:

| Script | Description | Dependencies |
|---|---|---|
| `generate_poam.py` | POA&M spreadsheet from findings JSON | `openpyxl` |
| `generate_assessment_worksheet.py` | Pre-populated control assessment worksheet | `openpyxl` |
| `generate_audit_report.py` | Audit summary report in Word format | `python-docx` |

### Usage

```bash
# Generate a POA&M from findings
python scripts/generate_poam.py --findings findings.json --output poam.xlsx --entity "Acme Corp" --framework "NIST SP 800-53 Rev 5"

# Generate an assessment worksheet
python scripts/generate_assessment_worksheet.py --framework 800-53 --baseline moderate --output caw.xlsx --entity "Acme Corp"

# Generate an audit report
python scripts/generate_audit_report.py --findings findings.json --output audit_report.docx
```

### Findings JSON Format

The scripts expect a JSON file structured as:

```json
{
  "metadata": {
    "entity": "Organization Name",
    "framework": "NIST SP 800-53 Rev 5",
    "baseline": "Moderate",
    "assessor": "Assessor Name",
    "date": "2026-03-07"
  },
  "findings": [
    {
      "title": "Finding title",
      "control_ids": "AC-2, AC-3",
      "control_family": "Access Control",
      "description": "Detailed description of the gap",
      "likelihood": 4,
      "impact": 3,
      "risk_score": 12,
      "status": "Open",
      "remediation": "Recommended remediation steps",
      "responsible": "System Owner",
      "evidence": "Evidence reviewed"
    }
  ]
}
```

## Reference Files

Documentation in `references/` that the skill loads during assessments:

| File | Content |
|---|---|
| `800-53-controls.md` | SP 800-53 Rev 5 control families, baselines, and control details |
| `800-171-controls.md` | SP 800-171 Rev 2 control families and requirements |
| `csf-functions.md` | NIST CSF 2.0 functions, categories, and subcategories |
| `ai-rmf.md` | NIST AI RMF 1.0 functions, categories, and subcategories |
| `assessment-procedures.md` | SP 800-53A assessment methodology (Examine, Interview, Test) |
| `scoring-methodology.md` | 5×5 risk matrix, maturity model, and POA&M prioritization |
| `crosswalks.md` | Cross-framework mappings (800-53 ↔ CSF, ISO 27001, CMMC, SOC 2, HIPAA) |

## Installation

Copy the `nist-auditor/` directory into your Claude Code skill path. No additional configuration is required — the skill activates on relevant keywords like "NIST audit", "800-53 assessment", "NIST compliance", "POA&M", "SSP", etc.

For the deliverable generation scripts, install Python dependencies:

```bash
pip install openpyxl python-docx
```

## License

See the repository root for license information.
