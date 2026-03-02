import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

def clean_and_prepare_data(filepath):
    """Loads, cleans, and encodes the churn dataset."""
    df = pd.read_csv(filepath)
    
    # Handle missing TotalCharges
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce').fillna(0)
    
    # Encode categorical target and key features
    le = LabelEncoder()
    df['Churn'] = le.fit_transform(df['Churn'])
    df['Contract'] = le.fit_transform(df['Contract'])
    df['PaperlessBilling'] = le.fit_transform(df['PaperlessBilling'])
    
    # Create an engineered feature: Avg Monthly Spend
    df['Avg_Spend'] = df['TotalCharges'] / (df['Tenure'] + 1)
    
    return df