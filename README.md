# Bluestock Mutual Fund Analytics Capstone Project

## Overview

The Bluestock Mutual Fund Analytics Capstone Project is a comprehensive end-to-end data analytics and business intelligence solution designed to analyze mutual fund performance, investor behavior, industry trends, and portfolio risk.

The project combines data engineering, ETL pipelines, exploratory data analysis (EDA), financial analytics, risk modeling, dashboard development, and recommendation systems to generate actionable insights for investors and financial decision-makers.

---

# Project Objectives

The primary objectives of the project are:

* Build a robust ETL pipeline for mutual fund datasets.
* Perform data cleaning and validation.
* Analyze industry trends, investor behavior, and fund performance.
* Calculate advanced financial and risk metrics.
* Create interactive Power BI dashboards.
* Develop a risk-based mutual fund recommendation engine.
* Generate professional reports and business intelligence outputs.

---

# Dataset Information

## Raw Datasets (10)

1. 01_fund_master.csv
2. 02_nav_history.csv
3. 03_aum_by_fund_house.csv
4. 04_monthly_sip_inflows.csv
5. 05_category_inflows.csv
6. 06_industry_folio_count.csv
7. 07_scheme_performance.csv
8. 08_investor_transactions.csv
9. 09_portfolio_holdings.csv
10. 10_benchmark_indices.csv

Additional NAV files:

* Axis_Bluechip_NAV.csv
* HDFC_Top_100_Direct_NAV.csv
* ICICI_Bluechip_NAV.csv
* Kotak_Bluechip_NAV.csv
* Nippon_Large_Cap_NAV.csv
* SBI_Bluechip_NAV.csv

---

## Processed Datasets

* nav_history_clean.csv
* investor_transactions_clean.csv
* scheme_performance_clean.csv

---

# Technology Stack

## Programming

* Python

## Data Analysis

* Pandas
* NumPy

## Visualization

* Matplotlib
* Seaborn

## Database

* SQLite

## Dashboarding

* Microsoft Power BI

## Development Environment

* Jupyter Notebook
* VS Code

---
## Project Structure

```text
bluestock_mf_capstone/
│
├── data/
├── notebooks/
├── scripts/
├── charts/
├── dashboard/
├── outputs/
│
├── Final_Report.pdf
├── Bluestock_MF_Presentation.pptx
├── README.md
└── run_pipeline.py
```

# Project Workflow

Raw Data
→ Data Cleaning
→ Data Validation
→ Feature Engineering
→ Exploratory Data Analysis
→ Performance Analytics
→ Advanced Risk Analytics
→ Dashboard Development
→ Reporting & Presentation

---

# ETL Pipeline

The ETL pipeline was developed to process raw mutual fund data into analysis-ready datasets.

### Extract

Data was imported from multiple CSV files representing mutual fund schemes, investor transactions, benchmark indices, portfolio holdings, SIP inflows, and industry statistics.

### Transform

Data cleaning included:

* Missing value handling
* Duplicate removal
* Date standardization
* Column validation
* Data type conversion
* Outlier checking

Feature engineering included:

* Daily Returns
* CAGR
* Sharpe Ratio
* Sortino Ratio
* Alpha
* Beta
* Maximum Drawdown
* VaR
* CVaR
* Rolling Sharpe Ratio

### Load

Processed datasets were exported for analytics and dashboard consumption.

---

# Exploratory Data Analysis (EDA)

More than 15 visualizations were created to understand trends and patterns.

Key analysis areas:

* AUM Growth Trends
* SIP Growth Trends
* Category-wise Inflows
* Investor Demographics
* Geographic Analysis
* State-wise Investments
* Age Group Distribution
* Transaction Type Analysis
* Benchmark Comparison
* Portfolio Allocation Analysis

---

# Fund Performance Analytics

The following metrics were calculated for mutual fund evaluation:

### Return Metrics

* Daily Returns
* CAGR (1-Year)
* CAGR (3-Year)
* CAGR (5-Year)

### Risk Adjusted Metrics

* Sharpe Ratio
* Sortino Ratio

### Benchmark Metrics

* Alpha
* Beta

### Risk Metrics

* Maximum Drawdown

### Fund Scorecard

A composite fund scorecard was developed using:

* 3-Year Returns
* Sharpe Ratio
* Alpha
* Expense Ratio
* Maximum Drawdown

---

# Advanced Risk Analytics

The following advanced analytics were implemented:

### Historical VaR (95%)

Measures potential downside loss under adverse market conditions.

### Conditional VaR (CVaR)

Measures average loss beyond the VaR threshold.

### Rolling 90-Day Sharpe Ratio

Evaluates changing risk-adjusted performance over time.

### Investor Cohort Analysis

Analyzes investor behavior based on first investment year.

### SIP Continuity Analysis

Identifies investors at risk of discontinuing SIP contributions.

### HHI Concentration Analysis

Measures portfolio diversification and concentration risk.

---

# Fund Recommendation System

A simple recommendation engine was developed.

Input:

* Low Risk
* Moderate Risk
* High Risk

Output:

* Top 3 recommended mutual funds based on Sharpe Ratio and Risk Grade.

---

# Power BI Dashboard

A four-page interactive dashboard was developed.

### Page 1 – Industry Overview

* Industry AUM
* SIP Inflows
* Folios
* Fund House Analysis

### Page 2 – Fund Performance

* Risk vs Return Analysis
* Benchmark Comparison
* Fund Scorecard

### Page 3 – Investor Analytics

* Investor Demographics
* Transaction Analysis
* Geographic Distribution

### Page 4 – SIP & Market Trends

* SIP Growth Trends
* Category Inflows
* Heatmap Analysis

---

# Deliverables

## Reports

* Final_Report.pdf
* Bluestock_MF_Presentation.pptx

## Dashboards

* bluestock_mf_dashboard.pbix

## Notebooks

* EDA_Analysis.ipynb
* Performance_Analytics.ipynb
* Advanced_Analytics.ipynb

## Scripts

* recommender.py
* run_pipeline.py

## Analytics Outputs

* fund_scorecard.csv
* alpha_beta.csv
* var_cvar_report.csv
* rolling_sharpe_chart.png
* hhi_concentration_report.csv

---

# How to Run

Clone the repository:

```bash
git clone <repository-url>
```

Install dependencies:

```bash
pip install pandas numpy matplotlib seaborn scipy
```

Run the pipeline:

```bash
python run_pipeline.py
```

Open:

* Jupyter Notebooks for analysis
* Power BI Dashboard (.pbix) for visualization

---

# Author

Anil Pachar

Bluestock Mutual Fund Analytics Capstone Project

Version: v1.0
