Title: Developing with OpenShift
Status: published
Date: 2018-04-15 15:00
Category: DevOp
Tags: #openshift, #docker, #kubernetes, #redhat, #paas

It has become time (for me) to explore OpenShift.
OpenShift is a Build and Deployment block using Kubernetes and Docker as deployment target. In other words: It connects GitHub and DockerHub to your cloud provider. It allows you to do do on-premise deployment and to monitor and operate your cloud.

## So how to get started with OpenShift?

### Which editions (products) are awailbale?

Currently (spring 2018) you get a good helicopter view from the free eBook [Deploying to OpenShift](https://www.openshift.com/promotions/deploying-to-openshift.html) - Preface - Online Resources.  
From there you'll learn that there are two editions (called products) of OpenShift:

* `OpenShift Origin` - This is the OpenShift repo, that you can also use while doing local dev.
* `OpenShift Container Platform` - An Enterprise version aimed for on-premise hosting of your own cloud.

On the [OpenShift documentation](https://docs.openshift.com/) homepage, you'll learn that there are also two more editions (products):

* `OpenShift Dedicated` - Redhat's managed public cloud edition of `OpenShift Container Platform`
* `OpenShift Online` - I think this is like the dedicated edition (single tenant) except that the VMs are not dedicated to only one customer, but are multi tenant.

The prior two editions seems to be clouds hosted by RedHat.

OpenShift is a managed PaaS, that must be deployed to some IaaS [explained here](https://developers.redhat.com/products/cdk/overview/) - Quote:
> The containers you build can be easily deployed on any Red Hat container host or platform, including: Red Hat Enterprise Linux, Red Hat Enterprise Linux Atomic Host, and our platform-as-a-service solution, OpenShift Container Platform 3.

I think this IaaS stack often will be RedHat OpenStack and probably also is it, when you are using RedHat Enterprise Linux as the container host.

### How do I start playing with the toy?

||`Origin`|`Container Platform`|
|---|---|---|
|Download and Run Openshift locally|[`MiniShift`](https://www.openshift.org/minishift/) *1|[`Container Development Kit (CDK)`](https://developers.redhat.com/products/cdk/overview/)|
|Test Hosted Openshift||[Red Hat Test Drive](https://aws.amazon.com/testdrive/redhat/)|
|Install Walkthrough||[Container Platform 3.9](https://docs.openshift.com/container-platform/3.9/getting_started/install_openshift.html)|
|Configure Walkthrough||[Container Platform 3.9](https://docs.openshift.com/container-platform/3.9/getting_started/configure_openshift.html)|
|`Web Console` Walkthrough|[Origin 3.9](https://docs.openshift.org/3.9/getting_started/developers_console.html)|[Container Platform 3.9](https://docs.openshift.com/container-platform/3.9/getting_started/developers_console.html)|
|`CLI` Walkthrough|[Origin 3.9](https://docs.openshift.org/3.9/getting_started/developers_cli.html)|[Container Platform 3.9](https://docs.openshift.com/container-platform/3.9/getting_started/developers_cli.html)|

*1: `MiniShift` is a newer method for local development than the method used in eBook `OpenShift for Developers` called `Vagrant all-in-one virtual machine`.  
In eBook `DevOps with OpenShift` a local all-in-one cluster is started using `oc cluster up`.

OK, so to play with it locally, then I can either use `MiniShift` or `Container Development Kit`.

### What is in the box?

When you run the box there will be a REST API enabling you to manage the box  
[![OpenShift access and control](https://cdn.levvel.io/blog_content/James+Buckett+Differences+Article/Differences2.png)](https://www.levvel.io/our-ideas/differences-between-kubernetes-and-openshift)

Your code (in docker containers) will be deployed to Kubernetes Pods inside the box  
[![OpenShift project (Namespace)](https://cdn.levvel.io/blog_content/James+Buckett+Differences+Article/Differences1.png)](https://www.levvel.io/our-ideas/differences-between-kubernetes-and-openshift)

Next: Will install MiniShift

... to be continued

# Links

* [OpenShift Blog](https://blog.openshift.com/)
    * [Announcing .NET Core 2.0 Support for OpenShift](https://blog.openshift.com/announcing-net-core-2-0-support-openshift/)
    * [ASP.NET on OpenShift: Getting started in ASP.NET](https://blog.openshift.com/asp-net-on-openshift-getting-started-in-asp-net/)
* [OpenShift Commons](https://commons.openshift.org/) - a community
    * [OpenShift .NET Special Interest Group](https://commons.openshift.org/sig/Openshift.NET.html)
* Free eBook [OpenShift for Developers](https://www.openshift.com/promotions/for-developers.html) (2016)
* Free eBook [Deploying to OpenShift](https://www.openshift.com/promotions/deploying-to-openshift.html) (2018)
* Free eBook [DevOps with OpenShift](https://www.openshift.com/promotions/devops-with-openshift.html) (2017)
    * [The Twelve-Factor App ](https://12factor.net/)
* [OpenShift: Interactive Learning Portal](https://learn.openshift.com/)
    * Above is based on [Katacoda - Interactive Learning Platform](https://katacoda.com/)
* Old [Cloud](https://rasor.wordpress.com/2013/11/26/cloud-services/) landscape anno 2013 - from my old blog.

The End
