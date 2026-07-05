from pathlib import Path

from retail_platform.cloud.storage.gcs_uploader import GCSUploader
from retail_platform.common.config import config
from retail_platform.common.logger import get_logger
from retail_platform.ingestion.framework.dataset_registry import DatasetRegistry
from retail_platform.ingestion.validators.file_validator import FileValidator

logger = get_logger(__name__)


class UploadToGCS:

    def __init__(self):

        self.registry = DatasetRegistry()
        self.uploader = GCSUploader()

        self.local_dataset_path = Path(
            config.get("paths", "local_dataset")
        )

        self.uploaded = 0
        self.failed = 0

    def execute(self):

        logger.info("Starting Raw Data Upload")

        for dataset in self.registry.get_all():

            source_file = (
                self.local_dataset_path /
                dataset["source_file"]
            )

            destination = (
                f"{dataset['target_path']}/"
                f"{dataset['target_file']}"
            )

            logger.info("--------------------------------")

            logger.info(
                "Dataset : %s",
                dataset["dataset_name"],
            )

            try:

                FileValidator.validate(source_file)

                self.uploader.upload_file(
                    source_file,
                    destination,
                )

                self.uploaded += 1

            except Exception as ex:

                logger.error(ex)

                self.failed += 1

        logger.info("--------------------------------")
        logger.info("Upload Summary")
        logger.info("Uploaded : %s", self.uploaded)
        logger.info("Failed   : %s", self.failed)
        logger.info("--------------------------------")


if __name__ == "__main__":

    UploadToGCS().execute()