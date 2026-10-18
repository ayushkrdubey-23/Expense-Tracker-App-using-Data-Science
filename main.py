"""Expense Tracker App - Main entry point.

Orchestrates the full pipeline:
    1. Data generation (synthetic expenses)
    2. Data cleaning
    3. EDA & analysis
    4. Visualization
    5. Insights generation

Optionally launches a Streamlit dashboard for interactive exploration.

Usage:
    python main.py                    # Run full pipeline (data -> insights)
    python main.py --dashboard        # Launch Streamlit dashboard
    streamlit run main.py             # Launch Streamlit dashboard directly

Requirements:
    pip install -r requirements.txt
"""

import argparse
import os
import subprocess
import sys

import pandas as pd
import streamlit as st

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(PROJECT_ROOT, "src")
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
OUTPUTS_DIR = os.path.join(PROJECT_ROOT, "outputs")
IMAGES_DIR = os.path.join(PROJECT_ROOT, "images")
CLEAN_DATA_PATH = os.path.join(DATA_DIR, "expenses_clean.csv")
ANALYSIS_RESULTS_PATH = os.path.join(OUTPUTS_DIR, "analysis_results.csv")


def run_module(module_name: str) -> None:
    """Run a src module as a script."""
    module_path = os.path.join(SRC_DIR, module_name)
    print(f"\n{'=' * 60}")
    print(f"Running {module_name}...")
    print(f"{'=' * 60}")
    result = subprocess.run([sys.executable, module_path], capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)
    if result.returncode != 0:
        print(f"[main] {module_name} exited with code {result.returncode}")
        sys.exit(result.returncode)


def run_pipeline(skip_data_gen: bool = False) -> None:
    """Run the full data pipeline end to end."""
    print("[main] Starting Expense Tracker pipeline...")
    if not skip_data_gen:
        run_module("data_generator.py")
    run_module("data_cleaning.py")
    run_module("analysis.py")
    run_module("visualization.py")
    run_module("insights.py")
    print("\n[main] Pipeline complete. Check outputs/ and images/ for results.")


# ---------------------------------------------------------------------------
# Streamlit Dashboard
# ---------------------------------------------------------------------------

