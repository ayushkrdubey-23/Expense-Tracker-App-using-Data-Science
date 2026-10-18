"""Synthetic expense dataset generator.

Generates a realistic synthetic expense dataset covering 6-12 months of records
with fields: date, category, amount, payment_method, description.

Output:
    data/expenses_raw.csv
"""

import os
import random
from datetime import datetime, timedelta

import numpy as np
import pandas as pd

# Reproducible random seed
RANDOM_SEED = 42
random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)

# Project root (one level up from src/)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
RAW_DATA_PATH = os.path.join(DATA_DIR, "expenses_raw.csv")

# Categoriy -> typical amount range (min, max) in INR
CATEGORY_AMOUNT_RANGES = {
    "Food": (100, 600),
    "Travel": (50, 500),
    "Rent": (8000, 15000),
    "Utilities": (500, 2500),
    "Entertainment": (200, 1200),
    "Shopping": (300, 3000),
    "Health": (200, 2000),
}

CATEGORIES = list(CATEGORY_AMOUNT_RANGES.keys())

PAYMENT_METHODS = ["UPI", "Credit Card", "Debit Card", "Cash", "Wallet"]
PAYMENT_WEIGHTS = [0.45, 0.2, 0.15, 0.1, 0.1]

DESCRIPTIONS = {
    "Food": ["Lunch at cafe", "Dinner with friends", "Groceries", "Snacks", "Food delivery"],
    "Travel": ["Uber ride", "Metro pass", "Fuel", "Bus ticket", "Train ticket"],
    "Rent": ["Monthly rent"],
    "Utilities": ["Electricity bill", "Internet bill", "Mobile bill", "Water bill"],
    "Entertainment": ["Movie tickets", "Concert", "Gaming subscription", "Streaming subscription"],
    "Shopping": ["Clothes", "Electronics", "Groceries bulk", "Home decor"],
    "Health": ["Pharmacy", "Doctor consultation", "Gym membership", "Diagnostic test"],
}


def generate_synthetic_expenses(start_date: str, end_date: str, records_per_month: int = 30) -> pd.DataFrame:
    """Generate synthetic expense records between start_date and end_date.

    Args:
        start_date: Start date in YYYY-MM-DD format.
        end_date: End date in YYYY-MM-DD format.
        records_per_month: Average number of expense records per month.

    Returns:
        DataFrame with columns: date, category, amount, payment_method, description.
    """
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")

    records = []
    current = start

    while current <= end:
        # Number of records for this month (with some randomness)
        n_records = max(1, int(np.random.normal(records_per_month, 5)))
        days_in_month = (end.replace(day=28) + timedelta(days=4)).day if current.month == 12 else 30

        for _ in range(n_records):
            # Random day within current month
            day = random.randint(1, min(28, days_in_month))
            try:
                expense_date = current.replace(day=day)
            except ValueError:
                expense_date = current

            if expense_date > end:
                break

            category = random.choice(CATEGORIES)
            amount_min, amount_max = CATEGORY_AMOUNT_RANGES[category]
            amount = round(random.uniform(amount_min, amount_max), 2)

            # Rent and utilities tend to be fixed monthly amounts
            if category == "Rent":
                amount = round(random.uniform(10000, 12000), 2)
            elif category == "Utilities":
                amount = round(random.uniform(800, 1800), 2)

            payment_method = random.choices(PAYMENT_METHODS, weights=PAYMENT_WEIGHTS, k=1)[0]
            description = random.choice(DESCRIPTIONS[category])

            records.append({
                "date": expense_date.strftime("%Y-%m-%d"),
                "category": category,
                "amount": amount,
                "payment_method": payment_method,
                "description": description,
            })

        # Move to next month
        if current.month == 12:
            current = current.replace(year=current.year + 1, month=1)
        else:
            current = current.replace(month=current.month + 1)

    df = pd.DataFrame(records)
    df = df.sort_values("date").reset_index(drop=True)
    return df


def main():
    """Generate and save the synthetic expense dataset."""
    os.makedirs(DATA_DIR, exist_ok=True)

    # Generate 10 months of synthetic data (Jan to Oct 2024)
    df = generate_synthetic_expenses("2024-01-01", "2024-10-31", records_per_month=25)

    # Introduce a small amount of noise for realism (missing values, duplicates)
    noise_indices = df.sample(n=max(1, int(len(df) * 0.02)), random_state=1).index
    df.loc[noise_indices, "category"] = np.nan

    df = pd.concat([df, df.sample(n=3, random_state=2)], ignore_index=True)

    df.to_csv(RAW_DATA_PATH, index=False)
    print(f"[data_generator] Generated {len(df)} synthetic expense records.")
    print(f"[data_generator] Saved to {RAW_DATA_PATH}")
    print(f"[data_generator] Date range: {df['date'].min()} to {df['date'].max()}")
    print(f"[data_generator] Categories: {df['category'].dropna().unique().tolist()}")


if __name__ == "__main__":
    main()
