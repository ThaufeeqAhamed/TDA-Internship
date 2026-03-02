import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Page Config
st.set_page_config(page_title="Churn Predictor", page_icon="📊", layout="centered")

@st.cache_resource
def load_models():
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    return model, scaler

model, scaler = load_models()

# UI Header
st.title("🛡️ Customer Retention AI")
st.markdown("Enter customer metrics below to evaluate their churn risk probability in real-time.")
st.divider()

# Input Form
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        tenure = st.number_input("Tenure (Months)", min_value=0, max_value=120, value=12)
        monthly_charges = st.number_input("Monthly Charges ($)", min_value=0.0, value=65.0)
        total_charges = tenure * monthly_charges
    with col2:
        contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
        senior = st.selectbox("Is Senior Citizen?", ["No", "Yes"])

# Preprocess Inputs
contract_map = {"Month-to-month": 0, "One year": 1, "Two year": 2}
senior_map = {"No": 0, "Yes": 1}
avg_spend = total_charges / (tenure + 1) if tenure > 0 else monthly_charges

if st.button("Analyze Risk", type="primary", use_container_width=True):
    # Array matches: ['Tenure', 'MonthlyCharges', 'TotalCharges', 'Contract', 'Avg_Spend', 'SeniorCitizen']
    input_data = np.array([[
        tenure, monthly_charges, total_charges, 
        contract_map[contract], avg_spend, senior_map[senior]
    ]])
    
    input_scaled = scaler.transform(input_data)
    probability = model.predict_proba(input_scaled)[0][1]
    
    st.divider()
    st.subheader("Analysis Results")
    
    # Visual Progress Bar for Risk
    st.progress(float(probability))
    
    if probability > 0.60:
        st.error(f"🚨 **CRITICAL RISK (Probability: {probability:.1%})**")
        st.write("This customer is highly likely to cancel. Immediate intervention required.")
        st.info("💡 **Recommendation:** Offer a 15% discount to upgrade to an annual contract.")
    elif probability > 0.30:
        st.warning(f"⚠️ **MODERATE RISK (Probability: {probability:.1%})**")
        st.write("This customer shows signs of dissatisfaction.")
    else:
        st.success(f"✅ **SAFE (Probability: {probability:.1%})**")
        st.write("This customer exhibits strong loyalty metrics.")