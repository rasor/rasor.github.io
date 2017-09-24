Title: Using Pelican blog on Github pages
Date: 2017-09-23 20:20
Modified: 2017-09-24 11:00
Category: Study
Tags: #blog, #pelican, #githubpages, #cms, #git

The blog is created using <http://docs.getpelican.com/en/stable/quickstart.html> and <https://pages.github.com/>

## HowTo
### Installation - Prerequisites
* Install [Python](https://www.python.org/downloads/)
* Create an account at <https://github.com>
* On Windows: Install [Git for Windows](https://git-scm.com/download/win)
### Installation - Pelican
* As admin:
    * `pip install pelican markdown`
* Create a folder for the Pelican source
    * `MKDIR username.github.io`
    * `CD username.github.io`
* Create a pelican site following <http://docs.getpelican.com/en/stable/quickstart.html>
* `pelican-quickstart`
    * Do you want to specify URL prefix? Answer https://username.github.io
    * Do you want to upload using xxx? Answer N untill the xxx = GitHub Pages
### Create some content
* Create a blog e.g `~/content/yourcategoryno1/myfirstblog.md`
* Preview content
    * `pelican content` 
    * `cd output`
    * `python -m pelican.server`
    * Browse to  <http://localhost:8000/>
* Images
    * In `pelicanconf.py` add line `STATIC_PATHS = ['img', 'pdf']`
    * Create an image e.g `~/content/img/hello.png`
    * Link to the file with
`![picture alt](img/hello.png "Mickey Mouse")`
* Optionally edit more settings in `pelicanconf.py` - see <http://docs.getpelican.com/en/3.7.1/settings.html>
* add a `favicon.ico` to root
### Prepare GIT as VersionControlSystem
* Fetch `.gitignore `from <https://github.com/getpelican/pelican-blog/blob/master/.gitignore> - save it to root
* Create a `~/README.md` - just for the source branch
* Install publich tool
    * `pip install ghp-import`
* Create local git repo
    * `git init`
* Create a remote repo via github.com for your github page build in GitHub. Call it `username.github.io`
* Connect to repo and print remote repo
    * `git remote add origin https://github.com/rasor/rasor.github.io.git`
    * `git remote -v`
* Create new branch for the pelican source
    * `git checkout -b pelican`
### Deploy you blog
* (Foreach) Commit source
    * `git add .`
    * `git commit -a -m "Initial commit"`
    * `git push -u origin pelican`
* (Foreach) [Publish](http://docs.getpelican.com/en/3.7.1/tips.html#publishing-to-github) build to master then publish
    * `pelican content -o output -s pelicanconf.py`
    * `ghp-import output -r origin -b master`
    * `git push origin master`
    * `git checkout pelican`
* On Windows - in root create a file called [publish.bat](https://github.com/rasor/rasor.github.io/blob/pelican/publish.bat) with the content:
```bash
git add .
git commit -a -m %1
git push -u origin pelican
pelican content -o output -s pelicanconf.py
ghp-import output -r origin -b master
git push origin master
git checkout pelican
```
* ... then you can publish by `publish.bat "some comment"`

## Editor
I'm using Visual Studio Code, that has a nice Markdown preview - probably a plugin.
But you could use NotePad for that matter.

![picture alt](img/2017-09-23-PelicanInVSCode.PNG "Pelican In VS Code")

### Links
* Create a repo for your github page site <https://pages.github.com/>
* <http://docs.getpelican.com/en/stable/publish.html>
* <http://docs.getpelican.com/en/stable/pelican-themes.html>
* <http://docs.getpelican.com/en/3.6.3/content.html#linking-to-static-files>
* <https://github.com/tchapi/markdown-cheatsheet>
* <http://pythonhosted.org/Markdown/reference.html>
* <http://docs.getpelican.com/en/stable/faq.html>
* <https://blog.getpelican.com/>
* <https://help.github.com/articles/about-supported-custom-domains/>
* My old blog: <https://rasor.wordpress.com/>

The End