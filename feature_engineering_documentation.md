# 🧠 Feature Engineering Documentation

## Introduction
Feature Engineering is the process of using domain knowledge to create new variables that make machine learning algorithms work better. For the Customer Churn project, 5 new features were synthesized from the raw data.

## Engineered Features Directory

### 1. `Tenure_Years`
* **Formula:** `Tenure / 12.0`
* **Rationale:** While tenure in months is useful, grouping tenure into years can help algorithms easily identify annual contract renewal cycles, which are high-risk periods for churn.

### 2. `Avg_Charge_Per_Month`
* **Formula:** `TotalCharges / (Tenure + 1)`
* **Rationale:** A customer's `MonthlyCharges` might fluctuate (e.g., adding/removing services). This feature calculates their *historical* average monthly spend.

### 3. `Is_High_Spender`
* **Formula:** `Binary Flag (MonthlyCharges > 80)`
* **Rationale:** High-paying customers often expect premium service and exhibit different churn triggers than budget customers. This binary feature explicitly isolates the premium segment.

### 4. `Is_New_Customer`
* **Formula:** `Binary Flag (Tenure <= 6)`
* **Rationale:** Industry data suggests the highest risk of churn occurs in the first 6 months (the "onboarding" phase). This feature helps the model apply different risk weights to new users.

### 5. `Log_TotalCharges`
* **Formula:** `np.log1p(TotalCharges)`
* **Rationale:** The `TotalCharges` distribution is highly right-skewed (many people pay a little, few pay a lot). Applying a logarithmic transformation normalizes the curve, satisfying the mathematical assumptions of linear ML models.