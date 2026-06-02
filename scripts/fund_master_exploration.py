import pandas as pd
from pathlib import Path

# Load Fund Master Dataset
file_path = Path("data/raw/01_fund_master.csv")

df = pd.read_csv(file_path)

print("=" * 80)
print("FUND MASTER EXPLORATION")
print("=" * 80)

print("\nDataset Shape")
print(df.shape)

print("\nColumns")
print(df.columns.tolist())

# Unique Fund Houses
print("\nUnique Fund Houses")
print(df["fund_house"].unique())

# Categories
print("\nCategories")
print(df["category"].unique())

# Sub Categories
print("\nSub Categories")
print(df["sub_category"].unique())

# Risk Categories
print("\nRisk Categories")
print(df["risk_category"].unique())