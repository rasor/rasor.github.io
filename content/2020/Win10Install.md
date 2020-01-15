Title: Install apps on Windows 10 on Laptop
Date: 2099-01-01 00:00
Category: DevOps
Tags: #windows, #os

This contains a list of app I need installed on a Laptop

# Install OS

Often the OS comes preinstalled on a Laptop, so that is not a procedure I'll cover here.

## After Install

### NVM for Windows

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
# install LTS - llokup on https://nodejs.org/en/
nvm install 12.14.1
# switch to LTS
nvm use 12.14.1
```

## Git 4 Windows

* Download `64-bit Git for Windows Setup` from [Git Download Package](https://git-scm.com/download/win)

## Visual Studio Code

* Download VSCode from [here](https://code.visualstudio.com/docs/?dv=win64user)
* [Plugins](https://github.com/rasor/awesome-tables/blob/master/awesome-plugins.md#visual-studio-code)

## Brave browser

* Download [Brave](https://laptop-updates.brave.com/latest/winx64)
* [Plugins](https://github.com/rasor/awesome-tables/blob/master/awesome-plugins.md#chrome)

The end