import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os

def main():
    print("Interactive Sales Dashboard")
    
    os.makedirs('visualizations', exist_ok=True)
    sns.set_theme(style="whitegrid", palette="pastel")
    try:
        df = pd.read_csv('sales_data.csv')
        print(f" Data Loaded: {len(df)} rows")
    except FileNotFoundError:
        print(" Error: 'sales_data.csv' not found.")
        return

    num_cols = df.select_dtypes(include=['number']).columns
    df[num_cols] = df[num_cols].fillna(df[num_cols].mean())
    
    cat_cols = df.select_dtypes(include=['object']).columns
    df[cat_cols] = df[cat_cols].fillna("Unknown")

    date_col = next((c for c in df.columns if 'date' in c.lower()), None)
    if date_col:
        df[date_col] = pd.to_datetime(df[date_col])

    print("\nGenerating Seaborn Statistical Plots...")

    plt.figure(figsize=(10, 8))
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    corr = numeric_df.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('Correlation Matrix Heatmap')
    plt.tight_layout()
    plt.savefig('visualizations/1_correlation_heatmap.png')
    plt.close()

    plt.figure(figsize=(12, 6))
    sns.boxplot(x='Product', y='Total_Sales', data=df)
    plt.title('Sales Distribution by Product (Box Plot)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('visualizations/2_sales_boxplot.png')
    plt.close()

    plt.figure(figsize=(12, 6))
    if 'Region' in df.columns:
        sns.violinplot(x='Region', y='Total_Sales', data=df)
        plt.title('Sales Density by Region (Violin Plot)')
        plt.tight_layout()
        plt.savefig('visualizations/3_region_violin.png')
        plt.close()

    print("Generating 2x2 Static Dashboard Grid...")
    fig, axes = plt.subplots(2, 2, figsize=(18, 12))
    fig.suptitle(' Statistical Sales Overview (Seaborn)', fontsize=20, weight='bold')

    sales_by_product = df.groupby('Product')['Total_Sales'].sum().reset_index()
    sns.barplot(ax=axes[0,0], x='Product', y='Total_Sales', data=sales_by_product, palette='viridis')
    axes[0,0].set_title('Total Sales by Product')
    axes[0,0].tick_params(axis='x', rotation=45)

    sns.boxplot(ax=axes[0,1], x='Region', y='Total_Sales', data=df, palette='Set2')
    axes[0,1].set_title('Sales Distribution by Region')

    if date_col:
        daily_sales = df.groupby(date_col)['Total_Sales'].sum().reset_index()
        sns.lineplot(ax=axes[1,0], x=date_col, y='Total_Sales', data=daily_sales, marker='o', color='purple')
        axes[1,0].set_title('Sales Trend Over Time')
        axes[1,0].tick_params(axis='x', rotation=45)

    sns.histplot(ax=axes[1,1], data=df, x='Total_Sales', kde=True, color='green')
    axes[1,1].set_title('Transaction Value Distribution')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig('visualizations/4_static_dashboard_grid.png')
    plt.close()

    print("\n✨ Generating Plotly Interactive Elements...")

    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=("Sales Trend (Interactive)", "Regional Breakdown", "Product Performance", "Price vs Sales"),
        specs=[[{"type": "xy"}, {"type": "domain"}], 
               [{"type": "xy"}, {"type": "xy"}]]
    )

    if date_col:
        daily_sales = df.groupby(date_col)['Total_Sales'].sum().reset_index()
        fig.add_trace(
            go.Scatter(x=daily_sales[date_col], y=daily_sales['Total_Sales'], mode='lines+markers', name='Trend'),
            row=1, col=1
        )

    if 'Region' in df.columns:
        region_sales = df.groupby('Region')['Total_Sales'].sum().reset_index()
        fig.add_trace(
            go.Pie(labels=region_sales['Region'], values=region_sales['Total_Sales'], hole=0.4, name='Region'),
            row=1, col=2
        )

    prod_sales = df.groupby('Product')['Total_Sales'].sum().reset_index()
    fig.add_trace(
        go.Bar(x=prod_sales['Product'], y=prod_sales['Total_Sales'], name='Product'),
        row=2, col=1
    )

    fig.add_trace(
        go.Scatter(x=df['Price'], y=df['Total_Sales'], mode='markers', name='Correlation', 
                   marker=dict(color=df['Quantity'], colorscale='Viridis', showscale=True)),
        row=2, col=2
    )

    fig.update_layout(height=800, width=1200, title_text=" Interactive Sales Dashboard (Plotly)", template="plotly_white")

    fig.write_html("visualizations/interactive_dashboard.html")
    print("Interactive Dashboard saved to 'visualizations/interactive_dashboard.html'")
    print(" All visualizations generated successfully.")

if __name__ == "__main__":
    main()