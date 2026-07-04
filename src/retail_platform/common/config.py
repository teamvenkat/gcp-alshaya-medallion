from typing import Any

import yaml

from retail_platform.common.paths import CONFIG_DIR


class Config:
    """
    Loads the application configuration from YAML.
    """

    def __init__(self) -> None:

        config_path = CONFIG_DIR / "gcp_config.yaml"

        with config_path.open("r", encoding="utf-8") as file:
            self._config = yaml.safe_load(file)

    def get(self, *keys: str) -> Any:

        value = self._config

        for key in keys:
            value = value[key]

        return value


config = Config()