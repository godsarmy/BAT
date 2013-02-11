#!/usr/bin/python

import os
import tornado.ioloop
import tornado.web
from tornado.escape import json_encode

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.tpl",
                    project_name=self.settings["globals"]["project_name"])

class AjaxHandler(tornado.web.RequestHandler):
    def get(self):
        type = self.get_argument('type')

        data ={}
        if type == "hero":
            data = {
                 "detail" : "This is detail inform generated via Ajax call by AngularJS."
               }
        elif type == "index":
            data = [
                { "url" : "/",             "name" : "Index" },
                { "url" : "hero",          "name" : "Hero" },
                { "url" : "fluid",         "name" : "Fluid" },
                { "url" : "signin",        "name" : "Sign In" },
                { "url" : "sticky-footer", "name" : "Sticky-Footer" },
                { "url" : "sfn",           "name" : "Sticky-Footer Navbar" },
                { "url" : "justified-nav", "name" : "Justified Navbar" },
            ]
        self.write(json_encode(data))

class SigninHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("signin.tpl",
                    project_name=self.settings["globals"]["project_name"])

class HeroHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("hero.tpl",
                    project_name=self.settings["globals"]["project_name"])

class SFNHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("sfn.tpl",
                    project_name=self.settings["globals"]["project_name"])

class StickyFooterHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("sticky-footer.tpl",
                    project_name=self.settings["globals"]["project_name"])

class JustifiedNavHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("justified-nav.tpl",
                    project_name=self.settings["globals"]["project_name"])

class FluidHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("fluid.tpl",
                    project_name=self.settings["globals"]["project_name"],
                    username="Unknown"
                   )

    def post(self):
        #self.set_header("Content-Type", "text/plain")
        self.render("fluid.tpl",
                    project_name=self.settings["globals"]["project_name"],
                    username=self.get_argument("address")
                   )

if __name__ == "__main__":
    settings = {
        "static_path": os.path.join(os.path.dirname(__file__), "static"),
        "template_path": os.path.join(os.path.dirname(__file__), "template"),
        "globals": { 
                       "project_name":"BAT -- Bootstrap, AngularJS, Tornado"
                   },
    }

    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/ajax", AjaxHandler),
        (r"/signin", SigninHandler),
        (r"/fluid", FluidHandler),
        (r"/hero", HeroHandler),
        (r"/sfn", SFNHandler),
        (r"/sticky-footer", StickyFooterHandler),
        (r"/justified-nav", JustifiedNavHandler),
    ], **settings)

    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
