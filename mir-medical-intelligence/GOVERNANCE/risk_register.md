# Hazard & Risk Management Register (ISO 14971 / EU AI Act Alignment)

## 1. Classification & Scope
This system is developed strictly as a research platform. Any future clinical deployment evaluation must align with EU MDR Rule 11 and EU AI Act high-risk AI system requirements.

## 2. Hazard Matrix
| Hazard ID | Failure Mode | Severity | Probability | Risk Level | Mitigation Strategy |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **HAZ-001** | False reassure from partial lab panel | High | Medium | Medium | Explicit data-coverage indicator & uncertainty interval |
| **HAZ-002** | Distributional shift across hospitals | High | High | High | Mandatory temporal & external validation pipelines |
| **HAZ-003** | Over-reliance on uncalibrated probabilities | Medium | High | Medium | Temperature scaling / Isotonic calibration verification |
| **HAZ-004** | Agent hallucination in clinical report | High | Low | High | Hard programmatic constraints & schema validation |
