Title:  Python Update
Date: 2099-01-01 00:00
Category: Develop
Tags: #python

## Python Update

```bash
# What Python versions do I have on this devbox? 
# 2.x:
python -V
# Python 2.7.15 
pip -V
# pip 9.0.3 from c:\program files (x86)\python27\lib\site-packages (python 2.7)

# 3.x:
py -V
# py -3 -V # alternative
# Python 3.6.4
pip3 -V
# py -3 -m pip -V # alternative
# pip 9.0.1 from c:\program files (x86)\python36-32\lib\site-packages (python 3.6)

# Windows installer
# https://stackoverflow.com/a/55069640/750989
choco
# Chocolatey v0.10.11

```

* [How do I upgrade the Python installation in Windows 10?](https://stackoverflow.com/questions/45137395/how-do-i-upgrade-the-python-installation-in-windows-10)

## Find more pip modules

Like npm in javascript

Visit [PyPI – the Python Package Index](https://pypi.org/)

## Update Pip

When getting message like:  
_You are using pip version 9.0.1, however version 19.0.3 is available._  
_You should consider upgrading via the 'python -m pip install --upgrade pip' command._

Run as Admin

```bash
# Upgrade pip (-3 for 3.x or -2 for 2.x)
py -3 -m pip install --upgrade pip # or
# pipenv run py -3 -m pip install -U pip==19.0.3
pip3 -V
# pip 19.0.3 from c:\program files (x86)\python36-32\lib\site-packages\pip (python 3.6)
```

## Lost Pip?

Run as Admin

```bash
pip3 -V # or
py -3 -m pip -V
# bash: /c/Program Files (x86)/Python36-32/Scripts/pip3: No such file or directory

# ... your pip is missing! Reinstall:
# Download pip from https://bootstrap.pypa.io/get-pip.py then:
py -3 get-pip.py
py -3 -m pip -V
# pip 19.0.3 from C:\Program Files (x86)\Python36-32\lib\site-packages\pip (python 3.6)

# More info: https://stackoverflow.com/a/12476379/750989
```

## pipenv

pipenv is yarn for python - it generates a .lock file.  

* Using pipenv virtualenv: [rasor/nuc-openfaas](https://github.com/rasor/nuc-openfaas/blob/master/Journal.md)
* [Pipenv: A Guide to the New Python Packaging Tool – Real Python](https://realpython.com/pipenv-guide/)
* [Advanced Usage of Pipenv](https://pipenv.readthedocs.io/en/latest/advanced/#configuration-with-environment-variables)
* [Using pip or pipenv](https://nucypher.readthedocs.io/en/latest/guides/installation_guide.html#standard-pipenv-installation)

```bash
# Have pipenv?
py -3 -m pipenv -V
# C:\Program Files (x86)\Python36-32\python.exe: No module named pipenv

# Run as admin
pip3 install pipenv
# Print
pipenv
# Usage: pipenv [OPTIONS] COMMAND [ARGS]...
# Options:
#   --where             Output project home information.
#   --venv              Output virtualenv information.
#   --py                Output Python interpreter information.
#   --envs              Output Environment Variable options.
#   --rm                Remove the virtualenv.
#   --bare              Minimal output.
#   --completion        Output completion (to be eval'd).
#   --man               Display manpage.
#   --support           Output diagnostic information for use in GitHub issues.
#   --site-packages     Enable site-packages for the virtualenv.  [env var:PIPENV_SITE_PACKAGES]
#   --python TEXT       Specify which version of Python virtualenv should use.
#   --three / --two     Use Python 3/2 when creating virtualenv.
#   --clear             Clears caches (pipenv, pip, and pip-tools).  [env var:PIPENV_CLEAR]
#   -v, --verbose       Verbose mode.
#   --pypi-mirror TEXT  Specify a PyPI mirror.
#   --version           Show the version and exit.
#   -h, --help          Show this message and exit.

# Usage Examples:
#    Create a new project using Python 3.7, specifically:
#    $ pipenv --python 3.7

#    Remove project virtualenv (inferred from current directory):
#    $ pipenv --rm

#    Install all dependencies for a project (including dev):
#    $ pipenv install --dev

#    Create a lockfile containing pre-releases:
#    $ pipenv lock --pre

#    Show a graph of your installed dependencies:
#    $ pipenv graph

#    Check your installed dependencies for security vulnerabilities:
#    $ pipenv check

#    Install a local setup.py into your virtual environment/Pipfile:
#    $ pipenv install -e .

#    Use a lower-level pip command:
#    $ pipenv run pip freeze

# Commands:
#   check      Checks for security vulnerabilities and against PEP 508 markers provided in Pipfile.
#   clean      Uninstalls all packages not specified in Pipfile.lock.
#   graph      Displays currently-installed dependency graph information.
#   install    Installs provided packages and adds them to Pipfile, or (if no packages are given), installs all packages from Pipfile.
#   lock       Generates Pipfile.lock.
#   open       View a given module in your editor.
#   run        Spawns a command installed into the virtualenv.
#   shell      Spawns a shell within the virtualenv.
#   sync       Installs all packages specified in Pipfile.lock.
#   uninstall  Un-installs a provided package and removes it from Pipfile.
#   update     Runs lock, then sync.

# Fix: https://stackoverflow.com/questions/51540404/how-to-resolve-python-package-depencencies-with-pipenv
# Clear cache and Fix dependencies
pipenv lock --pre --clear
# Locking [dev-packages] dependencies…
# Locking [packages] dependencies…
# Success!
# Updated Pipfile.lock (125640)!
```

## pylint

Also used by VSCode.

```bash
# install py linter
py -3 -m pip install -U pylint --user
# Installing collected packages: mccabe, colorama, wrapt, typed-ast, lazy-object-proxy, astroid, isort, pylint
#   Running setup.py install for wrapt ... done

#   The scripts epylint.exe, pylint.exe, pyreverse.exe and symilar.exe are installed in 'C:\Users\yourname\AppData\Roaming\Python\Python36\Scripts' 
#   which is not on PATH.
#   Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
```

## VSCode extensions

* [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
* [Visual Studio IntelliCode - Preview](https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode)

## VSCode editing

* [Python in Visual Studio Code](https://code.visualstudio.com/docs/languages/python)
* [Editing Python Code in Visual Studio Code](https://code.visualstudio.com/docs/python/editing)
* [Get Started Tutorial for Python in Visual Studio Code](https://code.visualstudio.com/docs/python/python-tutorial#_prerequisites)

## The language

* [6. Modules](https://docs.python.org/3/tutorial/modules.html)

The End