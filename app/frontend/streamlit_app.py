import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st

st.title("🧬 Protein Stability Explorer")

st.write("Predict protein mutation stability.")

position = st.number_input(
    "Mutation position",
    min_value=1,
    max_value=2000,
    value=100
)

amino_acids = [
    "A", "V", "L", "I",
    "D", "E", "K", "R",
    "S", "T", "Y", "F"
]

wild_type = st.selectbox(
    "Wild type amino acid",
    amino_acids
)

mutation = st.selectbox(
    "Mutated amino acid",
    amino_acids
)

import pandas as pd

from app.utils.model_loader import load_model
from app.utils.feature_engineering import build_features

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