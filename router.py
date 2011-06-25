
import os
import re
from webob import Request, Response, exc


def pair(iterable):
    """ Iter through an iterable container by unpacking by pair """
    it = iter(iterable)
    while True:
        try:
            yield it.next(), it.next()
        except StopIteration:
            break


class Root(object):

    def __call__(self, environ, start_response):
        meth = environ.get('REQUEST_METHOD', 'GET').lower()
        if hasattr(self, meth):
            call = getattr(self, meth)
            if callable(call):
                resp = call(environ)
                return resp(environ, start_response)
        resp = exc.HTTPMethodNotAllowed()
        return resp(environ, start_response)


class Router(object):

    def __init__(self):
        self._routes = {'default': []}
        self._compile = lambda value: [(re.compile(i), j) for i, j in pair(value)]

    def __setitem__(self, key, value):
        if key == '*':
            key = 'default'
        self._routes[key] = self._compile(value)

    def __getitem__(self, key):
        return self._routes[key]

    def append(self, value, vhost='default'):
        self._routes[vhost].append(self._compile(value))

    def _get_routes(self, environ):
        host_header = environ.get('HTTP_HOST', 'default').split(':')[0]
        if not host_header in self._routes:
            return self._routes['default']
        return self._routes[host_header]

    def __call__(self, environ, start_response):
        path_info = environ.get('PATH_INFO', '/')
        for route in self._get_routes(environ):
            (m, obj) = route
            exp = m.match(path_info)
            if exp:
                return obj(environ, start_response)
        resp = exc.HTTPNotFound()
        return resp(environ, start_response)
