# Structure of Repository

.
├─ .env
├─ .venv/                     # (local) Python virtual environment
├─ artifacts/                 # saved models, thresholds, plots, PDF reports
├─ data/
│  ├─ raw/
│  │  ├─ metadata_regen_clean.csv
│  │  ├─ metadata_wilk_aligned.csv
│  │  ├─ metadata_wilk_clean.csv
│  │  └─ RMBR4-2_export_test.csv
│  ├─ interim/
│  └─ processed/
├─ logs/                      # rotating file logs
├─ reports/                   # generated PDFs/PNGs (also copied to artifacts/)
├─ DataExtractionAnalysis/
│  ├─ __init__.py
│  └─ dataextractionanalysis.py
├─ DataPreparation/
│  ├─ __init__.py
│  └─ datapreparation.py
├─ ModelSelection/
│  ├─ __init__.py
│  └─ modelselection.py
├─ ModelTraining/
│  ├─ __init__.py
│  └─ modeltraining.py
├─ ModelEvaluationValidation/
│  ├─ __init__.py
│  └─ modelevaluationvalidation.py
├─ TrainedMLModel/
│  ├─ __init__.py
│  └─ trainedmlmodel.py
├─ scripts/
│  ├─ __init__.py
│  └─ playback.py
├─ Orchestrator_main.py       # CLI entry point (main)
└─ requirements.txt

# Streaming-Data-for-Predictive-Maintenance-with-Linear-Regression-Based-Alerts
📂 Practical Lab 1: Streaming Data for Predictive Maintenance with Linear Regression-Based Alerts

## Project Summary
This task simulates a Predictive Maintenance scenario, where early alerts and errors can flag potential failures before they occur.

## ❗ Clarify the Problem

Issue: Torque Tube Failure – 480 Minutes of Downtime
Root cause is the age of the equipment.
Roadblocks: Options to monitor equipment health are limited.
GAP: Lack of a tool to avoid reactive response to equipment breakdown.  

---

### 1. 🧭 Material Handling Operations
![Image Description](./images/KawasakiMaterialsHandling.png)


### ⚠️ What Goes Wrong Without ProperMaintenance
![Image Description](./images/KawasakiFailureCondition.png)

### 2. 📉 Robot Controller Hardware Configuration
![Image Description](./images/KawasakiASTerminalControl.png)

### 3. 📉 Collecting Data from the Robot Controller
![Image Description](./images/ASATerminalTelnetDataCollect.png)

### 4. 🧠 Predictive Maintenance Use Case
![Image Description](./images/FailurePredictionUseCase.png)

### 5. ✅ Predictive Maintenance (PM) Architecture
![Image Description](./images/PM_Architecture.png)

### 6. ➡️ PM Dashboard Design.
![Image Description](./images/PM_SampleDashboard.png)

### Setup Instruction

