from pathlib import Path

# Base dir
BASE_DIR = Path(__file__).resolve().parent.parent

# project dir
DATA_DIR = BASE_DIR / "src" / "data"
BIBLIOGRAPHY_DIR = DATA_DIR / "bibliography"
INPUT_DIR = BASE_DIR / "input"
OUTPUT_DIR = BASE_DIR / "output"

# json paths
MODELS_FILE = DATA_DIR / "models.json"
BIBLIOGRAPHY_FILE = DATA_DIR / "bibliography.json"
