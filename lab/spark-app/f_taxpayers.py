from common import create_spark
from pyspark.sql import functions as F
spark=create_spark('training-taxpayers-etl')
try:
 df=(spark.read.option('header',True).option('inferSchema',True)
     .csv('/home/spark/datasets/taxpayers.csv'))
 result=(df.filter(F.col('active')==True)
     .groupBy('region','sector').agg(F.count('*').alias('active_taxpayers')))
 result.orderBy('region','sector').show(30,False)
 result.write.mode('overwrite').parquet('/home/spark/outputs/taxpayer_summary')
 print('Saved /home/spark/outputs/taxpayer_summary')
finally:spark.stop()
