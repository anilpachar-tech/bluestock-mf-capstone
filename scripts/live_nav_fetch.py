from pathlib import Path
import requests
import pandas as pd

# Output Folder

OUTPUT_FOLDER = Path("data/raw")
OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

# Mutual Fund Scheme Codes

funds = {
    "HDFC_Top_100_Direct": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

# Fetch NAV Data

print("=" * 80)
print("Fetching Live NAV Data")
print("=" * 80)

for fund_name, scheme_code in funds.items():

    try:

        url = f"https://api.mfapi.in/mf/{scheme_code}"

        response = requests.get(url, timeout=30)

        response.raise_for_status()

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        output_file = OUTPUT_FOLDER / f"{fund_name}_NAV.csv"

        nav_df.to_csv(output_file, index=False)

        print(f"SUCCESS : {fund_name}")
        print(f"Rows Saved : {len(nav_df)}")
        print(f"File : {output_file}")
        print("-" * 60)

    except Exception as e:

        print(f"FAILED : {fund_name}")
        print(e)
        print("-" * 60)

print("\nAll NAV Fetch Operations Completed")
