from common import create_spark
from pyspark.sql import functions as F, types as T
spark=create_spark('training-payment-etl')
try:
 schema=T.StructType([T.StructField('payment_id',T.StringType()),T.StructField('taxpayer_id',T.StringType()),T.StructField('payment_date',T.DateType()),T.StructField('amount',T.LongType()),T.StructField('channel',T.StringType()),T.StructField('status',T.StringType())])
 payments=spark.read.option('header',True).schema(schema).csv('/home/spark/datasets/payments.csv')
 result=(payments.filter(F.col('status')=='PAID').groupBy('taxpayer_id')
     .agg(F.sum('amount').alias('payment_total')))
 result.write.mode('overwrite').parquet('/home/spark/outputs/payment_summary')
 print('Top payments:');result.orderBy(F.desc('payment_total')).show(10,False)
finally:spark.stop()
