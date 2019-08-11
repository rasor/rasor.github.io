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

#### From Pop Shop

* VSCode
* GParted
* Remote Desktop Viewer

#### Internet

* Brave Browser

#### Authenticator

For Timebased-OneTime-Passcodes (TOTP) using Yubikey:  

* [Yubico Authenticator](https://www.yubico.com/products/services-software/download/yubico-authenticator/)

```bash
# 64-bit Debian
sudo apt-add-repository ppa:yubico/stable
sudo apt update
sudo apt install yubioath-desktop
```

Notes

* Yubikey install also installed python 3
* Some browsers supporting Yubikey: Chrome, Brave, Opera

#### Keybase

Keybase is a cloud vault (a kind like password managers) using keys from devices for encryption (unlike the psw mgrs, that uses a master key).  
This enables encrypted sharing between users and trust based on proofs written to social networks.  

* [Install Linux | Keybase Docs](https://keybase.io/docs/the_app/install_linux)

```bash
# 64-bit Debian install
curl --remote-name https://prerelease.keybase.io/keybase_amd64.deb
sudo apt install ./keybase_amd64.deb
run_keybase

# Using:
# are you a programmer? some terminal examples
keybase prove twitter
keybase id chris
keybase help

# KBFS examples
cat /keybase/public/chris/plan.txt
echo "dirty secret" > /keybase/private/yourname/diary.txt
echo "Dear world, check me out." > /keybase/public/yourname/plan.txt
```

#### Git

* Prerequisites
    * From PopShop installed VSCode
* Guides
    * [How To Install and Configure Git on Ubuntu 18.04 | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-install-git-on-ubuntu-18-04)
    * [Configuring 2FA for Github with Microsoft Visual Studio Code Integration](https://mattselkey.com/configuring-2fa-for-github-microsoft-visual-code-integration/)

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