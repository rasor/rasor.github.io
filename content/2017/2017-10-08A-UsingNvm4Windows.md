Title: Using NVM for Windows and Yarn
Status: published
Date: 2017-10-08 11:00
Modified: 2021-06-15 11:00
Category: DevOps
Tags: #nvm, #nodejs, #npm, #yarn, #chocolatay, #symlink

Microsoft created Taco (Tools for Apache Cordova) - a set of Node.js tools with specific versions. It was to be used from within Visual Studio, so they knew what was global in their Cordova apps.
I blogged about it [here](https://rasor.wordpress.com/2017/03/13/ionic-in-visual-studio-2017/){:target="_blank"}

With Nvm For Windows you can stay in the shell and select yourself what you want to include in your set.

I need it to be able to switch between Node v6 and Node v8.
In my usecase there is v6 installed on a host (Azure), so I also need v6 locally for debugging.
And when not debugging for prod I can use newest v8.

## Using [nvm4windows](https://github.com/coreybutler/nvm-windows){:target="_blank"}

### Before you install nvm4windows you need to 

* uninstall node
* Delete folder C:\Program Files\nodejs
* Delete folder C:\Users\username\AppData\Roaming\npm
* Delete folder C:\Users\username\AppData\Roaming\npm-cache
* Remove envir var %NODE_ENV%
* Remove part of %path% C:\Users\username\AppData\Roaming\npm

### Download, install and use [nvm4windows](https://github.com/coreybutler/nvm-windows/releases){:target="_blank"}

* `nvm list` # shows nothing installed
* goto [Node downloads](https://nodejs.org/en/download/){:target="_blank"} and 
    * checkout LTS version - currently 6.11.4 (includes npm 3.10.10)
    * checkout current version - currently 8.6.0 (includes npm 5.3.0)
* Install the two versions:
```bash
nvm install 6.11.4 # Installs into \nvm\v6.11.4
nvm install 8.6.0 # Installs into \nvm\v8.6.0
nvm list

#    8.6.0
#    6.11.4

nvm use 8.6.0 # Creates a shortcut \nodejs\ pointing to the above \vx.x.x\ folder
# Now using node v8.6.0 (64-bit)
```

The shortcut \nodejs\ is also saved as %NVM_SYMLINK% and saved to %path%

```bash
nvm list

#  * 8.6.0 (Currently using 64-bit executable)
#    6.11.4
```

You need to `npm install -g` (globally install js libs into each of the nodejs versions you are using) e.g. `npm install -g cordova`.

Note

* Cli tools (e.g. cordova) are installed in `%ProgramFiles%\nodejs`, which might not be the path you chose for node.  
If not you need to add `%ProgramFiles%\nodejs` to `%path%`
* node_modules are scattered around the disk(s)
    * `C:\Users\username\AppData\Roaming\npm-cache`
    * Nvm path `%NVM_HOME%\vx.x.x\node_modules\npm\node_modules`
    * Nvm Nodejs paths `%NVM_SYMLINK%\node_modules`
    * Normal Nodejs paths `%ProgramFiles%\nodejs\node_modules` - CLI's installed with -g
    * and locally in project subfolder `\node_modules`

Well it seems like installation of nvm must be done to the default paths, since in the setup on my PC -g installs still ends up in a common place. I'll have to test that on another occation.

You might also need to set environment variable (for Express?):
`NODE_ENV=%NVM_SYMLINK%` and `refreshenv`

### Using nvm for multiple users

If you have two users on one PC that wants to use nvm then you must make some workaround for the symbolic link under program files.  

For the first user you would have 

```ini
# User1
# PrintEnv # from bash
# Set # from CMD
NVM_HOME=C:\Users\user1\AppData\Roaming\nvm
NVM_SYMLINK=C:\Program Files\nodejs
```

For user 2 you should make some local environment settings with these values

```ini
# User2
# PrintEnv # from bash
# Set # from CMD
NVM_HOME=C:\Users\user2\AppData\Roaming\nvm
NVM_SYMLINK=C:\Program Files\nodejs-user2
```

Then install nvm for user 2.

When you do `nvm install 8.6.0` it should install node under `NVM_HOME`.  
When you do `nvm use 8.6.0` it should add a symlink named `nodejs-user2` under `C:\Program Files` pointing to the selected node version under `NVM_HOME`.  

If it does not work out you can also create the symlink from gitbash: 

```bash
# bash
# Create a symnlink called nodejs-user2
cd /C/'Program Files'
export MSYS=winsymlinks:nativestrict
ln -s /C/Users/user2/AppData/Roaming/nvm/v8.6.0 nodejs-user2
```

## Using Yarn

The npm v5 coming with node v8 has a package.lock file - yes idea taken from Yarn. Meaning we don't need Yarn anymore - unless you need other features from Yarn.  
For npm v3 (node v6) we often need yarn.lock.

We need the lock file to keep track of all exact versions of dependencies in a project.

### Install Yarn

* [Download Yarn](https://yarnpkg.com/en/docs/install){:target="_blank"}
* Install [Chocolatey](https://chocolatey.org/install){:target="_blank"}
* Install Yarn 

```bash
nvm use 6.11.4 # yarn checks for npm
choco install yarn
yarn -v
#1.1.0
```

### Using Yarn

#### When starting from empty project

```bash
yarn init # create the yarn.lock file and a package.json
yarn add [package] # same as npm -install -save [package]
yarn add [package] --dev # same as npm -install --save-dev [package]
```

#### When starting from a working npm project

```bash
yarn import # create the yarn.lock file from node_modules folder
```
If it fails with `error An unexpected error occurred: "should have a resolved reference"`  
then it might work to just issue `yarn`.

#### When starting from a cloned npm project having yarn.lock

```bash
git clone "https://github.com/....."
yarn install # same as npm install, but using yarn.lock: download modules
```

#### When upgrading existing package in package.json

```bash
yarn upgrade [package]@latest # same as npm update [package]@latest, but using yarn.lock
```

-------------

## Links

* [Yarn usage](https://yarnpkg.com/en/docs/usage){:target="_blank"}
* [Npm vs. Yarn](https://yarnpkg.com/en/docs/migrating-from-npm){:target="_blank"}
* [Yarn commands](https://yarnpkg.com/en/docs/cli/){:target="_blank"}
* [Npm commands](https://docs.npmjs.com/cli){:target="_blank"}
* [Awesome CLI - on Windows - Chocolatey](https://github.com/rasor/awesome-tables/blob/master/awesome-cli-on-windows.md#chocolatey){:target="_blank"}

The End
