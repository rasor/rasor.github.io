Title: Using Pelican blog on Github pages
Date: 2017-09-23 20:20
Modified: 2017-11-26 20:00
Category: DevOp
Tags: #blog, #pelican, #githubpages, #cms, #git, #install

This blog is part of a serie 

1. [Using Pelican blog on Github pages]({filename}/2017/2017-09-23B-PelicanBlogOnGithubPages.md)
2. [Using Pelican Themes]({filename}/2017/2017-09-30A-PelicanThemes.md)

I had some reasons for moving a blog from Wordpress to GitHubPages. You can read about reason, pro and cons [here]({filename}/2017/2017-09-23A-Welcome.md){:target="_blank"}

In this blog I setup a [Pelican blog site](http://docs.getpelican.com/en/stable/quickstart.html){:target="_blank"} from Windows and host it on [GitHub Pages](https://pages.github.com/){:target="_blank"}.

## HowTo
### Installation - Prerequisites
* Install [Python](https://www.python.org/downloads/){:target="_blank"}
* Create an account at <https://github.com>
* On Windows: Install [Git for Windows](https://git-scm.com/download/win){:target="_blank"}
### Installation - Pelican
* As admin:
    * `pip install pelican markdown`
* Create a folder for the Pelican source
    * `MD username.github.io`
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
* On Windows - in root create a file called [serve.bat](https://github.com/rasor/rasor.github.io/blob/pelican/serve.bat){:target="_blank"} with the content:
```bash
pelican content
cd output
start "" "http://localhost:8000/"
python -m pelican.server
REM Ctrl-C to quit
```
* ... then you can pre-view your content with `.\serve`
* Images
    * In `pelicanconf.py` add line `STATIC_PATHS = ['img', 'pdf']`
    * Create an image e.g `~/content/img/hello.png`
    * Link to the file with
`![picture alt](img/hello.png "Mickey Mouse")`
* Links
    * External: `[link desc](https://blog.getpelican.com/){:target="_blank"}`
    * Internal: `[link desc]({filename}/yourcategoryno1/myfirstblog.md){:target="_blank"}`
* Optionally edit more settings in `pelicanconf.py` - see <http://docs.getpelican.com/en/3.7.1/settings.html>
* add a `favicon.ico` to root
### Prepare GIT as VersionControlSystem
* Fetch `.gitignore `from <https://github.com/getpelican/pelican-blog/blob/master/.gitignore> - save it to root
* Create a `~/README.md` - just for the source branch
* Install publish tool
    * `pip install ghp-import`
* Create local git repo
    * `git init`
* Create a remote repo via github.com for your github page build in GitHub. Call it `username.github.io`
* Connect to repo and print remote repo
    * `git remote add origin https://github.com/username/username.github.io.git`
    * `git remote -v`
* Create new branch for the pelican source
    * `git checkout -b pelican`
### Deploy you blog
* (Foreach) Commit source
    * `git add .`
    * `git commit -a -m "Initial commit"`
    * `git push -u origin pelican`
* (Foreach) [Publish](http://docs.getpelican.com/en/3.7.1/tips.html#publishing-to-github){:target="_blank"} build to master then publish
    * `pelican content -o output -s pelicanconf.py`
    * `ghp-import output -r origin -b master`
    * `git push origin master`
    * `git checkout pelican`
* On Windows - in root create a file called [publish.bat](https://github.com/rasor/rasor.github.io/blob/pelican/publish.bat){:target="_blank"} with the content:

```bash
git add .
git commit -a -m %1
git push -u origin pelican
pelican content -o output -s pelicanconf.py
ghp-import output -r origin -b master
git push origin master
git checkout pelican
```
* ... then you can publish by `.\publish "some comment"`

## Editor
I'm using Visual Studio Code, that has a nice Markdown preview - probably a plugin.
But you could use NotePad for that matter.

![picture alt](img/2017-09-23-PelicanInVSCode.PNG "Pelican In VS Code")

## Day to day Workflow
1. Open VS Code
2. Open VS Code terminal 1 - T1
    * `.\serve` [#code](https://github.com/rasor/rasor.github.io/blob/pelican/serve.bat)
    * A browser opens and navigates to http://localhost:8000
3. Add a new `.md` file in \content\ and add some content
4. Open VS Code terminal 2 - T2
    * `.\build` [#code](https://github.com/rasor/rasor.github.io/blob/pelican/build.bat)
    * F5 - refresh browser to see the new content
    * `.\publish "file new.md published"` [#code](https://github.com/rasor/rasor.github.io/blob/pelican/publish.bat)
5. Browse to https://username.github.io

Tip: If I don't want to publish a file I rename it to `.txt` - then it won't be visible before I rename it back to `.md`

Continue in [Using Pelican Themes]({filename}/2017/2017-09-30A-PelicanThemes.md){:target="_blank"}

-----------------------------

### Links

#### GitHub pages

* [Create a repo for your github page site](https://pages.github.com/){:target="_blank"}
* [Fork-n-Go](http://jlord.us/forkngo/){:target="_blank"}

#### Pelican

* <http://docs.getpelican.com/en/stable/publish.html>{:target="_blank"}
* <http://docs.getpelican.com/en/3.6.3/content.html#linking-to-static-files>{:target="_blank"}
* <http://docs.getpelican.com/en/stable/faq.html>{:target="_blank"}
* <https://blog.getpelican.com/>{:target="_blank"}
* <https://help.github.com/articles/about-supported-custom-domains/>{:target="_blank"}
* Another [install Pelican blog](https://www.fullstackpython.com/blog/generating-static-websites-pelican-jinja2-markdown.html){:target="_blank"}
* Pelican [tutorial for deployment](https://github.com/getpelican/pelican/wiki/Tutorials){:target="_blank"}
* [Pelican on Twitter](https://twitter.com/getpelican){:target="_blank"}

#### Markdown

* [StackEdit – Editor](https://stackedit.io/editor){:target="_blank"}
* <https://github.com/tchapi/markdown-cheatsheet>{:target="_blank"}
* [Syntax highlighting languages](http://tinker.kotaweaver.com/blog/?p=152){:target="_blank"}
* <http://pythonhosted.org/Markdown/reference.html>{:target="_blank"}
* [List of XML and HTML characters](https://en.wikipedia.org/wiki/List_of_XML_and_HTML_character_entity_references){:target="_blank"}

##### Other

* [My old Wordpress blog](https://rasor.wordpress.com/){:target="_blank"}

The End