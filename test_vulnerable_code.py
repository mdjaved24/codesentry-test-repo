"""
PRGate Safe Vulnerability Testing File
This file contains intentionally vulnerable patterns for testing PRGate.
All secrets are FAKE placeholders and safe for GitHub push.
DO NOT USE IN PRODUCTION.
"""

# ============================================================
# SAFE TEST PLACEHOLDERS
# ============================================================

FAKE_API_KEY = "dummy_test_key"
FAKE_STRIPE_KEY = "fake_stripe_testing_key"
FAKE_AWS_SECRET = "not_a_real_aws_secret"
DUMMY_DB_PASSWORD = "dummy_password"
TEST_JWT_SECRET = "fake_jwt_secret"
ADMIN_PASSWORD = "dummy_admin_password"

# ============================================================
# SQL INJECTION TESTS
# ============================================================

def login(username, password):
    query = f"SELECT * FROM users WHERE name='{username}' AND pass='{password}'"
    return query

def search_products(search_term):
    query = f"SELECT * FROM products WHERE name LIKE '%{search_term}%'"
    return query

def get_user_by_id(user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return query

# ============================================================
# COMMAND INJECTION TESTS
# ============================================================

def run_command(cmd):
    import os
    os.system(f"echo {cmd}")

def delete_file(filename):
    import subprocess
    subprocess.call(f"rm -rf {filename}", shell=True)

# ============================================================
# PATH TRAVERSAL TESTS
# ============================================================

def read_file(filename):
    with open(f"/var/www/uploads/{filename}", "r") as f:
        return f.read()

# ============================================================
# WEAK CRYPTOGRAPHY TESTS
# ============================================================

import hashlib

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def hash_api_key(key):
    return hashlib.sha1(key.encode()).hexdigest()

# ============================================================
# INSECURE DESERIALIZATION
# ============================================================

import pickle
import base64

def load_session(serialized_data):
    decoded = base64.b64decode(serialized_data)
    return pickle.loads(decoded)

# ============================================================
# XSS TESTS
# ============================================================

def display_comment(comment):
    return f"<div>{comment}</div>"

def render_profile(username):
    return f"<h1>Welcome {username}</h1>"

# ============================================================
# OPEN REDIRECT TEST
# ============================================================

def redirect_user():
    next_url = "https://malicious-example.com"
    return f'<meta http-equiv="refresh" content="0;url={next_url}">'

# ============================================================
# LDAP INJECTION
# ============================================================

def search_ldap(username):
    ldap_filter = f"(uid={username})"
    return ldap_filter

# ============================================================
# XXE TEST
# ============================================================

import xml.etree.ElementTree as ET

def parse_xml(xml_input):
    tree = ET.parse(xml_input)
    return tree.getroot()

# ============================================================
# INSECURE RANDOMNESS
# ============================================================

import random

def generate_reset_token():
    return random.randint(100000, 999999)

# ============================================================
# EVAL INJECTION
# ============================================================

def evaluate_expression(expression):
    return eval(expression)

# ============================================================
# HARDCODED COMMENT TEST
# ============================================================

# TODO: Remove dummy credentials before production deployment
# Username: testuser
# Password: dummy_password

# ============================================================
# DEBUG MODE TEST
# ============================================================

DEBUG_MODE = True

def get_debug_info():
    return {
        "debug": DEBUG_MODE,
        "environment": "development"
    }

# ============================================================
# TEST EXECUTION
# ============================================================

if __name__ == "__main__":

    print("Running vulnerable test file...")

    print(login("admin", "password"))

    print(search_products("laptop"))

    print(hash_password("mypassword"))

    print(render_profile("<script>alert('xss')</script>"))

    print(generate_reset_token())