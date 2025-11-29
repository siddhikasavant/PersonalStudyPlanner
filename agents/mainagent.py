import sqlite3
from tools.schedule_generator import generate_schedule

class MainAgent:
    def __init__(self, db_path='data/memory.db'):
        self.conn = sqlite3.connect(db_path)
        self.c = self.conn.cursor()
    
    def add_subject(self, name):
        self.c.execute("INSERT OR IGNORE INTO Subjects(name) VALUES(?)", (name,))
        self.conn.commit()
    
    def create_schedule(self, subjects, start_date):
        schedule = generate_schedule(subjects, start_date)
        # DB storing will go here later
        return schedule
    
    def close(self):
        self.conn.close()

