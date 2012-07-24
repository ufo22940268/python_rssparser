from xml.dom.minidom import parse
from xml.dom import Node
from download import downloader

url = "http://cn.engadget.com/rss.xml"
dom = parse(downloader(url).download())
#dom = parse("rss.xml")
titles = []
body = []
for item in dom.getElementsByTagName("item"):
    for t in item.childNodes:
        if t.nodeName == "title":
            
            #print t.childNodes[0].data
            #TODO Althougth is can prevent the convert error happens, but
            #it will ignore the special characters, so content may be not 
            #completed.
            print t.childNodes[0].data.encode("ascii", "ignore")
