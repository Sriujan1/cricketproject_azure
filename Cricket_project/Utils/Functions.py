# Databricks notebook source
# MAGIC %run "./Configurations"

# COMMAND ----------

import http.client

def getData(s):
    conn = http.client.HTTPSConnection("cricbuzz-cricket.p.rapidapi.com")
    headers = {
        'x-rapidapi-key': f"{secret_key}",
        'x-rapidapi-host': "cricbuzz-cricket.p.rapidapi.com"
    }

    conn.request("GET", f"{s}", headers=headers)

    res = conn.getresponse()
    data = res.read()

    return data
