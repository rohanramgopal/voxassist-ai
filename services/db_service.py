import sqlite3
from config.settings import DB_PATH


class DatabaseService:
    def __init__(self):
        self.db_path = DB_PATH
        self.init_db()

    def get_connection(self):
        return sqlite3.connect(self.db_path)

    def init_db(self):
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS memories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS reminders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT NOT NULL,
                remind_at TEXT,
                recurring TEXT DEFAULT 'none',
                triggered INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        conn.commit()

        cursor.execute("PRAGMA table_info(reminders)")
        columns = [row[1] for row in cursor.fetchall()]

        if "recurring" not in columns:
            cursor.execute("ALTER TABLE reminders ADD COLUMN recurring TEXT DEFAULT 'none'")
            conn.commit()

        conn.close()
