import sqlite3
import os

class MainAgent:
    def __init__(self, db_path="data/memory.db"):
        self.db_path = db_path
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self._create_tables()
    
    def _create_tables(self):
        """Create table if it doesn't exist"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                subject TEXT NOT NULL,
                date TEXT,
                duration INTEGER,
                completed INTEGER DEFAULT 0,
                notes TEXT
            )
        """)
        conn.commit()
        conn.close()

    def add_subject(self, subject, date="TBD", duration=2, notes=None):
        """Add a new subject/session"""
        if not subject.strip():
            raise ValueError("Subject cannot be empty")
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO sessions (subject, date, duration, completed, notes) VALUES (?, ?, ?, ?, ?)",
            (subject, date, duration, 0, notes)
        )
        conn.commit()
        conn.close()

    def view_schedule(self):
        """Return all sessions"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM sessions")
        data = cursor.fetchall()
        conn.close()
        return data

    def mark_completed(self, session_id):
        """Mark a session as completed"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("UPDATE sessions SET completed = 1 WHERE id = ?", (session_id,))
        conn.commit()
        conn.close()
