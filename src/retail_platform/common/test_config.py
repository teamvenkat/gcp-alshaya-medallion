from retail_platform.common.config import config

print("Project ID :", config.get("project", "id"))
print("Region     :", config.get("project", "region"))
print("Bucket     :", config.get("storage", "bucket"))
print("Raw Path   :", config.get("gcs", "raw"))