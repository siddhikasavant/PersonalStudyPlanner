import sqlite3

conn = sqlite3.connect('data/memory.db')
c = conn.cursor()

c.execute("INSERT INTO Subjects(name) VALUES(?)", ("Math",))
conn.commit()

c.execute("SELECT * FROM Subjects")
print(c.fetchall())

conn.close()
