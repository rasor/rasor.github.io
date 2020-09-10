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

But there are other options than **Arkade**:
* On localhost
    * Using **Kind**
        * [Installing Kubernetes with Kind](https://kubernetes.io/docs/setup/learning-environment/kind/)
    * Using **Minikube**
        * [Install Minikube](https://kubernetes.io/docs/tasks/tools/install-minikube/)
        * [Installing Kubernetes with Minikube](https://kubernetes.io/docs/setup/learning-environment/minikube/)
    * Enable k8s in **Docker Desktop**
* In cloud
    * All cloud providers have their own k8s services

So why use Arkade?
* If you only need a single node cluster then option 3 - using **Docker Desktop** automates the work you manually can do with **Minikube**.  
* If you need a multi node cluster then option 0 - using **Arkade** automates the work you manually can do with **Kind**.  
* **Arkade** also automates the work you need to do with other k8s related tools.

In short - it is a time- and money saver for DevOps workflows you need in production environments.  
So is Arkade worthwhile to use in dev envir?  
You'll be the judge for your own needs.  

#### Install Arkade





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
