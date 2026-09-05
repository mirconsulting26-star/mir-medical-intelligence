# Data Governance & Privacy Protocol

## 1. Patient Data Privacy & Compliance
- **Zero Raw Data in Public VCS**: Restricted patient-level datasets (e.g., MIMIC-IV, eICU, UK Biobank) must NEVER be committed to Git, GitHub, OSF, or Zenodo.
- **Data Use Agreements (DUA)**: Credentialed access (via PhysioNet / CITI Training) belongs strictly to the authorized researcher. Credentials and access tokens must never be shared.
- **De-identification**: Only derived, non-identifiable aggregate stats, synthetic data, or public open files (e.g. NHANES public release) are stored locally in `data/interim` or `data/processed`.

## 2. Dataset Access Log
| Dataset | Access Tier | Credentialed Researcher | DUA Status | Local Path (Ignored by Git) |
| :--- | :--- | :--- | :--- | :--- |
| NHANES | Public Open | Mir AbdulRehman & Co-Researcher | Active | `data/raw/nhanes/` |
| MIMIC-IV | Credentialed Tier 2 | Authorized Researcher | PhysioNet Approved | `data/raw/mimiciv/` |
| eICU | Credentialed Tier 2 | Authorized Researcher | PhysioNet Approved | `data/raw/eicu/` |
| Synthea | Synthetic Open | Mir AbdulRehman | Open | `data/raw/synthea/` |
