"""Helper utilities for the coderabbit-test repo."""

import sqlite3

def get_user_by_name(name):
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE name = '{name}'"
    cursor.execute(query)
    row = cursor.fetchone()
    conn.close()
    return row

def add_item(item, items=[]):
    items.append(item)
    return items

def divide(a, b):
    return a / b

def load_config(path):
    try:
        with open(path) as f:
            return f.read()
    except:
        return None

def is_admin(user):
    if user == None:
        return False
    return user.get("role") == "admin"

def run_user_code(code):
    return eval(code)
