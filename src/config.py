import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parent.parent / ".env"
print(f"Looking for .env at: {env_path}")
print(f".env exists: {env_path.exists()}")

load_dotenv(env_path)

BLYNK_AUTH_TOKEN = os.getenv("BLYNK_AUTH_TOKEN", "")
TEMP_HIGH_THRESHOLD = float(os.getenv("TEMP_HIGH_THRESHOLD", "26"))
HUMIDITY_HIGH_THRESHOLD = float(os.getenv("HUMIDITY_HIGH_THRESHOLD", "65"))

print(f"BLYNK_AUTH_TOKEN loaded: {bool(BLYNK_AUTH_TOKEN)}")