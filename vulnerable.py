# test_vulnerable.py - FIXED VERSION
import sqlite3
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def login(username, password):
    # FIXED: Use environment variable instead of hardcoded secret
    API_KEY = os.getenv('API_KEY')
    if not API_KEY:
        raise ValueError("API_KEY environment variable not set")
    
    # FIXED: Use parameterized query to prevent SQL injection
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Parameterized query - safe from SQL injection
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (username, password))
    
    result = cursor.fetchone()
    conn.close()
    
    return result is not None


# Optional: Add proper error handling
def login_safe(username, password):
    """Safer version with better error handling"""
    if not username or not password:
        return False
    
    try:
        API_KEY = os.getenv('API_KEY')
        if not API_KEY:
            print("Warning: API_KEY not configured")
        
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        
        # Using parameterized query
        cursor.execute(
            "SELECT * FROM users WHERE username = ? AND password = ?",
            (username, password)
        )
        
        return cursor.fetchone() is not None
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    finally:
        if conn:
            conn.close()