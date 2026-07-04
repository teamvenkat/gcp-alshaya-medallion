from retail_platform.cloud.storage.storage_initializer import StorageInitializer

initializer = StorageInitializer()

initializer.verify_bucket()

initializer.initialize_structure()