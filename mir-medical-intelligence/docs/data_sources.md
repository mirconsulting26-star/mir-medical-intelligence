# Data Sources & Acquisition Guide

## 1. NHANES (CDC Public Release)
- **Files**: Demographic (`DEMO`), Complete Blood Count (`CBC`), Biochemistry (`BIOPRO`).
- **Format**: SAS Transport (`.XPT`) converted to Parquet/CSV.
- **License**: Public Domain (US Government).

## 2. MIMIC-IV (PhysioNet Credentialed Access)
- **Tables**: `labevents`, `d_labitems`, `patients`, `admissions`, `transfers`.
- **License**: PhysioNet Restricted Data Use Agreement (DUA).
- **Access Constraint**: Requires CITI Data/Specimens Only Research training.
