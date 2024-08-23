# Databricks notebook source
# MAGIC %run "../Utils/Configurations"

# COMMAND ----------

# MAGIC
# MAGIC %run "../Utils/Functions"

# COMMAND ----------

teams_list = getData("/teams/v1/international")

# COMMAND ----------

import json
from pyspark.sql.functions import col

response_data = json.loads(teams_list)
df = spark.createDataFrame(response_data["list"]).sort("teamId"). \
        withColumnRenamed("teamId","team_id"). \
        withColumnRenamed("teamName","team_name"). \
        filter(col("teamName") != "Associate Teams"). \
        filter(col("teamName") != "Test Teams"). \
        drop("countryName", "teamSName", "imageId")

display(df)

# COMMAND ----------

df.write.mode("overwrite").parquet(f"{bronze_folder_path}/teams")
