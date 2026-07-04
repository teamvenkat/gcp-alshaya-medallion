from pathlib import Path

from retail_platform.ingestion.validators.file_validator import FileValidator

DATASET = Path(
    "data/sample/kaggle/olist/olist_customers_dataset.csv"
)

try:
    FileValidator.validate(DATASET)
    print("Validation Successful")
except Exception as ex:
    print(ex)