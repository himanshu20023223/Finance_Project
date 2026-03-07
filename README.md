# Finance_Project
Turned 7 months of real-world personal spending data into a full analytics pipeline — from messy multi-sheet Excel files to a clean, insight-driven dashboard. Covers data wrangling, EDA, category-wise breakdowns, and payment behavior analysis.
# 💸 Personal Finance Analytics & Expense Predictor
> *Because your money deserves better than a spreadsheet.*

A complete end-to-end data analytics project built on **7 months of real personal spending data** (Aug 2025 – Mar 2026). Covers everything from raw multi-sheet Excel wrangling to exploratory analysis, visual dashboards, and an upcoming ML model to predict future expenses.

---

## 📌 Project Stages

| Stage | Description | Status |
|-------|-------------|--------|
| 1 | Data Collection & Raw Excel Tracking | ✅ Done |
| 2 | Data Cleaning & Master Dataset Creation | ✅ Done |
| 3 | Exploratory Data Analysis (EDA) | ✅ Done |
| 4 | Dashboard & Visualizations | ✅ Done |
| 5 | ML Model — Expense Predictor | 🔄 In Progress |

---

## 📂 Dataset Overview

- **Source:** Personal spending tracked manually across 7 bi-monthly Excel sheets
- **Period:** August 2025 – March 2026
- **Total Records:** ~300+ transactions
- **Fields:** `Amount`, `Category`, `Description`, `Place`, `Payment-Mode`, `Date`
- **Categories:** Food, Rent, Travel, Supplements, Medicine, Miscellaneous, Education

---

## 🔧 Stage 1–2 : Data Cleaning & Master Dataset

**Problem:** Data was spread across 7 separate Excel sheets with inconsistent column structures, spelling errors, and mixed payment mode formats.

**What was done:**
- Loaded all sheets using `pd.ExcelFile()` and looped through `sheet_names`
- Standardized column names and fixed category typos (e.g. `"miscelanious"` → `"miscellaneous"`)
- Added a `month_period` column to each sheet before merging
- Combined all sheets into one master DataFrame using `pd.concat()`
- Dropped null rows and reset index

**Tools:** Python, Pandas, OpenPyXL

---

## 📊 Stage 3 : Exploratory Data Analysis (EDA)

**Key questions answered:**
- Which category consumed the most budget across 7 months?
- How does spending differ between Jind and Gurgaon?
- What % of spending is fixed (rent) vs discretionary?
- Which payment mode — UPI, Cash, or both — dominates?
- Which month had the highest and lowest spend, and what drove it?

**Tools:** Python, Pandas, Matplotlib, Seaborn

---

## 📈 Stage 4 : Dashboard & Visualizations

**Visuals built:**
- Monthly spending trend (line chart)
- Category-wise expense breakdown (bar + pie chart)
- Payment mode distribution
- Location-based spending comparison (Jind vs Gurgaon)
- Month-over-month delta analysis

**Tools:** Power BI / Tableau

---

## 🤖 Stage 5 : ML Model — Expense Predictor *(In Progress)*

**Goal:** Predict next month's total expenses based on current spending patterns.

**Planned approach:**
- Feature engineering from historical monthly aggregates (per category, per location, payment mode ratios)
- Baseline model: Linear Regression
- Improved model: Random Forest / XGBoost
- Evaluation: MAE, RMSE on holdout months
- Output: Predicted total spend + category-wise breakdown for next month

**Tools:** Scikit-learn, XGBoost, Pandas

---

## 🛠️ Tech Stack

| Area | Tools |
|------|-------|
| Data Wrangling | Python, Pandas, OpenPyXL |
| Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn, Power BI / Tableau |


---

## 📁 Project Structure

```
finance-analytics/
│
├── data/
│   ├── spendings-record.xlsx        # Raw source file, # Cleaned combined dataset
│             
├── dashboard/
│   └── finance_dashboard.pbix       # Power BI file
│
├── src/
│   ├── main.py                       # Core functions 
│   └── model.py                     # ML pipeline (coming soon)
│
└── README.md
```

---

## Key Insights (So Far)

- **UPI is the dominant payment mode**, accounting for the majority of total spend
- **Miscellaneous is the biggest spending trap** — the hardest category to control
- **Rent + Travel together form the largest fixed cost** block each month
- **Spending spikes in the first week** of each period — consistent across all months

---

## What's Next

- Complete the ML expense predictor (Stage 5)
- Build an interactive web dashboard using Streamlit
- Extend dataset to 12 months for better seasonal pattern detection
- Add income data to calculate a monthly **savings rate**

---

## 👤 Author

**Himanshu**  
Aspiring Data Scientist | Python · Pandas · SQL · Power BI · Machine Learning  
[LinkedIn](https://www.linkedin.com/in/himanshu-sharma-b1368931a/) • [GitHub](https://github.com/himanshu20023223)
