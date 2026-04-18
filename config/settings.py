import os
from dotenv import load_dotenv

load_dotenv()

ASSISTANT_NAME = os.getenv("ASSISTANT_NAME", "vox").lower()
USER_NAME = os.getenv("USER_NAME", "User")
ENABLE_AI = os.getenv("ENABLE_AI", "false").lower() == "true"
ENABLE_GUI = os.getenv("ENABLE_GUI", "true").lower() == "true"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
STT_MODE = os.getenv("STT_MODE", "google").lower()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
NOTES_DIR = os.path.join(DATA_DIR, "notes")
LOGS_DIR = os.path.join(DATA_DIR, "logs")
MEMORY_DIR = os.path.join(DATA_DIR, "memory")
DB_PATH = os.path.join(DATA_DIR, "voxassist.db")

for path in [DATA_DIR, NOTES_DIR, LOGS_DIR, MEMORY_DIR]:
    os.makedirs(path, exist_ok=True)
