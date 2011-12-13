from rocket import Rocket
from flaskengine import app

server = Rocket(('127.0.0.1', 5000), 'wsgi', {"wsgi_app":app})
server.start()
