from pathlib import Path

from retail_platform.common.config import config


class DatasetDiscovery:
    """
    Discovers source datasets available for ingestion.
    """

    def __init__(self) -> None:
        self.dataset_path = Path(
            config.get("paths", "local_dataset")
        )

    def discover(self) -> list[Path]:
        """
        Returns all CSV files sorted alphabetically.
        """

        return sorted(self.dataset_path.glob("*.csv"))