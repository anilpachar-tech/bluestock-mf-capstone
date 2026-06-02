import pandas as pd
from pathlib import Path

# Load datasets
fund_master = pd.read_csv(
    Path("data/raw/01_fund_master.csv")
)

nav_history = pd.read_csv(
    Path("data/raw/02_nav_history.csv")
)

# Unique scheme codes
master_codes = set(fund_master["amfi_code"])

nav_codes = set(nav_history["amfi_code"])

# Missing codes
missing_codes = master_codes - nav_codes

print("=" * 80)
print("AMFI CODE VALIDATION")
print("=" * 80)

print(f"\nFund Master Codes : {len(master_codes)}")
print(f"NAV History Codes : {len(nav_codes)}")

print(f"\nMissing Codes : {len(missing_codes)}")

if len(missing_codes) == 0:
    print("\nSUCCESS : All AMFI codes exist in NAV History")
else:
    print("\nMissing AMFI Codes")
    print(missing_codes)