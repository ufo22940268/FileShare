#coding:utf-8
import tornado.web
import tornado.ioloop
from tornado.template import Template
from tornado.template import Loader
import logging
import util
import parser
import json
import re
import urllib
import traceback

FILES_DIRECTORY = "./files/";
SERVER_IP = "http://192.168.2.124";
URL_PREFIX = SERVER_IP + "/files/";
logger = logging.getLogger("test");
class MainHandler(tornado.web.RequestHandler):
    def get(self):
	loader = Loader("./");
	self.write(loader.load("index.html").generate());

class UploadHandler(tornado.web.RequestHandler):

    def post(self):
        util.log(self.get_argument("id", default="0"));
        file1 = self.request.files['file'][0];
        fileName = file1['filename']
        util.log(file1['filename']);
        outfile = open(FILES_DIRECTORY + fileName, "w");
        outfile.write(file1['body']);
        outfile.close();
        util.log("finish");
        self.write(URL_PREFIX + fileName);

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/upload", UploadHandler),
    (r"/css/(.*)", tornado.web.StaticFileHandler, {"path": "./css/"}),
    (r"/js/(.*)", tornado.web.StaticFileHandler, {"path": "./js/"}),
    (r"/img/(.*)", tornado.web.StaticFileHandler, {"path": "./img/"}),
    (r"/server/(.*)", tornado.web.StaticFileHandler, {"path": "./server/"}),
    ]);

if __name__ == "__main__":
    application.listen(8885)
    tornado.ioloop.IOLoop.instance().start()
