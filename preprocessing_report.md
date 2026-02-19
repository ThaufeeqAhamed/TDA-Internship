# ⚙️ Data Preprocessing Report

## 1. Project Overview
This report details the data preprocessing pipeline constructed for the Customer Churn Prediction project. The goal was to clean, transform, and scale raw data to ensure it is optimized for Machine Learning algorithms.

## 2. Handling Missing Data & Outliers
* **Missing Values:** The `TotalCharges` column contained empty strings which were coerced to `NaN` and subsequently filled with `0` (representing customers in their first month).
* **Outlier Detection:** Used the **Interquartile Range (IQR)** method on `MonthlyCharges`. Calculations confirmed that $Q1 = 35.5$ and $Q3 = 89.85$. No extreme outliers were detected beyond the $1.5 \times IQR$ boundaries, so capping was not required.

## 3. Categorical Data Encoding (3 Methods Used)
Machine Learning models require numerical inputs. We applied three distinct encoding strategies:
1. **Label Encoding:** Applied to the target variable (`Churn`) to map 'Yes'/'No' to `1`/`0`.
2. **Ordinal Encoding:** Applied to the `Contract` feature because it has an inherent mathematical order (`Month-to-month` < `One year` < `Two year`).
3. **One-Hot Encoding:** Applied to `PaymentMethod` and `PaperlessBilling`. This creates binary dummy variables to prevent the model from assuming an artificial ranking between payment types.

## 4. Feature Scaling (2 Techniques Used)
Different algorithms (like Logistic Regression or KNN) are highly sensitive to the scale of data.
1. **Standardization (StandardScaler):** Applied to `MonthlyCharges` and `Log_TotalCharges`. This transforms the data to have a mean of 0 and a standard deviation of 1.
2. **Normalization (MinMaxScaler):** Applied to `Tenure` and `Avg_Charge_Per_Month` to bind the values strictly between `0` and `1`.

## 5. Pipeline Architecture
The entire transformation process was unified using `sklearn.compose.ColumnTransformer`. This ensures that when new customer data arrives, it can be processed identically with a single `.transform()` method, preventing data leakage.