from pathlib import Path

from retail_platform.cloud.storage.gcs_uploader import GCSUploader

uploader = GCSUploader()

uploader.upload_file(
    source_file=Path("README.md"),
    destination_path="logs/readme_test_upload.md",
)

print("\nUpload Successful")