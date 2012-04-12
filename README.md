# FlasGist

A blog based on <a href="http://twitter.github.com/bootstrap/">Bootstrap</a>, <a href="http://flask.pocoo.org/">Flask</a>, <a href="http://www.gevent.org/">Gevent</a>, <a href="https://github.com/">Github</a>, <a href="http://www.heroku.com/">Heroku</a>, <a href="http://python.org/">Python</a>, and <a href="http://docs.python-requests.org/en/latest/index.html">Requests</a>

FlasGist stores its blog data as Gist on Github. The heavy lifting is done via python-requests asynchronously. It uses the Github Gist API to access this data. Right now it uses youtube and flickr embed for the media, but I will convert those to API calls also. Github repositories are listed on the software page via the github API also.

![github.com: List of Starred Gists](https://github.com/davidthewatson/flasgist/raw/master/screenshots/github-listofstarredgists.png)

![davidwatson.org: List of Starred Gists](https://github.com/davidthewatson/flasgist/raw/master/screenshots/davidwatsonorg-listofstarredgists.png)

![github.com Specific Starred Gist](https://github.com/davidthewatson/flasgist/raw/master/screenshots/github-listofspecificgist.png)

![davidwatson.org: Specific Starred Gist](https://github.com/davidthewatson/flasgist/raw/master/screenshots/davidwatsonorg-specificgist.png)

You can see flasgist running at <a href="http://davidwatson.org/">davidwatson.org</a>.