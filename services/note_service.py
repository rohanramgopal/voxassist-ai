import os
from datetime import datetime
from config.settings import NOTES_DIR

class NoteService:
    def save_note(self, content: str) -> str:
        filename = os.path.join(
            NOTES_DIR,
            f"note_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        )
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        return f"Note saved as {os.path.basename(filename)}"