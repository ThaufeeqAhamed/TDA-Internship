# Customer Sales Analysis Report (Week 5)

## Executive Summary
- Total matched records after merge: **100**
- Total Revenue: **₹12,365,048.00**
- Average Revenue: **₹123,650.48**
- Highest Sale: **₹373,932.00**
- Lowest Sale: **₹6,540.00**

## Top 5 Customers
```
Customer_ID
CUST016    373932
CUST007    363870
CUST083    350888
CUST073    349510
CUST020    333992
```

## Top 5 Products
```
Product
Laptop        3889210
Tablet        2884340
Phone         2859394
Headphones    1384033
Monitor       1348071
```

## Pivot Table Summary
Pivot Table (Payment Method vs Product Sales):
```
Product           Headphones   Laptop  Monitor    Phone   Tablet
PaymentMethod                                                   
Bank Transfer         142088  2117341   246942   536619  1473843
Credit Card           623956   788359   769358  1746168   411644
Electronic Check      617989   983510   331771   576607   998853
```

## Visualizations Generated
- `visualizations/top_customers.png`
- `visualizations/top_10_products.png`
- `visualizations/sales_distribution.png`
- `visualizations/sales_boxplot.png`
- `visualizations/sales_by_contract.png`
- `visualizations/payment_method_heatmap.png`
- `visualizations/sales_by_payment_method.png`
- `visualizations/avg_sales_by_contract.png`

## Advanced Pandas Concepts Used
- GroupBy + Aggregation
- Filtering and Sorting
- Merge / Join using normalized Customer IDs
- Pivot Tables for cross-analysis
- Data Cleaning + Missing value handling
- Distribution Analysis (Histogram + KDE)
- Outlier Detection (Boxplot)
