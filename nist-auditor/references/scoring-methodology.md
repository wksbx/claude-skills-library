# Risk Scoring & Maturity Methodology Reference

## 5x5 Risk Matrix

### Likelihood Scale

| Score | Rating | Description | Indicators |
|-------|--------|-------------|------------|
| 1 | Rare | Requires significant effort, resources, or insider access to exploit | No known exploits; requires chaining multiple vulnerabilities; strong compensating controls exist |
| 2 | Unlikely | Possible but requires specific conditions or moderate effort | Theoretical vulnerability; limited attack surface; partial controls in place |
| 3 | Possible | Could reasonably occur during the assessment period | Known vulnerability with available exploit; moderate attack surface; control gaps exist |
| 4 | Likely | Expected to occur without remediation in near term | Actively scanned vulnerability; common attack vector; weak or absent controls |
| 5 | Almost Certain | Currently exploited or trivially exploitable | Active exploitation in the wild; public exploit code; no controls in place; internet-facing |

### Impact Scale

| Score | Rating | Description | Indicators |
|-------|--------|-------------|------------|
| 1 | Negligible | Minimal operational effect, no data exposure | Affects non-critical systems; no PII/CUI involved; quick recovery |
| 2 | Minor | Limited degradation, minor data exposure | Affects supporting systems; limited PII exposure; recovery in hours |
| 3 | Moderate | Significant degradation, partial mission impact | Affects primary operations; moderate data exposure; recovery in days; regulatory notification possible |
| 4 | Major | Major damage to operations, large-scale data exposure | Affects critical systems; large-scale PII/CUI exposure; recovery in weeks; regulatory action likely |
| 5 | Critical | Complete loss of capability, catastrophic data breach | Affects life safety or national security; massive data exposure; extended outage; existential organizational threat |

### Risk Matrix

```
                        IMPACT
              1        2        3        4        5
         ┌────────┬────────┬────────┬────────┬────────┐
    5    │   5    │  10    │  15    │  20    │  25    │
         │  MED   │  HIGH  │  HIGH  │  CRIT  │  CRIT  │
L   4    │   4    │   8    │  12    │  16    │  20    │
I        │  LOW   │  MED   │  HIGH  │  CRIT  │  CRIT  │
K   3    │   3    │   6    │   9    │  12    │  15    │
E        │  LOW   │  MED   │  MED   │  HIGH  │  HIGH  │
L   2    │   2    │   4    │   6    │   8    │  10    │
I        │  LOW   │  LOW   │  MED   │  MED   │  HIGH  │
H   1    │   1    │   2    │   3    │   4    │   5    │
O        │  LOW   │  LOW   │  LOW   │  LOW   │  MED   │
O        └────────┴────────┴────────┴────────┴────────┘
D
```

### Risk Response Thresholds

| Score | Level | Suggested Response | Timeline |
|-------|-------|-------------------|----------|
| 1-4 | LOW | Accept, monitor, or address opportunistically | As resources permit |
| 5-9 | MEDIUM | Mitigate through planned remediation | Within 180 days |
| 10-15 | HIGH | Prioritize remediation; escalate to management | Within 90 days |
| 16-25 | CRITICAL | Immediate action required; executive notification | Within 30 days or immediately |

## Control Effectiveness Rating

When a control is in place but its effectiveness needs to be scored:

| Rating | Effectiveness | Description |
|--------|-------------|-------------|
| 5 | Very Effective | Control fully addresses the risk; well-documented, tested, monitored |
| 4 | Effective | Control substantially addresses the risk; minor gaps in documentation or monitoring |
| 3 | Moderately Effective | Control partially addresses the risk; notable gaps in implementation or enforcement |
| 2 | Minimally Effective | Control provides limited risk reduction; significant implementation deficiencies |
| 1 | Ineffective | Control does not meaningfully reduce risk; exists on paper only or is misconfigured |
| 0 | Non-Existent | No control in place |

### Residual Risk Calculation

**Inherent Risk Score** = Likelihood × Impact (before controls)
**Control Effectiveness Factor** = Average control effectiveness / 5 (normalized to 0-1 scale)
**Residual Risk Score** = Inherent Risk × (1 - Control Effectiveness Factor)

Example:
- Inherent risk: Likelihood 4 × Impact 4 = 16 (Critical)
- Control effectiveness: 3 (Moderately Effective) → Factor = 3/5 = 0.6
- Residual risk: 16 × (1 - 0.6) = 6.4 → 6 (Medium)

## Maturity Model

### NIST-Aligned Maturity Levels

| Level | Name | Characteristics | Evidence |
|-------|------|----------------|----------|
| 1 | Initial / Ad Hoc | Processes are unpredictable, poorly controlled, reactive | No documented procedures; tribal knowledge; inconsistent execution |
| 2 | Repeatable | Basic processes established but inconsistently followed | Documented procedures exist; some training; manual execution; limited metrics |
| 3 | Defined | Processes are characterized, standardized, and documented organization-wide | Standard operating procedures; role-based training; consistent execution; basic metrics |
| 4 | Managed | Processes are measured, controlled, and monitored | KPIs tracked; regular reviews; automated controls; exception handling defined |
| 5 | Optimized | Focus on continuous improvement through quantitative feedback | Predictive metrics; lessons learned integrated; automation maximized; benchmarking against peers |

### Maturity Assessment Rubric

For each control family, assess maturity across these dimensions:

**Policy & Documentation**
- Level 1: No policy or outdated
- Level 2: Policy exists, not regularly reviewed
- Level 3: Policy current, approved, communicated
- Level 4: Policy reviewed per schedule, exceptions tracked
- Level 5: Policy continuously refined based on effectiveness data

**Process & Implementation**
- Level 1: Ad hoc, person-dependent
- Level 2: Some documented processes
- Level 3: Standardized, consistently applied
- Level 4: Measured and monitored
- Level 5: Automated, continuously optimized

**Training & Awareness**
- Level 1: No training program
- Level 2: Basic awareness, ad hoc training
- Level 3: Role-based training program
- Level 4: Training effectiveness measured
- Level 5: Adaptive training based on threat landscape

**Monitoring & Measurement**
- Level 1: No monitoring
- Level 2: Manual, periodic reviews
- Level 3: Regular monitoring, basic metrics
- Level 4: Automated monitoring, KPIs, dashboards
- Level 5: Predictive analytics, continuous improvement

**Technology & Automation**
- Level 1: Manual processes only
- Level 2: Basic tools
- Level 3: Integrated tooling
- Level 4: Automated workflows
- Level 5: AI/ML-enhanced, self-healing

## POA&M Risk Prioritization

When creating the Plan of Action & Milestones, prioritize items using this hierarchy:

1. **Critical findings** (score 16-25) — Assign immediately, executive sponsor required
2. **High findings** (score 10-15) — Assign within 2 weeks, management oversight
3. **Medium findings** (score 5-9) — Assign within 30 days, standard remediation
4. **Low findings** (score 1-4) — Track for next assessment cycle

For each POA&M item, capture:
- Finding ID and description
- Associated control(s)
- Risk score (inherent and residual)
- Planned remediation action
- Responsible individual/team
- Estimated completion date
- Resources required
- Milestones with dates
- Status (Open / In Progress / Completed / Risk Accepted)
