Title: Install LinuxPopOS on Laptop
Date: 2099-01-01 00:00
Category: DevOps
Tags: #linux, #popos, #ubuntu

HowTo get from Window to Ubuntu fork - Pop_OS

## After install

### Tips

* [RightClick = 2 finger click](https://who-t.blogspot.com/2018/04/gnome-328-uses-clickfinger-behaviour-by.html)
* [Create shortcut for URL](https://askubuntu.com/questions/359492/create-a-shortcut-for-url)

#### Going from Dos to Terminal

|Dos|Terminal|Comment|
|---|---|---|
|cls|clear||
||touch a.md|Create an empty file|
|"Hello" > a.md|cat > a.md|Create a file. Enter text. Ctrl-Z to save|

### Install

#### Pop Shop

* VSCode
* GParted
* Remote Desktop Viewer

#### Internet

* Brave Browser

#### Git

* Prerequisites
    * From PopShop installed VSCode
* Guide: [How To Install and Configure Git on Ubuntu 18.04 | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-install-git-on-ubuntu-18-04)

```bash
git --version
# git version 2.20.1
git config --global user.name "Your Name"
git config --global user.email "youremail@domain.com"
git config --list
# user.name=Your Name
# user.email=youremail@domain.com
```

#### xClip

Install [xClip](https://www.cyberciti.biz/faq/xclip-linux-insert-files-command-output-intoclipboard/)
```bash
sudo apt-get install xclip
```
xClip is used by [Paste URL](https://marketplace.visualstudio.com/items?itemName=kukushi.pasteurl) VSCode plugin


The End