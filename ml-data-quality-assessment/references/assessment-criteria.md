# ML Data Quality Assessment Criteria

## Scoring Methodology

Each dimension is scored **Green / Amber / Red** based on thresholds defined below. The overall readiness score is derived from the dimension scores:

- **Green (ML-Ready)**: All dimensions Green or Amber, no Red on critical dimensions (Completeness, Label Quality, Temporal Integrity)
- **Amber (Conditionally Ready)**: Some Amber scores, or one Red on a non-critical dimension; proceed with documented mitigations
- **Red (Not ML-Ready)**: Any Red on a critical dimension, or 3+ Red scores; remediate before model development

---

## 1. Completeness

**What to measure:**
- Per-field missing value rate (null, empty string, placeholder values like "N/A", "UNKNOWN", "0000")
- Systematic missingness patterns (by channel, product, date range, or source system)
- Critical field completeness vs. non-critical field completeness

**Critical fields for TM:**
- Transaction amount, transaction date/timestamp, transaction type/code
- Account/customer identifier, counterparty identifier
- Currency, originator name, beneficiary name
- Channel/product type

**Scoring thresholds:**
- **Green**: All critical fields <2% missing; non-critical fields <10% missing
- **Amber**: Any critical field 2-10% missing; or non-critical fields 10-30% missing
- **Red**: Any critical field >10% missing; or systematic gaps affecting >20% of records

**Automated checks:**
- `df.isnull().mean()` per column
- Check for placeholder values: empty strings, "N/A", "NULL", "UNKNOWN", "0", "0000-00-00"
- Group missingness by categorical fields to detect systematic patterns
- Correlation between missing fields (if A is missing, is B also missing?)

---

## 2. Accuracy & Consistency

