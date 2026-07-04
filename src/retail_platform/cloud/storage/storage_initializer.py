from google.cloud import storage

from retail_platform.common.config import config
from retail_platform.common.logger import get_logger

logger = get_logger(__name__)


class StorageInitializer:
    """
    Initializes the GCS Data Lake structure.
    """

    def __init__(self) -> None:
        self.client = storage.Client(
            project=config.get("project", "id")
        )

        self.bucket_name = config.get("storage", "bucket")
        self.bucket = self.client.bucket(self.bucket_name)

    def verify_bucket(self) -> None:
        """
        Verify that the configured bucket exists.
        """

        if not self.bucket.exists():
            raise Exception(
                f"Bucket '{self.bucket_name}' does not exist."
            )

        logger.info("Bucket verified: %s", self.bucket_name)

    def initialize_structure(self) -> None:
        """
        Create logical prefixes inside the bucket.
        """

        prefixes = [
            "raw/",
            "bronze/",
            "silver/",
            "gold/",
            "archive/",
            "logs/",
        ]

        for prefix in prefixes:

            blob = self.bucket.blob(f"{prefix}.keep")

            if not blob.exists():

                blob.upload_from_string("")

                logger.info("Created prefix: %s", prefix)

            else:

                logger.info("Prefix already exists: %s", prefix)