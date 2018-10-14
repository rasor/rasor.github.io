Title: Blockchain and Hyperledger
Date: 2099-01-01 00:00
Category: Develop
Tags: #blockchain, #cryptocurrency, #hyperledger, #curl, #python, #node_gyp

# Installing Hyperledger Composer on Windows 10

## PreRequisites

* Install NodeJs  
v8.9 or higher (note version 9 is not supported) - [v10](https://stackoverflow.com/questions/21658832/npm-install-error-msb3428-could-not-load-the-visual-c-component-vcbuild-ex/50714612#50714612)
 does not work either - perhaps a node-gyp issue.
* [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Install Docker including DockerCompose](https://rasor.github.io/docker-for-windows.html)  
Version 17.03 or higher. Compose: Version 1.8 or higher
* [Install cUrl](https://rasor.github.io/curl-cli-on-windows.html)
* Install [Python 2.7](https://www.python.org/downloads/)
* Install [VCBuild.exe](https://stackoverflow.com/questions/21658832/npm-install-error-msb3428-could-not-load-the-visual-c-component-vcbuild-ex/39235952#39235952) - now MSBuild
    * `npm install -g --production windows-build-tools` as Admin. This will both install Python 2.7 and C++.

Here is what is on my machine

CMD:  
```bash
ver
# Microsoft Windows [Version 10.0.17134.345]
```

Git Bash:  
```bash
git --version
# git version 2.17.1.windows.2
sh --version
# GNU bash, version 4.4.19(2)-release (x86_64-pc-msys)
tar --version
# tar (GNU tar) 1.30
node -v
# v8.11.1
npm -v
# 5.6.0
py --version
# Python 3.6.4
py -2 --version
# Python 2.7.15
docker -v
# Docker version 18.06.1-ce, build e68fc7a
docker-compose -v
# docker-compose version 1.22.0, build f46880fe
curl --version
# curl 7.60.0 (x86_64-w64-mingw32) libcurl/7.60.0 OpenSSL/1.0.2o (WinSSL) zlib/1.2.11 libidn2/2.0.5 nghttp2/1.31.1
code -v
# 1.27.1 - VisualStudio Code
C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\MSBuild\15.0\Bin>msbuild /version
# 15.8.166.59604 - for building c++ programs
```

## Try Hyperledger in playground

* [Hyperledger Composer](https://composer-playground.mybluemix.net/login)

## Installing Hyperledger on Windows

* HowTo: [Hyperledger Fabric on Windows 10 – Cochain – Medium](https://medium.com/cochain/hyperledger-fabric-on-windows-10-26723116c636)
    * Enable Developer Mode on Win10:  
    ```bash  
    start ms-settings:developers
    # Select Developer mode
    ```  
    ![Enable Developer Mode](https://cdn-images-1.medium.com/max/1600/1*_7TN03J1uZTo6VMyuNcbvQ.png)  
    Image by [Methus Kaewsaikao](https://medium.com/@methuz)
    * Share drive C: with Docker  
        * Open Docker settings
        * Goto Shared Drives
        * Select c and Apply  
    ![Share drive C](https://cdn-images-1.medium.com/max/1000/1*0VI5ra3uYZ1WGD3I19CPxQ.png)
    Image by [Methus Kaewsaikao](https://medium.com/@methuz)
    ```bash
    # From CMD:
    # Verify your host drive is shared
    docker run --rm -v c:/:/data alpine ls /data
    # Files should be shown
    ```
* HowTo: [Installing the development environment | Hyperledger Composer](https://hyperledger.github.io/composer/latest/installing/development-tools)
    ```bash
    # From CMD As Admin install
    npm install -g composer-cli@0.20
    composer -v
    # v0.20.2
    npm install -g composer-rest-server@0.20
    # install a hyperledger-composer generator for yoman
    npm install -g generator-hyperledger-composer@0.20
    npm install -g yo
    yo --version
    # 2.0.5
    npm install -g composer-playground@0.20
    composer-playground --version
    # 0.20.2
    # composer-playground opens http://localhost:8080/login
    # Read more on https://hyperledger.github.io/composer/latest/tutorials/playground-tutorial.html
    ```


* [Running Hyperledger Fabric on Windows - Revised - IBM OpenTech](https://developer.ibm.com/opentech/2017/11/29/running-hyperledger-fabric-windows-revised/)


* [https://raw.githubusercontent.com/hyperledger/fabric/master/scripts/bootstrap.sh](https://raw.githubusercontent.com/hyperledger/fabric/master/scripts/bootstrap.sh)





## Installing Hyperledger on Ubunto or Mac

* HowTo: [Installing pre-requisites | Hyperledger Composer](https://hyperledger.github.io/composer/latest/installing/installing-prereqs)

# Learning

## Blogs

* [Hyperledger Fabric - Are Channels Private Blockchain? (Deep Dive) - Reskilling IT](https://vitalflux.com/hyperledger-fabric-channels-private-blockchain-deep-dive/)

## Webinars

* [Webinars | Altoros](https://www.altoros.com/blog/events/?showcat=128)

The End
