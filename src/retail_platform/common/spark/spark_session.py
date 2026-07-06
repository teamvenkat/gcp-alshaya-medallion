from pyspark.sql import SparkSession

from retail_platform.common.config import config


class SparkSessionFactory:
    """
    Creates and manages SparkSession instances.
    """

    @staticmethod
    def create(app_name: str = "Retail Platform") -> SparkSession:

        return (
            SparkSession.builder
            .appName(app_name)
            .master("local[*]")
            .config("spark.sql.session.timeZone", "UTC")
            .getOrCreate()
        )