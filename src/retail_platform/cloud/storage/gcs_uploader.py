from pathlib import Path

from google.cloud import storage

from retail_platform.common.config import config
from retail_platform.common.logger import get_logger

logger = get_logger(__name__)


class GCSUploader:
    """
    Uploads files to Google Cloud Storage.
    """

    def __init__(self) -> None:
        self.project_id = config.get("project", "id")
        self.bucket_name = config.get("storage", "bucket")

        self.client = storage.Client(project=self.project_id)
        self.bucket = self.client.bucket(self.bucket_name)

    def upload_file(
        self,
        source_file: Path,
        destination_path: str,
    ) -> None:
        """
        Upload a local file to Google Cloud Storage.

        Parameters
        ----------
        source_file : Path
            Local file path.

        destination_path : str
            Destination object path inside the bucket.
        """

        logger.info(
            "Uploading '%s' to 'gs://%s/%s'",
            source_file.name,
            self.bucket_name,
            destination_path,
        )

        blob = self.bucket.blob(destination_path)

        blob.upload_from_filename(str(source_file))

        logger.info(
            "Upload completed for '%s'",
            source_file.name,
        )