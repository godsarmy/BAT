"""
Handlers
"""

import tornado.web
from tornado.escape import json_encode

# files to store handlers
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.tpl",
                    project_name=self.settings["globals"]["project_name"])

class AjaxHandler(tornado.web.RequestHandler):
    data = {
        "index":[
                  { "url" : "/",             "name" : "Index" },
                  { "url" : "hero",          "name" : "Hero" },
                  { "url" : "fluid",         "name" : "Fluid" },
                  { "url" : "signin",        "name" : "Sign In" },
                  { "url" : "sticky-footer", "name" : "Sticky-Footer" },
                  { "url" : "sfn",           "name" : "Sticky-Footer Navbar" },
                  { "url" : "justified-nav", "name" : "Justified Navbar" },
                  { "url" : "carousel",      "name" : "Carousel" },
                  { "url" : "market-narrow", "name" : "Market Narrow" },
                  { "url" : "static-grid",   "name" : "Static Grid" },
                  { "url" : "ajax-grid",     "name" : "Ajax Grid" },
                  { "url" : "angular-ui",    "name" : "Angular UI" },
        ],
        "grid": {
            "head": [
                  {"key":"name", "desc":"Name"},
                  {"key":"creator", "desc":"Creator"},
                  {"key":"engine", "desc":"Engine"},
                  {"key":"license", "desc":"Software License"},
            ],
            "body": [
                  {"name":"Chrome",  "creator":"Google", "engine":"Webkit", "license":"BSD"},
                  {"name":"Firefox", "creator":"Mozilla", "engine":"Gecko", "license":"MPL/GPL/LGPL"},
                  {"name":"Internet Explorer", "creator":"Microsoft", "engine":"Trident", "license":"Proprietary"},
            ]
        }
    }

    def get(self):
        call_type = self.get_argument('type')
        content = self.get_argument('content', [])

        data = {}
        if (content == 'detail'):
            data = { 
                 "detail" : ("This is %s detail inform generated via Ajax call by AngularJS." % call_type )
                 }
        else:
            data = self.data[call_type] 
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

class CarouselHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("carousel.tpl",
                    project_name=self.settings["globals"]["project_name"])

class MarketNarrowHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("market-narrow.tpl",
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


#static grid handler
class StaticGridHandler(tornado.web.RequestHandler):
    data = [
        {"name":"Chrome",  "creator":"Google", "engine":"Webkit", "license":"BSD"},
        {"name":"Firefox", "creator":"Mozilla", "engine":"Gecko", "license":"MPL/GPL/LGPL"},
        {"name":"Internet Explorer", "creator":"Microsoft", "engine":"Trident", "license":"Proprietary"},
    ]

    def get(self):
        self.render("grid.tpl",
                    project_name=self.settings["globals"]["project_name"],
                    data=self.data,
                   )

#ajax grid handler
class AjaxGridHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("ajax-grid.tpl",
                    project_name=self.settings["globals"]["project_name"],
                   )

#angular UI handler
class AngularUIHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("angularUI.tpl",
                    project_name=self.settings["globals"]["project_name"],
                   )

