Title: Welcome to my Pelican blog on Github pages
Date: 2017-09-23 20:20
Category: #blog
[//]: # (Category: #pelican, #githubpages, #cms)

The blog is created using <http://docs.getpelican.com/en/stable/quickstart.html> and <https://pages.github.com/>

### HowTo
* Install Python
* As admin:
    * `pip install pelican markdown`
* Create a folder for the Pelican source
* `MKDIR username.github.io.pelican`
* `CD username.github.io.pelican`
* Create a pelican site following <http://docs.getpelican.com/en/stable/quickstart.html>
* `pelican-quickstart`
    * Do you want to specify URL prefix? Answer https://username.github.io
    * Do you want to upload using xxx? Answer N untill the xxx = GitHub Pages
* Create a blog e.g `~/content/myfirstblog.md`
* `pelican content` 
* `cd output`
* `python -m pelican.server`
* Browse to  http://localhost:8000/
* Optionally edit more settings in `pelicanconf.py` - see <http://docs.getpelican.com/en/3.7.1/settings.html>
* add a `favicon.ico` to root
* Fetch `.gitignore `from <https://github.com/getpelican/pelican-blog/blob/master/.gitignore> - save it to root
* Create a `~/README.md` - just for the repo
* Create a remote repo for your github page source in GitHub. Call it `username.github.io.pelican`
* Create local git repo
    * `git init`
    z* `git remote add origin https://github.com/rasor/rasor.github.io.pelican.git`
* Create a remote repo for your github page build in GitHub. Call it `username.github.io`
* Connect to 2nd repo and print both remote repos
    * `git remote add target https://github.com/rasor/rasor.github.io.git`
    * `git remote -v`
    * `git branch pelican`
* Publish source
    * `git checkout pelican`
    * `git add --all`
    * `git commit -m "Initial commit"`
    * `git push -u origin pelican`
* Install publich tool
    * `pip install ghp-import`
* [Publish build](http://docs.getpelican.com/en/3.7.1/tips.html#publishing-to-github)
    * `pelican content -o output -s pelicanconf.py`
    * `ghp-import output -r origin -b master`
    * `git push origin master`

### Links
* Create a repo for your github page site following <https://pages.github.com/>
* <http://docs.getpelican.com/en/stable/publish.html>
* <http://docs.getpelican.com/en/stable/pelican-themes.html>
* <https://github.com/tchapi/markdown-cheatsheet>
* <http://pythonhosted.org/Markdown/reference.html>
* <http://docs.getpelican.com/en/stable/faq.html>
* <https://blog.getpelican.com/>
* <https://help.github.com/articles/about-supported-custom-domains/>
* My old blog: <https://rasor.wordpress.com/>

The End