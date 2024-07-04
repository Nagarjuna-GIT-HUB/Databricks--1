# Databricks notebook source
from pyspark.sql import SparkSession
from pyspark.sql.types import *
spark = SparkSession.builder.appName("tmp").getOrCreate()
#SparkSession.builder.appName("ExampleApp").getOrCreate()

data = [
    (1,"John","phy"),
    (2,"Anna","che"),
    (3,"Peter","mat"),
    (4,"Linda","sci")
]

schema = "Id int,name string ,Dept string"

# Create DataFrame
df = spark.createDataFrame(data, schema)

#df.write.csv("/Filterstore/csv/Dept.csv")


df1 = df.write.mode("overwrite").saveAsTable("Dept")

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Grant USE SCHEMA permission
# MAGIC GRANT USAGE ON DATABASE main TO 'labuser6946072@vocareum.com';
# MAGIC
# MAGIC -- Grant CREATE TABLE permission
# MAGIC -- GRANT CREATE ON DATABASE <database_name> TO `<your_username>`;
# MAGIC
# MAGIC -- Grant SELECT permission (if needed)
# MAGIC -- GRANT SELECT ON DATABASE <database_name> TO `<your_username>`;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC create database Itsector ;

# COMMAND ----------

# MAGIC %sql
# MAGIC
