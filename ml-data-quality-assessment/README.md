# ML Data Quality Assessment Skill: README

## Table of Contents

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Assessment Workflow](#assessment-workflow)
   - [Step 1: Data Intake](#step-1-data-intake)
   - [Step 2: Run the Automated Assessment](#step-2-run-the-automated-assessment)
   - [Step 3: Interpret and Present Results](#step-3-interpret-and-present-results)
   - [Step 4: Generate the Readiness Scorecard](#step-4-generate-the-readiness-scorecard)
   - [Step 5: Optionally Generate a Presentation](#step-5-optionally-generate-a-presentation)
   - [Step 6: Discuss and Advise](#step-6-discuss-and-advise)
4. [Assessment Dimensions](#assessment-dimensions)
5. [Output Deliverables](#output-deliverables)

## Overview

The `ml-data-quality-assessment` skill evaluates the readiness of transaction data for machine learning (ML) model training, particularly for anti-money laundering (AML) and transaction monitoring (TM) use cases. It assesses data quality across nine dimensions and provides a scored readiness report with remediation recommendations.

## Prerequisites

- Python with pandas, numpy, scipy installed
- A tabular transaction data sample (CSV, XLSX, TSV, etc.) provided by the user

## Assessment Workflow

### Step 1: Data Intake

Ask the user to upload a **random sample** of their transaction data. Emphasize the importance of a representative sample and encourage users to provide at least 1,000 rows. Additionally, ask if the dataset includes labeled outcomes and any specific ML models or typologies they are considering.

### Step 2: Run the Automated Assessment

After obtaining the data file, run the assessment script:

```bash
python /path/to/skill/scripts/assess_data_quality.py <uploaded_file_path> [--label-column <column_name>] [--date-column <column_name>] [--amount-column <column_name>]
```

The script auto-detects columns but accepts overrides. It outputs a JSON report to stdout. If the script fails or the data format is unusual, fall back to manual analysis using pandas following the criteria in [references/assessment-criteria.md](references/assessment-criteria.md).

### Step 3: Interpret and Present Results

Read the JSON output and present findings organized by assessment dimension. For each dimension, provide a score (Green/Amber/Red), key findings, and remediation steps. Use the assessment criteria reference for scoring thresholds: [references/assessment-criteria.md](references/assessment-criteria.md).

### Step 4: Generate the Readiness Scorecard

Create an XLSX scorecard using the xlsx skill with four tabs:

- Summary: Overall readiness score, dimension-level RAG status, go/no-go recommendation
- Detail: Per-field metrics (completeness %, unique values, data type, distribution stats)
- Findings: All findings with severity, dimension, description, and remediation
- Recommendations: Prioritized remediation roadmap

### Step 5: Optionally Generate a Presentation

If requested, create a PPTX deck using the pptx skill with twelve slides:

1. Title Slide
2. Executive Summary
3. Methodology
4. Scorecard Overview
5. Completeness Analysis
6. Accuracy & Consistency
7. Label Quality (if applicable)
8. Class Imbalance
9. Temporal Integrity
10. Feature Engineering Feasibility
11. Remediation Roadmap
12. Next Steps

### Step 6: Discuss and Advise

After presenting results, offer to deep-dive on specific dimensions, discuss remediation strategies, advise on model selection, and review regulatory defensibility of the data pipeline.

## Assessment Dimensions

The nine assessment dimensions are detailed in [references/assessment-criteria.md](references/assessment-criteria.md):

1. Completeness
2. Accuracy & Consistency
3. Label Quality
4. Class Imbalance
5. Temporal Integrity
6. Feature Availability & Engineering Feasibility
7. Volume & Representativeness
8. Data Lineage & Governance
9. Regulatory & Ethical Review

## Output Deliverables

1. Conversational Summary: Findings walkthrough in chat
2. XLSX Readiness Scorecard: Detailed metrics and RAG scoring
3. PPTX Presentation (optional): Stakeholder-ready deck
4. Remediation Recommendations: Prioritized action plan
