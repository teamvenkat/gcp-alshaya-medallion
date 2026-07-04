from retail_platform.ingestion.framework.dataset_registry import DatasetRegistry

registry = DatasetRegistry()

datasets = registry.get_all()

print(f"Datasets Loaded: {len(datasets)}")

for dataset in datasets:
    print(dataset["dataset_name"])