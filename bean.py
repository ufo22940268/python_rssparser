class bean:
    date = 0
    title = ""    
    guid = ""
    content = ""
    link = ""
    
    def __str__(self):
        return "data:" + str(self.date) + "\ttitle:" + self.title + "\tguid:" + self.guid\
                + "\tcontent:" + content + "\tlink:" + link +  "\n"
