import pandas as pd
import matplotlib.pyplot as plt
import os

def main():
    print("--- 📊 Starting Data Visualization Project ---")

    # 1. Setup Paths
    data_path = os.path.join('data', 'sales_data.csv')
    viz_path = 'visualizations'
    
    # Ensure folders exist
    os.makedirs(viz_path, exist_ok=True)
    os.makedirs('report', exist_ok=True)

    # 2. Load and Clean Data
    if not os.path.exists(data_path):
        print("❌ Error: 'sales_data.csv' not found in 'data/' folder.")
        return

    df = pd.read_csv(data_path)
    
    # Cleaning: Fill missing numeric values with mean, text with 'Unknown'
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].mean())
        
    print(f"✅ Data Loaded: {len(df)} rows found.")

    # 3. Visualization 1: Sales by Product (Bar Chart)
    # Requirement: Compare categories
    print("🎨 Generating Bar Chart...")
    product_sales = df.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False)
    
    plt.figure(figsize=(10, 6))
    product_sales.plot(kind='bar', color='green')
    plt.title('Total Sales by Product')
    plt.xlabel('Product')
    plt.ylabel('Sales ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(viz_path, 'sales_by_product_bar.png'))
    plt.close()

    # 4. Visualization 2: Sales Distribution by Region (Pie Chart)
    # Requirement: Show parts of a whole
    if 'Region' in df.columns:
        print("🎨 Generating Pie Chart...")
        region_sales = df.groupby('Region')['Total_Sales'].sum()
        
        plt.figure(figsize=(8, 8))
        plt.pie(region_sales, labels=region_sales.index, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
        plt.title('Sales Distribution by Region')
        plt.axis('equal')
        plt.savefig(os.path.join(viz_path, 'sales_by_region_pie.png'))
        plt.close()

    # 5. Visualization 3: Daily Sales Trend (Line Chart)
    # Requirement: Show trends over time
    if 'Date' in df.columns:
        print("🎨 Generating Line Chart...")
        df['Date'] = pd.to_datetime(df['Date'])
        daily_sales = df.groupby('Date')['Total_Sales'].sum()
        
        plt.figure(figsize=(12, 6))
        daily_sales.plot(kind='line', marker='o', color='red', linestyle='-')
        plt.title('Daily Sales Trend')
        plt.xlabel('Date')
        plt.ylabel('Total Sales ($)')
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(os.path.join(viz_path, 'sales_trend_line.png'))
        plt.close()

    # 6. Generate Text Report
    total_revenue = df['Total_Sales'].sum()
    best_product = product_sales.idxmax()
    
    report_content = f"""# 📊 Sales Analysis Report

## Executive Summary
- **Total Revenue:** ${total_revenue:,.2f}
- **Top Performing Product:** {best_product}

## Visualizations Generated
1. **Sales by Product:** stored in `visualizations/sales_by_product_bar.png`
2. **Regional Distribution:** stored in `visualizations/sales_by_region_pie.png`
3. **Sales Trend:** stored in `visualizations/sales_trend_line.png`
"""

    with open(os.path.join('report', 'summary.md'), "w", encoding="utf-8") as f:
        f.write(report_content)

    print("\n✅ Success! Check the 'visualizations' and 'report' folders.")

if __name__ == "__main__":
    main()