import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'secret_key'

# Initialize the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Create a connection to the database
conn = sqlite3.connect('database.db')

# Open the schema.sql file and read the SQL commands
with open('schema.sql', 'r') as f:
    schema = f.read()

# Execute the SQL commands to create the tables
conn.executescript(schema)

# Close the connection to the database
conn.close()

db.init_app(app)