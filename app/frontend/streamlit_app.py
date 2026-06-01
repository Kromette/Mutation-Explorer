import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import duckdb
import streamlit as st
from stmol import showmol
import pandas as pd
from app.utils.model_loader import load_model
from app.utils.feature_engineering import build_features
from app.utils.viewer import render_mutation

conn = duckdb.connect("data_pipeline/protein_stability_dbt/dev.duckdb")


proteins = conn.execute("""
SELECT * FROM mart_proteins
""").fetchdf()

mutations = conn.execute("""
SELECT * FROM stg_mutations
""").fetchdf()

st.title("🧬 Protein Stability Explorer")

st.write("Predict protein mutation stability.")

selected_protein = st.selectbox(
    "Select protein",
    proteins["protein_name"].tolist()
)

selected_protein_id = proteins[proteins["protein_name"] == selected_protein]["pdb_id"].iloc[0]
max_position = int(proteins[proteins["protein_name"] == selected_protein]["sequence_length"].iloc[0])

mutations = mutations[mutations["protein_name"] == selected_protein]
with st.expander("Protein informations"):
    st.write(f"Protein length: {max_position} aa")
    st.write(f"PDB ID: {selected_protein_id}")
    st.write("Known mutations for this protein:")
    st.dataframe(mutations[["mutation", "position", "ddG"]])



position = st.number_input(
    "Mutation position",
    min_value=1,
    max_value=max_position,
    value=int(max_position / 2)
)

wild_type_aa = mutations[mutations["protein_name"] == selected_protein]["wild_type"].iloc[0]

amino_acids = [
    "A", "V", "L", "I",
    "D", "E", "K", "R",
    "S", "T", "Y", "F"
]

col1, col2 = st.columns(2)

with col1:
    wild_type = st.selectbox(
    "Wild type amino acid",
    wild_type_aa
)

with col2:
    mutation = st.selectbox(
    "Mutated amino acid",
    amino_acids
)




# normalize to the first pdb id in case multiple ids are concatenated with '|'
pdb_id_only = str(selected_protein_id).split("|")[0]
pdb_path = ROOT / "data" / "raw" / "fireprot_upload" / "pdbs" / f"{pdb_id_only}.pdb"

if not pdb_path.exists():
    st.error(f"PDB file not found: {pdb_path.name}")
else:
    view = render_mutation(str(pdb_path), position)
    showmol(view, height=600, width=800)


model = load_model()

if st.button("Predict stability"):

    features = build_features(
        position,
        wild_type,
        mutation
    )

    X = pd.DataFrame([features])

    prediction = model.predict(X)[0]

    probability = model.predict_proba(X)[0].max()

    st.subheader("Prediction")

    if prediction:
        st.success("✅ Stable mutation")
    else:
        st.error("⚠️ Unstable mutation")

    st.write(f"Confidence: {probability:.2f}")

    st.write(features)