def _load_section(section_name: str) -> pd.DataFrame:
    """Load a named section from the combined analysis_results.csv file."""
    import io

    if not os.path.exists(ANALYSIS_RESULTS_PATH):
        return pd.DataFrame()

    with open(ANALYSIS_RESULTS_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    sections = {}
    current_section = None
    lines = []
    for line in content.splitlines():
        if line.startswith("===") and line.endswith("==="):
            if current_section is not None:
                sections[current_section] = "\n".join(lines)
            current_section = line.strip("= ").strip()
            lines = []
        else:
            lines.append(line)
    if current_section is not None:
        sections[current_section] = "\n".join(lines)

    if section_name not in sections:
        return pd.DataFrame()
    return pd.read_csv(io.StringIO(sections[section_name]))


def load_clean_data() -> pd.DataFrame:
    """Load cleaned expense data."""
    if os.path.exists(CLEAN_DATA_PATH):
        return pd.read_csv(CLEAN_DATA_PATH, parse_dates=["date"])
    return pd.DataFrame()


def render_dashboard() -> None:
    """Render the Streamlit dashboard with tabs."""
    st.set_page_config(page_title="Expense Tracker App", page_icon="💰", layout="wide")

    st.title("💰 Expense Tracker App")
    st.markdown("Data-driven expense tracking, categorization, and visualization.")

    # Sidebar controls
    st.sidebar.header("Controls")
    if st.sidebar.button("Run Full Pipeline"):
        with st.spinner("Running pipeline..."):
            run_pipeline(skip_data_gen=False)
        st.success("Pipeline complete!")

    st.sidebar.markdown("---")
    st.sidebar.subheader("Filters")

    df = load_clean_data()

    if df.empty:
        st.warning("No data found. Run the pipeline first: `python main.py`")
        return

    # Date filter
    min_date = df["date"].min()
    max_date = df["date"].max()
    date_range = st.sidebar.date_input(
        "Date Range",
        value=(min_date.date(), max_date.date()),
        min_value=min_date.date(),
        max_value=max_date.date(),
    )

    # Category filter
    categories = ["All"] + sorted(df["category"].dropna().unique().tolist())
    selected_category = st.sidebar.selectbox("Category", categories)

    # Payment method filter
    payment_methods = ["All"] + sorted(df["payment_method"].dropna().unique().tolist())
    selected_payment = st.sidebar.selectbox("Payment Method", payment_methods)

    # Apply filters
    filtered = df.copy()
    if len(date_range) == 2:
        start_date, end_date = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
        filtered = filtered[(filtered["date"] >= start_date) & (filtered["date"] <= end_date)]
    if selected_category != "All":
        filtered = filtered[filtered["category"] == selected_category]
    if selected_payment != "All":
        filtered = filtered[filtered["payment_method"] == selected_payment]

    # Load analysis sections
    category_df = _load_section("CATEGORY ANALYSIS")
    monthly_df = _load_section("MONTHLY TREND")
    payment_df = _load_section("PAYMENT METHOD ANALYSIS")
    budget_df = _load_section("BUDGET COMPARISON")

    # Tabs
    tab_overview, tab_analysis, tab_insights, tab_data, tab_pipeline = st.tabs(
        ["Overview", "Analysis", "Insights", "Data", "Pipeline"]
    )

    # ---- Tab 1: Overview ----
    with tab_overview:
        st.subheader("Overview")
        total_spend = filtered["amount"].sum()
        avg_transaction = filtered["amount"].mean()
        total_transactions = len(filtered)

        col1, col2, col3 = st.columns(3)
        col1.metric("Total Spend", f"₹{total_spend:,.2f}")
        col2.metric("Avg per Transaction", f"₹{avg_transaction:,.2f}")
        col3.metric("Total Transactions", f"{total_transactions}")

        st.markdown("---")
        st.write("### Expense Summary")
        st.write(f"**Date Range:** {min_date.date()} to {max_date.date()}")
        st.write(f"**Total Records:** {len(df)}")
        st.write(f"**Filtered Records:** {len(filtered)}")
        st.write(f"**Categories:** {df['category'].nunique()}")
        st.write(f"**Payment Methods:** {df['payment_method'].nunique()}")

    # ---- Tab 2: Analysis ----
    with tab_analysis:
        st.subheader("Spending Analysis")

        col_a, col_b = st.columns(2)
        with col_a:
            st.write("### Spend by Category")
            if not category_df.empty:
                st.bar_chart(category_df.set_index("category")["total_spend"])
            else:
                st.info("Run the pipeline to generate charts.")

        with col_b:
            st.write("### Monthly Spending Trend")
            if not monthly_df.empty:
                st.line_chart(monthly_df.set_index("month")["total_spend"])
            else:
                st.info("Run the pipeline to generate charts.")

        col_c, col_d = st.columns(2)
        with col_c:
            st.write("### Category Share")
            if not category_df.empty:
                st.write(category_df[["category", "total_spend", "percentage_of_total"]])
            else:
                st.info("Run the pipeline to generate charts.")

        with col_d:
            st.write("### Spend by Payment Method")
            if not payment_df.empty:
                st.bar_chart(payment_df.set_index("payment_method")["total_spend"])
            else:
                st.info("Run the pipeline to generate charts.")

    # ---- Tab 3: Insights ----
    with tab_insights:
        st.subheader("Insights & Budget Comparison")

        insights_path = os.path.join(OUTPUTS_DIR, "insights_report.md")
        if os.path.exists(insights_path):
            with open(insights_path, "r", encoding="utf-8") as f:
                st.markdown(f.read())
        else:
            st.info("Run the pipeline to generate the insights report.")

        st.markdown("---")
        st.write("### Budget Comparison Table")
        if not budget_df.empty:
            st.dataframe(budget_df, use_container_width=True)
        else:
            st.info("Run the pipeline to generate budget comparison.")

    # ---- Tab 4: Data ----
    with tab_data:
        st.subheader("Expense Records")
        st.dataframe(
            filtered.sort_values("date", ascending=False),
            use_container_width=True,
            height=400,
        )

        st.download_button(
            label="Download Filtered Data (CSV)",
            data=filtered.to_csv(index=False).encode("utf-8"),
            file_name="expenses_filtered.csv",
            mime="text/csv",
        )

    # ---- Tab 5: Pipeline ----
    with tab_pipeline:
        st.subheader("Pipeline Controls")
        st.markdown("Run the full data pipeline to regenerate synthetic data, clean it, analyze, visualize, and generate insights.")

        col_p1, col_p2 = st.columns(2)
        with col_p1:
            if st.button("Run Full Pipeline", type="primary"):
                with st.spinner("Running pipeline..."):
                    run_pipeline(skip_data_gen=False)
                st.success("Pipeline complete! Refresh the page to see updated results.")

        with col_p2:
            if st.button("Run Without Data Regeneration"):
                with st.spinner("Running pipeline..."):
                    run_pipeline(skip_data_gen=True)
                st.success("Pipeline complete! Refresh the page to see updated results.")

        st.markdown("---")
        st.write("### Pipeline Stages")
        st.write("1. **Data Generation** - Creates synthetic expense records")
        st.write("2. **Data Cleaning** - Parses dates, fixes amounts, removes duplicates")
        st.write("3. **Analysis** - Aggregates by category, month, payment method; budget comparison")
        st.write("4. **Visualization** - Generates bar, line, and pie charts")
        st.write("5. **Insights** - Auto-generates insights report with recommendations")


def main():
    parser = argparse.ArgumentParser(description="Expense Tracker App using Data Science")
    parser.add_argument(
        "--dashboard",
        action="store_true",
        help="Launch the Streamlit interactive dashboard",
    )
    parser.add_argument(
        "--skip-data-gen",
        action="store_true",
        help="Skip synthetic data generation (use existing raw data)",
    )
    args = parser.parse_args()

    if args.dashboard:
        render_dashboard()
        return

    # Otherwise run the CLI pipeline
    run_pipeline(skip_data_gen=args.skip_data_gen)


if __name__ == "__main__":
    main()
