"""Insights generation module.

Generates actionable text insights from the analysis results:
    - Top spending category
    - Highest spending month
    - Overspent categories vs budget
    - Savings recommendations

Output:
    outputs/insights_report.md
"""

import os

import pandas as pd

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUTS_DIR = os.path.join(PROJECT_ROOT, "outputs")
ANALYSIS_RESULTS_PATH = os.path.join(OUTPUTS_DIR, "analysis_results.csv")
INSIGHTS_REPORT_PATH = os.path.join(OUTPUTS_DIR, "insights_report.md")


def _load_section(section_name: str) -> pd.DataFrame:
    """Load a named section from the combined analysis_results.csv file."""
    if not os.path.exists(ANALYSIS_RESULTS_PATH):
        raise FileNotFoundError(
            f"Analysis results not found: {ANALYSIS_RESULTS_PATH}. Run analysis.py first."
        )
    import io

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

    return pd.read_csv(io.StringIO(sections[section_name]))


def generate_insights(category_df: pd.DataFrame, monthly_df: pd.DataFrame,
                      budget_df: pd.DataFrame) -> str:
    """Generate a markdown insights report."""
    total_spend = category_df["total_spend"].sum()
    top_category = category_df.iloc[0]
    highest_month = monthly_df.loc[monthly_df["total_spend"].idxmax()]
    lowest_month = monthly_df.loc[monthly_df["total_spend"].idxmin()]
    overspent = budget_df[budget_df["overspent"] == True]
    within_budget = budget_df[budget_df["overspent"] == False]

    lines = []
    lines.append("# Expense Tracker - Insights Report")
    lines.append("")
    lines.append("## Summary")
    lines.append(f"- **Total Spend:** ₹{total_spend:,.2f}")
    lines.append(f"- **Top Spending Category:** {top_category['category']} (₹{top_category['total_spend']:,.2f}, {top_category['percentage_of_total']}% of total)")
    lines.append(f"- **Highest Spending Month:** {highest_month['month']} (₹{highest_month['total_spend']:,.2f})")
    lines.append(f"- **Lowest Spending Month:** {lowest_month['month']} (₹{lowest_month['total_spend']:,.2f})")
    lines.append("")

    lines.append("## Category-wise Spending")
    lines.append("| Category | Total Spend (₹) | % of Total |")
    lines.append("|----------|-----------------|------------|")
    for _, row in category_df.iterrows():
        lines.append(f"| {row['category']} | {row['total_spend']:,.2f} | {row['percentage_of_total']}% |")
    lines.append("")

    lines.append("## Monthly Trend")
    lines.append("| Month | Total Spend (₹) | MoM Change (%) |")
    lines.append("|-------|-----------------|----------------|")
    for _, row in monthly_df.iterrows():
        mom = row["month_over_month_change_pct"]
        mom_str = f"{mom:+.2f}%" if pd.notna(mom) else "N/A"
        lines.append(f"| {row['month']} | {row['total_spend']:,.2f} | {mom_str} |")
    lines.append("")

    lines.append("## Budget Comparison & Overspending")
    if len(overspent) > 0:
        lines.append("### Overspent Categories")
        for _, row in overspent.iterrows():
            lines.append(
                f"- **{row['category']}:** Spent ₹{row['actual_spend']:,.2f} vs Budget ₹{row['budget']:,.2f} "
                f"(₹{row['variance']:,.2f} over, +{row['variance_pct']:.2f}%)"
            )
    else:
        lines.append("- No categories exceeded their budget. Well done!")
    lines.append("")

    if len(within_budget) > 0:
        lines.append("### Within Budget Categories")
        for _, row in within_budget.iterrows():
            lines.append(
                f"- **{row['category']}:** Spent ₹{row['actual_spend']:,.2f} vs Budget ₹{row['budget']:,.2f} "
                f"(₹{row['budget'] - row['actual_spend']:,.2f} remaining)"
            )
    lines.append("")

    lines.append("## Recommendations")
    if len(overspent) > 0:
        top_overspent = overspent.sort_values("variance_pct", ascending=False).iloc[0]
        lines.append(
            f"- Focus on reducing **{top_overspent['category']}** spending, which is "
            f"{top_overspent['variance_pct']:+.2f}% over budget (₹{top_overspent['variance']:,.2f} excess)."
        )
    if len(category_df) > 0:
        lines.append(
            f"- Set a stricter monthly limit for **{top_category['category']}**, your highest spending category "
            f"(₹{top_category['total_spend']:,.2f})."
        )
    lines.append("- Review the 'Entertainment' and 'Shopping' categories for discretionary spend that can be reduced.")
    lines.append("- Consider automating savings by transferring a fixed amount right after salary credit.")
    lines.append("- Track weekly spend to catch budget drift early in the month.")

    report = "\n".join(lines)
    return report


def main():
    """Generate the insights report from analysis results."""
    os.makedirs(OUTPUTS_DIR, exist_ok=True)

    category_df = _load_section("CATEGORY ANALYSIS")
    monthly_df = _load_section("MONTHLY TREND")
    budget_df = _load_section("BUDGET COMPARISON")

    report = generate_insights(category_df, monthly_df, budget_df)

    with open(INSIGHTS_REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"[insights] Saved insights report to {INSIGHTS_REPORT_PATH}")
    console_report = report.replace("\u20b9", "Rs.")
    print("\n" + console_report)


if __name__ == "__main__":
    main()
