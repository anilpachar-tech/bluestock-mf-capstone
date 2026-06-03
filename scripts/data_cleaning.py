from pathlib import Path
import pandas as pd

# Folders

RAW_FOLDER = Path("data/raw")
PROCESSED_FOLDER = Path("data/processed")

PROCESSED_FOLDER.mkdir(parents=True, exist_ok=True)

print("=" * 80)
print("DAY 2 - DATA CLEANING")
print("=" * 80)

# 1. NAV HISTORY CLEANING

print("\nCleaning NAV History...")

nav_df = pd.read_csv(
    RAW_FOLDER / "02_nav_history.csv"
)

# Date conversion
nav_df["date"] = pd.to_datetime(
    nav_df["date"]
)

# Sort
nav_df = nav_df.sort_values(
    ["amfi_code", "date"]
)

# Remove duplicates
nav_df = nav_df.drop_duplicates()

# NAV validation
nav_df = nav_df[
    nav_df["nav"] > 0
]

# Forward fill NAV within scheme
nav_df["nav"] = (
    nav_df
    .groupby("amfi_code")["nav"]
    .ffill()
)

nav_df.to_csv(
    PROCESSED_FOLDER / "nav_history_clean.csv",
    index=False
)

print("NAV History Cleaned")


# 2. INVESTOR TRANSACTIONS CLEANING

print("\nCleaning Investor Transactions...")

txn_df = pd.read_csv(
    RAW_FOLDER / "08_investor_transactions.csv"
)

# Date conversion
txn_df["transaction_date"] = pd.to_datetime(
    txn_df["transaction_date"]
)

# Standardize transaction type
txn_df["transaction_type"] = (
    txn_df["transaction_type"]
    .astype(str)
    .str.strip()
    .str.title()
)

# Amount validation
txn_df = txn_df[
    txn_df["amount_inr"] > 0
]

# Valid KYC statuses
valid_kyc = [
    "Verified",
    "Pending",
    "Rejected"
]

txn_df["kyc_status"] = (
    txn_df["kyc_status"]
    .astype(str)
    .str.strip()
    .str.title()
)

txn_df["kyc_valid"] = txn_df[
    "kyc_status"
].isin(valid_kyc)

txn_df.to_csv(
    PROCESSED_FOLDER /
    "investor_transactions_clean.csv",
    index=False
)

print("Investor Transactions Cleaned")


# 3. SCHEME PERFORMANCE CLEANING

print("\nCleaning Scheme Performance...")

perf_df = pd.read_csv(
    RAW_FOLDER /
    "07_scheme_performance.csv"
)

return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "expense_ratio_pct"
]

for col in return_columns:

    perf_df[col] = pd.to_numeric(
        perf_df[col],
        errors="coerce"
    )

# Expense ratio validation
perf_df["expense_ratio_flag"] = (
    (perf_df["expense_ratio_pct"] < 0.1)
    |
    (perf_df["expense_ratio_pct"] > 2.5)
)

perf_df.to_csv(
    PROCESSED_FOLDER /
    "scheme_performance_clean.csv",
    index=False
)

print("Scheme Performance Cleaned")


# SUMMARY

print("\n")
print("=" * 80)
print("ALL CLEANING COMPLETED")
print("=" * 80)