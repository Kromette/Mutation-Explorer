import duckdb
import pandas as pd

conn = duckdb.connect("data_pipeline/dbt/protein_stability_dbt/dev.duckdb")

df = pd.read_csv("data/raw/fireprot_upload/csvs/4_fireprotDB_bestpH.csv", index_col=0)

conn.execute("CREATE OR REPLACE TABLE raw_mutations AS SELECT * FROM df")
