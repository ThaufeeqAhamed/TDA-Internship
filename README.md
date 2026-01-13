# 📊 Week 5: Customer Sales & Churn Analysis

## 🚀 Project Overview
This project is an advanced data engineering and analysis pipeline designed to merge disparate datasets—**Sales Transactions** and **Customer Churn Profiles**. 

Unlike standard analysis scripts, this tool includes a **robust data cleaning engine** that normalizes inconsistent Customer IDs using Regular Expressions, ensuring a 100% match rate between datasets. It generates a comprehensive suite of **8 visualizations** to uncover deep insights into how customer contract types and payment methods influence purchasing behavior.

## 🛠️ Key Technical Features
- **Advanced Data Merging:** Implemented an `INNER JOIN` logic with a custom ID normalization function (`Regex`) to handle format mismatches (e.g., `CUST001` vs `C00001`).
- **Automated Data Cleaning:** Smart handling of missing values (filling numeric gaps with means and categorical gaps with placeholders).
- **Statistical Analysis:** Includes Outlier Detection (Boxplots) and Distribution Analysis (Histograms/KDE).
- **Dynamic Reporting:** Automatically detects column names (making the script adaptable) and generates a Markdown summary report.

## 📂 Repository Structure
```text
├── data/
│   ├── sales_data.csv        # Transactional data
│   └── customer_churn.csv    # Customer profile data
├── visualizations/           # Folder containing auto-generated charts
│   ├── payment_method_heatmap.png
│   ├── sales_boxplot.png
│   ├── top_customers.png
│   └── ... (5 others)
├── analysis_report.md        # Auto-generated text summary of metrics
├── customer_analysis.py      # Main executable script
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## ⚙️ Setup & Installation

1. **Clone the Repository**
   ```bash
   git clone <your-repo-url>
   git checkout week-5
 
2. **Clone the Repository**
   ```bash
   pip install pandas seaborn matplotlib
   
3. **Clone the Repository**
   ```bash
   python customer_analysis.py
   
## 📈 Visualizations Generated

The script automatically performs a deep-dive analysis and saves the following charts:

1. **Top Customers:** Identifies the "Whales" (highest spending clients).
2. **Product Heatmap:** Cross-analyzes Payment Methods vs. Product categories.
3. **Sales Distribution:** Histogram + KDE to show transaction frequency.
4. **Outlier Detection:** Boxplot to identify extreme sales values.
5. **Contract Analysis:** Bar charts showing Total and Average sales by contract length.


## 📊 Sample Insights
- **Total Revenue Analyzed:** $12,365,048

- **Top Selling Product:** Laptop

- **Highest Value Customer:** CUST016 ($373,932 Lifetime Value)

## 🧩 Libraries Used
- **Pandas:** For DataFrames, merging, and pivot tables.

- **Seaborn:** For statistical visualizations (Heatmaps, Boxplots).

- **Matplotlib:** For base plotting configuration.

- **OS:** For file system management.
