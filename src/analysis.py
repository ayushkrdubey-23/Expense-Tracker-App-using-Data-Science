"""Expense analysis module.

Computes aggregations, monthly trends, category-wise spending, payment method
split, budget comparison, and overspending flags.

Outputs:
    outputs/analysis_results.csv
    outputs/eda_summary.txt
"""

import os

import pandas as pd

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
OUTPUTS_DIR = os.path.join(PROJECT_ROOT, "outputs")
CLEAN_DATA_PATH = os.path.join(DATA_DIR, "expenses_clean.csv")
ANALYSIS_RESULTS_PATH = os.path.join(OUTPUTS_DIR, "analysis_results.csv")
EDA_SUMMARY_PATH = os.path.join(OUTPUTS_DIR, "eda_summary.txt")

# Monthly budget per category (INR)
MONTHLY_BUDGET = {
    "Food": 5000,
    "Travel": 2000,
    "Rent": 12000,
    "Utilities": 1500,
    "Entertainment": 1500,
    "Shopping": 3000,
    "Health": 1000,
    "Other": 1000,
}


def load_clean_data() -> pd.DataFrame:
    """Load the cleaned expense dataset."""
    if not os.path.exists(CLEAN_DATA_PATH):
        raise FileNotFoundError(f"Cleaned data not found: {CLEAN_DATA_PATH}. Run data_cleaning.py first.")
    df = pd.read_csv(CLEAN_DATA_PATH, parse_dates=["date"])
    return df


def compute_eda(df: pd.DataFrame) -> dict:
    """Compute exploratory data analysis summary statistics."""
    eda = {
        "total_records": len(df),
        "total_spend": float(df["amount"].sum()),
        "average_transaction": float(df["amount"].mean()),
        "min_transaction": float(df["amount"].min()),
        "max_transaction": float(df["amount"].max()),
        "date_start": df["date"].min().strftime("%Y-%m-%d"),
        "date_end": df["date"].max().strftime("%Y-%m-%d"),
        "unique_categories": df["category"].nunique(),
        "unique_payment_methods": df["payment_method"].nunique(),
    }
    return eda


def compute_category_analysis(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate total and average spend by category."""
    cat = (
        df.groupby("category")["amount"]
        .agg(["sum", "mean", "count"])
        .reset_index()
        .rename(columns={"sum": "total_spend", "mean": "avg_spend", "count": "transaction_count"})
    )
    cat["percentage_of_total"] = (cat["total_spend"] / cat["total_spend"].sum() * 100).round(2)
    cat = cat.sort_values("total_spend", ascending=False).reset_index(drop=True)
    return cat


def compute_monthly_trend(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate total spend by month."""
    df = df.copy()
    df["month"] = df["date"].dt.to_period("M").astype(str)
    monthly = (
        df.groupby("month")["amount"]
        .agg(["sum", "mean", "count"])
        .reset_index()
        .rename(columns={"sum": "total_spend", "mean": "avg_spend", "count": "transaction_count"})
    )
    monthly["month_over_month_change_pct"] = monthly["total_spend"].pct_change() * 100
    monthly["month_over_month_change_pct"] = monthly["month_over_month_change_pct"].round(2)
    return monthly


def compute_payment_method_analysis(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate spend by payment method."""
    pm = (
        df.groupby("payment_method")["amount"]
        .agg(["sum", "mean", "count"])
        .reset_index()
        .rename(columns={"sum": "total_spend", "mean": "avg_spend", "count": "transaction_count"})
    )
    pm["percentage_of_total"] = (pm["total_spend"] / pm["total_spend"].sum() * 100).round(2)
    pm = pm.sort_values("total_spend", ascending=False).reset_index(drop=True)
    return pm


def compute_budget_comparison(df: pd.DataFrame, monthly_budget: dict) -> pd.DataFrame:
    """Compare actual vs budget per category and flag overspending."""
    df = df.copy()
    df["month"] = df["date"].dt.to_period("M").astype(str)

    # Total spend per category across all months
    category_spend = df.groupby("category")["amount"].sum()

    rows = []
    for category, actual in category_spend.items():
        budget = monthly_budget.get(category, 1000)
        variance = actual - budget
        variance_pct = (variance / budget * 100) if budget > 0 else 0
        overspent = actual > budget
        rows.append({
            "category": category,
            "actual_spend": round(float(actual), 2),
            "budget": float(budget),
            "variance": round(float(variance), 2),
            "variance_pct": round(float(variance_pct), 2),
            "overspent": bool(overspent),
        })

    budget_df = pd.DataFrame(rows).sort_values("actual_spend", ascending=False).reset_index(drop=True)
    return budget_df


def save_analysis_results(category_df: pd.DataFrame, monthly_df: pd.DataFrame,
                          payment_df: pd.DataFrame, budget_df: pd.DataFrame) -> None:
    """Save all analysis results to a single CSV with section markers."""
    os.makedirs(OUTPUTS_DIR, exist_ok=True)

    with open(ANALYSIS_RESULTS_PATH, "w", encoding="utf-8") as f:
        f.write("=== CATEGORY ANALYSIS ===\n")
        category_df.to_csv(f, index=False)
        f.write("\n=== MONTHLY TREND ===\n")
        monthly_df.to_csv(f, index=False)
        f.write("\n=== PAYMENT METHOD ANALYSIS ===\n")
        payment_df.to_csv(f, index=False)
        f.write("\n=== BUDGET COMPARISON ===\n")
        budget_df.to_csv(f, index=False)

    print(f"[analysis] Saved analysis results to {ANALYSIS_RESULTS_PATH}")


def save_eda_summary(eda: dict) -> None:
    """Save EDA summary to a text file."""
    os.makedirs(OUTPUTS_DIR, exist_ok=True)
    lines = ["EXPENSE TRACKER - EDA SUMMARY", "=" * 40]
    for key, value in eda.items():
        lines.append(f"{key}: {value}")
    lines.append("=" * 40)
    with open(EDA_SUMMARY_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"[analysis] Saved EDA summary to {EDA_SUMMARY_PATH}")


def main():
    """Run the full analysis pipeline and save outputs."""
    df = load_clean_data()

    eda = compute_eda(df)
    print("[analysis] EDA Summary:")
    for key, value in eda.items():
        print(f"  {key}: {value}")

    category_df = compute_category_analysis(df)
    monthly_df = compute_monthly_trend(df)
    payment_df = compute_payment_method_analysis(df)
    budget_df = compute_budget_comparison(df, MONTHLY_BUDGET)

    save_analysis_results(category_df, monthly_df, payment_df, budget_df)
    save_eda_summary(eda)

    print("\n[analysis] Category Analysis:")
    print(category_df.to_string(index=False))
    print("\n[analysis] Monthly Trend:")
    print(monthly_df.to_string(index=False))
    print("\n[analysis] Budget Comparison (Overspent flags):")
    print(budget_df.to_string(index=False))


if __name__ == "__main__":
    main()
