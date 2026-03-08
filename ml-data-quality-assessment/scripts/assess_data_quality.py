#!/usr/bin/env python3
"""
ML Data Quality Assessment for Transaction Monitoring
Analyzes a transaction data sample and produces a structured readiness report.
"""

import argparse
import json
import sys
import warnings
from datetime import datetime, timedelta
from pathlib import Path

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")

# ---------------------------------------------------------------------------
# Column detection heuristics
# ---------------------------------------------------------------------------

DATE_HINTS = [
    "date", "time", "timestamp", "dt", "created", "posted", "value_date",
    "transaction_date", "txn_date", "trans_date", "booking_date", "effective_date",
]
AMOUNT_HINTS = [
    "amount", "amt", "value", "sum", "total", "credit", "debit",
    "transaction_amount", "txn_amount", "trans_amount", "payment",
]
LABEL_HINTS = [
    "label", "sar", "suspicious", "alert", "disposition", "outcome",
    "flag", "is_fraud", "fraud", "true_positive", "tp", "result",
    "is_suspicious", "risk_flag", "alert_status",
]
ACCOUNT_HINTS = [
    "account", "acct", "account_id", "acct_id", "customer_id", "cust_id",
    "client_id", "party_id", "entity_id",
]
COUNTERPARTY_HINTS = [
    "counterparty", "beneficiary", "payee", "recipient", "cp_id",
    "counterparty_id", "beneficiary_id", "receiver", "dest_account",
]
CURRENCY_HINTS = ["currency", "ccy", "curr", "iso_currency"]
CHANNEL_HINTS = ["channel", "product", "product_type", "channel_type", "payment_method", "txn_type", "trans_type"]
COUNTRY_HINTS = ["country", "nation", "geo", "geography", "region", "jurisdiction", "country_code"]
PROTECTED_HINTS = [
    "gender", "sex", "race", "ethnicity", "religion", "national_origin",
    "nationality", "dob", "date_of_birth", "birth_date", "age",
]
PROXY_HINTS = ["zip", "postal", "postcode", "zip_code", "first_name", "last_name", "surname", "name", "language"]

PLACEHOLDER_VALUES = {"", "n/a", "na", "null", "none", "unknown", "0000-00-00", "1900-01-01", "1970-01-01", "nan", "-"}


def detect_column(df, hints, override=None):
    if override and override in df.columns:
        return override
    lower_cols = {c.lower().strip(): c for c in df.columns}
    for hint in hints:
        if hint in lower_cols:
            return lower_cols[hint]
    for hint in hints:
        for lc, orig in lower_cols.items():
            if hint in lc:
                return orig
    return None


def detect_columns_multi(df, hints):
    found = []
    lower_cols = {c.lower().strip(): c for c in df.columns}
    for hint in hints:
        for lc, orig in lower_cols.items():
            if hint in lc and orig not in found:
                found.append(orig)
    return found


# ---------------------------------------------------------------------------
# Dimension assessors
# ---------------------------------------------------------------------------

