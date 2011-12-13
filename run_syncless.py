from flaskengine import app
from syncless import wsgi
import stackless

wsgi.RunHttpServer(app, ('0.0.0.0', 5000))
