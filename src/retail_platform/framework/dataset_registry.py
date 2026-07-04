from pathlib import Path
import yaml

from retail_platform.common.paths import CONFIG_DIR

class DatasetRegistry:
    """
    Loads dataset metadata from config/datasets.
    """

    def __init__(self):
        self._datasets = {}
        dataset_dir = CONFIG_DIR / "datasets"

        for file in sorted(dataset_dir.glob("*.yaml")):
            with file.open("r", encoding="utf-8") as f:
                metadata = yaml.safe_load(f)
                self._datasets[metadata["dataset_name"]] = metadata

    def get_all(self):
        return list(self._datasets.values())

    def get(self, dataset_name: str):
        return self._datasets.get(dataset_name)

    def get_by_source_file(self, source_file: str):
        for dataset in self._datasets.values():
            if dataset["source_file"] == source_file:
                return dataset
        return None