def assess_completeness(df, critical_cols, all_cols):
    results = {"dimension": "Completeness", "fields": {}, "findings": [], "score": "Green"}

    for col in all_cols:
        null_count = df[col].isnull().sum()
        placeholder_count = df[col].astype(str).str.strip().str.lower().isin(PLACEHOLDER_VALUES).sum()
        total_missing = null_count + placeholder_count
        rate = total_missing / len(df) if len(df) > 0 else 0
        results["fields"][col] = {
            "null_count": int(null_count),
            "placeholder_count": int(placeholder_count),
            "total_missing": int(total_missing),
            "missing_rate": round(rate, 4),
            "is_critical": col in critical_cols,
        }

    worst_critical = 0
    worst_noncritical = 0
    for col, stats in results["fields"].items():
        rate = stats["missing_rate"]
        if stats["is_critical"]:
            worst_critical = max(worst_critical, rate)
            if rate > 0.02:
                results["findings"].append(f"Critical field '{col}' has {rate:.1%} missing values")
        else:
            worst_noncritical = max(worst_noncritical, rate)
            if rate > 0.10:
                results["findings"].append(f"Non-critical field '{col}' has {rate:.1%} missing values")

    if worst_critical > 0.10:
        results["score"] = "Red"
        results["findings"].insert(0, "CRITICAL: One or more critical fields exceed 10% missing threshold")
    elif worst_critical > 0.02 or worst_noncritical > 0.10:
        results["score"] = "Amber"
    
    # Check for systematic missingness
    null_matrix = df[all_cols].isnull()
    if null_matrix.sum().sum() > 0:
        corr = null_matrix.corr()
        high_corr_pairs = []
        for i in range(len(corr.columns)):
            for j in range(i + 1, len(corr.columns)):
                if abs(corr.iloc[i, j]) > 0.7:
                    high_corr_pairs.append((corr.columns[i], corr.columns[j], round(corr.iloc[i, j], 2)))
        if high_corr_pairs:
            results["findings"].append(f"Systematic missingness detected: {len(high_corr_pairs)} correlated missing-field pairs")
            results["systematic_missingness"] = [{"field_a": a, "field_b": b, "correlation": c} for a, b, c in high_corr_pairs[:10]]

    return results


def assess_accuracy(df, date_col, amount_col, account_col):
    results = {"dimension": "Accuracy & Consistency", "findings": [], "score": "Green", "metrics": {}}

    # Duplicates
    n_exact_dupes = df.duplicated().sum()
    dupe_rate = n_exact_dupes / len(df) if len(df) > 0 else 0
    results["metrics"]["exact_duplicates"] = int(n_exact_dupes)
    results["metrics"]["duplicate_rate"] = round(dupe_rate, 4)

    if dupe_rate > 0.02:
        results["score"] = "Red"
        results["findings"].append(f"High duplicate rate: {dupe_rate:.1%} ({n_exact_dupes} exact duplicate rows)")
    elif dupe_rate > 0.005:
        results["score"] = "Amber"
        results["findings"].append(f"Moderate duplicate rate: {dupe_rate:.1%}")

    # Data type checks
    type_issues = []
    for col in df.columns:
        if df[col].dtype == object:
            numeric_parseable = pd.to_numeric(df[col], errors="coerce").notna().mean()
            if numeric_parseable > 0.8 and numeric_parseable < 1.0:
                type_issues.append(f"'{col}' appears numeric but stored as text ({numeric_parseable:.0%} parseable)")
    if type_issues:
        results["findings"].extend(type_issues)
        if results["score"] == "Green":
            results["score"] = "Amber"

    # Amount validation
    if amount_col and amount_col in df.columns:
        amounts = pd.to_numeric(df[amount_col], errors="coerce")
        neg_count = (amounts < 0).sum()
        zero_count = (amounts == 0).sum()
        neg_rate = neg_count / len(df)
        zero_rate = zero_count / len(df)
        results["metrics"]["negative_amounts"] = int(neg_count)
        results["metrics"]["zero_amounts"] = int(zero_count)
        if neg_rate > 0.05:
            results["findings"].append(f"Unusual: {neg_rate:.1%} of transactions have negative amounts")
        if zero_rate > 0.05:
            results["findings"].append(f"{zero_rate:.1%} of transactions have zero amounts")

        # Outlier detection (IQR)
        q1 = amounts.quantile(0.25)
        q3 = amounts.quantile(0.75)
        iqr = q3 - q1
        if iqr > 0:
            outlier_count = ((amounts < q1 - 3 * iqr) | (amounts > q3 + 3 * iqr)).sum()
            outlier_rate = outlier_count / len(df)
            results["metrics"]["extreme_outliers"] = int(outlier_count)
            results["metrics"]["outlier_rate"] = round(outlier_rate, 4)
            if outlier_rate > 0.05:
                results["findings"].append(f"{outlier_rate:.1%} extreme amount outliers detected (>3x IQR)")

    # Date validation
    if date_col and date_col in df.columns:
        dates = pd.to_datetime(df[date_col], errors="coerce")
        future_count = (dates > datetime.now() + timedelta(days=1)).sum()
        ancient_count = (dates < datetime(2000, 1, 1)).sum()
        if future_count > 0:
            results["findings"].append(f"{future_count} transactions have future dates")
        if ancient_count > 0:
            results["findings"].append(f"{ancient_count} transactions dated before 2000")

    if not results["findings"]:
        results["findings"].append("No significant accuracy issues detected")

    return results


