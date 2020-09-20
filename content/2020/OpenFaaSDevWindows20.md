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
        * [kind Quick Start](https://kind.sigs.k8s.io/docs/user/quick-start/)
    * Using **Rancher**
    * Using **k3d**
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

arkade version
#             _             _
#   __ _ _ __| | ____ _  __| | ___
#  / _` | '__| |/ / _` |/ _` |/ _ \
# | (_| | |  |   < (_| | (_| |  __/
#  \__,_|_|  |_|\_\__,_|\__,_|\___|
# Get Kubernetes apps the easy way
# Version: 0.6.12
# Git Commit: 0415b5fa9d0a6740feb3d9093b7555d38c7e1a51

ark get --help
# The get command downloads a CLI or application from the specific tool's releases or downloads page. 
# The tool is usually downloaded in binary format and provides a fast and easy alternative to a package manager.

# Usage:
#   arkade get [flags]

# Examples:
#   arkade get helm
#   arkade get linkerd2 --stash=false

# See which CLIs arkade can install:
ark get
# Use "arkade get TOOL" to download a tool or application:
# faas-cli
# helm
# kubectl
# kubectx
# kind
# k3d
# k3sup
# kubeseal
# inletsctl
# osm
# linkerd2
# kubebuilder
# kustomize
# doctl
# k9s
# civo
# terraform
```

#### Install k8s cluster

```bash
arkade get kubectl
# Downloading kubectl
# https://storage.googleapis.com/kubernetes-release/release/v1.18.0/bin/windows/amd64/kubectl.exe
# Tool written to: C:\Users\yourusername/.arkade/bin/kubectl.exe

# We will use kind to create a k8s cluster, but first install it:
arkade get kind
# Downloading kind
# https://github.com/kubernetes-sigs/kind/releases/download/v0.9.0/kind-windows-amd64
# Tool written to: C:\Users\yourusername/.arkade/bin/kind.exe
kind version
# kind v0.9.0 go1.15.2 windows/amd64

# Crate a k8s cluster:
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
# Kubernetes master is running at https://127.0.0.1:52295
# KubeDNS is running at https://127.0.0.1:52295/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy
# To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.

# And what is the name of cluster?
kind get clusters
# kind

# If you need to delete your cluster:
# kind delete cluster
# kind delete cluster --name kind

# Seems like I have a client version from docker and a server version is in the cluster with the version installed by arkade.
kubectl version
# Client Version: version.Info{Major:"1", Minor:"16+", GitVersion:"v1.16.6-beta.0", GitCommit:"e7f962ba86f4ce7033828210ca3556393c377bcc", GitTreeState:"clean", BuildDate:"2020-01-15T08:26:26Z", GoVersion:"go1.13.5", Compiler:"gc", Platform:"windows/amd64"}
# Server Version: version.Info{Major:"1", Minor:"19", GitVersion:"v1.19.1", GitCommit:"206bcadf021e76c27513500ca24182692aabd17e", GitTreeState:"clean", BuildDate:"2020-09-14T07:30:52Z", GoVersion:"go1.15", Compiler:"gc", Platform:"linux/amd64"}

# Check cluster location and credentials that kubectl knows about:
kubectl config view
# apiVersion: v1
# clusters:
# - cluster:
#     certificate-authority-data: DATA+OMITTED
#     server: https://127.0.0.1:52295
#   name: kind-kind
# contexts:
# - context:
#     cluster: kind-kind
#     user: kind-kind
#   name: kind-kind
# current-context: kind-kind
# kind: Config
# preferences: {}
# users:
# - name: kind-kind
#   user:
#     client-certificate-data: REDACTED
#     client-key-data: REDACTED

kubectl get nodes
# NAME                 STATUS   ROLES    AGE   VERSION
# kind-control-plane   Ready    master   18m   v1.19.1

kubectl get pods
# No resources found in default namespace.
```

So now having a master node running and no pod what is next?  

Issues: 
* Booting Windows made bash unable to access cluster. Why?
    * It was not an envir var problem, since after delete + create cluster then no new envir vars were created
    * In vid [Walk-through of arkade - for Kubernetes](https://www.youtube.com/watch?v=8wU9s_mua8M), Alex think boot persistence has been implemented - and before we had to recreate cluster after boot.
    * Tips about accessing clusters: [Accessing Clusters](https://kubernetes.io/docs/tasks/access-application-cluster/access-cluster/)

#### Install k8s apps

```bash
# Check which apps arkade lets you easily install:
ark install --help
# Install Kubernetes apps from helm charts or YAML files using the "install" command.

# You can also find the post-install message for each app with the "info" command.

# Usage:
#   arkade install [flags]
#   arkade install [command]

# Examples:
#   arkade install
#   arkade install openfaas  --gateways=2
#   arkade install inlets-operator --token-file $HOME/do-token

# Available Commands:
#   argocd                  Install argocd
#   cert-manager            Install cert-manager
#   chart                   Install the specified helm chart
#   cron-connector          Install cron-connector for OpenFaaS
#   crossplane              Install Crossplane
#   docker-registry         Install a Docker registry
#   docker-registry-ingress Install registry ingress with TLS
#   gitea                   Install gitea
#   grafana                 Install grafana
#   info                    Find info about a Kubernetes app
#   ingress-nginx           Install ingress-nginx
#   inlets-operator         Install inlets-operator
#   istio                   Install istio
#   jenkins                 Install jenkins
#   kafka-connector         Install kafka-connector for OpenFaaS
#   kube-image-prefetch     Install kube-image-prefetch
#   kube-state-metrics      Install kube-state-metrics
#   kubernetes-dashboard    Install kubernetes-dashboard
#   linkerd                 Install linkerd
#   loki                    Install Loki for monitoring and tracing
#   metrics-server          Install metrics-server
#   minio                   Install minio
#   mongodb                 Install mongodb
#   nats-connector          Install OpenFaaS connector for NATS
#   nfs-client-provisioner  Install nfs client provisioner
#   openfaas                Install openfaas
#   openfaas-ingress        Install openfaas ingress with TLS
#   openfaas-loki           Install Loki-OpenFaaS and Configure Loki logs provider for OpenFaaS
#   osm                     Install osm
#   portainer               Install portainer to visualise and manage containers
#   postgresql              Install postgresql
#   redis                   Install redis
#   registry-creds          Install registry-creds
#   tekton                  Install Tekton pipelines and dashboard
#   traefik2                Install traefik2

# Flags:
#   -h, --help                help for install
#       --kubeconfig string   Local path for your kubeconfig file (default "kubeconfig")
#       --wait                If we should wait for the resource to be ready before returning (helm3 only, default false)

```

## Links

* [Deploy on Kubernetes](https://docs.docker.com/docker-for-windows/kubernetes/)
* [kubectl Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)
* [OpenFaaS on Windows Devbox](https://rasor.github.io/openfaas-on-windows-devbox.html)
* [alexellis/arkade](https://github.com/alexellis/arkade)
    * [Alex Ellis - arkade](https://www.linkedin.com/posts/alexellisuk_kubernetes-cloudnative-cncf-activity-6702550586610487296-atGD)
    * Vid 2020: [Walk-through of arkade - for Kubernetes](https://www.youtube.com/watch?v=8wU9s_mua8M)
* [Kubernetes - OpenFaaS](https://docs.openfaas.com/deployment/kubernetes/)
* Vid 2017: [Create a 2-node Kubernetes cluster in 10 minutes](https://www.youtube.com/watch?v=6xJwQgDnMFE)

* [Alex Ellis posted on LinkedIn](https://www.linkedin.com/posts/alexellisuk_then-he-asked-me-is-kubernetes-right-for-activity-6703625976351346688-6343)

The End
