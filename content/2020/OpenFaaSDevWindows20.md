Title:  OpenFaaS on Windows Devbox - k8s
Date: 2099-01-01 00:00
Category: Develop
Tags: #arkade, #docker, #kubernetes, #openfaas, #curl, #hyperv, #virtualbox, #kitematic, #wsl2, #win10, #virtualmachineplatform

I want to install **OpenFaaS** again.  
This time running on **Kubernetes (k8s)**, **Docker Desktop**, **Windows Home 10** with **Virtual Machine Platform** on **WSL2**.  
Running Docker Desktop with [WSL2 backend has many improvements](https://docs.docker.com/docker-for-windows/wsl/) over alternatives.  
Last time I installed Docker (in this [blog](https://rasor.github.io/openfaas-on-windows-devbox.html)), I was running on **Docker Swarm**, **Docker CE**, **Windows Pro 10** and **Hyper-V**.

[@alexellisuk](https://twitter.com/alexellisuk) has build yet a great tool. One being [Arkade](https://github.com/alexellis/arkade).  
It is great for installing lots of K8s goodies both locally and in cloud. I also includes OpenFaaS.

## Arkade
Your one-stop CLI for Kubernetes

### Install on devbox on Windows

#### Prerequisites.

You need Docker. Start by typing    
```bash
docker -v
```  
to see if you already have it installed.  
If not then follow [this tutorial to get it](Docker4Win20.md).  
In that blog I ended up with **Docker Desktop** on **Windows Home 10** with **Virtual Machine Platform** incl. **WSL2**.

### K8S

Now that we have Docker, then it is time to play with Arkade to install k8s and other stuff

But there are other options than **Arkade** to install k8s?
* On localhost
    * Using **Kind**
        * [Installing Kubernetes with Kind](https://kubernetes.io/docs/setup/learning-environment/kind/)
    * Using **Minikube**
        * [Install Minikube](https://kubernetes.io/docs/tasks/tools/install-minikube/)
        * [Installing Kubernetes with Minikube](https://kubernetes.io/docs/setup/learning-environment/minikube/)
    * Enable k8s in **Docker Desktop**
* In cloud
    * All cloud providers have their own k8s services

So why use Arkade to install k8s?
* If you only need a single node cluster then option 3 - using **Docker Desktop** automates the work you manually can do with **Minikube**.  
* If you need a multi node cluster then option 0 - using **Arkade** automates the work you manually can do with **Kind**.  
* **Arkade** also automates the work you need to do with other k8s related tools.

#### Already have a k8s cluster?

k8s install is only the top of the iceberg of Arkade.  
If you already have a k8s cluster then Arkade kicks in by installing lost of 
* k8s apps from e.g. [Helm Hub](https://hub.helm.sh/) (with `ark install`) and/or
* CLIs for k8s or apps (with `ark get`) 

Arkade then __unifies fetching packages__ across platforms. Before:
* `apt-get` on some Linux versions
* `yum` on some other Linux versions
* `choco` on Windows
* `brew` on Mac

Under the hood Arkade __simplifies commands__ by using [Helm](https://helm.sh/) as the k8s package manager and `kubectl` commands.

#### Install Arkade

```bash
# Check that curl is installed
curl --version
# curl 7.67.0 (x86_64-w64-mingw32) libcurl/7.67.0 OpenSSL/1.1.1d (Schannel) zlib/1.2.11 libidn2/2.3.0 nghttp2/1.39.2
# Release-Date: 2019-11-06
# Protocols: dict file ftp ftps gopher http https imap imaps ldap ldaps pop3 pop3s rtsp smtp smtps telnet tftp
# Features: AsynchDNS HTTP2 HTTPS-proxy IDN IPv6 Kerberos Largefile libz Metalink MultiSSL NTLM SPNEGO SSL SSPI TLS-SRP

# Check that docker is installed
docker -v
# Docker version 19.03.12, build 48a66213fe

# Check that a k8s cluster is not yet installed
kubectl version
# Client Version: version.Info{Major:"1", Minor:"16+", GitVersion:"v1.16.6-beta.0", GitCommit:"e7f962ba86f4ce7033828210ca3556393c377bcc", GitTreeState:"clean", BuildDate:"2020-01-15T08:26:26Z", GoVersion:"go1.13.5", Compiler:"gc", Platform:"windows/amd64"}
# Unable to connect to the server: dial tcp [::1]:8080: connectex: No connection could be made because the target machine actively refused it.

# Check that arkade is not installed
arkade --help
# bash: arkade: command not found

# Install Arkade on Windows
# https://github.com/alexellis/arkade#get-arkade
curl -sLS https://dl.get-arkade.dev | sh
# Downloading package https://github.com/alexellis/arkade/releases/download/0.6.12/arkade.exe as //arkade.exe
# curl: (23) Failed writing body (0 != 16360)

# Trying as-admin
curl -sLS https://dl.get-arkade.dev | sh
# Downloading package https://github.com/alexellis/arkade/releases/download/0.6.12/arkade.exe as //arkade.exe
# chmod: cannot access '//arkade.exe': No such file or directory
# Download complete.

# Running with sufficient permissions to attempt to move arkade to /c/Users/Soren/bin
# mv: cannot stat '//arkade.exe': No such file or directory
# ln: failed to create symbolic link '/c/Users/Soren/bin/ark': No such file or directory
# Creating alias 'ark' for 'arkade'.
# main: line 172: arkade: command not found

```

Both attemps failed - instead get manual recipe: [get.sh](https://raw.githubusercontent.com/alexellis/arkade/master/get.sh)  
1. Open your web browser and go to https://github.com/alexellis/arkade/releases
2. Download the latest release for windows to C:\Users\yourusername\.arkade\bin\arkade`
3. Add path to environment  
```cmd
setx PATH "%path%;C:\Users\yourusername\.arkade\bin"
```
4. Create a symbolic link
```bash
export ALIAS_NAME="ark"
export REPO=arkade
export BINLOCATION="/c/users/yourusername/.arkade/bin"
chmod +x "$BINLOCATION/$REPO"
ln -sf "$BINLOCATION/$REPO" "$BINLOCATION/$ALIAS_NAME"
```

#### Install k8s cluster

```bash
arkade get kubectl
# Downloading kubectl
# https://storage.googleapis.com/kubernetes-release/release/v1.18.0/bin/windows/amd64/kubectl.exe
# Tool written to: C:\Users\yourusername/.arkade/bin/kubectl.exe

arkade get kind
# Downloading kind
# https://github.com/kubernetes-sigs/kind/releases/download/v0.9.0/kind-windows-amd64
# Tool written to: C:\Users\yourusername/.arkade/bin/kind.exe
kind --version
# kind version 0.9.0

kind create cluster
# Creating cluster "kind" ...
#  • Ensuring node image (kindest/node:v1.19.1) 🖼  ...
#  ✓ Ensuring node image (kindest/node:v1.19.1) 🖼
#  • Preparing nodes 📦   ...
#  ✓ Preparing nodes 📦
#  • Writing configuration 📜  ...
#  ✓ Writing configuration 📜
#  • Starting control-plane 🕹️  ...
#  ✓ Starting control-plane 🕹️
#  • Installing CNI 🔌  ...
#  ✓ Installing CNI 🔌
#  • Installing StorageClass 💾  ...
#  ✓ Installing StorageClass 💾
# Set kubectl context to "kind-kind"
# You can now use your cluster with:
kubectl cluster-info --context kind-kind
# Kubernetes master is running at https://127.0.0.1:54040
# KubeDNS is running at https://127.0.0.1:54040/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy
# To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
```

## Links

* [Deploy on Kubernetes](https://docs.docker.com/docker-for-windows/kubernetes/)
* [OpenFaaS on Windows Devbox](https://rasor.github.io/openfaas-on-windows-devbox.html)
* [alexellis/arkade](https://github.com/alexellis/arkade)
    * [Alex Ellis - arkade](https://www.linkedin.com/posts/alexellisuk_kubernetes-cloudnative-cncf-activity-6702550586610487296-atGD)
    * Vid 2020: [Walk-through of arkade - for Kubernetes](https://www.youtube.com/watch?v=8wU9s_mua8M)
* [Kubernetes - OpenFaaS](https://docs.openfaas.com/deployment/kubernetes/)
* Vid 2017: [Create a 2-node Kubernetes cluster in 10 minutes](https://www.youtube.com/watch?v=6xJwQgDnMFE)

* [Alex Ellis posted on LinkedIn](https://www.linkedin.com/posts/alexellisuk_then-he-asked-me-is-kubernetes-right-for-activity-6703625976351346688-6343)

The End
