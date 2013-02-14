#!/usr/bin/python

import os
import tornado.ioloop
import tornado.web

from handlers import *

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
        (r"/carousel", CarouselHandler),
        (r"/market-narrow", MarketNarrowHandler),
        (r"/static-grid", StaticGridHandler),
        (r"/ajax-grid", AjaxGridHandler),
    ], **settings)

    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
