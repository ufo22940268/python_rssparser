#!/usr/bin/python
import sys
import tornado.ioloop
import tornado.web
import tornado.options
import logging

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("home")

class DateHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.get_argument("date"))

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/query", DateHandler)
])

if __name__ == "__main__":
    tornado.options.parse_command_line()
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
