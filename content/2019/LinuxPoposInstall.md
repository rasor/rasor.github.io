Title: Install LinuxPopOS on Laptop
Date: 2099-01-01 00:00
Category: DevOps
Tags: #linux, #popos, #ubuntu, #ssh, #github

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

#### From Pop!_Shop

**Pop!_Shop** is an app installed into the Ubuntu distro [Pop!_OS](https://system76.com/pop).  
It is kind of a local appstore.

* VSCode
* GParted
* Remote Desktop Viewer

#### From SnapCraft

[SnapCraft](https://snapcraft.io/store) is a Linux appstore, which lets app developers distribute their apps.  

Install snapcraft

```bash
sudo apt update
sudo apt install snapd
```

[Install Snap Store](https://snapcraft.io/snap-store) - a graphical desktop application for snapd

```bash
sudo snap install snap-store
```

Install apps from the appstore

* [GitHub Desktop](https://snapcraft.io/install/github-desktop/ubuntu)  
    `sudo snap install github-desktop --beta --classic`

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

Your private files will now be available in `/run/user/1000/keybase/kbfs/private/<userid>`

#### xClip

Install [xClip](https://www.cyberciti.biz/faq/xclip-linux-insert-files-command-output-intoclipboard/)
```bash
sudo apt-get install xclip
```

xClip is used by 

* [Paste URL](https://marketplace.visualstudio.com/items?itemName=kukushi.pasteurl) VSCode plugin  
* The follwing Git install

#### Git

* Prerequisites
    * From PopShop installed VSCode
* Guides
    * [Connecting to GitHub with SSH](https://help.github.com/en/articles/connecting-to-github-with-ssh)
    * [Changing a remote URL](https://help.github.com/en/articles/changing-a-remotes-url#switching-remote-urls-from-https-to-ssh)

Optionally add some author info:

```bash
git --version
# git version 2.20.1

git config --global user.name "Your Name"
git config --global user.email "youremail@domain.com"
git config --list
# user.name=Your Name
# user.email=youremail@domain.com

# The information you entered is stored in your Git configuration file ~/.gitconfig
```

If you use 2FA on github, then SSH access with a private key avoids having a `Personal Access Token` to risk to loose and having to cache. More info on [Which remote URL should I use?](https://help.github.com/en/articles/which-remote-url-should-i-use#cloning-with-ssh-urls).  
So from VSCode rather like to use SSH access (opposed to HTTPS access).  
Since you can just regenerate a new SSH key pair, then you don't have to save your private key for later use.  

Warning: You should not give the SSH key a passphrase to avoid trouble in VSCode - Ref: 
[Version Control in Visual Studio Code](https://code.visualstudio.com/docs/editor/versioncontrol#_can-i-use-ssh-git-authentication-with-vs-code)

```bash
# Check for existing SSH keys
ls -al ~/.ssh
# Are there any you want to reuse?

# I want to generate a new key pair
cd ~/.ssh
ssh-keygen -t rsa -b 4096 -C "youremail@domain.com"
# Generating public/private rsa key pair.
# Enter file in which to save the key (/home/youruserid/.ssh/id_rsa): id_rsa_youruserid_github
# Enter passphrase (empty for no passphrase): 
# Enter same passphrase again: 
# Your identification has been saved in id_rsa_youruserid_github.
# Your public key has been saved in id_rsa_youruserid_github.pub.
# The key fingerprint is:
# SHA256:X4uMb123456789012345678901234567rWzWRZD1Szl youremail@domain.com
# The key's randomart image is:
# +---[RSA 4096]----+

# Start the ssh-agent in the background
eval "$(ssh-agent -s)"
# gent pid 17722
ssh-add ~/.ssh/id_rsa_youruserid_github

# If you want to remove keys from deamon
# ssh-add -D
# All identities removed.
```

Add a new SSH key to your GitHub account

```bash
# Copy the contents of the id_rsa_youruserid_github.pub file to your clipboard
xclip -sel clip < ~/.ssh/id_rsa_youruserid_github.pub
```

* Goto [https://github.com/settings/keys](https://github.com/settings/keys)
* New SSH key
* Paste key: Ctrl-V
* Title: vscode_youruserid_github
* Save key: Add SSH key

Finally you need to change urls on your local repos remote origin from HTTPS to SSH

```bash
cd your_local_repo
# Print remote url
git remote -v
# is it using HTTPS?

# Change to SSH (get the SSH url from your remote repo on github)
git remote set-url origin git@github.com:USERNAME/REPOSITORY.git

# Print remote url
git remote -v
```

* My related blogs
    * [Using SSH keys - Connect to Ionic Pro](https://rasor.github.io/using-ssh-keys-connect-to-ionic-pro.html#using-ssh-keys-connect-to-ionic-pro)
    * [cUrl CLI on Windows](https://rasor.github.io/curl-cli-on-windows.html#curl-cli-on-windows)
* Other Guides
    * [How To Install and Configure Git on Ubuntu 18.04 | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-install-git-on-ubuntu-18-04)
    * When accessing with HTTPS
        * [Configuring 2FA for Github with Microsoft Visual Studio Code Integration](https://mattselkey.com/configuring-2fa-for-github-microsoft-visual-code-integration/)
        * [Caching your GitHub password in Git - GitHub Help](https://help.github.com/en/articles/caching-your-github-password-in-git)
        * [How to setup Git Credential store in Windows](https://agilewarrior.wordpress.com/2017/09/25/how-to-setup-git-credential-store-in-windows/)
    * [How to Add a New Remote to your Git Repo](https://articles.assembla.com/en/articles/1136998-how-to-add-a-new-remote-to-your-git-repo)

The End