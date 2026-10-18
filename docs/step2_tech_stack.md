# Step 2 - Tech Stack Options: Expense Tracker App

Three tech stack options are presented below, ranging from Easy to Advanced. Each includes tools, visualization, app/dashboard availability, difficulty, and a use-case fit.

---

## Option A — Easy (Beginner)

| Aspect | Details |
|--------|---------|
| **Language** | Python 3.x |
| **Data tools** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn |
| **App/dashboard** | No (script-based, outputs charts to files/console) |
| **Storage** | CSV files |
| **Difficulty** | Beginner / Easy |
| **Best for** | Students new to Python, quick placement proof, simple reports |

**Description:** A single Python script (`main.py`) reads synthetic expense data from CSV, cleans it with Pandas, runs aggregations, and saves Matplotlib/Seaborn charts as PNG images plus a text insights report. No installation of web frameworks; runs anywhere Python is installed.

---

## Option B — Intermediate (Recommended for Students)

| Aspect | Details |
|--------|---------|
| **Language** | Python 3.x |
| **Data tools** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn |
| **App/dashboard** | Yes — Streamlit dashboard |
| **Storage** | CSV + optional SQLite |
| **Difficulty** | Intermediate |
| **Best for** | Placements/internships, Data Analyst & Business Analyst roles, GitHub proof |

**Description:** Same analysis core as Option A, wrapped in an interactive Streamlit dashboard. Users can upload their own CSV, filter by date/category, view charts live, and download reports. Adds a deployable web app that recruiters can actually interact with — strong portfolio evidence.

---

## Option C — Advanced

| Aspect | Details |
|--------|---------|
| **Language** | Python 3.x |
| **Data tools** | Pandas, NumPy, SQLAlchemy |
| **Visualization** | Matplotlib, Seaborn, Plotly (interactive) |
| **App/dashboard** | Yes — Streamlit + Plotly interactive dashboard |
| **Storage** | SQLite/PostgreSQL database |
| **Authentication** | Optional (login, per-user data) |
| **Difficulty** | Advanced |
| **Best for** | Full-stack Data Science roles, production-ready apps, capstone projects |

**Description:** Backend database with user authentication, role-based access, interactive Plotly charts, expense forecasting (regression/time-series), and deployment-ready architecture. More complex but closest to real FinTech products.

---

## Comparison Table

| Feature | Option A | Option B | Option C |
|---------|----------|----------|----------|
| Python + Pandas + NumPy | ✅ | ✅ | ✅ |
| Matplotlib / Seaborn | ✅ | ✅ | ✅ |
| CSV storage | ✅ | ✅ | ❌ (DB) |
| Streamlit dashboard | ❌ | ✅ | ✅ |
| Plotly interactive charts | ❌ | ❌ | ✅ |
| Database (SQLite/PostgreSQL) | ❌ | ⚠️ optional | ✅ |
| User authentication | ❌ | ❌ | ✅ |
| Forecasting / ML | ❌ | ❌ | ✅ |
| Difficulty | Easy | Intermediate | Advanced |

---

## Best Option Selected for Students: **Option B (Intermediate)**

### Reasons

1. **Placement-ready proof** — A live Streamlit dashboard is something recruiters can run and interact with, which is far more impressive than a static script.
2. **Beginner-friendly but professional** — Builds on Option A (easy core) and adds just enough interactivity to look polished without the complexity of databases and auth.
3. **Relevant to target roles** — Directly maps to Data Analyst, Business Analyst, and Financial Analyst work: data cleaning, aggregation, visualization, and reporting.
4. **Low barrier to run** — No database setup; runs with `pip install -r requirements.txt` and `streamlit run main.py`.
5. **GitHub-friendly** — All code, synthetic data, outputs, and requirements fit neatly in the folder structure from Step 5.

### What Option B delivers
- Synthetic expense dataset generation
- Data cleaning & categorization
- Monthly trend & category analysis
- Overspending detection vs. budgets
- Interactive Streamlit dashboard with filters
- Exportable charts and text insights report
- Complete README and GitHub-ready folder structure

---

**Step 2 complete.** Selected stack: **Option B — Intermediate (Python, Pandas, NumPy, Matplotlib, Seaborn, Streamlit, CSV storage).**

Please reply with **"c"** to acknowledge Step 2, and I will proceed to Step 3 (Project Architecture).