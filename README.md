# Diabetes Risk Prediction for Clinical Triage

## Overview

This project presents an end-to-end machine learning pipeline designed to support early-stage diabetes risk screening. Rather than aiming for clinical diagnosis, the system functions as a triage tool, prioritizing sensitivity to identify individuals who should undergo further medical evaluation.

The project emphasizes decision-aware modeling, explicit trade-off management, and interpretability, reflecting real-world constraints commonly encountered in applied machine learning systems.

## Problem Framing

Diabetes often progresses silently for years before diagnosis, leading to severe long-term complications and increased healthcare costs. Healthcare systems face the challenge of identifying high-risk individuals early, while operating under limited clinical resources.

In this context, missing a true diabetic case is significantly more costly than performing additional low-risk follow-up tests. This asymmetry directly influences modeling decisions throughout the project.

## Approach

The project follows a structured machine learning workflow:

- Data cleaning and integrity validation
- Exploratory data analysis guided by clinical hypotheses
- Domain-informed feature engineering
- Model development with emphasis on class imbalance handling
- Threshold optimization aligned with clinical triage requirements
- Model interpretability using SHAP values

## Modeling Highlights

- A Random Forest baseline was used to validate assumptions and establish reference performance.
- Gradient Boosting (XGBoost) was selected to better capture minority class patterns and improve recall.
- Class imbalance was explicitly addressed using scale_pos_weight.
- The classification threshold was adjusted from 0.5 to 0.3 to prioritize recall in a screening context.
- Model interpretability was validated using SHAP to ensure alignment with known clinical risk factors.

## Results

The final model achieves high sensitivity for diabetic cases, successfully identifying the majority of at-risk individuals. While precision decreases as a consequence of threshold adjustment, this trade-off is acceptable within the intended screening context, where false positives incur low operational cost compared to false negatives.

## Repository Structure

- `data/` — Raw and processed datasets
- `notebooks/` — Step-by-step analysis and modeling notebooks
- `src/` — Reusable preprocessing pipeline
- `requirements.txt` — Project dependencies

## Key Takeaways

- Machine learning systems must be aligned with real-world decision constraints.
- Metric optimization should reflect the cost of errors in the target domain.
- Interpretability is a requirement, not an optional feature, in high-stakes applications.
- End-to-end pipeline design is as important as model selection.
