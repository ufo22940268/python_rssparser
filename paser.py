from xml.parsers import expat

xmlparser = expat.ParserCreate()
file = open("rss.xml", "r")
item = xmlparser.ParseFile(file)
while item != "":
    print item
    item = xmlparser.ParseFile(file)
