#!/usr/bin/python

from os import path

from tornado import web, ioloop, gen

from handlers import *


def load_app(port, root):
    settings = {
        "static_path": path.join(root, "static"),
        "template_path": path.join(root, "template"),
        "globals": {
            "project_name": "BAT -- Bootstrap, AngularJS, Tornado"
        },
        "flash_policy_port": 843,
        "flash_policy_file": path.join(root, 'flashpolicy.xml'),
        "socket_io_port": port,
    }

    routers = [
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
        (r"/angular-ui", AngularUIHandler),
        (r"/gen", SocketIOGenHandler)
    ]

    try:
        from tornadio2 import TornadioRouter, SocketServer
        from connections import QueryConnection
        # Create tornadio router
        QueryRouter = TornadioRouter(QueryConnection)
        # Create socket application
        application = web.Application(
            QueryRouter.apply_routes(routers),
            **settings
        )
        #application.listen(8888)
        SocketServer(application)
    except ImportError:
        print "Failed to load module tornadio2"
        application = web.Application(
            routers,
            **settings
        )
        application.listen(port)
        tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":

    root = path.dirname(__file__)
    port = 8888

    load_app(port, root)
