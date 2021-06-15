Title: Using SSH keys - Connect to Ionic Pro
Status: published
Date: 2017-10-03 20:30
Modified: 2021-06-15 11:00
Category: Develop
Tags: #git, #ssh, #ionic

HowTo connect to Ionic Pro, when `ionic link` fails?  
*[Ionic Pro](https://ionicframework.com/docs/pro/){:target="_blank"} is a new site taking over the features from Ionic Cloud - a hosted mobile build, test and deploy service*

# Intro

### The problem

I wanted to connect to Ionic Pro from Windows.  
But the attempt failed.

It kept coming with one error after the other. The latest I had difficulty to pass was:

```bash
>ionic link
× Looking up your apps - failed!
Request: GET https://api.ionicjs.com/apps?page=1&page_size=25
Response: 401
Body:
{ type: 'Unauthorized', link: null, message: 'Invalid Token' }
```

This blog has a **workaround** for `ionic link`.

### ionic link

[`ionic link`](https://ionicframework.com/docs/cli/link/){:target="_blank"} CLI command connects your local git repo with a remote repo at Ionic Pro.
That remote repo was created when you manually created an app at [Ionic Pro](https://dashboard.ionicjs.com/apps){:target="_blank"} site.

It does that by doing probably all these tasks

1. creating a set of SSH keys, 
2. uploading the public key to Ionic Pro and
3. adding the app id to project-root\ionic.config.json
4. adding remote ionic repo to your local project

So when it won't we can do it ourselves.

# The workaround

### Prerequisites

* Create a ionic app in [Ionic Pro](https://dashboard.ionicjs.com){:target="_blank"}  
After creation the id of the app will be the last part of the url - e.g. as in https://apps.ionic.io/app/09faf85a
* Create a [ionic starter app](http://ionicframework.com/getting-started/){:target="_blank"} on your PC

### 1. Create a set of SSH keys

You need `ssh-keygen.exe` to generate a set of public/private SSH keys.
`ssh-keygen.exe` is installed as part of 

* Git (default installed into `C:\Program Files\Git\usr\bin`) or
* OpenSSH (default installed into `C:\Program Files\OpenSSH-Win64`)

On my PC I also had HerokuToolkit installed with a path in `ssh-keygen.bat` to `ssh-keygen.exe`.  
But this path was wrong. It seemed to be part of some problems. Rename that file, so it is not called instead of one of the real .exe files.

From Git bash:

```bash
# https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/

# Generate key-pair into C:\Users\your_userid\.ssh\
c:
cd C:/Users/your_userid/.ssh
# http://docs.ionic.io/services/ssh-keys/
ssh-keygen.exe -t rsa -b 4096 -C "your_email@example.com"

# Check if ssh agent is running
eval $(ssh-agent -s)
# Agent pid 12345 - yes

# Add private key to agent - 
ssh-add C:/Users/your_userid/.ssh/id_rsa
```

### 2. Upload the public key to Ionic Pro

Paste the content of file `id_rsa.pub` to a new key in [Ionic Pro's SSH store](https://dashboard.ionicjs.com/settings/ssh-keys){:target="_blank"}

### 3. Add the app id to your Ionic config in your local repo

Edit `project-root\ionic.config.json`

```yaml
{
  "name": "Your Magic App",
  "app_id": "09faf85a", # replace with your id
```

### 4. Add remote ionic repo to your local project

```bash
# https://dashboard.ionicjs.com/app/09faf85a/settings/git
# Add Ionic Pro as remote repo
git remote add ionic ssh://git@git.ionicjs.com:your_ionic_userid/your_ionic_appname.git
```

# After the workaround

### 5. Upload your app to Ionic Pro
```bash
# Upload to Ionic Pro
git push ionic master
```

### 6. Make Github your default remote repo

```bash
# Add github as remote repo
git remote add origin https://github.com/your_git_userid/your_git_appname.git
# Upload to github and set it default (for pull)
git push --set-upstream origin master
# Check your remotes
git remote -v
```

### 7. Continue to use Ionic Pro

On the url for your app - e.g. https://dashboard.ionicjs.com/app/09faf85a/code/builds/list you can continue to deploy, preview and more.

You might also need to modify `src/app/app.module.ts`. [Define a CloudSettings object](http://docs.ionic.io/setup.html#configuration){:target="_blank"}. 

-----------------------------

# Tips

### Download an app as a starter app

If you have access to a Ionic Pro app, you can `git clone` it with

```bash
ionic start --pro-id 09faf85a
```

... if I am asuming correct.

### If you want OpenSSH on Windows

.. then here is how you [install OpenSSH](https://github.com/PowerShell/Win32-OpenSSH/wiki/Win32-OpenSSH-Automated-Install-and-Upgrade-using-Chocolatey){:target="_blank"}

```bash
# do this from an admin prompt
choco install openssh # takes a while
# reload environment variables
refresh env
```

### If you want Git Bash to add your Github SSH key to an agent

[How to Setup SSH Authentication for Git Bash on Windows](https://dev.to/bsara/how-to-setup-ssh-authentication-for-git-bash-on-windows-a63)

### If you want Powershell to add your SSH key to an agent

[Setting up the SSH Agent](https://code.visualstudio.com/docs/remote/troubleshooting#_setting-up-the-ssh-agent)

```ps1
# PS1
# Make sure you're running as an Administrator
Set-Service ssh-agent -StartupType Automatic
Start-Service ssh-agent
Get-Service ssh-agent
# Add SSH private key to agent
ssh-add c:\users\<yourid>\.ssh\id_rsa
# Verity key added
ssh-add -l
```

# Links

* <http://ionicframework.com/docs/pro/basics/getting-started/>{:target="_blank"}
* <https://github.com/PowerShell/Win32-OpenSSH/wiki/ssh.exe-examples>{:target="_blank"}
* [How to Setup SSH Authentication for Git Bash on Windows](https://dev.to/bsara/how-to-setup-ssh-authentication-for-git-bash-on-windows-a63)
* Scripts: [Setup ssh auth on windows](https://gist.github.com/rasor/3970bf55838c0f53f77ba2e5f350ed66)
* [LinuxKubuntuInstall - Git](https://github.com/rasor/rasor.github.io/blob/pelican/content/2020/LinuxKubuntuInstall.md#git)

The End
