import joblib
from pathlib import Path

def load_model():
    repo_root = Path(__file__).resolve().parents[2]
    model_path = repo_root / "ml" / "models" / "random_forest.pkl"
    model = joblib.load(model_path)
    return model