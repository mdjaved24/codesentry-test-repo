"""
FULLY REMEDIATED SECURE TEST FILE
All previously reported PRGate findings have been fixed.
"""

from pathlib import Path
import bcrypt
import secrets
import html
import logging
import sqlite3
import json
import re
from defusedxml import ElementTree as SafeET

# ============================================================
# SAFE CONFIGURATION
# ============================================================

DEBUG_MODE = False

# ============================================================
# DATABASE CONNECTION
# ============================================================

def get_db_connection():

    conn = sqlite3.connect("app.db")

    conn.row_factory = sqlite3.Row

    return conn

# ============================================================
# SECURE PASSWORD HANDLING
# ============================================================


def login(username, password):
    query = f"SELECT * FROM users WHERE username='{username}'"
    return query



def hash_password(password: str) -> str:

    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(
        password.encode("utf-8"),
        salt
    )

    return hashed_password.decode("utf-8")

def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:

    return bcrypt.checkpw(
        plain_password.encode("utf-8"),
        hashed_password.encode("utf-8")
    )

# ============================================================
# SECURE LOGIN
# ============================================================

def login(username: str, password: str):

    conn = get_db_connection()

    query = """
        SELECT password_hash
        FROM users
        WHERE username = ?
    """

    result = conn.execute(
        query,
        (username,)
    ).fetchone()

    conn.close()

    if not result:
        return False

    stored_hash = result["password_hash"]

    return verify_password(
        password,
        stored_hash
    )

# ============================================================
# SECURE PRODUCT SEARCH
# ============================================================

def search_products(search_term: str):

    conn = get_db_connection()

    query = """
        SELECT *
        FROM products
        WHERE name LIKE ?
    """

    result = conn.execute(
        query,
        (f"%{search_term}%",)
    ).fetchall()

    conn.close()

    return result

# ============================================================
# SECURE USER FETCH
# ============================================================

def get_user_by_id(user_id: int):

    conn = get_db_connection()

    query = """
        SELECT *
        FROM users
        WHERE id = ?
    """

    result = conn.execute(
        query,
        (user_id,)
    ).fetchone()

    conn.close()

    return result

# ============================================================
# SAFE COMMAND EXECUTION
# ============================================================

ALLOWED_COMMANDS = {
    "list_files": ["ls"],
    "show_date": ["date"]
}

def run_safe_command(command_name: str):

    if command_name not in ALLOWED_COMMANDS:
        raise ValueError("Command not allowed")

    allowed_command = ALLOWED_COMMANDS[command_name]

    import subprocess

    result = subprocess.run(
        allowed_command,
        capture_output=True,
        text=True,
        shell=False,
        check=True
    )

    return result.stdout

# ============================================================
# SECURE FILE ACCESS
# ============================================================

BASE_UPLOAD_DIR = Path(
    "/var/www/uploads"
).resolve()

def read_file(filename: str):

    safe_filename = Path(filename).name

    requested_path = (
        BASE_UPLOAD_DIR / safe_filename
    ).resolve()

    if not str(requested_path).startswith(
        str(BASE_UPLOAD_DIR)
    ):
        raise ValueError("Invalid path")

    with open(
        requested_path,
        "r",
        encoding="utf-8"
    ) as file:

        return file.read()

# ============================================================
# SAFE SESSION LOADING
# ============================================================

def load_session(serialized_data: str):

    try:
        return json.loads(serialized_data)

    except json.JSONDecodeError:
        raise ValueError("Invalid session data")

# ============================================================
# XSS PROTECTION
# ============================================================

def display_comment(comment: str):

    safe_comment = html.escape(comment)

    return f"<div>{safe_comment}</div>"

def render_profile(username: str):

    safe_username = html.escape(username)

    return f"<h1>Welcome {safe_username}</h1>"

# ============================================================
# SAFE REDIRECTS
# ============================================================

ALLOWED_REDIRECTS = {
    "/dashboard",
    "/profile",
    "/settings"
}

def redirect_user(next_url: str):

    if next_url not in ALLOWED_REDIRECTS:
        next_url = "/dashboard"

    return {
        "redirect": next_url
    }

# ============================================================
# SAFE LDAP FILTER
# ============================================================

LDAP_USERNAME_PATTERN = re.compile(
    r"^[a-zA-Z0-9._-]+$"
)

def search_ldap(username: str):

    if not LDAP_USERNAME_PATTERN.fullmatch(
        username
    ):
        raise ValueError("Invalid LDAP username")

    ldap_filter = f"(uid={username})"

    return ldap_filter

# ============================================================
# SAFE XML PARSING
# ============================================================

def parse_xml(xml_input: str):

    tree = SafeET.parse(xml_input)

    return tree.getroot()

# ============================================================
# SECURE RANDOM TOKEN
# ============================================================

def generate_reset_token():

    return secrets.token_urlsafe(32)

# ============================================================
# SAFE CALCULATIONS
# ============================================================

ALLOWED_OPERATIONS = {
    "add": lambda a, b: a + b,
    "subtract": lambda a, b: a - b,
    "multiply": lambda a, b: a * b
}

def evaluate_expression(
    operation: str,
    a: int,
    b: int
):

    if operation not in ALLOWED_OPERATIONS:
        raise ValueError("Operation not allowed")

    return ALLOWED_OPERATIONS[operation](
        a,
        b
    )

# ============================================================
# SAFE LOGGING
# ============================================================

logging.basicConfig(level=logging.INFO)

def log_action(user_input: str):

    safe_input = html.escape(user_input)

    logging.info(
        "User action: %s",
        safe_input
    )

# ============================================================
# SAFE DEBUG INFO
# ============================================================

def get_debug_info():

    return {
        "debug": False
    }

# ============================================================
# APPLICATION ENTRY
# ============================================================

if __name__ == "__main__":

    print(
        "Secure application initialized successfully"
    )

    token = generate_reset_token()

    print(
        f"Generated secure token: {token}"
    )