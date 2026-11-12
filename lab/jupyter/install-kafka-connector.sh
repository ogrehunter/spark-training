#!/bin/sh
set -eu

KAFKA_PACKAGE="org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.7"
EXAMPLES_JAR="/opt/spark/examples/jars/spark-examples_2.12-3.5.7.jar"

/opt/spark/bin/spark-submit \
  --master 'local[1]' \
  --packages "$KAFKA_PACKAGE" \
  --class org.apache.spark.examples.SparkPi \
  "$EXAMPLES_JAR" 1

cp /root/.ivy2/jars/*.jar /opt/spark/jars/
rm -rf /root/.ivy2
