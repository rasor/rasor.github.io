Title: Using Pelican Themes
Date: 2017-09-30 10:00
Category: DevOp
Tags: #blog, #pelican, themes, #cms, #install

This blog is part of a serie 

1. [Using Pelican blog on Github pages]({filename}/2017/2017-09-23B-PelicanBlogOnGithubPages.md)
2. [Using Pelican Themes]({filename}/2017/2017-09-30A-PelicanThemes.md)

## Installation - Plugins and Themes

Plugins and Themes are two seperate repos being used by some themes.
To be able to reach them from `pelicanconf.py` is best to clone them to place with an absolute path.

Since preference will differ I will put part of the path in system-wide environment variables

* `SystemPropertiesAdvanced.exe`
    * Environment Variables – System vars – New
    * Name: `PYTHON_HOME`, Value: `C:\ProgramFilesExtra\Python\Python36-32`(Use the path to Python installed in top of previous blog)
    * Press OK until all dialogs are closed, so you are sure the variable is stored
* Start new cmd promt (this will load the new environment variable)
* Create a folder for the cloned repos:

```bash
c:
cd %PYTHON_HOME%
md pelican-addon-clones
cd pelican-addon-clones
# Download plugins and themes
git clone --recursive https://github.com/getpelican/pelican-plugins
git clone --recursive https://github.com/getpelican/pelican-themes
```

```bash
```

# Themes Test

## View installed themes and themes you can install

```bash
# Which themes are ready to use by Pelican?
> pelican-themes -v -l
c:\programfilesextra\python\python36-32\lib\site-packages\pelican\themes\notmyidea
c:\programfilesextra\python\python36-32\lib\site-packages\pelican\themes\simple
# Which themes are downloaded and ready to install?
> start C:\ProgramFilesExtra\Python\Python36-32\pelican-addon-clones\pelican-themes\
```
Command start opens an explorer, so you can go into the folders and see if there are any images showing how the theme looks like.
Or you can checkout <http://www.pelicanthemes.com/>

I am at time of writing running with theme Flex.

## Theme "Flex"

### Installation

[Online Instruction](https://github.com/alexandrevicenzi/Flex)



```bash
c:
cd %PYTHON_HOME%\pelican-addon-clones
md pelican-themes-extra
cd pelican-themes-extra
git clone https://github.com/alexandrevicenzi/Flex
[pelican-themes](http://docs.getpelican.com/en/stable/pelican-themes.html) --install C:\ProgramFilesExtra\Python\Python36-32\pelican-addon-clones\pelican-themes-extra\Flex --verbose
#pelican-themes --remove Flex
```
* Add to `pythonconf.py` 
```Python
THEME = 'Flex'
```
* More to add: <https://github.com/alexandrevicenzi/Flex/wiki/Configuration-example>

### Verdict

#### Pros

* Nice looking
* Images are shown in its full width - and resized to screen width
* Syntax highligting is ggood

#### Cons

* It is missing links categories in left black sidemenu
* Links in the left black sidemenu is only hooked to LINKS from publishconf. SOCIAL is missing
* Modified/Updated date is not shown

## Them "HTML5 Up striped"

### Installation

[Online Instruction](https://github.com/getpelican/pelican-themes/tree/master/pelican-striped-html5up)
```bash
c:
pelican-themes --install C:\ProgramFilesExtra\Python\Python36-32\pelican-addon-clones\pelican-themes\pelican-striped-html5up --verbose
#pelican-themes --remove pelican-striped-html5up
```

Plugin `neighbors` is needed by the theme
* Add to `pythonconf.py`

```Python
PLUGIN_PATHS = ['C:\ProgramFilesExtra\Python\Python36-32\pelican-addon-clones\pelican-plugins']
PLUGINS = ['neighbors']
THEME = 'pelican-striped-html5up'
```

### Verdict

#### Pros

* Nice looking
* Images are shown in its full width

#### Cons

* It does not have any syntax coding and block around code
* It is missing links to categories and tags links
* Links in the left black sidemenu are not hooked to content from publishconf or other

################################################

Links

* <http://www.pelicanthemes.com/>
* <http://docs.getpelican.com/en/stable/pelican-themes.html>

* In path: C:\ProgramFilesExtra\Python\Python36-32
* C:\ProgramFilesExtra\Python\Python36-32\Lib\site-packages\pelican\themes
* https://media.readthedocs.org/css/sphinx_rtd_theme.css





* http://pygments.org/languages/
* Plugins https://github.com/getpelican/pelican-plugins
* Pelican Themes
    * http://www.pelicanthemes.com/
    * https://github.com/getpelican/pelican-themes
    * http://docs.getpelican.com/en/stable/pelican-themes.html
    * Days https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3
    * - 6M https://github.com/getpelican/pelican-themes/tree/master/pelican-striped-html5up
    * 10M https://github.com/alexandrevicenzi/Flex/tree/5bc235cf579cb03bcc8f54b6029ff74493a0cb44
    * 2Y https://github.com/Parbhat/pelican-blue/tree/1dda054242f9267f4bd49891b022ac41c9ecfbe8
    * 2Y https://github.com/jody-frankowski/blue-penguin/tree/c5e23e7753367b5beacce87b732cd1567c4818f9
    * 3Y https://github.com/nasskach/pelican-blueidea/tree/8f11c0e3b4b8e9ef45d1243b0175db91b7b42ba8
    * Edit https://www.fullstackpython.com/blog/generating-static-websites-pelican-jinja2-markdown.html
* Jekyll Themes https://github.com/rasor/rasor.github.io/settings/pages/themes?utf8=%E2%9C%93&source=master

* Images https://unsplash.com/ 

################################################

The End
