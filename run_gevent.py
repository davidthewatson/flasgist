from views import app
import argparse


def parse_arguments():
    """Parse any additional arguments that may be passed to `bootstrap.py`."""
    parser = argparse.ArgumentParser()
    parser.add_argument('port', nargs='?', default=5000, type=int,
                        help="An integer for the port you want to use.")
    parser.add_argument('--gevent', action='store_true',
                        help="Run gevent's production server.")
    args = parser.parse_args()
    return args

dev_environment = parse_arguments()
port=dev_environment.port
from gevent.wsgi import WSGIServer
http_server = WSGIServer(('', port), app)
http_server.serve_forever()
