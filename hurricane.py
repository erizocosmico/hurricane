#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Hurricane
----------------

Hurricane is an attempt to make Tornado more friendly for API developers. You can still use all the functionality that Tornado provides, Hurricane will just act as a wrapper
to make Tornado more friendly.

With tornado you would have to define a class and its methods but Hurricane provides Flask-like functionality to do the same with a function and a decorator.
In that decorator you specify the route and the method allowed for the request.

Then all you have to do is run the app at the specified port.

>>> from hurricane import Hurricane
>>> api = Hurricane()
>>> @api.route(r\"/say/hello\", 'GET')
>>> def say_hello(handler): handler.write('Hello!')
>>> api.run(8888)
"""

from __future__ import print_function
import tornado.ioloop
import tornado.web
import sys

__version__ = '1.0.0'
__all__ = 'Hurricane'

class HurricaneRequest(tornado.web.RequestHandler):
    def initialize(self, **kwargs):
        self.__fn = kwargs['func']
        
    def get(self):
        self.__fn(self)
        
    def post(self):
        self.__fn(self)
        
    def put(self):
        self.__fn(self)
        
    def delete(self):
        self.__fn(self)
        
    def head(self):
        self.__fn(self)
        
    def options(self):
        self.__fn(self)

class Hurricane(object):
    def __init__(self):
        self.app = None
        self.__routes = []
        
    def route(self, path, method = 'GET'):
        def wrapped(fn):
            if not method in ('GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'OPTIONS'):
                print('Invalid method supplied for route: %s' % str(route))
                sys.exit(2)
            self.__routes.append((path, HurricaneRequest, dict(func=fn)))
        return wrapped
    
    def run(self, port=8888, default_host="", transforms=None, wsgi=False, **settings):
        self.app = tornado.web.Application(self.__routes, default_host, transforms, wsgi, **settings)
        if isinstance(port, int):
            self.app.listen(port)
            tornado.ioloop.IOLoop.instance().start()
        else:
            print('Given port is not an integer.')
            sys.exit(2)