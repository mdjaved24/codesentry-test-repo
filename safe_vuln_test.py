"""
SAFE VULNERABLE TEST FILE
All values are explicitly fake to avoid GitHub secret scanning
"""

# Use these patterns - these won't trigger GitHub's scanner
API_KEY = "FAKE_API_KEY_12345_TEST_ONLY"
STRIPE_KEY = "FAKE_STRIPE_TEST_KEY_98765"
AWS_SECRET = "FAKE_AWS_SECRET_FOR_TESTING"
DB_PASSWORD = "TEST_DB_PASS_123_FAKE"

# Vulnerable SQL Injection
def login(username, password):
    query = f"SELECT * FROM users WHERE name='{username}' AND pass='{password}'"
    return query

# Vulnerable Command Injection  
def run_cmd(cmd):
    import os
    os.system(f"echo {cmd}")