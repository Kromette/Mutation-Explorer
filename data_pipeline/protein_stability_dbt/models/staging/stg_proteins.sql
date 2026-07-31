{{ config(materialized='table') }}

SELECT *
FROM read_parquet(
    '{{ var("export_dir") }}/stg_proteins.parquet'
)