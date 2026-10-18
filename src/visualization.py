"""Visualization module.

Generates charts for expense analysis:
    - Bar chart: total spend by category
    - Line chart: monthly spending trend
    - Pie chart: category share of total spend
    - Bar chart: spend by payment method

Outputs:
    outputs/*.png
    images/*.png (copied for README display)
"""

import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUTS_DIR = os.path.join(PROJECT_ROOT, "outputs")
IMAGES_DIR = os.path.join(PROJECT_ROOT, "images")
ANALYSIS_RESULTS_PATH = os.path.join(OUTPUTS_DIR, "analysis_results.csv")

# Consistent color palette
sns.set_style("whitegrid")
PALETTE = sns.color_palette("Set2")


def _load_section(section_name: str) -> pd.DataFrame:
    """Load a named section from the combined analysis_results.csv file."""
    if not os.path.exists(ANALYSIS_RESULTS_PATH):
        raise FileNotFoundError(
            f"Analysis results not found: {ANALYSIS_RESULTS_PATH}. Run analysis.py first."
        )
    # Read the file and split by section markers
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

    import io
    return pd.read_csv(io.StringIO(sections[section_name]))


def save_fig(fig, filename: str) -> None:
    """Save a figure to both outputs/ and images/ directories."""
    os.makedirs(OUTPUTS_DIR, exist_ok=True)
    os.makedirs(IMAGES_DIR, exist_ok=True)

    output_path = os.path.join(OUTPUTS_DIR, filename)
    image_path = os.path.join(IMAGES_DIR, filename)

    fig.savefig(output_path, dpi=150, bbox_inches="tight")
    fig.savefig(image_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"[visualization] Saved {output_path} and {image_path}")


def plot_category_spend(category_df: pd.DataFrame) -> None:
    """Bar chart: total spend by category."""
    fig, ax = plt.subplots(figsize=(10, 6))
    cat_palette = PALETTE[: len(category_df)]
    sns.barplot(
        data=category_df,
        x="total_spend",
        y="category",
        hue="category",
        palette=cat_palette,
        legend=False,
        ax=ax,
    )
    ax.set_title("Total Spend by Category", fontsize=14, fontweight="bold")
    ax.set_xlabel("Total Spend (INR)")
    ax.set_ylabel("Category")
    for i, v in enumerate(category_df["total_spend"]):
        ax.text(v + max(category_df["total_spend"]) * 0.01, i, f"₹{v:,.0f}", va="center")
    plt.tight_layout()
    save_fig(fig, "category_spend.png")


def plot_monthly_trend(monthly_df: pd.DataFrame) -> None:
    """Line chart: monthly spending trend."""
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(
        monthly_df["month"],
        monthly_df["total_spend"],
        marker="o",
        linewidth=2,
        color="#2E86AB",
    )
    ax.set_title("Monthly Spending Trend", fontsize=14, fontweight="bold")
    ax.set_xlabel("Month")
    ax.set_ylabel("Total Spend (INR)")
    ax.tick_params(axis="x", rotation=45)
    for i, v in enumerate(monthly_df["total_spend"]):
        ax.annotate(f"₹{v:,.0f}", (i, v), textcoords="offset points", xytext=(0, 8), ha="center", fontsize=8)
    plt.tight_layout()
    save_fig(fig, "monthly_trend.png")


def plot_category_share(category_df: pd.DataFrame) -> None:
    """Pie chart: category share of total spend."""
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(
        category_df["total_spend"],
        labels=category_df["category"],
        autopct="%1.1f%%",
        colors=PALETTE,
        startangle=90,
        wedgeprops={"edgecolor": "white"},
    )
    ax.set_title("Category Share of Total Spend", fontsize=14, fontweight="bold")
    plt.tight_layout()
    save_fig(fig, "category_share.png")


def plot_payment_method(payment_df: pd.DataFrame) -> None:
    """Bar chart: spend by payment method."""
    fig, ax = plt.subplots(figsize=(10, 6))
    pm_palette = PALETTE[: len(payment_df)]
    sns.barplot(
        data=payment_df,
        x="total_spend",
        y="payment_method",
        hue="payment_method",
        palette=pm_palette,
        legend=False,
        ax=ax,
    )
    ax.set_title("Spend by Payment Method", fontsize=14, fontweight="bold")
    ax.set_xlabel("Total Spend (INR)")
    ax.set_ylabel("Payment Method")
    for i, v in enumerate(payment_df["total_spend"]):
        ax.text(v + max(payment_df["total_spend"]) * 0.01, i, f"₹{v:,.0f}", va="center")
    plt.tight_layout()
    save_fig(fig, "payment_method.png")


def main():
    """Generate all visualization charts from analysis results."""
    category_df = _load_section("CATEGORY ANALYSIS")
    monthly_df = _load_section("MONTHLY TREND")
    payment_df = _load_section("PAYMENT METHOD ANALYSIS")

    plot_category_spend(category_df)
    plot_monthly_trend(monthly_df)
    plot_category_share(category_df)
    plot_payment_method(payment_df)

    print("[visualization] All charts generated successfully.")


if __name__ == "__main__":
    main()
