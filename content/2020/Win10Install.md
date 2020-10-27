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

## Chocolatey - package manager for Windows

* Install [Chocolatey](https://chocolatey.org/install)

```ps1
# ps1 - run as admin:
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
# Getting Chocolatey from https://chocolatey.org/api/v2/package/chocolatey/0.10.15.
# .........
# Installing chocolatey on this machine
# .........
# PATH environment variable does not have C:\ProgramData\chocolatey\bin in it. Adding...
# Adding Chocolatey to the profile. This will provide tab completion, refreshenv, etc.
# WARNING: Unable to add Chocolatey to the profile. You will need to do it manually. Error was 'Cannot process argument transformation on parameter 'Encoding'. 'byte' is not a supported encoding name. For information on defining a custom encoding, see the documentation for the Encoding.RegisterProvider method. (Parameter 'name')'
# This is how add the Chocolatey Profile manually.
# Find your $profile. Then add the following lines to it:

# $ChocolateyProfile = "$env:ChocolateyInstall\helpers\chocolateyProfile.psm1"
# if (Test-Path($ChocolateyProfile)) {
#   Import-Module "$ChocolateyProfile"
# }
# Chocolatey (choco.exe) is now ready.
# You can call choco from anywhere, command line or powershell by typing choco.
# Run choco /? for a list of functions.
# You may need to shut down and restart powershell and/or consoles
#  first prior to using choco.
# Ensuring chocolatey commands are on the path
# Ensuring chocolatey.nupkg is in the lib folder

choco -v
# 0.10.15
```
Hmm - apparently you need a non-admin prompt to add above to ps1 profile

```ps1
# edit ps1 profile:
notepad $PROFILE
# paste into file:
#---------------------
$ChocolateyProfile = "$env:ChocolateyInstall\helpers\chocolateyProfile.psm1"
if (Test-Path($ChocolateyProfile)) {
  Import-Module "$ChocolateyProfile"
}
#---------------------
```

## Git 4 Windows

* Download `64-bit Git for Windows Setup` from [Git Download Package](https://git-scm.com/download/win)
* Verify install:
```bash
git --version
# git version 2.24.1.windows.2
```

### jq

jq is like `sed` for JSON data - you can use it to slice and filter and map and transform structured data with the same ease that `sed, awk, grep`. See examples in [Tutorial](https://stedolan.github.io/jq/tutorial/).  

* Install [jq](https://stedolan.github.io/jq/download/) to Windows using choco:

```ps1
# ps1 run-as-admi:
choco install jq
# C:\ProgramData\chocolatey\lib\jq\tools\jq.exe
#  ShimGen has successfully created a shim for jq.exe
#  The install of jq was successful.
jq --version
# jq-1.6
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

## Yubikey

For Timebased-OneTime-Passcodes (TOTP) using Yubikey:  

* [Yubico Authenticator](https://www.yubico.com/products/services-software/download/yubico-authenticator/)

## Apple iCloud

* [Get iCloud - Microsoft Store](https://www.microsoft.com/en-us/p/icloud/9pktq5699m62?rtc=1)

## pCloud

pCloud is an idrive.  
It [integrates into filemanagers](https://www.pcloud.com/how-to-install-pcloud-drive-windows.html?download=windows-10-64bit).  

## iTunes

* [Service Unavailable](https://www.microsoft.com/en-us/p/itunes/9pb2mz1zmb1s)

## PDF reader

* [Adobe Acrobat Reader DC, free PDF viewer download](https://get.adobe.com/uk/reader/)

## MovesLink

For uploading GPS data from Suunto GPS watches to [Movescount](http://www.movescount.com/) 

* [Moveslink](https://www.suunto.com/en-gb/Support/software-support/moveslink/)

## Keybase

Keybase is a cloud vault (a kind like password managers) using keys from devices for encryption (unlike the psw mgrs, that uses a master key).  
This enables encrypted sharing between users and trust based on proofs written to social networks.  

* [Install Windows | Keybase Docs](https://keybase.io/docs/the_app/install_windows)

## Windows Terminal or Ps7

* [How to make a pretty prompt in Windows Terminal with Powerline, Nerd Fonts, Cascadia Code, WSL, and oh-my-posh](https://www.hanselman.com/blog/HowToMakeAPrettyPromptInWindowsTerminalWithPowerlineNerdFontsCascadiaCodeWSLAndOhmyposh.aspx)
    * Download: [Get Windows Terminal - Microsoft Store](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701?activetab=pivot:overviewtab)
* PS7: [Installing PowerShell on Windows - PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-windows?view=powershell-7)
    * Download: [PowerShell/PowerShell](https://github.com/PowerShell/PowerShell/releases)
* In either terminal you can get git info by doing:
```ps1
# as admin:
Set-ExecutionPolicy RemoteSigned
# as any
Install-Module posh-git -Scope CurrentUser
Install-Module oh-my-posh -Scope CurrentUser
# if ps core (6+, I think)
Install-Module -Name PSReadLine -AllowPrerelease -Scope CurrentUser -Force -SkipPublisherCheck

# edit ps1 profile:
notepad $PROFILE
# paste into file:
#---------------------
Import-Module posh-git
Import-Module oh-my-posh
Set-Theme Paradox
#---------------------
```

## WSL2

* [Download Windows 10 May 2020 Update (v 2004)](https://www.microsoft.com/en-us/software-download/windows10)
    * Click Udate Now

The end