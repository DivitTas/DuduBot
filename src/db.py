import sqlite3
from datetime import datetime

DB_name= "finances.db"
 def connect():
    return sqlite3.connect(DB_name)

def init_db():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS FINANCES"(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT NOT NULL,
        amount REAL NOT NULL,
        category TEXT,
        notes TEXT,
        timestamp TEXT NOT NULL

    )""")
    conn.commit()
    conn.close()

def add_expense(user_id,amount,category,notes):
    con = connect()
    cur = con.cursor()
    cur.execute("""
                INTERT INTO FINANCES (user_id,amount,category,notes,timestamp)
                VALUES (?,?,?,?,?)
                """, (str(user_id),amount,category,notes,datetime.now()))
    con.commit()
    con.close()

def get_expense(user_id,limit: int =10):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT amount, category, timestamp
        FROM expenses
        WHERE user_id = ? AND guild_id = ?
        ORDER BY timestamp DESC
        LIMIT ?
    """, (str(user_id), str(guild_id), limit))
    rows = cur.fetchall()
    conn.close()
    return rows



