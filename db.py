import sqlite3
def create():
    conn = sqlite3.connect("rss.db")
    c = conn.cursor()
    c.execute('drop table data')
    c.execute('''CREATE TABLE data
                (_id INTEGER PRIMARY KEY AUTOINCREMENT, hash_guid INTEGER, title TEXT, date INTEGER)''');
    conn.commit()
    c.close()

if __name__ == '__main__':
    create()
