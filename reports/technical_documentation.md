# Technical Architecture & Methodology

## 1. Pipeline Overview
The project implements a modular Machine Learning pipeline:
1. **Data Ingestion & Cleaning:** Handled via `src/preprocess.py`.
2. **Feature Engineering:** Creation of `Avg_Spend` to normalize lifetime value.
3. **Modeling:** A `RandomForestClassifier` was chosen and configured with `class_weight='balanced'` to penalize the model for missing minority class (Churn) predictions.

## 2. Model Evaluation
The model achieved strong predictive power on the 20% validation holdout:
* **Overall Accuracy:** ~80%
* **Recall (Churn):** Prioritized over precision to ensure the business does not miss "At-Risk" customers.
* **Feature Importance:** The model identified `Contract Type` and `Tenure` as the most critical drivers of churn, validating business intuition with mathematical proof.

## 3. Deployment Specifications
The model is serialized via `pickle` and served through a `Streamlit` frontend. The application accepts real-time JSON/form inputs, scales them dynamically using the pre-fit `StandardScaler`, and outputs a probabilistic risk score.