Title: Using Pelican Themes
Status: published
Date: 2017-09-30 11:00
Modified: 2017-09-30 15:00
Category: DevOp
Tags: #blog, #pelican, #themes, #cms, #install

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

The above repo pelican-themes in some cases is not linked to the latest version of a theme.
So for those themes you can clone them into another folder called pelican-themes-extra.

```bash
c:
cd %PYTHON_HOME%\pelican-addon-clones
md pelican-themes-extra
```

# Testing Themes

## View installed themes and themes you can install

```bash
# Which themes are ready to use by Pelican? - By default Pelican is running theme "notmyidea"
> pelican-themes -v -l
c:\programfilesextra\python\python36-32\lib\site-packages\pelican\themes\notmyidea
c:\programfilesextra\python\python36-32\lib\site-packages\pelican\themes\simple
# Which themes are downloaded and ready to install?
> start %PYTHON_HOME%\pelican-addon-clones\pelican-themes\
```

Command `start` opens an explorer, so you can go into the folders and see if there are any images showing how the theme looks like.
Or you can checkout <http://www.pelicanthemes.com/>{:target="_blank"}

I am at time of writing running with theme Flex.

Ref: Command [pelican-themes](http://docs.getpelican.com/en/stable/pelican-themes.html)

## Switch to Theme "Flex"

### Installation

[Online Instruction](https://github.com/alexandrevicenzi/Flex){:target="_blank"}

Flex is one of the themes that is not latest in pelican-themes repo, so I want to download latest from its own repo.

```bash
c:
cd %PYTHON_HOME%\pelican-addon-clones\pelican-themes-extra
# Download Flex
git clone https://github.com/alexandrevicenzi/Flex
# Install Flex into Pelican
pelican-themes --install C:\ProgramFilesExtra\Python\Python36-32\pelican-addon-clones\pelican-themes-extra\Flex --verbose
# pelican-themes --remove Flex
```

* Add to [`pelicanconf.py`](https://github.com/rasor/rasor.github.io/blob/pelican/pelicanconf.py){:target="_blank"}

```python
THEME = 'Flex'
STATIC_PATHS = ['img', 'static']
FAVICON = 'img/favicon.ico'
CUSTOM_CSS = 'static/custom.css'
```

* Notice: If you don't want to add extra CSS, then `THEME` is all you have to set
* In the CUSTOM_CSS I am just adding a shadow to images
* In \content\static\ create a file called [`custom.css`](https://github.com/rasor/rasor.github.io/blob/pelican/content/static/custom.css){:target="_blank"} with the content:

```css
img {
    box-shadow: 5px 5px 12px grey;
}
```

* More configurations you can add: <https://github.com/alexandrevicenzi/Flex/wiki/Configuration-example>{:target="_blank"}. You probably will want many of them.

### Verdict

#### Pros

* Nice looking
* Images are shown in its full width - and resized to screen width
* Syntax highligting is good

#### Cons

* Modified/Updated date is not shown

## Switch to Theme "HTML5 Up striped"

### Installation

[Online Instruction](https://github.com/getpelican/pelican-themes/tree/master/pelican-striped-html5up){:target="_blank"}

```bash
c:
# Install striped-html5up into Pelican
pelican-themes --install C:\ProgramFilesExtra\Python\Python36-32\pelican-addon-clones\pelican-themes\pelican-striped-html5up --verbose
#pelican-themes --remove pelican-striped-html5up
```

Plugin `neighbors` is needed by the theme

* Add to `pythonconf.py`

```python
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

# Extending Themes

I extended theme "Flex" so it shows Modified date.

The workflow for updating a theme can be:

1. Edit the theme in its local repo
2. Remove the theme from Pelican
3. Re-intall the theme to Pelican
4. Build your output and see the change

### 1. Edit Theme

* Goto the root of your theme folder and open the theme in your favorite editor. In this case I edit Flex in VS Code

```bash
c:
cd %PYHON_HOME%\pelican-addon-clones\pelican-themes-extra\Flex
# start VS Code
code .
```

* On each blog post I want to add the `Modified` field below the publish date. Add to [`templates\article.html`](https://github.com/alexandrevicenzi/Flex/blob/master/templates/article.html){:target="_blank"}

```html
      <!-- Inside p-tag contining when=article.locale_date -->
      </br>
      {% if article.modified %}
        Updated: {{ article.modified |strftime(DEFAULT_DATE_FORMAT) }}
      {% endif %}
```

* Before you re-install the theme you should also goto your Pelican project and make sure you have `DEFAULT_DATE_FORMAT` set to the same format as `locale_date`. In `pelicanconf.py` you could do it like this

```python
DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%B %d, %Y'
DATE_FORMATS = {
    'en': DEFAULT_DATE_FORMAT,
}
```

### 2. Remove Theme from Pelican

```bash
# Easiest way to remove a theme from Pelican is to delete the folder where it is installed into
start %PYTHON_HOME%\lib\site-packages\pelican\themes
```

### 3. Install Theme to Pelican

See "Switch to Theme" above.

### 4. Build and see output

See "Day to day Workflow" in [previous]({filename}/2017/2017-09-23B-PelicanBlogOnGithubPages.md){:target="_blank"} blog.

# Links

* <http://www.pelicanthemes.com/>{:target="_blank"}
* <https://github.com/getpelican/pelican-themes>{:target="_blank"}
* <http://docs.getpelican.com/en/stable/pelican-themes.html>{:target="_blank"}
* <https://media.readthedocs.org/css/sphinx_rtd_theme.css>{:target="_blank"}
* <http://pygments.org/languages/>{:target="_blank"}
* <https://github.com/getpelican/pelican-plugins>{:target="_blank"}
* <https://www.fullstackpython.com/blog/generating-static-websites-pelican-jinja2-markdown.html>{:target="_blank"}
* Some Pelican Themes I looked at
    * Days <https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3>{:target="_blank"}
    * 6M <https://github.com/getpelican/pelican-themes/tree/master/pelican-striped-html5up>{:target="_blank"}
    * 10M <https://github.com/alexandrevicenzi/Flex/tree/5bc235cf579cb03bcc8f54b6029ff74493a0cb44>{:target="_blank"}
    * 2Y <https://github.com/Parbhat/pelican-blue/tree/1dda054242f9267f4bd49891b022ac41c9ecfbe8>{:target="_blank"}
    * 2Y <https://github.com/jody-frankowski/blue-penguin/tree/c5e23e7753367b5beacce87b732cd1567c4818f9>{:target="_blank"}
    * 3Y <https://github.com/nasskach/pelican-blueidea/tree/8f11c0e3b4b8e9ef45d1243b0175db91b7b42ba8>{:target="_blank"}
* Images <https://unsplash.com/>{:target="_blank"}

The End
