# 📊 Week 6: Interactive Sales Dashboard

## 📝 Project Overview
**Goal:** Design a professional dashboard to analyze sales trends, customer segmentation, and product performance. 

This project implements a **Hybrid Visualization Strategy**:
1.  **Statistical Analysis (Seaborn):** Used for deep-dives into data distribution (Box Plots) and feature correlations (Heatmaps).
2.  **Interactive Exploration (Plotly):** Used for dynamic trend tracking and drill-down analysis with hover capabilities.

## 📂 Code Structure
The repository is organized to separate logic (scripts), presentation (notebooks), and output (visualizations).

```text
week-6/
├── dashboard.py          # Main execution script (Generates all outputs)
├── dashboard.ipynb       # Interactive presentation notebook (for Demo)
├── sales_data.csv        # Source dataset
├── requirements.txt      # Python dependencies
├── dashboard_demo.gif    # Video demonstration of interactivity
├── visualizations/       # Folder containing generated assets
│   ├── 1_correlation_heatmap.png
│   ├── 2_sales_boxplot.png
│   ├── 3_region_violin.png
│   ├── 4_static_dashboard_grid.png
│   └── interactive_dashboard.html
└── README.md             # Project documentation
```

## Setup Instructions
1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
 
2. **Generate Visualizations**
   ```bash
   python dashboard.py
   
3. **Run the Presentation**
   ```bash
   jupyter notebook dashboard.ipynb

## 📈 Dashboard Guide & Interpretations
1. **Correlation Matrix (Heatmap)**
2. **Sales Distribution (Box Plot)**
3. **Sales Trend (Interactive Line Chart)**
4. **Regional Performance (Interactive Pie/Bar)**
   
## 🛠️ Technical Details
**Data Cleaning**: Implemented in dashboard.py. Missing numeric values are imputed with the mean, and missing categorical values are labeled as "Unknown".

**Architecture:** Backend: Pandas for data manipulation.

**Static Engine:** Matplotlib/Seaborn for high-resolution exportable images.

**Dynamic Engine:** Plotly Graph Objects for HTML-based interactive rendering.

## ✅ Testing Evidence
**Automated Generation:** The dashboard.py script automatically creates the visualizations/ directory if it does not exist.

**Interactivity Check:** The dashboard_demo.gif file demonstrates the hover and zoom functionality working in real-time.
