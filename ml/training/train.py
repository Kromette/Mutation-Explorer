import duckdb
import pandas as pd

conn = duckdb.connect("data_pipeline/dbt/protein_stability/dev.duckdb")

df = conn.execute("""
SELECT * FROM mart_ml_dataset
""").fetchdf()

print(df.head())