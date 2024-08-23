# Databricks notebook source
bronze_folder_path = "abfss://bronze@footballprojectadls.dfs.core.windows.net/"
silver_folder_path = "abfss://silver@footballprojectadls.dfs.core.windows.net/"
gold_folder_path = "abfss://gold@footballprojectadls.dfs.core.windows.net/"
secret_key = dbutils.secrets.get(scope="football_project_secret_scope",key="rapid-api-key")
