# Expense Tracker App using Data Science

A data-driven Expense Tracker App built with Python, Pandas, NumPy, Matplotlib, Seaborn, and Streamlit. Track, categorize, analyze, and visualize your expenses to make better financial decisions. Built with synthetic data — ideal for student portfolios, placements, and internships.

🔗 **Live Demo / Repo:** `https://github.com/YOUR-USERNAME/Expense-Tracker-App-using-Data-Science`

---

## 📌 Project Overview

**Project Title:** Expense Tracker App using Data Science  
**Objective:** To build a data-driven app that allows users to track, categorize, and visualize their expenses, enabling better financial decision-making through insights.  
**Industry Relevance:** Expense tracking is a key feature in FinTech, banking, and personal finance platforms used for budgeting, categorization, and spending insights. Companies like Google Pay, CRED, Mint, Razorpay, Paytm, Splitwise, and PhonePe use similar data-driven systems.

---

## 🎯 Problem Statement

Most individuals and small businesses do not have a clear picture of where their money goes each month. Without categorized, time-based expense data, it is difficult to:
- Set and stick to budgets
- Identify overspending categories
- Plan savings and investments
- Make data-driven financial decisions

Students and early professionals often lack access to real financial datasets, making it hard to build portfolio projects that demonstrate data analysis skills.

---

## 💡 Solution

The **Expense Tracker App** solves this by:
1. Generating **synthetic expense data** (no real financial data needed)
2. **Cleaning** the data (dates, amounts, duplicates, missing categories)
3. **Analyzing** spending by category, month, and payment method
4. **Visualizing** trends with bar, line, and pie charts
5. **Detecting overspending** against defined budgets
6. Generating **actionable insights and recommendations**

All wrapped in an interactive **Streamlit dashboard** for exploration.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| Synthetic data generation | 6–12 months of realistic expense records with reproducible seed |
| Data cleaning | Date parsing, numeric conversion, missing value handling, duplicate removal |
| Category analysis | Total and average spend by category with % of total |
| Monthly trends | Month-over-month spending changes and peaks/valleys |
| Payment method analysis | Spend split across UPI, Credit Card, Debit Card, Cash, Wallet |
| Budget comparison | Actual vs. budget per category with overspending flags |
| Visualizations | 4 charts: category bar, monthly trend line, category share pie, payment method bar |
| Insights report | Auto-generated Markdown report with top category, highest month, recommendations |
| Streamlit dashboard | Interactive filters (date, category, payment method) with live KPIs |
| Jupyter notebook | EDA demo for exploration and presentation |

---

## 🛠 Tech Stack

| Layer | Tool |
|-------|------|
| Language | Python 3.x |
| Data manipulation | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Dashboard | Streamlit |
| Storage | CSV files |
| Version control | Git + GitHub |

**Selected stack:** Option B — Intermediate (recommended for students)

---

## 📁 Folder Structure

```
Expense-Tracker-App-using-Data-Science/
├── .gitignore
├── README.md
├── requirements.txt
├── main.py
├── data/
│   ├── expenses_raw.csv
│   ├── expenses_clean.csv
│   └── expenses_enriched.csv
├── notebooks/
│   └── expense_analysis.ipynb
├── src/
│   ├── data_generator.py
│   ├── data_cleaning.py
│   ├── analysis.py
│   ├── visualization.py
│   └── insights.py
├── outputs/
│   ├── eda_summary.txt
│   ├── analysis_results.csv
│   ├── category_spend.png
│   ├── monthly_trend.png
│   ├── category_share.png
│   ├── payment_method.png
│   └── insights_report.md
├── images/
│   ├── category_spend.png
│   ├── monthly_trend.png
│   ├── category_share.png
│   └── payment_method.png
└── docs/
    ├── step1_project_explanation.md
    ├── step2_tech_stack.md
    ├── step3_project_architecture.md
    ├── step4_implementation_plan.md
    ├── step5_folder_structure.md
    ├── step6_installation_guide.md
    ├── step7_full_project_code.md
    ├── step8_virtual_simulation.md
    ├── step9_how_to_run.md
    └── step10_github_upload.md
```

