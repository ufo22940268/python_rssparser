from bean import bean
import dbutils
from xml.etree import ElementTree as ET
import sys
from xml.dom import minidom

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
    return beans

def gen_xml(beans):
    root = ET.Element("data")
    for b in beans:
        item = ET.Element("item")
        title = ET.Element("title")
        title.text = b.title
        item.append(title)
        root.append(item)

    return root

def pretty_string(str):
    return minidom.parseString(str).toprettyxml()

def gen(date):
    beans = load_beans(date)
    root = gen_xml(beans)
    return pretty_string(ET.tostring(root))

if __name__ == '__main__':
    print gen(0)
