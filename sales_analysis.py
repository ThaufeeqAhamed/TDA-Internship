import pandas as pd
import os

def main():
    print("--- Sales Data Analysis Program ---")

    file_path = 'sales_data.csv'
    
    if not os.path.exists(file_path):
        print(" Error: 'sales_data.csv' not found. Please make sure it's in the same folder.")
        return

    try:
        df = pd.read_csv(file_path)
        print(" Data loaded successfully!")
        
        print("\n--- 🔍 Data Overview ---")
        print(df.head())
        print("\nColumns:", df.columns.tolist())

        print("\n--- Cleaning Data ---")
        missing_count = df.isnull().sum().sum()
        print(f"Found {missing_count} missing values.")
        numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
        for col in numeric_cols:
            df[col] = df[col].fillna(df[col].mean())
            
        object_cols = df.select_dtypes(include=['object']).columns
        for col in object_cols:
            df[col] = df[col].fillna("Unknown")
            
        print(" Missing values handled.")
        print("\n---  Analysis Results ---")
        
        sales_col = None
        for col in df.columns:
            if 'sale' in col.lower() or 'revenue' in col.lower() or 'amount' in col.lower():
                sales_col = col
                break
        
        if sales_col:
            total_sales = df[sales_col].sum()
            avg_sales = df[sales_col].mean()
            best_product = "N/A"
            
            product_col = None
            for col in df.columns:
                if 'product' in col.lower() or 'item' in col.lower():
                    product_col = col
                    break
            
            if product_col:
                best_product = df.groupby(product_col)[sales_col].sum().idxmax()

            print(f" Total Sales:      ${total_sales:,.2f}")
            print(f" Average Sales:    ${avg_sales:,.2f}")
            print(f" Best Product:     {best_product}")
            
            with open("analysis_report.md", "w") as f:
                f.write(f"# Sales Analysis Report\n\n")
                f.write(f"- **Total Sales:** ${total_sales:,.2f}\n")
                f.write(f"- **Average Transaction:** ${avg_sales:,.2f}\n")
                f.write(f"- **Best Selling Product:** {best_product}\n")
            print("\n Report generated: 'analysis_report.md'")
            
        else:
            print(" Could not automatically find a 'Sales' column. Please check CSV headers.")

    except Exception as e:
        print(f" An error occurred: {e}")

if __name__ == "__main__":
    main()