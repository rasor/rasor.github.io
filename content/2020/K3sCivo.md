Title: k3s hosted in Civo
Date: 2099-01-01 00:00
Category: DevOps
Tags: #k3s, #civo, #k8s

## Intro

[Civo](https://www.civo.com/features) offers a hosted k3s cluster with an app market: [civo/kubernetes-marketplace](https://github.com/civo/kubernetes-marketplace), like Arkade.

At time of writing Civo k8s is in beta. You can [apply](https://www.civo.com/kube100) for $70 monthly free service.

You can work with Civo from 
* Civo web via [https://www.civo.com/account/kubernetes](https://www.civo.com/account/kubernetes)
* [Civo CLI](https://www.civo.com/learn/kubernetes-cluster-administration-using-civo-cli) that you download from [Release v0.6.39 · civo/cli](https://github.com/civo/cli/releases/tag/v0.6.39)

From those you create a k8s cluster.  
Then you download the kubeconfig and continue work on that remote cluster via your local installed kubectl.  

## Prerequisites

You must have `kubectl` installed.  

## Get started

* First you [download civo cli](https://github.com/civo/cli/releases/tag/v0.6.39) and save it into `C:\Program Files\Civo`.  
* Next add that path to environment path.  
* Test civo:
```bash
# is civo reachable?
civo verision
# Civo CLI v0.6.39
```

Get [API key](https://www.civo.com/account/security)

```bash
# save API key into civo CLI
civo apikey add My_Api_Key DAb75oyqVeaE7BI6Aa74FaRSP0E2tMZXkDWLC9wNQdcpGfH51r
# Saved the API Key DAb75oyqVeaE7BI6Aa74FaRSP0E2tMZXkDWLC9wNQdcpGfH51r as My_Api_Key

# Set the key as current
civo apikey current My_Api_Key
# The current API Key is now My_Api_Key

# help me create a cluster
civo k8s create -h
# create a cluster and wait for it to finish
civo k8s create Cluster-1-just-dashboard --size=g2.xsmall --nodes=1 --wait -a=kubernetes-dashboard

# print kube config for the created cluster
civo k8s config Cluster-1-just-dashboard
# apiVersion: v1
# clusters:
# - cluster:
#   name: cluster-1-just-dashboard

# save (or merge) the config into your kubeconfig
civo k8s config Cluster-1-just-dashboard --save
# Saved config to ~/.kube/config

# print nodes and apps in your cluster
civo k8s show Cluster-1-just-dashboard
#           ID : 18779094-3e4e-4db5-85d4-6294c5ffffff
#         Name : Cluster-1-just-dashboard
#        Nodes : 1
#         Size : g2.xsmall
#       Status : ACTIVE
#      Version : 1.18.6+k3s1
# API Endpoint : https://91.211.144.244:6443
#    Master IP : 91.211.144.244
# DNS A record : 18779094-3e4e-4db5-85d4-6294c5ffffff.k8s.civo.com

# Nodes:
# +------------------+----+--------+-----------+-----------+------+----------+
# | Name             | IP | Status | Size      | Cpu Cores | Ram  | SSD disk |
# +------------------+----+--------+-----------+-----------+------+----------+
# | kube-master-5cbc |    | ACTIVE | g2.xsmall |         1 | 1024 |       25 |
# +------------------+----+--------+-----------+-----------+------+----------+
# Applications:
# +----------------------+---------+-----------+------------+
# | Name                 | Version | Installed | Category   |
# +----------------------+---------+-----------+------------+
# | kubernetes-dashboard | v2.0.0  | true      | management |
# +----------------------+---------+-----------+------------+
```

With the cluster up browse to  
https://www.civo.com/account/kubernetes/18779094-3e4e-4db5-85d4-6294c5ffffff  
and expand kubernetes-dashboard.
It will tell you howto connect:

```bash
# Get login token
kubectl -n kubernetes-dashboard describe secret admin-user-token | grep ^token
# get api access
kubectl proxy

# Open dashboard in browser
start http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/
# Signin and paste token
```

You can add more apps out of the box:  
```bash

# Print the apps you can install
civo k8s applications list
# +---------------------------+------------------+--------------+-----------------+-----------------------------+
# | Name                      | Version          | Category     | Plans           | Dependencies                |
# +---------------------------+------------------+--------------+-----------------+-----------------------------+
# | argo                      | (default)        | ci_cd        |                 |                             |
# | cert-manager              | v1.0.2           | architecture |                 | Helm                        |
# | docker-registry           | ALPHA            | architecture |                 | Helm, cert-manager, Traefik |
# | dynamic-pv-scaler         | 0.1.0            | storage      |                 | prometheus-operator         |
# | Ghost                     | 3.35.5           | management   | 5GB, 10GB, 15GB | longhorn                    |
# | gitea                     | 1.12.5           | management   |                 |                             |
# | haproxy                   | 1.4.6            | architecture |                 |                             |
# | Helm                      | 2.16.5           | management   |                 |                             |
# | Jaeger-Operator           | 1.2.0            | monitoring   |                 |                             |
# | Jenkins                   | 2.190.1          | ci_cd        | 5GB, 10GB, 20GB | Longhorn                    |
# | keptn                     | 0.7.1            | ci_cd        |                 |                             |
# | kube-hunter               | latest           | security     |                 |                             |
# | kube-scan                 | v20.5            | security     |                 |                             |
# | KubeDB                    | v0.12.0-r1       | database     |                 | Longhorn                    |
# | Kubei                     | 1.0.7            | security     |                 |                             |
# | Kubeless                  | 1.0.5            | architecture |                 |                             |
# | kubernetes-dashboard      | v2.0.0           | management   |                 |                             |
# | Linkerd                   | Latest           | architecture |                 |                             |
# | loki-stack                | v0.41.2          | monitoring   |                 | prometheus-operator         |
# | Longhorn                  | 1.0.2            | storage      |                 |                             |
# | Maesh                     | Latest           | architecture |                 | Helm                        |
# | MariaDB                   | 10.4.7           | database     | 5GB, 10GB, 20GB | Longhorn                    |
# | metrics-server            | (default)        | architecture |                 |                             |
# | MinIO                     | 2019-08-29       | storage      | 5GB, 10GB, 20GB | Longhorn                    |
# | MongoDB                   | 4.2.0            | database     | 5GB, 10GB, 20GB | Longhorn                    |
# | Netdata                   | Latest           | monitoring   |                 | Helm                        |
# | Nginx                     | latest           | architecture |                 |                             |
# | OpenFaaS                  | 0.18.0           | architecture |                 | Helm                        |
# | permission-manager        | 1.6.0            | management   |                 |                             |
# | Polaris                   | 1.2.0            | security     |                 |                             |
# | Portainer                 | ce               | management   |                 |                             |
# | PostgreSQL                |             11.5 | database     | 5GB, 10GB, 20GB | Longhorn                    |
# | prometheus-operator       | 0.35.0           | monitoring   |                 |                             |
# | RabbitMQ                  | 3.8.8-management | architecture |                 |                             |
# | Rancher                   | v2.5.0           | management   |                 |                             |
# | Redis                     |              3.2 | database     |                 |                             |
# | sealed-secrets            | v0.12.4          | architecture |                 |                             |
# | Selenium                  | 3.141.59-r1      | ci_cd        |                 |                             |
# | system-upgrade-controller | v0.6.2           | architecture |                 |                             |
# | Tekton                    | v0.17.0          | ci_cd        |                 |                             |
# | Traefik                   | (default)        | architecture |                 |                             |
# | Traefik-v2                |              2.3 | architecture |                 |                             |
# | Wordpress                 | 5.5.1            | management   | 5GB, 10GB, 20GB | longhorn, mariadb:5GB       |
# +---------------------------+------------------+--------------+-----------------+-----------------------------+

civo kubernetes applications add PostgreSQL --cluster=Cluster-1-just-dashboard
# You requested to add PostgreSQL but didn't select a plan. Please choose one... (5GB, 10GB, 20GB) [5GB]: 5GB
# Thank you, next time you could use "PostgreSQL:5GB" to choose automatically
# Added PostgreSQL 11.5 to Kubernetes cluster Cluster-1-just-dashboard

```

And finally - tear down and stop costs:  
```bash
# Delete cluster
civo kubernetes remove Cluster-1-just-dashboard
# The Kubernetes cluster called Cluster-1-just-dashboard with ID 18779094-3e4e-4db5-85d4-6294c5ffffff was deleted
```

## Links

* Learn
    * [Learn](https://www.civo.com/learn)
    * [Civo Kubernetes Quick Start Guide](https://www.civo.com/learn/civo-kubernetes-quick-start-guide)
    * [Kubernetes Cluster Administration Using Civo CLI](https://www.civo.com/learn/kubernetes-cluster-administration-using-civo-cli)
    * [What’s the difference between k3s vs k8s](https://www.civo.com/blog/k8s-vs-k3s)
* Signup
    * Apply: [Join the world’s first managed k3s Kubernetes service](https://www.civo.com/kube100)
    * Operate: [https://www.civo.com/account](https://www.civo.com/account)
    * [kubernetes-marketplace](https://github.com/civo/kubernetes-marketplace)
    * Incidents: [Civo Status](http://status.civo.com/)
    * email: info@civo.com
* Deploy
    * [Deploy OpenFaaS with k3s on Civo – Civo.com](https://www.civo.com/learn/deploy-openfaas-with-k3s-on-civo)
* Develop
    * [Civo Cloud API Documentation - Civo.com](https://www.civo.com/api)
* Rancher
    * [K3s: Lightweight Kubernetes](https://k3s.io/)
    * Persistent volumes: [longhorn](https://github.com/longhorn/longhorn)
    * [Quick Start](https://rancher.com/quick-start/)
    * Training: [Kubernetes Online Master Class Series](https://rancher.com/kubernetes-master-class)
        * [Kubernetes Master Class: Cluster Monitoring with Prometheus, Grafana and Alertmanager in Rancher 2.5 - Oct 27](https://info.rancher.com/kubernetes-master-class-oct27-2020)
    * [All Things Open](https://allthingsopen.6connex.com/event/ATO/en-us/?mcc=ato-day-8am#!/RancherBooth)

The End
