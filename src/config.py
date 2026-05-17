import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parent.parent / ".env"

load_dotenv(env_path)

BLYNK_AUTH_TOKEN = os.getenv("BLYNK_AUTH_TOKEN", "")
TEMP_HIGH_THRESHOLD = float(os.getenv("TEMP_HIGH_THRESHOLD", "21"))
HUMIDITY_HIGH_THRESHOLD = float(os.getenv("HUMIDITY_HIGH_THRESHOLD", "45"))
SIMULATE_SENSOR = os.getenv("SIMULATE_SENSOR", "false").lower() == "true"

