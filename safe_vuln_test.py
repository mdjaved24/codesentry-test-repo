"""
VULNERABLE TEST FILE FOR PRGATE - DO NOT USE IN PRODUCTION
Contains multiple security vulnerabilities for testing purposes only
"""

# ============================================================
# CRITICAL SEVERITY VULNERABILITIES
# ============================================================

# Hardcoded Secrets (CWE-798)
API_KEY = "TEST_API_KEY_12345_TEST_ONLY"
STRIPE_KEY = "TEST_STRIPE_TEST_KEY_98765"
AWS_SECRET = "TEST_AWS_SECRET_FOR_TESTING"
DB_PASSWORD = "TEST_DB_PASS_123_FAKE"
JWT_SECRET = "TEST_JWT_SECRET_2024"
ADMIN_PASSWORD = "TEST_ADMIN_123"

# SQL Injection (CWE-89)
def login(username, password):
    query = f"SELECT * FROM users WHERE name='{username}' AND pass='{password}'"
    return query

def search_products(search_term):
    query = f"SELECT * FROM products WHERE name LIKE '%{search_term}%'"
    return query

def get_user_by_id(user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return query

# Command Injection (CWE-78)
def run_command(cmd):
    import os
    os.system(f"echo {cmd}")

def delete_file(filename):
    import subprocess
    subprocess.call(f"rm -rf {filename}", shell=True)

def ping_host(host):
    import subprocess
    result = subprocess.run(f"ping -c 4 {host}", shell=True, capture_output=True)
    return result.stdout

# ============================================================
# HIGH SEVERITY VULNERABILITIES
# ============================================================

# Path Traversal (CWE-22)
def read_file(filename):
    with open(f"/var/www/uploads/{filename}", 'r') as f:
        return f.read()

def load_config(config_name):
    with open(f"./config/{config_name}", 'r') as f:
        return f.read()

# Weak Cryptography (CWE-327)
import hashlib
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def hash_api_key(key):
    return hashlib.sha1(key.encode()).hexdigest()

# Insecure Deserialization (CWE-502)
import pickle
import base64
def load_session(serialized_data):
    decoded = base64.b64decode(serialized_data)
    return pickle.loads(decoded)

# ============================================================
# MEDIUM SEVERITY VULNERABILITIES
# ============================================================

# XSS - Cross-Site Scripting (CWE-79)
def display_comment(comment):
    return f"<div class='comment'>{comment}</div>"

def render_profile(username):
    return f"<h1>Welcome, {username}!</h1>"

# Path Traversal in File Upload
def save_uploaded_file(filename, content):
    with open(f"/tmp/uploads/{filename}", 'w') as f:
        f.write(content)

# No Rate Limiting
login_attempts = {}
def process_login(username, password):
    if username == "admin" and password == ADMIN_PASSWORD:
        return "Login successful"
    login_attempts[username] = login_attempts.get(username, 0) + 1
    return "Invalid credentials"

# ============================================================
# LOW SEVERITY VULNERABILITIES
# ============================================================

# Information Disclosure
def get_debug_info():
    import os
    import socket
    return {
        "debug": True,
        "environment": "development",
        "hostname": socket.gethostname(),
        "current_dir": os.getcwd(),
        "python_path": os.environ.get("PYTHONPATH", "")
    }

# Predictable Random Numbers (CWE-330)
import random
def generate_reset_token():
    return random.randint(100000, 999999)

def generate_session_id():
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=10))

# ============================================================
# ADDITIONAL TEST VULNERABILITIES
# ============================================================

# XXE - XML External Entity (CWE-611)
import xml.etree.ElementTree as ET
def parse_xml(xml_string):
    tree = ET.parse(xml_string)
    return tree.getroot()

# LDAP Injection (CWE-90)
def search_ldap(username):
    ldap_filter = f"(uid={username})"
    return ldap_filter

# Log Injection (CWE-117)
def log_action(user_input):
    import logging
    logging.info(f"User action: {user_input}")

# Open Redirect (CWE-601)
def redirect_url():
    next_url = "https://evil-site.com"
    return f'<meta http-equiv="refresh" content="0;url={next_url}">'

# Missing CSRF Token
def transfer_money(amount, to_account):
    return {"status": "transferred", "amount": amount, "to": to_account}

# Insecure CORS Configuration
def add_cors_headers(response):
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Credentials'] = 'true'
    return response

# Debug Mode Enabled
DEBUG_MODE = True
def get_debug_endpoint():
    if DEBUG_MODE:
        return {"debug": True, "config": "exposed"}

# ============================================================
# DATABASE VULNERABILITIES
# ============================================================

# SQL Injection in ORDER BY
def get_users_sorted(order_by):
    query = f"SELECT * FROM users ORDER BY {order_by}"
    return query

# Second-Order SQL Injection
def create_user(username, email):
    # First insert - safe
    insert_query = f"INSERT INTO users (username, email) VALUES ('{username}', '{email}')"
    return insert_query

def get_user_profile(username):
    # Second query - vulnerable (username comes from DB)
    query = f"SELECT * FROM profiles WHERE username = '{username}'"
    return query

# ============================================================
# CODE QUALITY ISSUES
# ============================================================

# Unused dangerous function
def eval_expression(expression):
    return eval(expression)

# Hardcoded credentials in comment
# TODO: Remove test credentials - testuser / testpass123

# Exposed internal API
def get_internal_api():
    return {
        "internal_endpoint": "http://internal-api.company.com/v1",
        "api_key": "TEST_INTERNAL_API_KEY",
        "secret": "TEST_INTERNAL_SECRET"
    }

# Weak encryption
def simple_encrypt(data):
    key = "weak_key"
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(data))

# No input validation
def process_user_input(user_input):
    # Directly using user input without validation
    result = eval(user_input)
    return result

# Test function with multiple issues
def test_function():
    # Hardcoded credential
    api_secret = "TEST_SECRET_123"
    
    # SQL Injection
    user_id = "1 OR 1=1"
    query = f"DELETE FROM users WHERE id = {user_id}"
    
    # Command Injection
    import os
    filename = "test; rm -rf /"
    os.system(f"cat {filename}")
    
    return query

# ============================================================
# MAIN EXECUTION (for testing)
# ============================================================

if __name__ == "__main__":
    print("Vulnerable test file loaded")
    print(f"API_KEY: {API_KEY}")
    print(f"Login query: {login('admin', 'password')}")
    print(f"Command: {run_command('test')}")
    print(f"Hash: {hash_password('password')}")