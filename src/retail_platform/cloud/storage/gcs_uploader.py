"""
Component : GCSUploader
Version   : 1.1.0

Responsibilities
----------------
- Upload files to Google Cloud Storage
- Retry uploads on transient failures
- Log upload duration
- Log file size
"""

import time
from pathlib import Path

from google.cloud import storage

from retail_platform.common.config import config
from retail_platform.common.logger import get_logger

logger = get_logger(__name__)


class GCSUploader:

    def __init__(self):

        self.project_id = config.get("project", "id")
        self.bucket_name = config.get("storage", "bucket")

        self.max_retries = config.get("upload", "max_retries")
        self.retry_delay = config.get("upload", "retry_delay_seconds")

        self.client = storage.Client(project=self.project_id)
        self.bucket = self.client.bucket(self.bucket_name)

    def upload_file(
        self,
        source_file: Path,
        destination_path: str,
    ) -> None:

        if not source_file.exists():
            raise FileNotFoundError(source_file)

        file_size_mb = source_file.stat().st_size / (1024 * 1024)

        logger.info(
            "Uploading '%s' (%.2f MB)",
            source_file.name,
            file_size_mb,
        )

        logger.info(
            "Destination : gs://%s/%s",
            self.bucket_name,
            destination_path,
        )

        blob = self.bucket.blob(destination_path)

        last_exception = None

        for attempt in range(1, self.max_retries + 1):

            try:

                start = time.perf_counter()

                blob.upload_from_filename(str(source_file))

                elapsed = time.perf_counter() - start

                logger.info(
                    "Upload completed in %.2f seconds",
                    elapsed,
                )

                return

            except Exception as ex:

                last_exception = ex

                logger.warning(
                    "Attempt %s/%s failed : %s",
                    attempt,
                    self.max_retries,
                    ex,
                )

                if attempt < self.max_retries:

                    wait_time = self.retry_delay * (2 ** (attempt - 1))

                    logger.info(
                        "Retrying in %s seconds...",
                        wait_time,
                    )

                    time.sleep(wait_time)

        raise last_exception