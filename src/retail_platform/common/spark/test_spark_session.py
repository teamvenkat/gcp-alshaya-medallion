from retail_platform.common.spark.spark_session import SparkSessionFactory


def main():

    spark = SparkSessionFactory.create("Spark Test")

    print("=" * 50)
    print("Spark Version :", spark.version)
    print("Application   :", spark.sparkContext.appName)
    print("Master        :", spark.sparkContext.master)
    print("=" * 50)

    spark.stop()


if __name__ == "__main__":
    main()