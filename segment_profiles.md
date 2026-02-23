# 👥 Customer Segment Profiles

## Overview
Using **K-Means Clustering** and the Elbow Method, the customer base was partitioned into exactly 3 distinct behavioral segments based on `Tenure` and `MonthlyCharges`. 

## 1. Segment A: New/Budget Users (Approx. 40-50%)
* **Characteristics:** Short tenure (typically < 20 months) and low monthly spending (< $40).
* **Behavior:** Highly price-sensitive. They are often testing the service on a month-to-month basis.
* **Risk Level:** High risk of churn due to lack of financial or contractual commitment.

## 2. Segment B: Loyal High-Spenders (Approx. 25-30%)
* **Characteristics:** Long tenure (50+ months) and high monthly spending ($80+).
* **Behavior:** Deeply integrated into the product ecosystem. They likely utilize premium services (Fiber, multiple add-ons).
* **Risk Level:** Low risk of churn. They represent the core revenue drivers.

## 3. Segment C: Mid-Tier/At-Risk Users (Approx. 25-30%)
* **Characteristics:** Moderate to short tenure with surprisingly high monthly bills ($70 - $110).
* **Behavior:** These users are paying premium prices but have not been with the company very long.
* **Risk Level:** Extreme risk of churn. They are likely experiencing "bill shock" or feel they are not getting enough value for their premium payment early in their lifecycle.