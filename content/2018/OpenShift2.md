Title: Developing with OpenShift
Date: 2099-01-01 00:00
Category: DevOp
Tags: #openshift, #docker, #kubernetes, #redhat, #paas, #virtualbox, #ansible, #dockerswarm

This a blog in 2 parts

* Part 1: [Developing with OpenShift](https://rasor.github.io/developing-with-openshift.html)
* Part 2: [Developing with OpenShift Part 2](https://rasor.github.io/developing-with-openshift-part-2.html) (this blog)

In part 1 a local PaaS box called MiniShift was installed and started with the script [shiftcli.sh](https://gist.github.com/rasor/2060037307731d2c2bb740e503c951bb).  
In part 2 I'll deploy a nodejs webapp and perhaps a .ASTNET Core MVC webapp.  

## [Deploying](https://docs.openshift.org/latest/minishift/getting-started/quickstart.html#deploy-sample-app) to MiniShift



### Deploy via oc CLI



Start VirtualBox and Git Bash and run following in the shell

```bash
# Start Minishift using script from Part 1
shiftcli.sh

oc login developer
# New Project
oc new-project nodejs-echo --display-name="nodejs" --description="Sample Node.js app"
oc project nodejs-echo

# Following is shamelessly copy from the MiniShift QuickStart

# 1. Create a Node.js example app
oc new-app https://github.com/openshift/nodejs-ex -l name=myapp
# 2. Track the build log until the app is built and deployed
oc logs -f bc/nodejs-ex
# 3. Expose a route to the service
oc expose svc/nodejs-ex
# 4. Access the application
minishift openshift service nodejs-ex --in-browser
```

More deploy variants [here](https://github.com/sclorg/nodejs-ex).

The webapp will probably use [xip.io](https://xip.io/) for DNS according to eBook 1 (see bottom links).  

# Links

## References

* [MiniShift - Command Reference](https://docs.openshift.org/latest/minishift/command-ref/minishift.html)
* [oc CLI Reference](https://docs.openshift.org/latest/cli_reference/index.html)
* [apb CLI - Ansible Playbook Bundle Development Guide](https://docs.openshift.org/latest/apb_devel/index.html)

## Getting Started

* Free eBook 1 [OpenShift for Developers](https://www.openshift.com/promotions/for-developers.html) (2016)
* Free eBook 2 [DevOps with OpenShift](https://www.openshift.com/promotions/devops-with-openshift.html) (2017)
    * [The Twelve-Factor App ](https://12factor.net/)
* Free eBook 3 [Deploying to OpenShift](https://www.openshift.com/promotions/deploying-to-openshift.html) (2018)

## Docker

* ng devserver: [Angular Seed](https://mgechev.github.io/angular-seed/)

## Kubernetes and Swarm

* [The key differences between Kubernetes and Docker Swarm](https://medium.com/packt-hub/the-key-differences-between-kubernetes-and-docker-swarm-edb519730757)
* [Kubernetes: Flannel networking](https://blog.laputa.io/kubernetes-flannel-networking-6a1cb1f8ec7c)
* GUI: [Kubernetic - The Kubernetes Desktop Client](http://kubernetic.com/)

The End
