# NIST AI Risk Management Framework (AI RMF 1.0) Reference

## Overview

The NIST AI RMF (January 2023) provides a voluntary framework for managing risks associated with AI systems throughout their lifecycle. It complements existing frameworks like 800-53 and CSF by addressing AI-specific risks: bias, transparency, reliability, safety, privacy, and security.

The companion document **NIST AI 600-1** (Generative AI Profile) extends the AI RMF with specific guidance for generative AI systems.

## Core Structure

The AI RMF is organized into **4 Functions** and **19 Categories**, each with associated subcategories (actions and outcomes).

### GOVERN

Cultivate and implement a culture of risk management within organizations designing, developing, deploying, or using AI systems.

| Category | ID | Description |
|----------|----|-------------|
| Policies and processes | GV.1 | Policies, processes, procedures, and practices across the organization are in place, transparent, and implemented effectively |
| Accountability structures | GV.2 | Accountability structures are in place so that the appropriate teams and individuals are empowered, responsible, and trained for mapping, measuring, and managing AI risks |
| Workforce diversity | GV.3 | Workforce diversity, equity, inclusion, and accessibility processes are prioritized in the mapping, measuring, and managing of AI risks |
| Organizational commitments | GV.4 | Organizational teams are committed to a culture that considers and communicates AI risk |
| Policies for third-party AI | GV.5 | Processes are in place for robust engagement with relevant AI Actors |
| Risk management integration | GV.6 | Policies and procedures are in place to address AI risks and benefits arising from third-party software and data and other supply chain issues |

### MAP

Context is established and understood. AI risks related to mapping the AI system are identified.

| Category | ID | Description |
|----------|----|-------------|
| Intended purpose | MAP.1 | Context is established and understood |
| Categorization | MAP.2 | Categorization of the AI system is performed |
| Benefits and costs | MAP.3 | AI capabilities, targeted usage, goals, and expected benefits and costs are understood |
| Risks and impacts | MAP.4 | Risks and benefits are mapped for all components of the AI system including third-party software and data |
| Impact characterization | MAP.5 | Impacts to individuals, groups, communities, organizations, and society are characterized |

### MEASURE

Identified risks are assessed, analyzed, or tracked. Metrics and methodologies are applied.

| Category | ID | Description |
|----------|----|-------------|
| Appropriate metrics | ME.1 | Appropriate methods and metrics are identified and applied |
| AI systems evaluated | ME.2 | AI systems are evaluated for trustworthy characteristics |
| Mechanisms for tracking | ME.3 | Mechanisms for tracking identified AI risks over time are in place |
| Feedback mechanisms | ME.4 | Feedback about efficacy of measurement is collected and incorporated into AI system updates |

### MANAGE

Risks are prioritized and acted upon. Plans to maximize benefits and minimize negative impacts are executed.

| Category | ID | Description |
|----------|----|-------------|
| Risk prioritization | MG.1 | AI risks based on assessments and other analytical output are prioritized, responded to, and managed |
| Risk treatment strategies | MG.2 | Strategies to maximize AI benefits and minimize negative impacts are planned, prepared, implemented, documented, and informed by input from relevant AI actors |
| Risk management monitoring | MG.3 | AI risks and benefits from third-party entities are managed |
| Risk communication | MG.4 | Risk treatments, including response and recovery, and communication plans are monitored and maintained |

## Trustworthy AI Characteristics

The AI RMF defines seven characteristics of trustworthy AI. Assessments should evaluate each:

1. **Valid and Reliable** — AI system performs as intended and consistently under expected conditions
2. **Safe** — AI system does not endanger human life, health, property, or the environment
3. **Secure and Resilient** — AI system maintains confidentiality, integrity, availability; withstands adverse conditions
4. **Accountable and Transparent** — Appropriate access to information about the AI system is available; responsibility is clear
5. **Explainable and Interpretable** — Outputs and processes can be understood by relevant stakeholders
6. **Privacy-Enhanced** — AI system protects human autonomy and dignity through privacy values
7. **Fair with Harmful Bias Managed** — AI system proactively addresses and manages bias and promotes equity

## AI RMF to 800-53 Mapping

AI systems still need underlying IT security controls. Key mappings:

| AI RMF Area | Related 800-53 Families |
|---|---|
| GV (Govern) | PM, PL, RA, AT |
| MAP (Map) | RA, SA, PT |
| MEASURE (Measure) | CA, SI, AU |
| MANAGE (Manage) | IR, CP, CM |
| Data governance | PT, MP, SC |
| Security of AI systems | AC, IA, SC, SI |
| Supply chain for AI | SR, SA |
| AI model integrity | SI-7, SC-28, CM-3 |
| Monitoring and logging | AU-2, AU-3, SI-4, CA-7 |

## Generative AI Profile (AI 600-1) Additions

For generative AI systems, additional risks to assess:

- **CBRN Information** — Can the system provide dangerous information about chemical, biological, radiological, or nuclear threats?
- **Confabulation** — Does the system generate plausible but false information?
- **Data Privacy** — Are personal data used in training? Can the system reveal training data?
- **Environmental Impact** — What are the computational and energy costs?
- **Harmful Bias and Homogenization** — Does the system perpetuate or amplify biases?
- **Human-AI Configuration** — Are appropriate human oversight mechanisms in place?
- **Information Integrity** — Can the system be used to generate disinformation?
- **Information Security** — Is the system vulnerable to prompt injection, data poisoning, model theft?
- **Intellectual Property** — Does the system respect IP rights in training data and outputs?
- **Obscene, Degrading, and/or Abusive Content** — Can the system generate harmful content?
- **Value Chain and Component Integration** — Are third-party components assessed for risk?

## Assessment Approach

1. Identify all AI systems in scope (inventory)
2. For each AI system, assess against the 4 functions and 19 categories
3. Evaluate each trustworthy AI characteristic
4. For generative AI, additionally evaluate against AI 600-1 risk areas
5. Score maturity and identify gaps
6. Prioritize and create remediation plans
7. Map findings to underlying 800-53 controls where applicable
