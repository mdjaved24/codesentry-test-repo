# test_vulnerable.py
import sqlite3
import os

def login(username, password):
    # Hardcoded secret - CRITICAL
    API_KEY = "sk-1234567890abcdef"
    
    # SQL Injection - CRITICAL
    conn = sqlite3.connect('users.db')
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor = conn.execute(query)
    
    return cursor.fetchone() is not None