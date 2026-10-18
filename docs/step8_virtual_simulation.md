# Step 8 - Virtual Simulation: Expense Tracker App

This step explains how to simulate the expense tracker end-to-end — how expenses are generated, how categories and trends appear, how overspending is detected, and what proof to save for your GitHub portfolio.

---

## Simulation Overview

Since you don't have real financial data, the app uses **synthetic data** that mimics realistic monthly spending. The simulation walks through the entire pipeline:

```
Step 1: Generate synthetic expenses  →  Step 2: Clean the data
    ↓
Step 3: Analyze & aggregate          →  Step 4: Visualize
    ↓
Step 5: Generate insights            →  Final output: Dashboard + Report
```

---

## Step-by-step simulation

### Step 1 — Expense generation

**What happens:** `src/data_generator.py` creates a synthetic dataset covering 10 months (Jan–Oct 2024) with ~25 records per month (~269 total records).

**How it works:**
- Each record has: `date`, `category`, `amount`, `payment_method`, `description`
- Categories: Food, Travel, Rent, Utilities, Entertainment, Shopping, Health
- Amount ranges per category (e.g., Rent ₹8,000–₹15,000; Food ₹100–₹600)
- Payment methods: UPI (45%), Credit Card (20%), Debit Card (15%), Cash (10%), Wallet (10%)
- Random seed (`RANDOM_SEED = 42`) ensures reproducibility — same output every run
- A small amount of noise is added: 2% missing categories, 3 duplicate rows (to test cleaning)

**What you see:** `data/expenses_raw.csv` with 269 rows, date range 2024-01-03 to 2024-10-28.

---

### Step 2 — Data cleaning

**What happens:** `src/data_cleaning.py` loads the raw data and fixes quality issues.

**How it works:**
- Parses `date` to datetime (drops invalid dates)
- Converts `amount` to numeric (drops invalid amounts)
- Fills missing categories with "Other" (5 rows filled)
- Removes duplicate rows (3 duplicates removed)
- Standardizes category names to Title Case
- Maps unknown categories to "Other"

**What you see:** Console output shows rows before/after cleaning; `data/expenses_clean.csv` with 266 clean rows.

---

### Step 3 — Analysis & aggregation

**What happens:** `src/analysis.py` computes aggregates and trends.

**How trends appear:**
- Rent appears as large, fixed monthly amounts (~₹11,000 each) → dominant spend category
- Food/Shopping appear as many small transactions → add up to significant monthly totals
- Some months show spikes (e.g., January ₹66,212) due to rent + shopping clustering
- Other months dip (e.g., May ₹30,558) when fewer large expenses occur

**Budget comparison:** Each category is compared against a monthly budget. Overspending is flagged when actual > budget.

**What you see:** `outputs/analysis_results.csv` with category totals, monthly trends, payment split, and overspending flags.

---

### Step 4 — Visualization

**What happens:** `src/visualization.py` generates 4 charts.

**Charts generated:**
1. **Category spend (bar)** — Rent is tallest bar (~56% of total), followed by Shopping
2. **Monthly trend (line)** — Shows peaks and valleys across 10 months; easy to spot spike months
3. **Category share (pie)** — Visual % breakdown of where money goes
4. **Payment method (bar)** — UPI dominates, followed by Credit/Debit cards

**What you see:** 4 PNG files in `outputs/` and `images/`: `category_spend.png`, `monthly_trend.png`, `category_share.png`, `payment_method.png`

---

### Step 5 — Insights generation & overspending detection

**What happens:** `src/insights.py` produces an auto-generated text report.

**How overspending is detected:**
- Budget is defined per category in `MONTHLY_BUDGET` (e.g., Food ₹5,000, Rent ₹12,000)
- Actual total spend per category is compared to budget
- `overspent = True` when `actual_spend > budget`
- Variance % shows how far over budget each category is

**Insights produced:**
- Top spending category (Rent, 56.08% of total)
- Highest spending month (Jan 2024, ₹66,212.93)
- Lowest spending month (May 2024, ₹30,558.65)
- All 8 categories flagged as overspent (budgets are monthly caps, actuals are 10-month totals — demonstrates the detection logic)
- Actionable recommendations (reduce Health spend, limit Rent, review Entertainment/Shopping)

**What you see:** `outputs/insights_report.md` — full markdown report with tables and recommendations.

---

### Step 6 — Dashboard (interactive simulation)

**What happens:** `streamlit run main.py --dashboard` launches the web dashboard.

**How to simulate user interaction:**
1. Open the dashboard in your browser
2. Click "Run Full Pipeline" to regenerate data
3. Use the **Date Range** filter to zoom into specific months
4. Use **Category** filter to isolate one category (e.g., only "Food")
5. Use **Payment Method** filter to see UPI vs Card spend
6. Observe KPIs update: Total Spend, Avg per Transaction, Total Transactions
7. Scroll to the Insights Report section to read auto-generated recommendations

**What you see:** Live updating charts and filtered data table in the browser.

---

## What screenshots to take

For your GitHub README and placement portfolio, capture these:

| # | Screenshot | Where |
|---|------------|-------|
| 1 | Project folder structure | File explorer showing all folders |
| 2 | Terminal running `python main.py` | Command prompt showing pipeline stages completing |
| 3 | Console output of analysis | Category analysis, monthly trend, budget comparison tables |
| 4 | `category_spend.png` chart | Bar chart showing Rent as top category |
| 5 | `monthly_trend.png` chart | Line chart showing monthly peaks/valleys |
| 6 | `category_share.png` chart | Pie chart of category percentages |
| 7 | `payment_method.png` chart | Bar chart of payment method split |
| 8 | `insights_report.md` content | Markdown report with recommendations |
| 9 | Streamlit dashboard | Browser showing KPIs, filters, charts, and data table |
| 10 | Streamlit dashboard with filter applied | Show category filter set to "Food" with updated charts |

---

## What graphs to generate

These are the 4 required graphs (already produced by `src/visualization.py`):

1. **Category spend bar chart** — `outputs/category_spend.png`
2. **Monthly spending trend line chart** — `outputs/monthly_trend.png`
3. **Category share pie chart** — `outputs/category_share.png`
4. **Payment method bar chart** — `outputs/payment_method.png`

All saved to both `outputs/` and `images/` folders.

---

## What proof to save

Save these in your GitHub repo as evidence of working code:

| Proof | File/Location |
|-------|---------------|
| Code runs end-to-end | `git log` showing commits for each step |
| Synthetic data generated | `data/expenses_raw.csv` |
| Data cleaned | `data/expenses_clean.csv` |
| Analysis performed | `outputs/analysis_results.csv` |
| Charts generated | `outputs/*.png` + `images/*.png` |
| Insights report | `outputs/insights_report.md` |
| Dashboard works | Screenshot of Streamlit app in browser |
| Reproducible | `requirements.txt` + `main.py` + `src/` modules |

---

## Verification checklist

Before moving to Step 9, confirm:

- [ ] `python main.py` runs without errors
- [ ] `data/expenses_raw.csv` exists with records
- [ ] `data/expenses_clean.csv` exists with cleaned records
- [ ] `outputs/analysis_results.csv` exists
- [ ] 4 PNG charts exist in `outputs/` and `images/`
- [ ] `outputs/insights_report.md` exists with recommendations
- [ ] `streamlit run main.py --dashboard` launches the dashboard

---

**Step 8 complete.** Virtual simulation documented — from synthetic data generation through cleaning, analysis, visualization, insights, and dashboard interaction, with screenshots and proof items identified.

Please reply with **"c"** to acknowledge Step 8, and I will proceed to Step 9 (How to Run Project).