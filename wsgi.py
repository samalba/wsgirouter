
from webob import Request, Response, exc
import router


class Hello(router.Root):

    def get(self, req):
        name = req.path_info.split('/').pop()
        return Response('Hello ' + name)


class Yo(router.Root):

    def get(self, req):
        name = req.path_info.split('/').pop()
        return Response('Yo ' + name)


if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    urls = router.Router()
    urls['*'] = (
            '/.*', Hello()
            )
    urls['toto.com'] = (
            '/.*', Yo()
            )
    print 'http://localhost:4242/'
    make_server('localhost', 4242, urls).serve_forever()
