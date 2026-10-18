"""Data cleaning module.

Loads the raw expense dataset, performs cleaning operations, and saves the
cleaned dataset.

Operations:
    - Parse date column to datetime
    - Convert amount to numeric
    - Handle missing category values
    - Remove duplicate rows
    - Standardize category names (title case)

Output:
    data/expenses_clean.csv
"""

import os

import pandas as pd

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
RAW_DATA_PATH = os.path.join(DATA_DIR, "expenses_raw.csv")
CLEAN_DATA_PATH = os.path.join(DATA_DIR, "expenses_clean.csv")

VALID_CATEGORIES = ["Food", "Travel", "Rent", "Utilities", "Entertainment", "Shopping", "Health"]


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean the raw expense DataFrame.

    Args:
        df: Raw expense DataFrame.

    Returns:
        Cleaned DataFrame.
    """
    df = df.copy()

    initial_rows = len(df)
    print(f"[data_cleaning] Starting with {initial_rows} rows.")

    # Parse dates
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    date_nan_count = df["date"].isna().sum()
    if date_nan_count > 0:
        print(f"[data_cleaning] Dropping {date_nan_count} rows with invalid dates.")
        df = df.dropna(subset=["date"])

    # Convert amount to numeric
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    amount_nan_count = df["amount"].isna().sum()
    if amount_nan_count > 0:
        print(f"[data_cleaning] Dropping {amount_nan_count} rows with invalid amounts.")
        df = df.dropna(subset=["amount"])

    # Handle missing categories: fill with 'Other' then standardize
    missing_cat_count = df["category"].isna().sum()
    if missing_cat_count > 0:
        print(f"[data_cleaning] Filling {missing_cat_count} missing categories with 'Other'.")
        df["category"] = df["category"].fillna("Other")

    # Standardize category names to title case
    df["category"] = df["category"].astype(str).str.strip().str.title()

    # Map unknown categories to 'Other'
    df.loc[~df["category"].isin(VALID_CATEGORIES + ["Other"]), "category"] = "Other"

    # Remove duplicates
    before_dup = len(df)
    df = df.drop_duplicates()
    after_dup = len(df)
    if before_dup != after_dup:
        print(f"[data_cleaning] Removed {before_dup - after_dup} duplicate rows.")

    # Sort by date
    df = df.sort_values("date").reset_index(drop=True)

    final_rows = len(df)
    print(f"[data_cleaning] Cleaned dataset: {final_rows} rows (removed {initial_rows - final_rows}).")
    return df


def main():
    """Load raw data, clean it, and save the cleaned dataset."""
    os.makedirs(DATA_DIR, exist_ok=True)

    if not os.path.exists(RAW_DATA_PATH):
        print(f"[data_cleaning] Raw data file not found: {RAW_DATA_PATH}")
        print("[data_cleaning] Run src/data_generator.py first to generate raw data.")
        return

    df = pd.read_csv(RAW_DATA_PATH)
    print(f"[data_cleaning] Loaded {len(df)} rows from {RAW_DATA_PATH}")

    df_clean = clean_data(df)
    df_clean.to_csv(CLEAN_DATA_PATH, index=False)
    print(f"[data_cleaning] Saved cleaned data to {CLEAN_DATA_PATH}")


if __name__ == "__main__":
    main()
