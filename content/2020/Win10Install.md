Title: Install apps on Windows 10 on Laptop
Date: 2099-01-01 00:00
Category: DevOps
Tags: #windows, #os

This contains a list of app I need installed on a Laptop

# Install OS

Often the OS comes preinstalled on a Laptop, so that is not a procedure I'll cover here.

## After Install

### NVM for Windows and NodeJs

* Download `nvm-setup.zip` from [nvm-windows](https://github.com/coreybutler/nvm-windows/releases).
* Verify checksum from file nvm-setup.zip.checksum.txt with 
`certutil -hashfile nvm-setup.zip MD5`
* Extract and run setup
* Use nvm:
```bash
# get help
nvm
# print installed
nvm list
# install NodeJs LTS - llokup on https://nodejs.org/en/
nvm install 12.14.1
# switch to LTS
nvm use 12.14.1
# verify node
node -v
# v12.14.1
```

## Git 4 Windows

* Download `64-bit Git for Windows Setup` from [Git Download Package](https://git-scm.com/download/win)
* Verify install:
```bash
git --version
# git version 2.24.1.windows.2
```

### SSH

* [Create a SSH keypair and add to known_hosts](https://github.com/rasor/rasor.github.io/blob/pelican/content/2020/LinuxKubuntuInstall.md#git)
* [Setup SSH Authentication for Git Bash on Windows](https://dev.to/bsara/how-to-setup-ssh-authentication-for-git-bash-on-windows-a63)

## Visual Studio Code

* Download VSCode from [here](https://code.visualstudio.com/docs/?dv=win64user)
* Installs in C:\Users\user\AppData\Local\Programs\Microsoft VS Code
* [Plugins](https://github.com/rasor/awesome-tables/blob/master/awesome-plugins.md#visual-studio-code)
* Verify install:
```bash
code -v
# 1.41.1
```

## Brave browser

* Download [Brave](https://laptop-updates.brave.com/latest/winx64)
* [Plugins](https://github.com/rasor/awesome-tables/blob/master/awesome-plugins.md#chrome)

## Python

* [Download Python](https://www.python.org/downloads/)
* On last screen of install: [Remove MAX_PATH limitation](https://docs.python.org/3/using/windows.html#removing-the-max-path-limitation)
* Re-run setup - Modify - verify that you are happy with all options
* Installs in C:\Users\user\AppData\Local\Programs\Python
* Docs: [3. Using Python on Windows &#8212; Python 3.8.1 documentation](https://docs.python.org/3/using/windows.html)
* Verify install:
```bash
py
# Python 3.8.1
>>> exit()
py -V
#Python 3.8.1
pip -V
# pip 19.2.3
pip3 -V
# pip 19.2.3
```

### Pelican static site generator

* [Using Pelican blog on Github pages](https://rasor.github.io/using-pelican-blog-on-github-pages.html)


The end