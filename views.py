from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, send_from_directory 
from os.path import join, curdir
import os
import markdown
import datetime
import threading
import requests
from requests import async
import json
# helpers                                                                                                                                                                                                                                                                     
def to_markdown(value):
    """Converts a string into valid Markdown."""
    return markdown.markdown(value)

# create our little application :)                                                                                                                                                                                                                                            
app = Flask(__name__)
app.jinja_env.filters['markdown'] = to_markdown
app.secret_key = os.environ['secret_key']

@app.route('/ideas/<page>', methods=['GET'])
def page(page):
    if page in ['first', 'next', 'prev', 'last']:
        uri = session['paginate'][page]
    elif page in session.keys():
        try:
            uri = 'https://api.github.com/gists/' + session[page]
        except:
            abort(404)
    else:
        try:
                uri = 'https://api.github.com/gists/starred' #users/davidthewatson/gists'
                r = requests.get(uri, auth=(os.environ['GIST_USR'], os.environ['GIST_PWD']))
                if r.status_code == 200:
                    gists = json.loads(r.content)
                    id = [d['id'] for d in get_gists(gist['id'] for gist in gists) if d['filename'] == page][0]
                    uri = 'https://api.github.com/gists/' + id
        except:
            abort(404)
        
    r = requests.get(uri, auth=(os.environ['GIST_USR'], os.environ['GIST_PWD']))
    if r.status_code == 200:
        l = []
        gist = json.loads(r.content)
        l.append(process_gist(r))
        return render_template('ideas.html', title=l[0]['description'] + ' - ', l=l)
    abort(r.status_code)        

@app.route('/ideas/', methods=['GET'])
def ideas():
    uri = 'https://api.github.com/gists/starred' #users/davidthewatson/gists'
    r = requests.get(uri, auth=(os.environ['GIST_USR'], os.environ['GIST_PWD']))
    if r.status_code == 200:
        gists = json.loads(r.content)
        if 'link' in r.headers.keys():
            paginate = link_parser(r.headers['link'])
            session['paginate'] = paginate
        return render_template('ideas.html', title='ideas - ', l = get_gists(gist['id'] for gist in gists))
    abort(r.status_code)

def get_gists(gists):
    return [ process_gist(r) for r in async.map(async.get('https://api.github.com/gists/' + gist) for gist in gists ) ]

    
def process_gist(gist):
    content = json.loads(gist.content)
    session[content['files'].keys()[0]] = content['id']
    d = {'filename': content['files'].keys()[0],
       'date': datetime.datetime.strptime(content['created_at'], '%Y-%m-%dT%H:%M:%SZ').strftime('%m/%d/%Y@%H:%M:%S'),
       'description': content['description'],
       'content': content['files'][content['files'].keys()[0]]['content'],
       'id': content['id']}
    return d

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(join(app.root_path, 'static'),'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/sights/', methods=['GET'])
def sights():
    return render_template('sights.html', title='sights - ')

@app.route('/sounds/', methods=['GET'])
def sounds():
    return render_template('sounds.html', title='sounds - ')

@app.route('/software/', methods=['GET'])
def software():
    r = requests.get('http://github.com/api/v2/json/repos/show/davidthewatson/')
    repositories = []
    if r.status_code == 200:
        d = json.loads(r.content)
        repositories = d['repositories']
    return render_template('software.html', title='software - ', repos=repositories)

@app.route('/2008/02/python-couchdb-rocks.html')
@app.route('/2007/05/broadcom-4306-on-feisty-fawn.html')
@app.route('/2007/01/happy-new-year-mythtv.html')
@app.route('/2007/07/you-have-entered-an-invalid-value.html')
@app.route('/2008/11/acer-restore-failed-reason-0xd0000017.html')
@app.route('/2007/02/on-merits-of-evans-ec-snare-drum-head.html')
def redirect_to_new_page():
    page = str.replace(request.url[request.url.rfind('/')+1:], '-', '_')
    return redirect(url_for('page', page=page), 301)
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title='404 page not found - '), 404
    
def link_parser(s):
    tokens = s.split(',')
    d = {}
    for pairs in tokens:
        split_pairs(pairs, d)
    return d

def split_pairs(pairs, d):
    link_rel = pairs.split(';')
    link, rel = link_rel[0].strip()[1:-1], link_rel[1].split('=')[1].strip()[1:-1]
    d[rel] = link
