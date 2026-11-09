"""Run while host executes: python3 scripts/emit_stream.py"""
from common import create_spark
from pyspark.sql import functions as F, types as T
spark=create_spark('training-streaming')
schema=T.StructType([T.StructField('event_id',T.StringType()),T.StructField('taxpayer_id',T.StringType()),T.StructField('event_time',T.StringType()),T.StructField('amount',T.LongType()),T.StructField('channel',T.StringType())])
source=(spark.readStream.schema(schema).option('maxFilesPerTrigger',1)
  .json('/home/spark/stream-input').withColumn('ts',F.to_timestamp('event_time')))
windowed=(source.withWatermark('ts','2 minutes').groupBy(F.window('ts','1 minute'),'channel').agg(F.sum('amount').alias('amount_total')))
query=(windowed.writeStream.outputMode('update').format('console')
    .option('truncate',False).option('checkpointLocation','/home/spark/outputs/stream_checkpoint_cli').start())
try:query.awaitTermination()
except KeyboardInterrupt:query.stop()
finally:spark.stop()
