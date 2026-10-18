# Step 9 - How to Run Project: Expense Tracker App

Complete instructions to run the Expense Tracker App, expected outputs, charts, and reports.

---

## Prerequisites

- Python 3.8+ installed
- Virtual environment activated
- Dependencies installed (`pip install -r requirements.txt`)

---

## Method 1: Run the full pipeline (CLI)

This generates synthetic data, cleans it, runs analysis, creates charts, and produces the insights report.

### Windows (PowerShell)

```powershell
# 1. Navigate to project folder
cd "C:\Users\kumar\OneDrive\Desktop\Ayush_Kumar_Dubey\Data Science\Project (4)\Expense-Tracker-App-using-Data-Science"

# 2. Activate virtual environment
.\.venv\Scripts\Activate.ps1

# 3. Run the pipeline
python main.py
```

### Mac / Linux (Terminal)

```bash
# 1. Navigate to project folder
cd "Expense-Tracker-App-using-Data-Science"

# 2. Activate virtual environment
source .venv/bin/activate

# 3. Run the pipeline
python main.py
# or
python3 main.py
```

### Expected terminal output

```
[main] Starting Expense Tracker pipeline...

============================================================
Running data_generator.py...
============================================================
[data_generator] Generated 269 synthetic expense records.
[data_generator] Saved to data\expenses_raw.csv
[data_generator] Date range: 2024-01-03 to 2024-10-28

============================================================
Running data_cleaning.py...
============================================================
[data_cleaning] Cleaned dataset: 266 rows (removed 3).
[data_cleaning] Saved cleaned data to data\expenses_clean.csv

============================================================
Running analysis.py...
============================================================
[analysis] EDA Summary:
  total_records: 266
  total_spend: 493023.77
  ...

============================================================
Running visualization.py...
============================================================
[visualization] Saved outputs\category_spend.png and images\category_spend.png
[visualization] All charts generated successfully.

============================================================
Running insights.py...
============================================================
[insights] Saved insights report to outputs\insights_report.md

[main] Pipeline complete. Check outputs/ and images/ for results.
```

---

## Method 2: Launch the Streamlit dashboard

Interactive web dashboard with filters, charts, and insights report.

### Command

```powershell
# Windows
python main.py --dashboard

# or directly with streamlit
streamlit run main.py --dashboard
```

```bash
# Mac / Linux
python main.py --dashboard
# or
streamlit run main.py --dashboard
```

### Expected result

- Streamlit starts a local web server (usually `http://localhost:8501`)
- Browser opens automatically or you open the URL manually
- Dashboard shows:
  - KPI metrics: Total Spend, Avg per Transaction, Total Transactions
  - Date Range, Category, and Payment Method filters
  - Bar chart: Spending by Category
  - Line chart: Monthly Spending Trend
  - Category Share table
  - Bar chart: Spend by Payment Method
  - Expense Records data table
  - Insights Report section

### To stop the dashboard

Press `Ctrl + C` in the terminal where Streamlit is running.

---

## Method 3: Skip data generation (use existing raw data)

If you already have `data/expenses_raw.csv` and want to re-run cleaning/analysis without regenerating:

```powershell
python main.py --skip-data-gen
```

---

## Expected outputs

After running the pipeline, these files are created:

| File | Location | Description |
|------|----------|-------------|
| Raw dataset | `data/expenses_raw.csv` | ~269 synthetic expense records |
| Cleaned dataset | `data/expenses_clean.csv` | ~266 cleaned records |
| EDA summary | `outputs/eda_summary.txt` | Key statistics (total spend, avg, date range) |
| Analysis results | `outputs/analysis_results.csv` | Category, monthly, payment, budget tables |
| Insights report | `outputs/insights_report.md` | Markdown report with recommendations |
| Category chart | `outputs/category_spend.png` | Bar chart: total spend by category |
| Monthly trend chart | `outputs/monthly_trend.png` | Line chart: monthly spending trend |
| Category share chart | `outputs/category_share.png` | Pie chart: category % of total |
| Payment chart | `outputs/payment_method.png` | Bar chart: spend by payment method |

Charts are also copied to `images/` for README display.

---

## Sample expected results

Based on the synthetic data (Jan–Oct 2024):

- **Total Spend:** Rs. 493,023.77
- **Top Category:** Rent (56.08% of total)
- **Highest Month:** 2024-01 (Rs. 66,212.93)
- **Lowest Month:** 2024-05 (Rs. 30,558.65)
- **All categories** flagged vs. monthly budgets with overspending details

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `python` not found | Use `py` or `python3` instead |
| `streamlit` command not found | Use `python -m streamlit run main.py --dashboard` |
| Activation blocked (Windows) | Run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` |
| No data found | Run `python main.py` first (without `--skip-data-gen`) |
| Charts not generated | Ensure `analysis.py` ran before `visualization.py` (pipeline handles order) |

---

## Verification checklist

- [ ] `python main.py` completes without errors
- [ ] `data/expenses_clean.csv` exists
- [ ] `outputs/analysis_results.csv` exists
- [ ] 4 PNG charts exist in `outputs/` and `images/`
- [ ] `outputs/insights_report.md` exists
- [ ] `streamlit run main.py --dashboard` opens in browser

---

**Step 9 complete.** You can now run the project via CLI pipeline or Streamlit dashboard, with all expected outputs documented.

Please reply with **"c"** to acknowledge Step 9, and I will proceed to Step 10 (GitHub Upload Steps).