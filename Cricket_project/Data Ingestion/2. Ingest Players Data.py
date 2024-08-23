# Databricks notebook source
# MAGIC %run "../Utils/Configurations"

# COMMAND ----------

# MAGIC %run "../Utils/Functions"

# COMMAND ----------

df = spark.read.parquet(f"{bronze_folder_path}/teams")
display(df)

# COMMAND ----------

import json

data = []

for i in df.select("team_id").rdd.flatMap(lambda x: x).collect():
    print(i)
    response_data = getData(f"/teams/v1/{i}/players")
    if response_data:
        json_data = json.loads(response_data)
        print(json_data)
        # if "player" in json_data:
        #     data.append(json_data["player"][1:])

# print(data)
