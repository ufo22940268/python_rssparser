from bean import bean
import dbutils

def query(date):
    conn = dbutils.connect()
    c = conn.cursor()
    c.execute("select * from data where date >= ?", (date,))
    return c

def load_single_bean(row):
    b = bean()
    b.title = row[1]
    return b

def load_beans(date):
    beans = []
    c = query(date)
    row = c.fetchone()
    while row != None:
        beans.append(load_single_bean(row))
        row = c.fetchone()
    return "".join(map(str, beans))

if __name__ == '__main__':
    print load_beans(0)
