# FlasGist

A blog based on <a href="http://twitter.github.com/bootstrap/">Bootstrap</a>, <a href="http://flask.pocoo.org/">Flask</a>, <a href="http://www.gevent.org/">Gevent</a>, <a href="https://github.com/">Github</a>, <a href="http://www.heroku.com/">Heroku</a>, <a href="http://python.org/">Python</a>, and <a href="http://docs.python-requests.org/en/latest/index.html">Requests</a>

FlasGist stores its blog data as Gist on Github. The heavy lifting is done via python-requests asynchronously. It uses the Github Gist API to access this data. Right now it uses youtube and flickr embed for the media, but I will convert those to API calls also. Github repositories are listed on the software page via the github API also.

##FlasGist works like this: 

###I create a starred gist on github

![github.com Specific Starred Gist](https://github.com/davidthewatson/flasgist/raw/master/screenshots/github-specificstarredgist.png)

###I save the starred gist on github; it shows up on github

![github.com: List of Starred Gists](https://github.com/davidthewatson/flasgist/raw/master/screenshots/github-listofstarredgists.png)

###A user hits my blog; the blog software makes an API request and gets the starred gists from github

![davidwatson.org: List of Starred Gists](https://github.com/davidthewatson/flasgist/raw/master/screenshots/davidwatsonorg-listofstarredgists.png)

### If the user clicks a specific link, the content for that article is returned from github and rendered as markdown or html

![davidwatson.org: Specific Starred Gist](https://github.com/davidthewatson/flasgist/raw/master/screenshots/davidwatsonorg-specificstarredgist.png)

You can see flasgist running at <a href="http://davidwatson.org/">davidwatson.org</a>.