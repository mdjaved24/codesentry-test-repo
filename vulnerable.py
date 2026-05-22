"""
VULNERABLE APP - FOR TESTING ONLY
This file contains multiple security vulnerabilities for PRGate to detect
"""

import sqlite3
import hashlib
import subprocess
import pickle
import base64

# VULNERABILITY 1: Hardcoded Secret (CRITICAL)
SECRET_KEY = "super_secret_key_12345"
API_TOKEN = "sk-1234567890abcdef"
PASSWORD = "admin123"

# VULNERABILITY 2: SQL Injection (CRITICAL)
def get_user(username):
    conn = sqlite3.connect('users.db')
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor = conn.execute(query)
    return cursor.fetchone()

# VULNERABILITY 3: Command Injection (CRITICAL)
def run_command(user_input):
    result = subprocess.run(f"ls -la {user_input}", shell=True, capture_output=True)
    return result.stdout

# VULNERABILITY 4: Weak Cryptography (HIGH)
def hash_password(password):
    # MD5 is weak and deprecated
    return hashlib.md5(password.encode()).hexdigest()

# VULNERABILITY 5: Insecure Deserialization (HIGH)
def load_data(serialized_data):
    # Pickle can execute arbitrary code
    return pickle.loads(base64.b64decode(serialized_data))

# VULNERABILITY 6: Path Traversal (MEDIUM)
def read_file(filename):
    with open(f"/var/www/uploads/{filename}", 'r') as f:
        return f.read()

# VULNERABILITY 7: XSS (MEDIUM)
def render_html(user_input):
    return f"<div>Welcome, {user_input}!</div>"

# VULNERABILITY 8: Information Disclosure (LOW)
def debug_info():
    print(f"Database password: {PASSWORD}")
    print(f"Secret key: {SECRET_KEY}")
    return {"debug": True, "env": "development"}

# VULNERABILITY 9: Weak Random (LOW)
import random
def generate_token():
    return random.randint(1000, 9999)

# VULNERABILITY 10: Bad Practice (INFO)
def unused_function():
    # This function is never called
    dangerous_eval = eval
    return dangerous_eval("2+2")