from pathlib import Path
import subprocess
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[2]

SCRIPTS_DIR = PROJECT_ROOT / "data_pipeline" / "scripts"

FIREPROT_DBT = PROJECT_ROOT / "data_pipeline" / "fireprotdb_dbt"


def run_command(command, cwd=None):
    print("\n▶", " ".join(map(str, command)))

    subprocess.run(
        command,
        cwd=cwd,
        check=True
    )


def main():

    print("=" * 60)
    print("INITIALISATION COMPLETE DU PIPELINE MUTATION-EXPLORER")
    print("=" * 60)

    print("\n1) Restauration FireProtDB PostgreSQL")

    run_command(
        [
            str(SCRIPTS_DIR / "restore_fireprotdb.sh")
        ]
    )

    print("\n2) Construction des tables staging PostgreSQL")

    run_command(
        [
            "dbt",
            "run"
        ],
        cwd=FIREPROT_DBT
    )

    print("\n3) Export des tables staging vers Parquet")

    run_command(
        [
            sys.executable,
            str(SCRIPTS_DIR / "export_from_postgres.py")
        ]
    )

    print("\n4) Construction de la base DuckDB")

    run_command(
        [
            sys.executable,
            str(SCRIPTS_DIR / "build_duckdb.py")
        ]
    )

    print("\n" + "=" * 60)
    print("PIPELINE INITIALISE AVEC SUCCES")
    print("=" * 60)


if __name__ == "__main__":
    main()
