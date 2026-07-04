from pathlib import Path

import yaml

from retail_platform.common.paths import CONFIG_DIR


class DatasetRegistry:
    """
    Loads dataset metadata from the configuration directory.
    """

    def __init__(self) -> None:

        self._datasets = {}

        dataset_directory = CONFIG_DIR / "datasets"

        if not dataset_directory.exists():
            raise FileNotFoundError(
                f"Dataset configuration directory not found: {dataset_directory}"
            )

        for yaml_file in sorted(dataset_directory.glob("*.yaml")):

            with yaml_file.open("r", encoding="utf-8") as file:

                metadata = yaml.safe_load(file)

                dataset_name = metadata["dataset_name"]

                self._datasets[dataset_name] = metadata

    def get(self, dataset_name: str) -> dict:

        return self._datasets.get(dataset_name)

    def get_all(self) -> list:

        return list(self._datasets.values())

    def get_by_source_file(self, source_file: str) -> dict:

        for dataset in self._datasets.values():

            if dataset["source_file"] == source_file:
                return dataset

        return None