**What to measure:**
- Duplicate transaction records (exact and near-duplicates)
- Data type consistency (e.g., amounts stored as strings, dates in mixed formats)
- Value range validation (negative amounts where unexpected, future dates, amounts of exactly 0)
- Cross-field consistency (transaction date vs. account open date, currency vs. country)
- Referential integrity (customer IDs that don't map, orphaned records)

**Scoring thresholds:**
- **Green**: <0.5% duplicates; no data type inconsistencies; <1% range violations
- **Amber**: 0.5-2% duplicates; minor type inconsistencies; 1-5% range violations
- **Red**: >2% duplicates; significant type issues; >5% range violations; cross-field contradictions

**Automated checks:**
- `df.duplicated()` for exact duplicates
- `df.dtypes` validation against expected types
- Statistical outlier detection (IQR method) on numeric fields
- Date validation: future dates, dates before reasonable minimum
- Amount validation: negative values, zero values, extreme outliers

---

## 3. Label Quality

**What to measure (only if labeled data exists):**
- Label distribution across dispositions (SAR filed, escalated, closed-no action, etc.)
- Label consistency: same patterns labeled differently over time
- Analyst-level patterns: do certain analysts always close or always escalate?
- Label currency: how old are the labels? Have typologies changed since?
- Label granularity: binary (suspicious/not) vs. multi-class (typology-level)

**Scoring thresholds:**
- **Green**: Consistent labeling patterns; no obvious analyst bias; labels <18 months old; >500 positive samples
- **Amber**: Some inconsistency; mild analyst skew; labels 18-36 months old; 100-500 positive samples
- **Red**: High inconsistency; severe analyst bias; labels >36 months old; <100 positive samples

**Automated checks (proxies, since we can't measure true inter-rater reliability from a sample):**
- Label distribution: `df[label_col].value_counts(normalize=True)`
- If analyst ID available: label distribution per analyst
- Label over time: label distribution per quarter/month
- Positive sample count

---

## 4. Class Imbalance

**What to measure:**
- Ratio of suspicious to legitimate transactions
- Imbalance by segment (product, channel, geography)
- Whether minority class has sufficient volume for learning

**Scoring thresholds:**
- **Green**: Imbalance ratio <100:1 with >1,000 minority class samples
- **Amber**: Imbalance ratio 100:1 to 500:1, or 200-1,000 minority class samples
- **Red**: Imbalance ratio >500:1, or <200 minority class samples

**Automated checks:**
- `df[label_col].value_counts()` — raw counts and ratios
- Minority class count
- If segment fields available: minority class distribution across segments

**Notes:**
- Imbalance alone is not disqualifying — techniques exist (SMOTE, cost-sensitive learning, focal loss)
- The key concern is whether the minority class is *large enough in absolute terms* to learn from
- For TM, ratios of 200:1 to 1000:1 are typical; the question is absolute volume

---

## 5. Temporal Integrity

**What to measure:**
- Date range coverage (minimum 12 months recommended, 24 months ideal)
- Gaps in transaction flow (missing days, weeks, or months)
- Timestamp granularity (second-level vs. day-level)
- Volume consistency over time (sudden drops/spikes suggesting system issues)
- Seasonality patterns present and learnable

**Scoring thresholds:**
- **Green**: 18+ months coverage; no gaps >2 days; second/minute-level timestamps; stable volume
- **Amber**: 12-18 months; gaps of 2-7 days; day-level timestamps; minor volume anomalies
- **Red**: <12 months; gaps >7 days; date-only (no time); significant volume anomalies

**Automated checks:**
- Date range: `df[date_col].min()` to `df[date_col].max()`
- Gap detection: identify missing dates in expected daily/hourly sequence
- Volume by period: `df.groupby(df[date_col].dt.to_period('M')).size()`
- Timestamp precision: check if all times are midnight (date-only proxy)

---

## 6. Feature Availability & Engineering Feasibility

**What to measure:**
- Which standard TM features can be derived from the available fields
- What critical features are NOT derivable (and what source data would be needed)
- Cardinality of categorical fields (too many unique values = encoding challenges)
- Availability of fields needed for network/graph features

**Standard TM feature categories and their data requirements:**
- **Velocity features**: Transaction count/volume over rolling windows → requires timestamp + amount + account ID
- **Peer comparison**: Deviation from similar accounts → requires customer segment/type fields
- **Geographic risk**: Country/region risk scoring → requires geography fields
- **Counterparty network**: Transaction graph metrics → requires counterparty identifiers
- **Behavioral deviation**: Change from historical pattern → requires sufficient history per account
- **Structuring indicators**: Amounts just below thresholds → requires amount field
- **Channel patterns**: Unusual channel usage → requires channel/product fields

**Scoring thresholds:**
- **Green**: Can derive 5+ feature categories; key identifiers present; reasonable cardinality
- **Amber**: Can derive 3-4 feature categories; some identifiers missing; high cardinality fields present
- **Red**: Can derive <3 feature categories; missing critical identifiers; severe cardinality issues

**Automated checks:**
- Map available columns to feature categories
- Cardinality: `df[col].nunique()` for categorical fields
- Account-level record counts: `df.groupby(account_col).size().describe()`
- Check for required ID fields (account, customer, counterparty)

---

## 7. Volume & Representativeness

**What to measure:**
- Total record count (absolute volume)
- Records per unique account/customer
- Segment coverage: are all products, channels, geographies represented?
- Sample vs. population: is this sample representative? (hard to assess without population stats)

**Scoring thresholds:**
- **Green**: >100K transactions; >10 records per account on average; all major segments represented
- **Amber**: 10K-100K transactions; 5-10 records per account; most segments represented
- **Red**: <10K transactions; <5 records per account; missing major segments

**Automated checks:**
- `len(df)` — total records
- Records per account: `df.groupby(account_col).size().describe()`
- Unique values in segment fields (product, channel, geography)
- Distribution skew across segments

---

## 8. Data Lineage & Governance

**What to measure (largely qualitative — ask the user):**
- Source system(s) for the data
- Number of ETL transformations between source and sample
- Known data quality issues in the pipeline
- Data dictionary availability
- Change management processes for schema changes

**Scoring thresholds:**
- **Green**: Clear lineage documented; data dictionary available; <3 transformation steps
- **Amber**: Partial documentation; some known issues; 3-5 transformation steps
- **Red**: No documentation; unknown transformations; no data dictionary

**Assessment approach:**
- Ask the user directly about lineage
- Check for metadata indicators (column naming conventions suggest governed vs. ad hoc)
- Note any columns that appear derived/calculated (might indicate transformation layers)

---

## 9. Regulatory & Ethical Review

**What to measure:**
- Presence of protected attributes (race, ethnicity, gender, age, national origin, religion)
- Proxy fields that could encode protected attributes (zip code → race, name → ethnicity)
- Geographic concentration that could create bias
- Whether the model could produce disparate impact

**Scoring thresholds:**
- **Green**: No direct protected attributes; proxy risk assessed and mitigated; documented fairness approach
- **Amber**: Protected attributes present but can be excluded; proxy risk identified but not yet mitigated
- **Red**: Protected attributes embedded in features; high proxy risk; no fairness consideration

**Automated checks:**
- Scan column names for protected attribute indicators (gender, race, ethnicity, dob/age, nationality, religion)
- Flag high-proxy-risk fields (zip/postal code, name fields, language preference)
- Note any fields that should be excluded from model training but retained for fairness testing

---

## Overall Readiness Determination

| Scenario | Recommendation |
|----------|---------------|
| All Green | Proceed to model development |
| Mix of Green/Amber, no Red on critical | Proceed with documented mitigations and monitoring |
| Any Red on critical (Completeness, Labels, Temporal) | Remediate before proceeding |
| 3+ Red on any dimensions | Significant data remediation program needed |
| No labels available | Unsupervised approaches only; or invest in labeling program |

## Regulatory Defensibility Checklist

For model risk management (SR 11-7, OCC 2011-12, NYDFS) the assessment should document:
- Data sources and lineage
- Known data quality limitations and mitigations
- Label quality methodology and limitations
- Bias and fairness analysis
- Data sufficiency justification
- Ongoing monitoring plan for data quality drift
