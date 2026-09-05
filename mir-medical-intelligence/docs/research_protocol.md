# Comprehensive Research Protocol (v2.2)

## 1. Scope & Research Boundaries
MIR Medical Intelligence is a laboratory-first clinical intelligence research platform.
- **In-Scope**: Routine non-imaging laboratory tests (CBC, BMP, CMP, LFTs, lipid panels, inflammatory markers), longitudinal EHR trajectory modeling, disease outcome predictions, missingness-aware reasoning, adaptive next-test selection.
- **Out-of-Scope (Initial Phase)**: CT, X-ray, MRI, ultrasound, pathology slides, ECG waveforms (reserved for Track F / Stage 4 Multimodal expansion).

## 2. Research Tracks (A through F)
1. **Track A (Data Harmonization & Physiological Anomaly Detection)**: LOINC mapping, canonical schema normalization, unsupervised anomaly benchmarks (NHANES, MIMIC-IV).
2. **Track B (Disease-Specific Baseline Benchmarks)**: Logistic regression, XGBoost, LightGBM, CatBoost benchmarks for acute/chronic outcomes.
3. **Track C (Longitudinal, Sequential & Survival Models)**: Temporal deep learning (RNN/LSTM/Transformer), survival curves (Cox, Random Survival Forests, DeepSurv).
4. **Track D (External Validation & Shift Evaluation)**: Evaluating performance drop under cross-institutional shift (MIMIC-IV to eICU / UK Biobank).
5. **Track E (Federated Laboratory Intelligence)**: Privacy-preserving multi-institutional training (Flower / NVIDIA FLARE).
6. **Track F (Constrained Agentic Clinical Orchestration)**: Structured agent workflow for evidence ingestion, safety verification, and report synthesis.
