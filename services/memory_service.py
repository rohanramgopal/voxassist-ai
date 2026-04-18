from services.db_service import DatabaseService


class MemoryService:
    def __init__(self):
        self.db = DatabaseService()

    def remember(self, text: str) -> str:
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO memories (content) VALUES (?)", (text.strip(),))
        conn.commit()
        conn.close()
        return "I will remember that."

    def recall_all(self) -> str:
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT content FROM memories ORDER BY id DESC LIMIT 10")
        rows = cursor.fetchall()
        conn.close()

        if not rows:
            return "I do not remember anything yet."

        memories = [row[0] for row in rows]
        return "Here is what I remember: " + "; ".join(memories)

    def clear_memory(self) -> str:
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM memories")
        conn.commit()
        conn.close()
        return "Memory cleared."
