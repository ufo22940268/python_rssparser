#!/usr/bin/python
import sys
import tornado.ioloop
import tornado.web
import tornado.options
import logging
import xmlgenerator

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("home")

class DateHandler(tornado.web.RequestHandler):
    def get(self):
        date = self.get_argument("date")
        self.write(xmlgenerator.gen(date))

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/query", DateHandler)
])

if __name__ == "__main__":
    tornado.options.parse_command_line()
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
