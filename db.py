import sqlite3
def create():
    conn = sqlite3.connect("rss.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE data
                (_id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, date INTEGER)''');
    conn.commit()
    c.close()

if __name__ == '__main__':
    create()
