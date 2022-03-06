# import tornado.web     # tornadoku框架搭建一个http服务器的固定写法
from tornado import web
from tornado import httpserver
from tornado import ioloop

# application = tornado.web.Application
class IndexHandler(web.RedirectHandler):
    def get(self, *args, **kwargs):
        self.write('hello wold!')
application = web.Application([
            (r"/", IndexHandler),
        ])
if __name__ == '__main__':
    http_server = httpserver.HTTPServer(application)
    http_server.listen(8080)
    ioloop.IOLoop.current().start()