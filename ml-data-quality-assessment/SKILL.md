---
name: ml-data-quality-assessment
description: "ML-readiness data quality assessment for transaction monitoring systems. Use when Claude needs to: (1) Assess whether transaction data is ready for ML model training (XGBoost, Random Forest, etc.), (2) Evaluate data quality for AML/TM model development, (3) Conduct completeness, accuracy, label quality, class imbalance, temporal integrity, or feature engineering feasibility analysis on transaction datasets, (4) Generate data readiness scorecards or reports, (5) Identify data remediation steps before ML model build. Triggers on keywords: data quality assessment, ML readiness, transaction monitoring data, AML data quality, model-ready data, data assessment, TM data, feature engineering feasibility, class imbalance, label quality, data completeness, data profiling for ML."
---

# ML Data Quality Assessment Skill

## Overview

Conducts a structured ML-readiness data quality assessment on transaction data samples. Evaluates whether the data can support supervised or unsupervised ML models (XGBoost, Random Forest, neural nets, etc.) for transaction monitoring / AML use cases. Produces a scored readiness report with remediation recommendations.

## Prerequisites

- Python with pandas, numpy, scipy (all pre-installed)
- User must provide a data sample as CSV, XLSX, TSV, or similar tabular format

## Assessment Workflow

### Step 1: Data Intake

Ask the user to upload a **random sample** of their transaction data. Emphasize:

Ask: **"Please upload a random sample of your transaction monitoring data (CSV, XLSX, or TSV). For a meaningful assessment, I recommend at least 1,000 rows — but even a few hundred will give us directional insights. Make sure it's a representative random sample, not filtered to a specific date range, product, or customer segment."**

Also ask: **"Does this dataset include labeled outcomes (e.g., SAR filed, alert disposition, true positive/false positive flags)? This affects whether I can assess label quality and class imbalance."**

Optionally ask:
- "What ML model or approach are you considering?" (supervised vs unsupervised, specific algorithms)
- "What typologies or scenarios are you targeting?" (structuring, layering, rapid movement, etc.)
- "Are there any known data issues I should be aware of?"

### Step 2: Run the Automated Assessment

Once the file is uploaded, run the assessment script:

```bash
python /path/to/skill/scripts/assess_data_quality.py <uploaded_file_path> [--label-column <column_name>] [--date-column <column_name>] [--amount-column <column_name>]
```

The script auto-detects columns where possible but accepts overrides. It outputs a JSON report to stdout.

If the script fails or the data format is unusual, fall back to manual pandas analysis following the criteria in [references/assessment-criteria.md](references/assessment-criteria.md).

### Step 3: Interpret and Present Results

Read the JSON output and present findings organized by assessment dimension. For each dimension:

1. **Score** (Green / Amber / Red)
2. **Key Findings** — specific metrics and observations
3. **Remediation** — what to fix before model development

Use the assessment criteria reference for scoring thresholds: [references/assessment-criteria.md](references/assessment-criteria.md).

### Step 4: Generate the Readiness Scorecard

Create an **XLSX scorecard** using the xlsx skill with:

- **Summary tab**: Overall readiness score, dimension-level RAG status, go/no-go recommendation
- **Detail tab**: Per-field metrics (completeness %, unique values, data type, distribution stats)
- **Findings tab**: All findings with severity, dimension, description, and remediation
- **Recommendations tab**: Prioritized remediation roadmap

### Step 5: Optionally Generate a Presentation

If the user requests it (or if the assessment is for stakeholder consumption), create a **PPTX deck** using the pptx skill with:

1. Title Slide — Assessment name, dataset description, date
2. Executive Summary — Overall readiness score and go/no-go
3. Methodology — Assessment dimensions and scoring approach
4. Scorecard Overview — RAG heatmap across all dimensions
5. Completeness Analysis — Missing data patterns and field-level detail
6. Accuracy & Consistency — Data quality issues found
7. Label Quality (if applicable) — Disposition analysis and reliability
8. Class Imbalance — Ratio analysis and implications
9. Temporal Integrity — Time coverage and gap analysis
10. Feature Engineering Feasibility — Derivable vs. missing features
11. Remediation Roadmap — Prioritized actions with effort estimates
12. Next Steps — Recommendations for proceeding

### Step 6: Discuss and Advise

After presenting results, offer to:
- Deep-dive on any specific dimension
- Discuss remediation strategies
- Advise on model selection given the data constraints
- Discuss feature engineering approaches
- Review regulatory defensibility of the data pipeline

## Assessment Dimensions

The nine assessment dimensions are detailed in [references/assessment-criteria.md](references/assessment-criteria.md):

1. **Completeness** — Missing values, systematic gaps
2. **Accuracy & Consistency** — Data integrity, duplicates, contradictions
3. **Label Quality** — Disposition reliability, analyst agreement proxies
4. **Class Imbalance** — Suspicious vs. legitimate ratio
5. **Temporal Integrity** — Time coverage, gaps, seasonality
6. **Feature Availability & Engineering Feasibility** — Derivable features from raw data
7. **Volume & Representativeness** — Sample size, segment coverage
8. **Data Lineage & Governance** — Field origins, transformation concerns
9. **Regulatory & Ethical Review** — Protected attributes, bias risk

## Output Deliverables

1. **Conversational Summary** — Findings walkthrough in chat
2. **XLSX Readiness Scorecard** — Detailed metrics and RAG scoring
3. **PPTX Presentation** (optional) — Stakeholder-ready deck
4. **Remediation Recommendations** — Prioritized action plan