def assess_label_quality(df, label_col):
    results = {"dimension": "Label Quality", "findings": [], "score": "Green", "metrics": {}}

    if not label_col or label_col not in df.columns:
        results["score"] = "Amber"
        results["findings"].append("No label column detected — supervised learning not possible without labels")
        results["findings"].append("Consider: unsupervised approaches (isolation forest, autoencoder) or invest in a labeling program")
        return results

    labels = df[label_col].dropna()
    dist = labels.value_counts()
    dist_pct = labels.value_counts(normalize=True)
    results["metrics"]["label_distribution"] = {str(k): int(v) for k, v in dist.items()}
    results["metrics"]["label_distribution_pct"] = {str(k): round(float(v), 4) for k, v in dist_pct.items()}
    results["metrics"]["unique_labels"] = int(labels.nunique())
    results["metrics"]["label_null_rate"] = round(float(df[label_col].isnull().mean()), 4)

    # Check positive sample count
    # Heuristic: the minority class is the "positive" (suspicious) class
    minority_count = dist.min()
    minority_label = dist.idxmin()
    results["metrics"]["minority_class"] = str(minority_label)
    results["metrics"]["minority_count"] = int(minority_count)

    if minority_count < 100:
        results["score"] = "Red"
        results["findings"].append(f"Only {minority_count} samples in minority class ('{minority_label}') — insufficient for supervised learning")
    elif minority_count < 500:
        results["score"] = "Amber"
        results["findings"].append(f"{minority_count} minority class samples — marginal for robust model training")

    if labels.nunique() == 1:
        results["score"] = "Red"
        results["findings"].append("Only one unique label value — no discriminative signal for supervised learning")

    label_null_rate = df[label_col].isnull().mean()
    if label_null_rate > 0.1:
        results["findings"].append(f"{label_null_rate:.1%} of records have no label — verify this is expected")
        if results["score"] == "Green":
            results["score"] = "Amber"

    return results


def assess_class_imbalance(df, label_col):
    results = {"dimension": "Class Imbalance", "findings": [], "score": "Green", "metrics": {}}

    if not label_col or label_col not in df.columns:
        results["score"] = "N/A"
        results["findings"].append("No label column — class imbalance not assessable")
        return results

    labels = df[label_col].dropna()
    dist = labels.value_counts()
    if len(dist) < 2:
        results["score"] = "Red"
        results["findings"].append("Single class present — no imbalance to measure, but also no learning signal")
        return results

    majority_count = dist.max()
    minority_count = dist.min()
    ratio = majority_count / minority_count if minority_count > 0 else float("inf")
    results["metrics"]["imbalance_ratio"] = round(ratio, 1)
    results["metrics"]["majority_class"] = str(dist.idxmax())
    results["metrics"]["majority_count"] = int(majority_count)
    results["metrics"]["minority_class"] = str(dist.idxmin())
    results["metrics"]["minority_count"] = int(minority_count)

    if ratio > 500 or minority_count < 200:
        results["score"] = "Red"
        results["findings"].append(f"Severe imbalance: {ratio:.0f}:1 ratio with {minority_count} minority samples")
        results["findings"].append("Recommended: SMOTE, cost-sensitive learning, or hybrid unsupervised pre-filter")
    elif ratio > 100 or minority_count < 1000:
        results["score"] = "Amber"
        results["findings"].append(f"Moderate imbalance: {ratio:.0f}:1 ratio with {minority_count} minority samples")
        results["findings"].append("Manageable with appropriate sampling/weighting techniques")
    else:
        results["findings"].append(f"Imbalance ratio: {ratio:.0f}:1 — within normal range for TM")

    return results


