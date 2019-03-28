Title:  OpenFaaS Cloud app
Date: 2099-01-01 00:00
Category: Develop
Tags: #openfaas

# Running OpenFaas in Dev

Finally the time has arrived, when I'll start using [OpenFaas](https://www.openfaas.com/).  
I first heard about OpenFaaS at a meetup in May 2018, [6 Cloud Native Talks, 1 Evening: Special KubeCon + CloudNativeCon EU Meetup!](https://www.meetup.com/GOTO-Nights-CPH/events/249895973/) by OpenFaaS creator, [Alex Ellis](https://github.com/alexellis).  
Next I bought the book [Docker for Serverless Applications](https://www.packtpub.com/virtualization-and-cloud/docker-serverless-applications) (D4S) by [Chanwit Kaewkasi](https://github.com/chanwit), but only skimmed it. I highly recommed it!  
Now it is time to practice.

## Why? - OpenFaaS vs Cloud Native Serverless

[But how about](https://twitter.com/rasor/status/1111244201738620928)

* Why not just use cloud native serverless?
    * When you don't want the auto-kill feature.
    * When you want serverless in you dev box
* You don't get pay-per-invocation?
    * No you have to deploy a #k8s or #docker_swarm cluster. This can be as cheap by using #spot_instance s. @chanwits teach you how to do that.
* You don't get seemless integration with cloud native services?
    * No - but aren't you used to that when you integrate to the services from your dev box?

## How?

You can run OpenFaaS either on top of Kubernetes (k8s) or Docker Swarm.  

### Production

For deploying to OpenFaaS to a **cloud container cluster** there are some good guides on **k8s** like [ofc-bootstrap](https://github.com/openfaas-incubator/ofc-bootstrap). I guess you are managing the cluster here.  

But there is a great guide in the D4S book chapter 7, where Chanwit uses **AWS spot instances** for running **Swarm** worker nodes. This solution can keep the price as low as Native Serverles, Chanwit claims. The challenge with spot instances is that you have to restart nodes, when they are marked for termination.  
In this guide you are managing the cluster.  
Chanwits [code is here](https://github.com/PacktPublishing/Docker-for-Serverless-Applications/tree/master/ch_operating).

But OpenFaaS has build-in scaling and monitoring, so the managing part is limited.  

### Development

For local deployment there are guides, too.

In the D4S book chapter 4 teaches you to deploy OpenFaaS on Swarm.  
Chanwits [code is here](https://github.com/PacktPublishing/Docker-for-Serverless-Applications/tree/master/ch_openfaas).

* Swarm: [Docker Swarm - OpenFaaS](https://docs.openfaas.com/deployment/docker-swarm/)
* k8s: [Kubernetes - OpenFaaS](https://docs.openfaas.com/deployment/kubernetes/)
* D4W + k8s: [Run your own FaaS with OpenFaas and .Net Core](https://secanablog.wordpress.com/2018/06/10/run-your-own-faas-with-openfaas-and-net-core/)

Other

* [openfaas/workshop](https://github.com/openfaas/workshop)
* CLI
    * [Installation - OpenFaaS](https://docs.openfaas.com/cli/install/)
    * [openfaas/faas-cli](https://github.com/openfaas/faas-cli)
* docker-machine
    * [docker/machine](https://github.com/docker/machine)
    * [Running OpenFaaS on Windows 10 - using Docker Swarm on Hyper-V](https://gist.github.com/johnmccabe/55baab605c0fb82df9c1cbf8c3dde407)

## Practice

I'll select **Windows + Docker for Windows (D4W) + Hyper-V + Swarm**.  
On a Windows laptop you can run D4W on VirtualBox or Hyper-V hypervisor. I'll choose Hyper-V, since that was what I [used previously](https://rasor.github.io/docker-for-windows.html). Using [Kitematic](https://kitematic.com/) you should be able to _swap from Hyper-V to VirtualBox_.  
My reason for choosing Swarm is that I think it is easier to getting started with. In D4W kubernetes settings you can _change from k8s to Swarm_ `docker stack` commands - this is configured in `~\.docker\config.json`.  

# Links

## OpenFaaS Cloud app

* [How to build a Serverless Single Page App](https://www.openfaas.com/blog/serverless-single-page-app/)
    * [alexellis/leaderboard-app](https://github.com/alexellis/leaderboard-app)
    * [openfaas-incubator/openfaas-sinatra-guestbook](https://github.com/openfaas-incubator/openfaas-sinatra-guestbook)
* Deploy: [openfaas/openfaas-cloud](https://github.com/openfaas/openfaas-cloud#get-started)
    * One-Click install on k8s cluster: [openfaas-incubator/ofc-bootstrap](https://github.com/openfaas-incubator/ofc-bootstrap) - watch vid!
        * [OpenFaaS Cloud in 100 seconds](https://www.youtube.com/watch?v=Sa1VBSfVpK0)
        * [Get your own OpenFaaS Cloud in 1 minute](https://www.youtube.com/watch?v=J9xoNf9yZ60)
        * [Create a 2-node Kubernetes cluster in 10 minutes](https://www.youtube.com/watch?v=6xJwQgDnMFE)
    * Manual install: [openfaas/openfaas-cloud](https://github.com/openfaas/openfaas-cloud/blob/master/docs/README.md)
    * Deploy docs: [Deployment - OpenFaaS](https://docs.openfaas.com/deployment/)
        * Swarm cluster is good for dev: [Docker Swarm - OpenFaaS](https://docs.openfaas.com/deployment/docker-swarm/)
        * [Running OpenFaaS on Windows 10 - using Docker Swarm on Hyper-V](https://gist.github.com/johnmccabe/55baab605c0fb82df9c1cbf8c3dde407)
            * Using [docker/machine](https://github.com/docker/machine)
        * [Run your own FaaS with OpenFaas and .Net Core](https://secanablog.wordpress.com/2018/06/10/run-your-own-faas-with-openfaas-and-net-core/)
    * FaaS-Cli: [openfaas/faas-cli](https://github.com/openfaas/faas-cli)
        * [Download faas-cli.exe](https://github.com/openfaas/faas-cli/releases/) to e.g. c:\Program Files\OpenFaaS\ and put it in path
    * [OpenFaaS on OpenShift - Red Hat OpenShift Blog](https://blog.openshift.com/openfaas-on-openshift/)
    * Uses [moby/buildkit](https://github.com/moby/buildkit)
* [openfaas/workshop](https://github.com/openfaas/workshop)
* My own blogs
    * [Docker](https://rasor.github.io/tag/docker.html)
    * [Kubernetes](https://rasor.github.io/tag/kubernetes.html)

### Cloud IaaS container cluster hosts

* [DigitalOcean](https://www.digitalocean.com/)
* AWS
* Azure
* GCP
* [Deploying with Docker | Heroku Dev Center](https://devcenter.heroku.com/categories/deploying-with-docker)

## More Links

* [Docker Secrets in action: Github integration](https://blog.alexellis.io/swarm-secrets-in-action/)
* [ngrok - secure introspectable tunnels to localhost](https://ngrok.com/)

## Books

* 2018-04: [Docker for Serverless Applications | PACKT Books](https://www.packtpub.com/virtualization-and-cloud/docker-serverless-applications)

The End