import os
from datetime import datetime
from config.settings import LOGS_DIR

LOG_FILE = os.path.join(LOGS_DIR, "assistant.log")

def write_log(message: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")
