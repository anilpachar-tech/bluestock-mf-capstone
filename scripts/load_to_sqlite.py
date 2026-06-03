from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine

# Database Connection

db_path = "sqlite:///data/db/bluestock_mf.db"

engine = create_engine(db_path)

print("Database Connected")

# Load Datasets

fund_df = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

nav_df = pd.read_csv(
    "data/processed/nav_history_clean.csv"
)

txn_df = pd.read_csv(
    "data/processed/investor_transactions_clean.csv"
)

perf_df = pd.read_csv(
    "data/processed/scheme_performance_clean.csv"
)

aum_df = pd.read_csv(
    "data/raw/03_aum_by_fund_house.csv"
)


# DIM FUND


dim_fund = fund_df[
    [
        "amfi_code",
        "scheme_name",
        "fund_house",
        "category",
        "sub_category",
        "risk_category"
    ]
].copy()

dim_fund.rename(
    columns={
        "risk_category": "risk_grade"
    },
    inplace=True
)

dim_fund.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

print("dim_fund loaded")


# FACT NAV


fact_nav = nav_df[
    [
        "amfi_code",
        "date",
        "nav"
    ]
].copy()

fact_nav.rename(
    columns={
        "date": "nav_date"
    },
    inplace=True
)

fact_nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

print("fact_nav loaded")


# FACT TRANSACTIONS


fact_transactions = txn_df.copy()

fact_transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

print("fact_transactions loaded")


# FACT PERFORMANCE


fact_performance = perf_df.copy()

fact_performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("fact_performance loaded")


# FACT AUM


fact_aum = aum_df.copy()

fact_aum.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

print("fact_aum loaded")


# Row Counts


print("\nRow Count Verification")

print(
    "dim_fund:",
    len(dim_fund)
)

print(
    "fact_nav:",
    len(fact_nav)
)

print(
    "fact_transactions:",
    len(fact_transactions)
)

print(
    "fact_performance:",
    len(fact_performance)
)

print(
    "fact_aum:",
    len(fact_aum)
)

print("\nAll datasets loaded successfully")