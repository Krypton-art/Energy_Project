from pyspark.sql import SparkSession
from pyspark.sql.functions import month, year, sum as spark_sum
import pandas as pd

# Create Spark session
spark = SparkSession.builder \
    .appName("EnergyBatchProcessing") \
    .master("local[*]") \
    .getOrCreate()

# Read CSV
df = spark.read.csv("energy_data.csv", header=True, inferSchema=True)

# Extract month and year
df = df.withColumn("month", month("date")) \
       .withColumn("year", year("date"))

# Aggregate monthly consumption
monthly_usage = df.groupBy("year", "month") \
    .agg(spark_sum("consumption_kwh").alias("total_consumption")) \
    .orderBy("year", "month")

# Show result
monthly_usage.show()

# Convert to Pandas
pandas_df = monthly_usage.toPandas()

# Save to CSV
pandas_df.to_csv("monthly_aggregated.csv", index=False)

spark.stop()

print("Spark batch processing completed!")