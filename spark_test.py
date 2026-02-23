from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder \
    .appName("EnergyTest") \
    .master("local[*]") \
    .getOrCreate()

print("Spark Version:", spark.version)

spark.stop()