def assess_temporal_integrity(df, date_col):
    results = {"dimension": "Temporal Integrity", "findings": [], "score": "Green", "metrics": {}}

    if not date_col or date_col not in df.columns:
        results["score"] = "Red"
        results["findings"].append("No date/timestamp column detected — temporal analysis impossible")
        return results

    dates = pd.to_datetime(df[date_col], errors="coerce")
    valid_dates = dates.dropna()
    if len(valid_dates) == 0:
        results["score"] = "Red"
        results["findings"].append("Date column contains no parseable dates")
        return results

    parse_rate = len(valid_dates) / len(df)
    results["metrics"]["date_parse_rate"] = round(parse_rate, 4)

    min_date = valid_dates.min()
    max_date = valid_dates.max()
    coverage_days = (max_date - min_date).days
    coverage_months = coverage_days / 30.44
    results["metrics"]["min_date"] = str(min_date.date())
    results["metrics"]["max_date"] = str(max_date.date())
    results["metrics"]["coverage_days"] = int(coverage_days)
    results["metrics"]["coverage_months"] = round(coverage_months, 1)

    if coverage_months < 12:
        results["score"] = "Red"
        results["findings"].append(f"Only {coverage_months:.1f} months of data — minimum 12 months recommended")
    elif coverage_months < 18:
        results["score"] = "Amber"
        results["findings"].append(f"{coverage_months:.1f} months of data — acceptable but 18+ months preferred for seasonality")
    else:
        results["findings"].append(f"{coverage_months:.1f} months of data coverage — sufficient")

    # Timestamp precision
    has_time = (valid_dates.dt.hour != 0).any() or (valid_dates.dt.minute != 0).any()
    midnight_pct = ((valid_dates.dt.hour == 0) & (valid_dates.dt.minute == 0) & (valid_dates.dt.second == 0)).mean()
    results["metrics"]["has_time_component"] = bool(has_time)
    results["metrics"]["midnight_percentage"] = round(float(midnight_pct), 4)
    if midnight_pct > 0.95:
        results["findings"].append("Timestamps appear date-only (>95% midnight) — may limit intraday pattern detection")
        if results["score"] == "Green":
            results["score"] = "Amber"

    # Gap detection (daily)
    daily_counts = valid_dates.dt.date.value_counts().sort_index()
    all_dates = pd.date_range(start=min_date.date(), end=max_date.date(), freq="D")
    missing_dates = set(all_dates.date) - set(daily_counts.index)
    gap_rate = len(missing_dates) / len(all_dates) if len(all_dates) > 0 else 0
    results["metrics"]["missing_days"] = len(missing_dates)
    results["metrics"]["gap_rate"] = round(gap_rate, 4)

    if gap_rate > 0.1:
        results["findings"].append(f"{len(missing_dates)} missing days ({gap_rate:.1%}) — significant gaps in transaction flow")
        results["score"] = "Red" if gap_rate > 0.2 else "Amber"
    elif len(missing_dates) > 7:
        results["findings"].append(f"{len(missing_dates)} missing days detected — investigate data pipeline gaps")

    # Volume stability (monthly coefficient of variation)
    monthly = valid_dates.dt.to_period("M").value_counts().sort_index()
    if len(monthly) > 2:
        cv = monthly.std() / monthly.mean() if monthly.mean() > 0 else 0
        results["metrics"]["monthly_volume_cv"] = round(float(cv), 4)
        if cv > 0.5:
            results["findings"].append(f"High volume variability across months (CV={cv:.2f}) — investigate system changes")
            if results["score"] == "Green":
                results["score"] = "Amber"

    return results


