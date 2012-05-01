# coding=utf-8

from __future__ import unicode_literals
import tornado.web

class index(tornado.web.RequestHandler):
    def get(self):
        self.render('main.html');

