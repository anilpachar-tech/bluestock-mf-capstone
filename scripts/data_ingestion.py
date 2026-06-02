from pathlib import Path
import pandas as pd

# Data Folder Path

DATA_FOLDER = Path("data/raw")

# Get all CSV files
csv_files = sorted(DATA_FOLDER.glob("*.csv"))

print("=" * 80)
print(f"Found {len(csv_files)} CSV files")
print("=" * 80)

# Store datasets and quality report
datasets = {}
quality_report = []


# Read and Inspect Each Dataset

for file in csv_files:

    print("\n")
    print("=" * 80)
    print(f"Dataset : {file.name}")
    print("=" * 80)

    try:
        # Load dataset
        df = pd.read_csv(file)

        # Store dataframe
        datasets[file.stem] = df

        # Basic information
        print(f"\nShape : {df.shape}")

        print("\nData Types")
        print(df.dtypes)

        print("\nFirst 5 Rows")
        print(df.head())

        # Missing values
        missing_count = df.isnull().sum().sum()

        print("\nMissing Values By Column")
        print(df.isnull().sum())

        # Duplicate rows
        duplicate_count = df.duplicated().sum()

        print("\nDuplicate Rows")
        print(duplicate_count)

        # Save summary
        quality_report.append({
            "dataset": file.name,
            "rows": df.shape[0],
            "columns": df.shape[1],
            "missing_values": missing_count,
            "duplicate_rows": duplicate_count
        })

    except Exception as e:
        print(f"\nError loading {file.name}")
        print(e)


# Save Data Quality Summary


report_df = pd.DataFrame(quality_report)

report_path = Path("reports/data_quality_summary.csv")

report_df.to_csv(
    report_path,
    index=False
)

print("\n")
print("=" * 80)
print("Data Quality Summary Saved Successfully")
print(f"Location : {report_path}")
print("=" * 80)