def assess_feature_feasibility(df, date_col, amount_col, account_col, counterparty_col, channel_col, country_col, currency_col):
    results = {"dimension": "Feature Engineering Feasibility", "findings": [], "score": "Green", "metrics": {}}

    feature_categories = {
        "Velocity/Volume": {"required": [date_col, amount_col, account_col], "description": "Rolling transaction counts and sums"},
        "Peer Comparison": {"required": [account_col], "description": "Deviation from similar account behavior"},
        "Geographic Risk": {"required": [country_col], "description": "Country/region risk scoring"},
        "Counterparty Network": {"required": [counterparty_col, account_col], "description": "Graph-based relationship features"},
        "Behavioral Deviation": {"required": [date_col, account_col, amount_col], "description": "Change from historical baselines"},
        "Structuring Indicators": {"required": [amount_col], "description": "Amounts near reporting thresholds"},
        "Channel Patterns": {"required": [channel_col], "description": "Unusual channel or product usage"},
    }

    derivable = 0
    not_derivable = []
    for cat, info in feature_categories.items():
        available = all(col and col in df.columns for col in info["required"])
        if available:
            derivable += 1
        else:
            missing = [col for col in info["required"] if not col or col not in df.columns]
            not_derivable.append(f"{cat} (missing: {', '.join(str(m) for m in missing)})")

    results["metrics"]["derivable_categories"] = derivable
    results["metrics"]["total_categories"] = len(feature_categories)
    results["metrics"]["not_derivable"] = not_derivable

    if derivable >= 5:
        results["findings"].append(f"{derivable}/{len(feature_categories)} feature categories derivable — strong foundation")
    elif derivable >= 3:
        results["score"] = "Amber"
        results["findings"].append(f"{derivable}/{len(feature_categories)} feature categories derivable — some gaps")
    else:
        results["score"] = "Red"
        results["findings"].append(f"Only {derivable}/{len(feature_categories)} feature categories derivable — significant data gaps")

    if not_derivable:
        results["findings"].append(f"Cannot derive: {'; '.join(not_derivable)}")

    # Cardinality check on categorical columns
    high_cardinality = []
    for col in df.select_dtypes(include=["object", "category"]).columns:
        nunique = df[col].nunique()
        ratio = nunique / len(df) if len(df) > 0 else 0
        if nunique > 1000 or ratio > 0.5:
            high_cardinality.append(f"'{col}' ({nunique} unique values)")
    if high_cardinality:
        results["findings"].append(f"High cardinality fields (may need encoding strategy): {', '.join(high_cardinality)}")

    # Records per account
    if account_col and account_col in df.columns:
        rpa = df.groupby(account_col).size()
        results["metrics"]["avg_records_per_account"] = round(float(rpa.mean()), 1)
        results["metrics"]["median_records_per_account"] = float(rpa.median())
        if rpa.mean() < 5:
            results["findings"].append(f"Low average records per account ({rpa.mean():.1f}) — limits behavioral feature engineering")

    return results


def assess_volume(df, account_col, channel_col, country_col):
    results = {"dimension": "Volume & Representativeness", "findings": [], "score": "Green", "metrics": {}}

    n_records = len(df)
    results["metrics"]["total_records"] = n_records

    if n_records < 10_000:
        results["score"] = "Red"
        results["findings"].append(f"Only {n_records:,} records — likely insufficient for robust ML training")
    elif n_records < 100_000:
        results["score"] = "Amber"
        results["findings"].append(f"{n_records:,} records — adequate for initial modeling, but more data preferred")
    else:
        results["findings"].append(f"{n_records:,} records — sufficient volume")

    # Segment coverage
    for col_name, col in [("account", account_col), ("channel", channel_col), ("country", country_col)]:
        if col and col in df.columns:
            nunique = df[col].nunique()
            results["metrics"][f"unique_{col_name}s"] = int(nunique)
            top5 = df[col].value_counts().head(5)
            top5_pct = top5.sum() / len(df)
            results["metrics"][f"top5_{col_name}_concentration"] = round(float(top5_pct), 4)
            if top5_pct > 0.95:
                results["findings"].append(f"Top 5 {col_name} values account for {top5_pct:.0%} of records — low diversity")

    return results


