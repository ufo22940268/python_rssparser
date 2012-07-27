import sqlite3

def connect():
    conn = sqlite3.connect("rss.db")
    conn.row_factory = sqlite3.Row
    return conn
