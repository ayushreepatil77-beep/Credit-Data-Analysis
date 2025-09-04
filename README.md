# Credit Data Analysis

**Goal:** Analyze credit card client data to extract insights and trends.

## Dataset
- Source: Sample data inspired by the UCI Credit Card Dataset
- Columns:
  - ID: Client ID
  - LIMIT_BAL: Credit limit
  - SEX: 1 = Male, 2 = Female
  - EDUCATION: 1 = Graduate, 2 = University, 3 = High School, 4 = Others
  - MARRIAGE: 1 = Married, 2 = Single, 3 = Others
  - AGE: Client age
  - default.payment.next.month: 0 = No default, 1 = Default

## Analysis Performed
- Age and credit limit distributions
- Correlation heatmap of features
- Count and percentage of clients defaulting on payments

## Key Insights
- Majority of clients are aged 25–50
- ~12% of clients defaulted in the sample dataset
- Some correlation observed between credit limit and default

## Tools
- Python
- Pandas, Matplotlib, Seaborn
- Jupyter Notebook
