"""
SECURE VERSION - PRGate Fixed Vulnerability Test File
All previously reported vulnerabilities have been remediated.
"""

from pathlib import Path
import bcrypt
import secrets
import html
import logging
import subprocess
import sqlite3
import json
from defusedxml import ElementTree as SafeET

# ============================================================
# SAFE CONFIGURATION
# ============================================================

DEBUG_MODE = False

# ============================================================
# SECURE DATABASE ACCESS
# ============================================================

def get_db_connection():
    conn = sqlite3.connect("app.db")
    conn.row_factory = sqlite3.Row
    return conn

def login(username, password):

    conn = get_db_connection()

    query = "SELECT * FROM users WHERE name=? AND pass=?"

    result = conn.execute(
        query,
        (username, password)
    ).fetchone()

    conn.close()

    return result

def search_products(search_term):

    conn = get_db_connection()

    query = "SELECT * FROM products WHERE name LIKE ?"

    result = conn.execute(
        query,
        (f"%{search_term}%",)
    ).fetchall()

    conn.close()

    return result

def get_user_by_id(user_id):

    conn = get_db_connection()

    query = "SELECT * FROM users WHERE id=?"

    result = conn.execute(
        query,
        (user_id,)
    ).fetchone()

    conn.close()

    return result

# ============================================================
# SECURE COMMAND EXECUTION
# ============================================================

ALLOWED_COMMANDS = {
    "ping": ["ping", "-c", "4"],
    "ls": ["ls"]
}

def run_safe_command(command_name):

    if command_name not in ALLOWED_COMMANDS:
        raise ValueError("Command not allowed")

    result = subprocess.run(
        ALLOWED_COMMANDS[command_name],
        capture_output=True,
        text=True,
        check=True
    )

    return result.stdout

# ============================================================
# SECURE FILE ACCESS
# ============================================================

BASE_UPLOAD_DIR = Path("/var/www/uploads").resolve()

def read_file(filename):

    requested_path = (BASE_UPLOAD_DIR / filename).resolve()

    if not str(requested_path).startswith(str(BASE_UPLOAD_DIR)):
        raise ValueError("Invalid file path")

    with open(requested_path, "r", encoding="utf-8") as file:
        return file.read()

# ============================================================
# STRONG PASSWORD HASHING
# ============================================================

def hash_password(password):

    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(
        password.encode(),
        salt
    )

    return hashed_password.decode()

def verify_password(password, hashed_password):

    return bcrypt.checkpw(
        password.encode(),
        hashed_password.encode()
    )

# ============================================================
# SAFE SESSION HANDLING
# ============================================================

def load_session(serialized_data):

    try:
        return json.loads(serialized_data)

    except json.JSONDecodeError:
        raise ValueError("Invalid session data")

# ============================================================
# XSS PROTECTION
# ============================================================

def display_comment(comment):

    safe_comment = html.escape(comment)

    return f"<div>{safe_comment}</div>"

def render_profile(username):

    safe_username = html.escape(username)

    return f"<h1>Welcome {safe_username}</h1>"

# ============================================================
# SAFE REDIRECT
# ============================================================

ALLOWED_REDIRECTS = {
    "/dashboard",
    "/profile",
    "/settings"
}

def redirect_user(next_url):

    if next_url not in ALLOWED_REDIRECTS:
        next_url = "/dashboard"

    return {
        "redirect": next_url
    }

# ============================================================
# SAFE LDAP FILTERING
# ============================================================

def search_ldap(username):

    safe_username = username.replace(
        "(",
        ""
    ).replace(
        ")",
        ""
    )

    ldap_filter = f"(uid={safe_username})"

    return ldap_filter

# ============================================================
# SAFE XML PARSING
# ============================================================

def parse_xml(xml_input):

    tree = SafeET.parse(xml_input)

    return tree.getroot()

# ============================================================
# SECURE RANDOM TOKEN GENERATION
# ============================================================

def generate_reset_token():

    return secrets.token_urlsafe(32)

# ============================================================
# REMOVE EVAL USAGE
# ============================================================

ALLOWED_OPERATIONS = {
    "add": lambda a, b: a + b,
    "subtract": lambda a, b: a - b
}

def evaluate_expression(operation, a, b):

    if operation not in ALLOWED_OPERATIONS:
        raise ValueError("Operation not allowed")

    return ALLOWED_OPERATIONS[operation](a, b)

# ============================================================
# SAFE LOGGING
# ============================================================

logging.basicConfig(level=logging.INFO)

def log_action(user_input):

    safe_input = html.escape(user_input)

    logging.info("User action: %s", safe_input)

# ============================================================
# SAFE DEBUG HANDLING
# ============================================================

def get_debug_info():

    if DEBUG_MODE:
        return {"debug": True}

    return {"debug": False}

# ============================================================
# MAIN EXECUTION
# ============================================================

if __name__ == "__main__":

    print("Secure application loaded successfully")

    token = generate_reset_token()

    print(f"Generated secure token: {token}")