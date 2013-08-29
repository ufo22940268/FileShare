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
from setting import *
import file_manager

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

class FileListHandler(tornado.web.RequestHandler):
    def get(self):
        files = file_manager.getAllFiles();
        loader = Loader("./");
        self.write(loader.load("file_list.html").generate(files=files));

application = tornado.web.Application([
    (r"/file_share", MainHandler),
    (r"/file_list", FileListHandler),
    (r"/upload", UploadHandler),
    (r"/css/(.*)", tornado.web.StaticFileHandler, {"path": "./css/"}),
    (r"/js/(.*)", tornado.web.StaticFileHandler, {"path": "./js/"}),
    (r"/img/(.*)", tornado.web.StaticFileHandler, {"path": "./img/"}),
    (r"/server/(.*)", tornado.web.StaticFileHandler, {"path": "./server/"}),
    ], debug=True);

if __name__ == "__main__":
    application.listen(8889)
    tornado.ioloop.IOLoop.instance().start()
