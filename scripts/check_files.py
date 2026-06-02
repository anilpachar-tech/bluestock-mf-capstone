from pathlib import Path

data_path = Path(r"D:\Bluestock Internship Project\bluestock_mf_capstone\data\raw")
for file in data_path.glob("*.csv"):
    print(file.name)