from pathlib import Path
import pandas as pd

# Location of the downloaded dataset
DATASET_PATH = Path("data/sample/kaggle/olist")


def profile_dataset(csv_file: Path) -> None:
    """Profile a single CSV dataset."""

    print("=" * 80)
    print(f"Dataset : {csv_file.name}")
    print("=" * 80)

    df = pd.read_csv(csv_file)

    print(f"Rows    : {len(df):,}")
    print(f"Columns : {len(df.columns)}")

    print("\nColumn Information")
    print("-" * 80)

    summary = pd.DataFrame(
        {
            "Column": df.columns,
            "Data Type": df.dtypes.astype(str),
            "Null Count": df.isnull().sum().values,
        }
    )

    print(summary.to_string(index=False))

    print("\nSample Records")
    print("-" * 80)

    print(df.head())

    print("\n")


def main():

    csv_files = sorted(DATASET_PATH.glob("*.csv"))

    if not csv_files:
        print(f"No CSV files found in {DATASET_PATH}")
        return

    print(f"\nFound {len(csv_files)} datasets.\n")

    for csv in csv_files:
        profile_dataset(csv)


if __name__ == "__main__":
    main()