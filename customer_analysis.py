import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def find_column(df, keywords):
    cols = df.columns.tolist()
    for col in cols:
        col_lower = col.lower()
        for keyword in keywords:
            if keyword.lower() in col_lower:
                return col
    return None

def normalise_join_id(series):
    extracted = series.astype(str).str.extract(r"(\d+)")[0]
    return pd.to_numeric(extracted, errors="coerce")

def clean_missing_values(df):
    for col in df.select_dtypes(include=['int64', 'float64']).columns:
        df[col] = df[col].fillna(df[col].mean())
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].fillna('Unknown')
    return df

def main():
    print("Customer Sales Analysis\n")

    # Create required folders
    os.makedirs("visualizations", exist_ok=True)

    sales_path = os.path.join('data', 'sales_data.csv')
    churn_path = os.path.join('data', 'customer_churn.csv')

    if not os.path.exists(sales_path) or not os.path.exists(churn_path):
        print("Data files not found. Please ensure 'sales_data.csv' and 'customer_churn.csv' are in the 'data' directory.")
        return

    sales_df = pd.read_csv(sales_path)
    churn_df = pd.read_csv(churn_path)

    print("Sales Data Shape:", sales_df.shape)
    print("Churn Data Shape:", churn_df.shape)

    sales_df = clean_missing_values(sales_df)
    churn_df = clean_missing_values(churn_df)

    sales_col = find_column(sales_df, ['total_sales', 'sales', 'revenue', 'amount'])
    product_col = find_column(sales_df, ['product', 'item', 'goods'])
    customer_id_sales = find_column(sales_df, ["customer_id", "customerid", "custid", "client_id", "id"])

    if sales_col is None or product_col is None or customer_id_sales is None:
        print("Required columns not found in sales data.")
        return

    customer_id_churn = find_column(churn_df, ["customerid", "customer_id", "custid", "client_id", "id"])
    contract_col = find_column(churn_df, ["contract"])
    payment_col = find_column(churn_df, ["paymentmethod", "payment_method", "payment"])

    if customer_id_sales is None or customer_id_churn is None:
        print("Customer ID columns not found in one of the datasets.")
        return

    print("\nMerging datasets...")

    sales_df["join_id"] = normalise_join_id(sales_df[customer_id_sales])
    churn_df["join_id"] = normalise_join_id(churn_df[customer_id_churn])

    sales_df = sales_df.dropna(subset=["join_id"])
    churn_df = churn_df.dropna(subset=["join_id"])

    sales_df["join_id"] = sales_df["join_id"].astype(int)
    churn_df["join_id"] = churn_df["join_id"].astype(int)

    merged_df = pd.merge(sales_df, churn_df, on="join_id", how="inner")

    print(f"Merge Completed. Matched Records: {len(merged_df)}")

    if len(merged_df) == 0:
        print("No matching records found after merge. Please check the Customer ID columns.")
        return

    total_revenue = merged_df[sales_col].sum()
    avg_revenue = merged_df[sales_col].mean()
    max_sale = merged_df[sales_col].max()
    min_sale = merged_df[sales_col].min()

    top_customers = merged_df.groupby(customer_id_sales)[sales_col].sum().sort_values(ascending=False).head(5)
    top_products = merged_df.groupby(product_col)[sales_col].sum().sort_values(ascending=False).head(5)

    print("\nKey Metrics:")
    print("Total Revenue:", total_revenue)
    print("Average Revenue:", avg_revenue)
    print("Maximum Sale:", max_sale)
    print("Minimum Sale:", min_sale)

    print("\nTop 5 Customers:")
    print(top_customers)
    print("\nTop 5 Products:")
    print(top_products)

    # Visualization 1: Sales by Contract (Bar Chart)
 
    contract_plot_saved = False
    if contract_col is not None:
        contract_sales = merged_df.groupby(contract_col)[sales_col].sum().sort_values(ascending=False)

        plt.figure(figsize=(10, 6))
        sns.barplot(x=contract_sales.index, y=contract_sales.values,color="green")
        plt.title("Total Sales by Contract Type")
        plt.xlabel("Contract Type")
        plt.ylabel("Total Sales")
        plt.xticks(rotation=25)
        plt.tight_layout()
        plt.savefig("visualizations/sales_by_contract.png")
        plt.close()

        contract_plot_saved = True

    # Visualization 2: Heatmap (Pivot Table)
   
    heatmap_saved = False
    pivot_table = None

    if payment_col is not None and product_col is not None:
        pivot_table = pd.pivot_table(
            merged_df,
            index=payment_col,
            columns=product_col,
            values=sales_col,
            aggfunc="sum",
            fill_value=0
        )

        plt.figure(figsize=(12, 8))
        sns.heatmap(pivot_table, annot=False, cmap="YlGnBu")
        plt.title("Heatmap: Product Sales by Payment Method")
        plt.tight_layout()
        plt.savefig("visualizations/payment_method_heatmap.png")
        plt.close()

        heatmap_saved = True

    # Visualization 3: Top Customers Chart
    
    plt.figure(figsize=(10, 6))
    top_customers.plot(kind="bar", color=["red", "green", "blue", "orange", "purple"])
    plt.title("Top 5 Customers by Total Sales")
    plt.xlabel("Customer")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=25)
    plt.tight_layout()
    plt.savefig("visualizations/top_customers.png")
    plt.close()

    # Visualization 4: Top 10 Products by Total Sales
    top_10_products = merged_df.groupby(product_col)[sales_col].sum().sort_values(ascending=False).head(10)

    plt.figure(figsize=(10, 6))
    top_10_products.plot(kind="bar")
    plt.title("Top 10 Products by Total Sales")
    plt.xlabel("Product")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=25)
    plt.tight_layout()
    plt.savefig("visualizations/top_10_products.png")
    plt.close()

    # Visualization 5: Sales Distribution (Histogram)
    plt.figure(figsize=(10, 6))
    sns.histplot(merged_df[sales_col], bins=20, kde=True)
    plt.title("Sales Distribution")
    plt.xlabel("Sales Amount")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("visualizations/sales_distribution.png")
    plt.close()

    # Visualization 6: Sales Boxplot (Outlier Detection)
    plt.figure(figsize=(8, 5))
    sns.boxplot(y=merged_df[sales_col])
    plt.title("Sales Boxplot (Outlier Detection)")
    plt.ylabel("Sales Amount")
    plt.tight_layout()
    plt.savefig("visualizations/sales_boxplot.png")
    plt.close()

    # Visualization 7: Total Sales by Payment Method
    payment_plot_saved = False
    if payment_col is not None:
        payment_sales = merged_df.groupby(payment_col)[sales_col].sum().sort_values(ascending=False)

    plt.figure(figsize=(10, 6))
    sns.lineplot(x=payment_sales.index, y=payment_sales.values, marker="o")

    plt.title("Total Sales by Payment Method (Line Plot)")
    plt.xlabel("Payment Method")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=25)
    plt.tight_layout()
    plt.savefig("visualizations/sales_by_payment_method.png")
    plt.close()

    payment_plot_saved = True

    # Visualization 8: Average Sales by Contract Type
    avg_contract_plot_saved = False
    if contract_col is not None:
        avg_contract_sales = merged_df.groupby(contract_col)[sales_col].mean().sort_values(ascending=False)

        plt.figure(figsize=(10, 6))
        sns.barplot(x=avg_contract_sales.index, y=avg_contract_sales.values)
        plt.title("Average Sales by Contract Type")
        plt.xlabel("Contract Type")
        plt.ylabel("Average Sales")
        plt.xticks(rotation=25)
        plt.tight_layout()
        plt.savefig("visualizations/avg_sales_by_contract.png")
        plt.close()

        avg_contract_plot_saved = True

    # Save analysis_report.md

    report = []
    report.append("# Customer Sales Analysis Report (Week 5)\n")

    report.append("## Executive Summary")
    report.append(f"- Total matched records after merge: **{len(merged_df)}**")
    report.append(f"- Total Revenue: **₹{total_revenue:,.2f}**")
    report.append(f"- Average Revenue: **₹{avg_revenue:,.2f}**")
    report.append(f"- Highest Sale: **₹{max_sale:,.2f}**")
    report.append(f"- Lowest Sale: **₹{min_sale:,.2f}**\n")

    report.append("## Top 5 Customers")
    report.append("```")
    report.append(top_customers.to_string())
    report.append("```\n")

    report.append("## Top 5 Products")
    report.append("```")
    report.append(top_products.to_string())
    report.append("```\n")

    report.append("## Pivot Table Summary")
    if pivot_table is not None:
        report.append("Pivot Table (Payment Method vs Product Sales):")
        report.append("```")
        report.append(pivot_table.to_string())
        report.append("```\n")
    else:
        report.append("Pivot table could not be generated because required columns were not found.\n")

    report.append("## Visualizations Generated")
    report.append("- `visualizations/top_customers.png`")
    report.append("- `visualizations/top_10_products.png`")
    report.append("- `visualizations/sales_distribution.png`")
    report.append("- `visualizations/sales_boxplot.png`")
    report.append(f"- `visualizations/sales_by_contract.png`{'' if contract_plot_saved else ' (Contract column not found)'}")
    report.append(f"- `visualizations/payment_method_heatmap.png`{'' if heatmap_saved else ' (Payment/Product column not found)'}")
    report.append(f"- `visualizations/sales_by_payment_method.png`{'' if payment_plot_saved else ' (Payment column not found)'}")
    report.append(f"- `visualizations/avg_sales_by_contract.png`{'' if avg_contract_plot_saved else ' (Contract column not found)'}\n")

    report.append("## Advanced Pandas Concepts Used")
    report.append("- GroupBy + Aggregation")
    report.append("- Filtering and Sorting")
    report.append("- Merge / Join using normalized Customer IDs")
    report.append("- Pivot Tables for cross-analysis")
    report.append("- Data Cleaning + Missing value handling")
    report.append("- Distribution Analysis (Histogram + KDE)")
    report.append("- Outlier Detection (Boxplot)\n")

    with open("analysis_report.md", "w", encoding="utf-8") as f:
        f.write("\n".join(report))

    print("\nanalysis_report.md generated successfully!")
    print("Charts saved inside visualizations/")
    print("\nCOMPLETED SUCCESSFULLY.")

if __name__ == "__main__":
    main()
