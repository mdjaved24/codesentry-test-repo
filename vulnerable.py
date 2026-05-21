# vulnerable.py
import sqlite3

def login(username, password):
    # Hardcoded secret - CRITICAL
    SECRET_KEY = "my_super_secret_password_123"
    
    # SQL Injection - CRITICAL  
    conn = sqlite3.connect('users.db')
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    conn.execute(query)
    
    return True