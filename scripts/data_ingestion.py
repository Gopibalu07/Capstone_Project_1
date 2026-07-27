from pathlib import Path
import pandas as pd

data_path = Path("data/raw")

csv_files = list(data_path.glob("*.csv"))

print(f"Total CSV Files: {len(csv_files)}")

for file in csv_files:
    print("="*60)
    print(file.name)

    df = pd.read_csv(file)

    print("Shape")
    print(df.shape)

    print("\nColumns")
    print(df.columns)

    print("\nData Types")
    print(df.dtypes)

    print("\nFirst 5 Rows")
    print(df.head())

    print("\n")