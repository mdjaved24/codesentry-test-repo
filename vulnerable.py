# vulnerable.py - FIXED VERSION
import sqlite3
import os

def login(username, password):
    # FIXED: Use environment variable instead of hardcoded secret
    SECRET_KEY = os.getenv('DATABASE_SECRET_KEY')
    if not SECRET_KEY:
        raise ValueError("DATABASE_SECRET_KEY environment variable not set")
    
    # FIXED: Use parameterized query to prevent SQL injection
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username=? AND password=?"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    conn.close()
    
    return result is not None