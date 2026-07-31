from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
DBT_PROJECT = ROOT / "protein_stability_dbt"

subprocess.run(
    ["dbt", "run"],
    cwd=DBT_PROJECT,
    check=True,
)
