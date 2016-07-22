# Update

I'm no longer using FlasGist. Instead, I've designed a similar system called <a href="https://github.com/davidthewatson/zegibl">ZeGiBl</a> entirely using client-side JavaScript instead of server-side python. Thus, there is no server footprint as the system functions entirely using github pages, gists, static HTML, and javascript.

## FlasGist

Flasgist is a blog based on <a href="http://twitter.github.com/bootstrap/">Bootstrap</a>, <a href="http://flask.pocoo.org/">Flask</a>, <a href="http://www.gevent.org/">Gevent</a>, <a href="https://github.com/">Github</a>, <a href="http://www.heroku.com/">Heroku</a>, <a href="http://python.org/">Python</a>, and <a href="http://docs.python-requests.org/en/latest/index.html">Requests</a>

FlasGist stores its blog data as Gist on Github. The heavy lifting is done via python-requests asynchronously. It uses the Github Gist API to access this data. Right now it uses youtube and flickr embed for the media, but I will convert those to API calls also. Github repositories are listed on the software page via the github API also.

##FlasGist works like this 

###I create a starred gist on github

![github.com Specific Starred Gist](https://github.com/davidthewatson/flasgist/raw/master/screenshots/github-specificstarredgist.png)

###I save the starred gist on github; it shows up on github

![github.com: List of Starred Gists](https://github.com/davidthewatson/flasgist/raw/master/screenshots/github-listofstarredgists.png)

###A user hits my blog; flasgist makes an API request, gets the starred gists from github, and displays them

![davidwatson.org: List of Starred Gists](https://github.com/davidthewatson/flasgist/raw/master/screenshots/davidwatsonorg-listofstarredgists.png)

### If the user clicks a specific link, the content for that starred gist is returned from github and rendered as markdown or html

![davidwatson.org: Specific Starred Gist](https://github.com/davidthewatson/flasgist/raw/master/screenshots/davidwatsonorg-specificstarredgist.png)

This precludes me from having to implement content management functions such as content creation, editing, updating, and deleting. In addition, I get versioning and forking of content for free - this is beneficial for both annotation of existing content and attribution of content that I did not create, but rather may have extended.

<a href="http://davidwatson.org/">david watson</a>
