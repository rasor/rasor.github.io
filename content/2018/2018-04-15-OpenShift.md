Title: Developing with OpenShift
Status: published
Date: 2018-04-15 15:00
Modified: 2018-04-17 16:00
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

The latter two editions seems to be clouds hosted by RedHat.

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

RedHats own picture of OpenShift runtime environment looks like this:  
[![OpenShift runtime environment](https://blog.openshift.com/wp-content/uploads/arch-diagram.png)](https://blog.openshift.com/openshift-enterprise-3-evolving-paas-future/)

## Installation

### VirtualBox

I am installing on Windows 10. Openshift needs a hypervisor. There are two options: Hyper-v or VirtualBox.  
VirtualBox is the easy one to handle. It is also an option that can be chosen both on Windows, Linux and Mac.  
I have used hypervisors some years ago on my local PC, so I know that I have already enabled Intel Virtualization Technology (also known as Intel VT) in the Bios. It was required for Hyper-v, so I assume it is either beneficial or required for VirtualBox, too.  
Notice: Not all PC's comes with Intel VT.  

When you have [downloaded VirtualBox](https://www.virtualbox.org/wiki/Downloads) and start to install it you are told that it will disconnect your network (why did I also just start a long running upload? - I'll abort that for a while)  
![Will disconnect network](img/2018/2018-04-15-OpenShift1.PNG)

After restart I had an extra network adapter

```bash
ipconfig /all

# output:
# Ethernet adapter VirtualBox Host-Only Network:
#   Connection-specific DNS Suffix  . :
#   Description . . . . . . . . . . . : VirtualBox Host-Only Ethernet Adapter
#   IPv4 Address. . . . . . . . . . . : 192.168.56.1(Preferred)
```

### MiniShift

I downloded and unzipped [minishift/minishift](https://github.com/minishift/minishift/releases) for Windows.  
It could be unzipped to anywhere. I chose `C:\Program Files\`, so after unzip the MiniShift path was `C:\Program Files\minishift-1.15.1-windows-amd64`. That path had to be added to the enviroment %path%.

```bash
# Verify minishift can be reached from any local path
# Note: On Windows minishift cannot be executed from a network drive
minishift --help
```

If any issues consult [Installing Minishift](https://docs.openshift.org/latest/minishift/getting-started/installing.html) guide.

## Test driving MiniShift

```bash
# Start hypervisor
C:\Program Files\Oracle\VirtualBox\VirtualBox.exe
# Start minishift
minishift start --vm-driver=virtualbox
```

Output

```text
-- Starting profile 'minishift'
-- Checking if requested OpenShift version 'v3.7.2' is valid ... OK
-- Checking if requested OpenShift version 'v3.7.2' is supported ... OK
-- Checking if requested hypervisor 'virtualbox' is supported on this platform ... OK
-- Checking if VirtualBox is installed ... OK
-- Checking the ISO URL ... OK
-- Downloading OpenShift binary 'oc' version 'v3.7.2'
 38.44 MiB / 38.44 MiB [=======================================================================================================================================] 100.00% 0s-- Downloading OpenShift v3.7.2 checksums ... OK
-- Checking if provided oc flags are supported ... OK
-- Starting local OpenShift cluster using 'virtualbox' hypervisor ...
-- Minishift VM will be configured with ...
   Memory:    2 GB
   vCPUs :    2
   Disk size: 20 GB

   Downloading ISO 'https://github.com/minishift/minishift-b2d-iso/releases/download/v1.2.0/minishift-b2d.iso'
 40.00 MiB / 40.00 MiB [=======================================================================================================================================] 100.00% 0s
-- Starting Minishift VM ...................................... OK
-- Checking for IP address ... OK
-- Checking for nameservers ... OK
-- Checking if external host is reachable from the Minishift VM ...
   Pinging 8.8.8.8 ... OK
-- Checking HTTP connectivity from the VM ...
   Retrieving http://minishift.io/index.html ... OK
-- Checking if persistent storage volume is mounted ... OK
-- Checking available disk space ... 0% used OK
   Importing 'openshift/origin:v3.7.2' . CACHE MISS
   Importing 'openshift/origin-docker-registry:v3.7.2' . CACHE MISS
   Importing 'openshift/origin-haproxy-router:v3.7.2' . CACHE MISS
-- OpenShift cluster will be configured with ...
   Version: v3.7.2
Starting OpenShift using openshift/origin:v3.7.2 ...
Pulling image openshift/origin:v3.7.2
Pulled 1/4 layers, 26% complete
Pulled 2/4 layers, 78% complete
Pulled 3/4 layers, 90% complete
Pulled 4/4 layers, 100% complete
Extracting
Image pull complete
OpenShift server started.

The server is accessible via web console at:
    https://192.168.99.100:8443

You are logged in as:
    User:     developer
    Password: <any value>

To login as administrator:
    oc login -u system:admin

-- Exporting of OpenShift images is occuring in background process with pid 11256.
>
```

If your screen looks like above the downloded minishift image wil be cached to  
`c:\users\youruserid\.minishift\cache\iso\b2d\v1.2.0\`

In VirtualBox you'll see the VM running:
![Minishift running](img/2018/2018-04-15-OpenShift2.PNG)

If you have trouble consult [Minishift Quickstart](https://docs.openshift.org/latest/minishift/getting-started/quickstart.html).

Next: Operating Minishift

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
