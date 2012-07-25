import dbutils

def print_data():
    conn = dbutils.connect()
    c = conn.cursor()
    c.execute("select * from data")
    conn.commit()
    data = c.fetchone()
    while data != None:
        print data
        data = c.fetchone()
    c.close()

def clear_data():
    conn = dbutils.connect()
    c = conn.cursor()
    c.execute("delete from data")
    conn.commit()

if __name__ == '__main__':
    print_data()
