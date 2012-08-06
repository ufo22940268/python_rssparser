import dbutils

if __name__ == '__main__':
    conn = dbutils.connect()
    c = conn.cursor() 
    ids = []
    for row in c.execute("select _id from data"):
        id = row[0]
        ids.append(id)

    date = 0
    for id in ids:
        c.execute("update data set date = ? where _id = ?", (date, id))
        date += 1

    conn.commit()
    conn.close()
