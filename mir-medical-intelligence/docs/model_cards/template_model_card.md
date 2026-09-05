# Model Card Template

## Model Overview
- **Model Name**: `[e.g. MIR-CBC-XGBoost-v1]`
- **Model Version**: `1.0.0`
- **Model Type**: Gradient Boosted Decision Trees (XGBoost)
- **Target Outcome**: `[e.g. 30-day Acute Kidney Injury / Mortality]`

## Intended Use
- **Primary Use**: Non-diagnostic research benchmarking.
- **Out-of-Scope**: Direct automated clinical triage or diagnostic determination without clinician review.

## Training & Evaluation Data
- **Training Set**: MIMIC-IV (n = 40,000 encounters, train split).
- **Validation Set**: Internal temporal split + External eICU evaluation.

## Performance & Metrics
- **AUROC**: `0.842 (95% CI: 0.828 - 0.856)`
- **AUPRC**: `0.615 (95% CI: 0.592 - 0.638)`
- **Expected Calibration Error (ECE)**: `0.021`

## Limitations & Subgroup Performance
- Reduced performance observed in severe thrombocytopenia (< 50 x10^3/uL).