---

## 🚀 How to Run

### Prerequisites
- Python 3.8+
- pip
- Internet connection (for library installation)

### Step 1: Clone or download
```bash
git clone https://github.com/YOUR-USERNAME/Expense-Tracker-App-using-Data-Science.git
cd Expense-Tracker-App-using-Data-Science
```

### Step 2: Create and activate virtual environment
```powershell
# Windows
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```
```bash
# Mac / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the full pipeline
```bash
python main.py
```

### Step 5: Launch the dashboard (optional)
```bash
streamlit run main.py --dashboard
```

---

## 📊 Results

### Sample Output (10 months of synthetic data)

**EDA Summary:**
- Total Records: 266
- Total Spend: Rs. 493,023.77
- Average Transaction: Rs. 1,853.47
- Date Range: 2024-01-03 to 2024-10-28
- Categories: 8 (Food, Travel, Rent, Utilities, Entertainment, Shopping, Health, Other)
- Payment Methods: 5

**Top Spending Category:** Rent (Rs. 276,475.07, 56.08% of total)  
**Highest Spending Month:** 2024-01 (Rs. 66,212.93)  
**Lowest Spending Month:** 2024-05 (Rs. 30,558.65)

### Generated Outputs
| Output | Location |
|--------|----------|
| Cleaned data | `data/expenses_clean.csv` |
| Analysis results | `outputs/analysis_results.csv` |
| Insights report | `outputs/insights_report.md` |
| Category chart | `outputs/category_spend.png` |
| Monthly trend chart | `outputs/monthly_trend.png` |
| Category share chart | `outputs/category_share.png` |
| Payment method chart | `outputs/payment_method.png` |

---

## 📸 Screenshots

Add the following screenshots to your README for a polished GitHub profile:

1. **Project folder structure** — File explorer showing all folders
2. **Terminal pipeline run** — `python main.py` completing all stages
3. **Category spend chart** — Bar chart with Rent as top category
4. **Monthly trend chart** — Line chart showing peaks and valleys
5. **Category share pie chart** — Percentage breakdown of spending
6. **Payment method chart** — UPI vs Card vs Cash split
7. **Insights report** — Markdown report with recommendations
8. **Streamlit dashboard** — Browser with KPIs, filters, and charts
9. **Dashboard with filter applied** — Category filter set to a specific value

---

## 🧠 Virtual Simulation

The app simulates realistic expense behavior:
- **Rent** appears as large, fixed monthly amounts (~₹11,000 each)
- **Food/Shopping** appear as many small transactions that add up
- Some months spike (January) due to rent + shopping clustering
- Other months dip (May) when fewer large expenses occur
- Overspending is detected by comparing actual spend vs. monthly budgets per category

See `docs/step8_virtual_simulation.md` for the full step-by-step simulation guide.

---

## 📈 Workflow

```
Data Input → Storage → Cleaning → Categorization → Aggregation → Analysis
                                                       ↓
                                               Visualization → Insights → Decision-Making
```

---

## 🎓 Who This Is For

- **Students** building placement/internship portfolios
- **Data Analysts** demonstrating EDA and visualization skills
- **Business Analysts** showing budget tracking and cost control analysis
- **Financial Analysts** presenting spending insights and recommendations

---

## 📝 License

This project is for educational and portfolio purposes. Feel free to use, modify, and extend it.

---

## 🔗 Connect

- **GitHub:** `https://github.com/YOUR-USERNAME`
- **LinkedIn:** `https://linkedin.com/in/YOUR-PROFILE`

---

## 🙏 Acknowledgments

Built as part of the "Expense Tracker App using Data Science" student project. Inspired by real-world FinTech expense tracking systems.

---

*Generated with synthetic data — no real financial information used.*