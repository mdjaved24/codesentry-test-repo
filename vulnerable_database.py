"""
VULNERABLE DATABASE OPERATIONS - FOR TESTING ONLY
Database security vulnerabilities
"""

import sqlite3
import psycopg2
import mysql.connector
from pymongo import MongoClient

# ============ VULNERABILITY 1: Connection String Exposure (CRITICAL) ============
DB_USERNAME = "admin"
DB_PASSWORD = "SuperSecret123!"
DB_HOST = "prod-database.internal.com"
DB_NAME = "customer_data"

# Connection string with credentials exposed
POSTGRES_URI = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
MYSQL_URI = f"mysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
MONGO_URI = f"mongodb://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:27017/"

# ============ VULNERABILITY 2: NoSQL Injection (CRITICAL) ============
def search_users_nosql(username):
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    # Vulnerable to NoSQL injection
    query = {"$where": f"this.username == '{username}'"}
    return db.users.find(query)

# ============ VULNERABILITY 3: SQL Injection in ORDER BY (HIGH) ============
def get_users_sorted(order_by):
    conn = psycopg2.connect(POSTGRES_URI)
    cursor = conn.cursor()
    # ORDER BY injection vulnerability
    query = f"SELECT * FROM users ORDER BY {order_by}"
    cursor.execute(query)
    return cursor.fetchall()

# ============ VULNERABILITY 4: Second-Order SQL Injection (CRITICAL) ============
def create_user(username, email):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # First insert - safe
    cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", 
                   (username, email))
    conn.commit()
    
def get_user_profile(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # Second query - vulnerable (username comes from DB)
    cursor.execute(f"SELECT * FROM profiles WHERE username = '{username}'")
    return cursor.fetchone()

# ============ VULNERABILITY 5: Batch Query Injection (MEDIUM) ============
def batch_update(user_ids, status):
    conn = mysql.connector.connect(user=DB_USERNAME, password=DB_PASSWORD)
    cursor = conn.cursor()
    # Vulnerable batch update
    for user_id in user_ids:
        cursor.execute(f"UPDATE users SET status='{status}' WHERE id={user_id}")

# ============ VULNERABILITY 6: Stored Procedure Injection (HIGH) ============
def execute_stored_procedure(user_input):
    conn = psycopg2.connect(POSTGRES_URI)
    cursor = conn.cursor()
    # Vulnerable stored procedure call
    cursor.execute(f"CALL search_users('{user_input}')")
    return cursor.fetchall()

# ============ VULNERABILITY 7: Database Error Disclosure (LOW) ============
def get_user_by_id(user_id):
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
        return cursor.fetchone()
    except Exception as e:
        # Exposes database structure in error messages
        return {"error": str(e)}