def assess_governance(df):
    results = {"dimension": "Data Lineage & Governance", "findings": [], "score": "Amber", "metrics": {}}

    # Heuristic checks based on column naming
    cols = df.columns.tolist()
    has_consistent_naming = all("_" in c or c.islower() for c in cols) or all(c[0].isupper() for c in cols if len(c) > 0)
    results["metrics"]["column_count"] = len(cols)
    results["metrics"]["consistent_naming_convention"] = has_consistent_naming

    if has_consistent_naming:
        results["findings"].append("Column naming appears consistent — suggests governed data source")
    else:
        results["findings"].append("Mixed column naming conventions — may indicate multiple source systems or ad-hoc extraction")

    # Check for columns that look derived/calculated
    derived_hints = ["_calc", "_derived", "_computed", "ratio", "score", "_pct", "_flag", "is_"]
    derived_cols = [c for c in cols if any(h in c.lower() for h in derived_hints)]
    if derived_cols:
        results["findings"].append(f"Possibly pre-derived fields detected: {', '.join(derived_cols[:5])}")

    results["findings"].append("NOTE: Data lineage requires manual verification — ask the user about source systems, ETL processes, and data dictionary availability")

    return results


def assess_regulatory(df):
    results = {"dimension": "Regulatory & Ethical Review", "findings": [], "score": "Green", "metrics": {}}

    protected_cols = detect_columns_multi(df, PROTECTED_HINTS)
    proxy_cols = detect_columns_multi(df, PROXY_HINTS)

    results["metrics"]["protected_attribute_columns"] = protected_cols
    results["metrics"]["proxy_risk_columns"] = proxy_cols

    if protected_cols:
        results["score"] = "Amber"
        results["findings"].append(f"Protected attribute fields detected: {', '.join(protected_cols)}")
        results["findings"].append("These should be EXCLUDED from model features but RETAINED for fairness/bias testing")

    if proxy_cols:
        results["findings"].append(f"Potential proxy fields for protected attributes: {', '.join(proxy_cols)}")
        results["findings"].append("Assess whether these encode demographic information that could cause disparate impact")
        if results["score"] == "Green":
            results["score"] = "Amber"

    if not protected_cols and not proxy_cols:
        results["findings"].append("No obvious protected attributes or high-risk proxy fields detected")

    return results


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def load_data(filepath):
    path = Path(filepath)
    ext = path.suffix.lower()
    if ext in (".csv", ".tsv"):
        sep = "\t" if ext == ".tsv" else ","
        try:
            return pd.read_csv(filepath, sep=sep, low_memory=False)
        except Exception:
            return pd.read_csv(filepath, sep=sep, low_memory=False, encoding="latin1")
    elif ext in (".xlsx", ".xls", ".xlsm"):
        return pd.read_excel(filepath)
    elif ext == ".json":
        return pd.read_json(filepath)
    elif ext == ".parquet":
        return pd.read_parquet(filepath)
    else:
        raise ValueError(f"Unsupported file format: {ext}")


