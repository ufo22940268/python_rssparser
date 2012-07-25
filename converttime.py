from datetime import datetime
def convert(t):
    t = "Sat, 21 Jul 2012 00:30:00 EST"
    date = datetime.strptime(t, "%a, %d %b %Y %H:%M:%S EST")
    return date
