from xml.dom.minidom import parse
from xml.dom import Node
from download import downloader
import converttime
import dbutils
import testutils
import hashlib
from bean import bean

def read_urls():
    file = open("config", "r")
    urls = []
    line = file.readline().rstrip()
    while line != "":
        urls.append(line)
        line = file.readline().rstrip()
    return urls

def gen_dom(url):
    return parse(downloader(url).download())


def get_item_data(t):
    #TODO Althougth is can prevent the convert error happens, but
    #it will ignore the special characters, so content may be not 
    #completed.
    data = t.childNodes[0].data.encode("ascii", "ignore")
    return escape(data)

def escape(s):
    return s.replace("'", "''")

def insert_to_db(list):
    print [x.guid for x in list]
    conn = dbutils.connect()
    c = conn.cursor()
    for t in list:
        c.execute("insert into data(title, date, hash_guid) values(?, ?, ?)", (t.title, t.date, t.guid));
    conn.commit()
    c.close()

def hash(s):
    m = hashlib.md5()
    m.update(s)
    return m.hexdigest()
    
def main():
    urls = read_urls()
    for url in urls:
        dom = gen_dom(url)
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


if __name__ == '__main__':
    #test
    testutils.clear_data();
    while True:
        main()
