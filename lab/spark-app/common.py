"""Shared Spark creation for trainer-managed CLI jobs."""
import os
from pyspark.sql import SparkSession

def create_spark(name):
    return (SparkSession.builder.appName(name)
        .master(os.getenv('SPARK_MASTER','spark://spark-master:7077'))
        .config('spark.driver.host','jupyter')
        .config('spark.driver.bindAddress','0.0.0.0')
        .config('spark.driver.port','4050')
        .config('spark.blockManager.port','4051')
        .config('spark.executor.cores','1')
        .config('spark.executor.memory','1g')
        .config('spark.sql.shuffle.partitions','4')
        .config('spark.ui.port','4040')
        .getOrCreate())
