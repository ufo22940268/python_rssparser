from xml.dom.minidom import parse
from xml.dom import Node
from download import downloader
import converttime
import dbutils
import testutils
import hashlib

def gen_dom():
    url = "http://cn.engadget.com/rss.xml"
    dom = parse(downloader(url).download())
    return dom

def get_item_data(t):
    #TODO Althougth is can prevent the convert error happens, but
    #it will ignore the special characters, so content may be not 
    #completed.
    return t.childNodes[0].data.encode("ascii", "ignore")

def insert_to_db(list):
    conn = dbutils.connect()
    c = conn.cursor()
    for t in list:
        c.execute("insert into data(title, date, hash_guid) values('%(title)s', %(date)d, '%(guid)s')" % \
                {"title": t.title, "date": t.date, "guid": t.guid});
    conn.commit()
    c.close()

def hash(s):
    m = hashlib.md5()
    m.update(s)
    return m.hexdigest()
    
def main():
    dom = gen_dom()
    list = []
    for item in dom.getElementsByTagName("item"):
        if not contains_in_db(parse_guid(item)):
            b = bean()
            for t in item.childNodes:
                item_data = get_item_data(t)
                if t.nodeName == "pubDate":
                    b.date = converttime.convert(item_data)
                elif t.nodeName == "title":
                    b.title = item_data
                elif t.nodeName == "guid":
                    b.guid = hash(item_data)
            list.append(b)
    insert_to_db(list);

    #test
    testutils.print_data()

def parse_guid(item):
    return hash(get_item_data(item.getElementsByTagName("guid")[0]))
    

def contains_in_db(guid):
    conn = dbutils.connect()
    c = conn.cursor()
    c.execute("select * from data where hash_guid = '%s'" % guid);
    if c.fetchall() == []:
        return False
    else:
        return True

class bean:
    date = 0
    title = ""    
    guid = ""


if __name__ == '__main__':
    #test
    testutils.clear_data();

    main()