def main():
    parser = argparse.ArgumentParser(description="ML Data Quality Assessment for Transaction Monitoring")
    parser.add_argument("filepath", help="Path to the transaction data file")
    parser.add_argument("--label-column", help="Column containing labels/dispositions", default=None)
    parser.add_argument("--date-column", help="Column containing transaction dates", default=None)
    parser.add_argument("--amount-column", help="Column containing transaction amounts", default=None)
    parser.add_argument("--account-column", help="Column containing account/customer IDs", default=None)
    args = parser.parse_args()

    # Load data
    df = load_data(args.filepath)

    # Detect columns
    date_col = detect_column(df, DATE_HINTS, args.date_column)
    amount_col = detect_column(df, AMOUNT_HINTS, args.amount_column)
    label_col = detect_column(df, LABEL_HINTS, args.label_column)
    account_col = detect_column(df, ACCOUNT_HINTS, args.account_column)
    counterparty_col = detect_column(df, COUNTERPARTY_HINTS)
    currency_col = detect_column(df, CURRENCY_HINTS)
    channel_col = detect_column(df, CHANNEL_HINTS)
    country_col = detect_column(df, COUNTRY_HINTS)

    detected = {
        "date": date_col, "amount": amount_col, "label": label_col,
        "account": account_col, "counterparty": counterparty_col,
        "currency": currency_col, "channel": channel_col, "country": country_col,
    }

    # Parse date column if found
    if date_col and date_col in df.columns:
        df[date_col] = pd.to_datetime(df[date_col], errors="coerce")

    # Critical columns for completeness
    critical_cols = [c for c in [date_col, amount_col, account_col, counterparty_col, currency_col] if c and c in df.columns]
    all_cols = list(df.columns)

    # Run all assessments
    assessments = [
        assess_completeness(df, critical_cols, all_cols),
        assess_accuracy(df, date_col, amount_col, account_col),
        assess_label_quality(df, label_col),
        assess_class_imbalance(df, label_col),
        assess_temporal_integrity(df, date_col),
        assess_feature_feasibility(df, date_col, amount_col, account_col, counterparty_col, channel_col, country_col, currency_col),
        assess_volume(df, account_col, channel_col, country_col),
        assess_governance(df),
        assess_regulatory(df),
    ]

    # Overall score
    scores = [a["score"] for a in assessments if a["score"] != "N/A"]
    critical_dims = ["Completeness", "Label Quality", "Temporal Integrity"]
    critical_reds = [a for a in assessments if a["dimension"] in critical_dims and a["score"] == "Red"]
    all_reds = [a for a in assessments if a["score"] == "Red"]

    if critical_reds:
        overall = "Red"
        overall_recommendation = "NOT ML-READY: Remediate critical data issues before model development"
    elif len(all_reds) >= 3:
        overall = "Red"
        overall_recommendation = "NOT ML-READY: Multiple dimensions failing — significant data remediation needed"
    elif all_reds:
        overall = "Amber"
        overall_recommendation = "CONDITIONALLY READY: Proceed with documented mitigations for failing dimensions"
    elif any(a["score"] == "Amber" for a in assessments):
        overall = "Amber"
        overall_recommendation = "CONDITIONALLY READY: Minor issues to address; can proceed with monitoring"
    else:
        overall = "Green"
        overall_recommendation = "ML-READY: Data quality sufficient to proceed with model development"

    # Build report
    report = {
        "assessment_date": datetime.now().isoformat(),
        "file": str(args.filepath),
        "rows": len(df),
        "columns": len(df.columns),
        "column_list": list(df.columns),
        "detected_columns": detected,
        "overall_score": overall,
        "overall_recommendation": overall_recommendation,
        "dimensions": assessments,
        "data_profile": {
            "numeric_columns": list(df.select_dtypes(include=[np.number]).columns),
            "categorical_columns": list(df.select_dtypes(include=["object", "category"]).columns),
            "datetime_columns": list(df.select_dtypes(include=["datetime"]).columns),
            "dtypes": {col: str(dtype) for col, dtype in df.dtypes.items()},
        },
    }

    print(json.dumps(report, indent=2, default=str))


if __name__ == "__main__":
    main()
