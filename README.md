FlaskEngine v0.3.0
===

A replica of [Flaskr](http://flask.pocoo.org/docs/tutorial/ "Flaskr - Flask Tutorial"), using [MongoEngine](http://hmarr.com/mongoengine/ "MongoEngine Docs") for persistence, enhanced with [Markdown](http://www.freewisdom.org/projects/python-markdown/ "Markdown in Python").

Forked from artisonian, I added the missing CRUD pieces for Update and Delete, modded the CSS for a simple black and white treatment, and started generating semantic URLs based on title.

I also added pagination, with a simple pagination class discovered here:

https://gist.github.com/347333

## Getting Started

Clone the repository, install the requirements, then run the server.

    git clone git://github.com/davidthewatson/flaskengine.git
    pip install -r requirements.txt
    python runserver.py 

Then point your browser at http://yourhost/

## Requirements

* flask >= 0.2 (in development)
* mongoengine
* python-markdown

## TODO

* Combine `runserver.py` and `runtests.py` into a single `manage.py` script.
* Add support for Markdown extensions.
* Implement tumblelog post types from the [MongoEngine tutorial](http://hmarr.com/mongoengine/tutorial.html).
* Add support for multiple users.
* Improve authentication.
* Add license.
