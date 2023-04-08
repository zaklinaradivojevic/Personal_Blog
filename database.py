import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

conn = sqlite3.connect('database.db')
c = conn.cursor()

# Create users table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )''')

# Add a test user
test_username = 'testuser'
test_password = 'testpassword'
hashed_password = generate_password_hash(test_password)
c.execute('''INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)''', (test_username, hashed_password))

conn.commit()
conn.close()
