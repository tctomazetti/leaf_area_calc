from pathlib import Path

# Base dir
BASE_DIR = Path(__file__).resolve().parent.parent

# project dir
DATA_DIR = BASE_DIR / 'src' / 'data'
INPUT_DIR = BASE_DIR / 'input'
OUTPUT_DIR = BASE_DIR / 'output'

# models.json path
MODELS_FILE = DATA_DIR / 'models.json'


