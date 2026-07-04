from pathlib import Path
from typing import Any

import yaml


class Config:
    """
    Loads and provides access to the project configuration.
    """

    def __init__(self) -> None:
        config_path = (
            Path(__file__).resolve()
            .parent.parent.parent
            / "config"
            / "gcp_config.yaml"
        )

        with open(config_path, "r", encoding="utf-8") as file:
            self._config = yaml.safe_load(file)

    def get(self, *keys: str) -> Any:
        """
        Retrieve a configuration value using nested keys.

        Example:
            config.get("project", "id")
        """

        value = self._config

        for key in keys:
            value = value[key]

        return value


config = Config()