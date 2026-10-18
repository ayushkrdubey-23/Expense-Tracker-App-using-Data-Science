# Step 3 - Project Architecture: Expense Tracker App

## 1. Input

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| date | datetime | Date of expense | 2024-01-15 |
| category | string | Expense category | Food |
| amount | float | Amount spent | 250.00 |
| payment_method | string | Mode of payment | UPI |
| description | string | Optional note | Lunch at cafe |

## 2. Processing

| Stage | Operation | Purpose |
|-------|-----------|---------|
| Data cleaning | Parse dates, convert amounts to numeric, handle missing values, remove duplicates | Ensure reliable analysis |
| Categorization | Assign standard categories (Food, Travel, Rent, Utilities, Entertainment, Shopping, Health) | Group similar spends |
| Aggregation | Sum amounts by category, month, payment method | Compute totals and shares |
| Trend analysis | Month-over-month change, rolling averages, category-wise trend | Detect spending patterns |
| Budget comparison | Compare actual vs. planned budget per category | Flag overspending |

## 3. Output

| Output | Format | Description |
|--------|--------|-------------|
| Cleaned dataset | CSV | Cleaned expense records |
| Category report | CSV / text | Total and % spend per category |
| Monthly trend report | CSV / text | Total spend per month |
| Charts | PNG images | Bar, line, pie charts |
| Insights report | Markdown / text | Auto-generated text insights |
| Dashboard | Streamlit web app | Interactive filters and live charts |

## 4. Text-based architecture diagram

```
┌─────────────────────────────────────────────────────────────┐
│                        LAYER 1: INPUT                        │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │ User Input  │  │ Synthetic   │  │   Uploaded CSV      │  │
│  │ (manual)    │  │ Data Gen    │  │   (external file)   │  │
│  └──────┬──────┘  └──────┬──────┘  └──────────┬──────────┘  │
│         └────────────────┴────────────────────┘             │
│                         ▼                                   │
│              expense_input.csv  (date, category, amount,   │
│              payment_method, description)                    │
└─────────────────────────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                    LAYER 2: STORAGE                           │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  Pandas DataFrame loaded from CSV                      │  │
│  │  Columns: date, category, amount, payment_method, desc │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                 LAYER 3: PROCESSING                            │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │  Cleaning   │  │ Categorize  │  │   Aggregate         │  │
│  │ (dates,     │  │ (standard   │  │ (by cat, month,     │  │
│  │  amounts,   │  │  categories)│  │  payment method)    │  │
│  │  duplicates)│  └─────────────┘  └──────────┬──────────┘  │
│  └──────┬──────┘                           │               │
│         └──────────────────────────────────┘               │
│                         ▼                                  │
│              cleaned_data.csv + aggregated results           │
└─────────────────────────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                 LAYER 4: ANALYSIS                              │
│  • Monthly totals & trend                                      │
│  • Category share (%)                                          │
│  • Payment method split                                        │
│  • Budget vs. actual comparison                                │
│  • Overspending flags                                          │
└─────────────────────────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                LAYER 5: VISUALIZATION                           │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │  Bar chart  │  │  Line chart │  │   Pie chart         │  │
│  │ (category)  │  │  (monthly)  │  │  (category share)   │  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
│  Saved to /outputs as PNG images                              │
└─────────────────────────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                  LAYER 6: INSIGHTS                              │
│  • Top spending category                                       │
│  • Highest spending month                                      │
│  • Overspent categories vs budget                              │
│  • Savings recommendations                                     │
│  Saved to /outputs as insights_report.md                       │
└─────────────────────────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                 LAYER 7: DECISION-MAKING                       │
│  User reviews dashboard & report → adjusts budget / cuts cost  │
└─────────────────────────────────────────────────────────────┘
```

## 5. Data flow explanation

1. **Input** — Expense records enter the system through one of three paths: manual entry, synthetic data generation, or an uploaded CSV file. Each record contains date, category, amount, payment method, and an optional description.
2. **Storage** — Raw records are loaded into a Pandas DataFrame and persisted to `data/expenses.csv` for reproducibility and audit.
3. **Cleaning** — Dates are converted to `datetime64`, amounts to `float`, missing categories are filled or dropped, and duplicate rows are removed to ensure data quality.
4. **Categorization** — Each expense is mapped to a standard category so similar spends can be grouped together for analysis.
5. **Aggregation** — Amounts are summed and averaged grouped by category, month, and payment method to produce totals, percentages, and trends.
6. **Analysis** — Month-over-month changes and rolling averages reveal spending trajectories; actual spend is compared against a defined budget to flag overspending.
7. **Visualization** — Matplotlib/Seaborn render category bar charts, monthly line trends, and category-share pie charts, saved as PNG files in `outputs/`.
8. **Insights** — A text report summarizes the top spending category, highest-spend month, overspent categories, and actionable savings recommendations.
9. **Dashboard** — A Streamlit app loads the cleaned data and charts, letting users filter by date/category and explore charts interactively.
10. **Decision-making** — The user reviews insights and dashboard to adjust next month's budget, cut high-spend categories, or increase savings.

---

**Step 3 complete.** Architecture designed with 7 layers: Input → Storage → Processing → Analysis → Visualization → Insights → Decision-Making. Selected stack: Option B (Streamlit + Pandas + Matplotlib/Seaborn + CSV).

Please reply with **"c"** to acknowledge Step 3, and I will proceed to Step 4 (Implementation Plan).