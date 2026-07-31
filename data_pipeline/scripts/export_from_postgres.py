from pathlib import Path
import duckdb

ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = ROOT.parent

EXPORT_DIR = PROJECT_ROOT / "data" / "intermediate" / "exports"
EXPORT_DIR.mkdir(parents=True, exist_ok=True)

POSTGRES = (
    "host=localhost "
    "port=5432 "
    "dbname=fireprotdb "
    "user=fireprot "
    "password=fireprot"
)

TABLES = [
    ("staging", "stg_mutations"),
    ("staging", "stg_proteins"),
]

conn = duckdb.connect()

conn.execute("INSTALL postgres")
conn.execute("LOAD postgres")

for schema, table in TABLES:

    output = EXPORT_DIR / f"{table}.parquet"

    print(f"Export {table}")

    conn.execute(f"""
        COPY (

            SELECT *

            FROM postgres_scan(
                '{POSTGRES}',
                '{schema}',
                '{table}'
            )

        )

        TO '{output}'

        (FORMAT PARQUET);
    """)

print("Done")