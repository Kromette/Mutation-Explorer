from pathlib import Path
import subprocess
import sys

# Répertoire contenant ce script
SCRIPT_DIR = Path(__file__).resolve().parent

print("=== Étape 1 : Export PostgreSQL → Parquet ===")
subprocess.run(
    [sys.executable, str(SCRIPT_DIR / "export_from_postgres.py")],
    check=True,
)

print("=== Étape 2 : Construction de DuckDB ===")
subprocess.run(
    [sys.executable, str(SCRIPT_DIR / "build_duckdb.py")],
    check=True,
)

print("✅ Pipeline terminée avec succès.")