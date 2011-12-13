from views import app
import tornado.wsgi
import tornado.httpserver
import tornado.ioloop
import argparse


def parse_arguments():
    """Parse any additional arguments that may be passed to `bootstrap.py`."""
    parser = argparse.ArgumentParser()
    parser.add_argument('port', nargs='?', default=5000, type=int,
                        help="An integer for the port you want to use.")
    parser.add_argument('--gevent', action='store_true',
                        help="Run gevent's production server.")
    parser.add_argument('--tornado', action='store_true',
                        help="Run gevent's production server.")
    args = parser.parse_args()
    return args

dev_environment = parse_arguments()
port=dev_environment.port
container = tornado.wsgi.WSGIContainer(app)
server = tornado.httpserver.HTTPServer(container)
server.listen(port)
tornado.ioloop.IOLoop.instance().start()
