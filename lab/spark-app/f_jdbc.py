from common import create_spark
from pyspark.sql import functions as F
import os
spark=create_spark('training-jdbc')
url=f"jdbc:postgresql://{os.getenv('POSTGRES_HOST','postgres')}:5432/{os.getenv('POSTGRES_DB','training')}"
properties={'user':os.getenv('POSTGRES_USER','spark'),'password':os.getenv('POSTGRES_PASSWORD','spark'),'driver':'org.postgresql.Driver'}
try:
 reference=spark.read.jdbc(url,'taxpayer_reference',properties=properties)
 reference.show(truncate=False)
 # Demonstration write; precreated table has a primary key, so use a separate table for reproducibility.
 metrics=reference.groupBy('region').agg(F.count('*').alias('reference_count'))
 metrics.write.mode('overwrite').jdbc(url,'reference_region_metrics',properties=properties)
 print('Written reference_region_metrics to PostgreSQL')
finally:spark.stop()
