from retail_platform.ingestion.discovery.dataset_discovery import (
    DatasetDiscovery,
)

discovery = DatasetDiscovery()

files = discovery.discover()

print(f"Found {len(files)} datasets\n")

for file in files:
    print(file.name)