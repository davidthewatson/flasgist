import fapws._evwsgi as evwsgi
from fapws import base
from flaskengine import app
 
def start():
    evwsgi.start("0.0.0.0", '5000')
    evwsgi.set_base_module(base)
 
    evwsgi.wsgi_cb(("/", app))
 
    evwsgi.set_debug(0)
    evwsgi.run()
 
if __name__=="__main__":
    start()
