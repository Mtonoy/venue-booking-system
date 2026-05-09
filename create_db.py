import sqlite3

conn = sqlite3.connect('database.db')

conn.execute('''
CREATE TABLE IF NOT EXISTS bookings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_name TEXT,
    event_type TEXT,
    venue TEXT,
    start_datetime TEXT,
    end_datetime TEXT,
    organizer TEXT,
    email TEXT,
    requirements TEXT,
    status TEXT DEFAULT 'Pending',
    conflict INTEGER DEFAULT 0
)
''')

conn.commit()
conn.close()

print("Database created successfully!")