class bean:
    date = 0
    title = ""    
    guid = ""
    
    def __str__(self):
        return "data:" + str(self.date) + "\ttitle:" + self.title + "\tguid:" + self.guid + "\n"
