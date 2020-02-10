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
    * Password manager
* [Settings](brave://settings/)
    * Appearance: Hide Brave Rewards button
    * Privacy and security: Turn off most things 
    * Autofill: Turn off everything 

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
* Remember: `pip install ghp-import`
* Test build + publish
```bash
# CMD
.\build
.\publish "msg"
```

### Yubikey

For Timebased-OneTime-Passcodes (TOTP) using Yubikey:  

* [Yubico Authenticator](https://www.yubico.com/products/services-software/download/yubico-authenticator/)

### pCloud

pCloud is an idrive.  
It [integrates into filemanagers](https://www.pcloud.com/how-to-install-pcloud-drive-windows.html?download=windows-10-64bit).  

### PDF reader

* [Adobe Acrobat Reader DC, free PDF viewer download](https://get.adobe.com/uk/reader/)

### MovesLink

For uploading GPS data from Suunto GPS watches to [Movescount](http://www.movescount.com/) 

* [Moveslink](https://www.suunto.com/en-gb/Support/software-support/moveslink/)

### Keybase

Keybase is a cloud vault (a kind like password managers) using keys from devices for encryption (unlike the psw mgrs, that uses a master key).  
This enables encrypted sharing between users and trust based on proofs written to social networks.  

* [Install Windows | Keybase Docs](https://keybase.io/docs/the_app/install_windows)

The end