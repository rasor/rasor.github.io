Title: Microsoft Architecture and Implementations
Status: published
Date: 2018-08-18 20:00
Category: Develop
Tags: #microsoft, #architecture, #ebooks, #azure, #microservices, #faas

This blog will help you choosing the right design and corresponding code, when you build microsoft web and services in 2017 and 2018.

# Lists of Architectures and Implementations

Here are some lists that can be gives you several designs.  

* [.NET Application Architecture Guidance](https://www.microsoft.com/net/learn/architecture)  
Mobile, Desktop, Web and Azure
* [Azure Reference Architectures](https://docs.microsoft.com/en-us/azure/architecture/reference-architectures/)  
Big data, Web applications, N-tier applications, Virtual networks, Active Directory, VM workloads
    * eBook (2017, 333 pages): [Cloud Application Architecture Guide](https://azure.microsoft.com/en-us/campaigns/cloud-application-architecture-guide/)
* [.NET Architecture Guidance](https://docs.microsoft.com/en-us/dotnet/standard/guidance-architecture)  
eBooks and Code

## WebApps and services

This blog only looks at webapps and webservices.  

### Intro

Should you choose simple monolitic webs, scalable microservices or cost saving functions?  
Have a look at **Architecture styles** below to quickly see what you get.  
Read the Fowler Article [Serverless Architectures](https://martinfowler.com/articles/serverless.html) to understand when you continue from microservices to serverless functions.  
Follow the [Design principles for Azure applications](https://docs.microsoft.com/en-us/azure/architecture/guide/design-principles/index).  
Follow the [Azure security best practices and patterns](https://docs.microsoft.com/en-us/azure/security/security-best-practices-and-patterns).  
Review your design with [Resiliency checklist](https://docs.microsoft.com/en-us/azure/architecture/checklist/resiliency).  

#### Architecture from real life

* [Vue Storefront](https://github.com/DivanteLtd/vue-storefront)
    * eBook (2018, 122 pages): [Microservices Architecture for eCommerce](http://go.divante.co/microservices-architecture-ecommerce/)  
    The book is not about Azure nor about C#. It is about architecting for cloud and PWA.

#### [Architecture styles](https://docs.microsoft.com/en-us/azure/architecture/guide/architecture-styles/)

The drawings below gives you a fast overview of some web patterns you can use.  

* N-tier - Monolitic - The most simple - Good for PaaS  
![N-tier](https://docs.microsoft.com/en-us/azure/architecture/guide/architecture-styles/images/n-tier-sketch.svg)
* Web-Queue-Worker - Good for PaaS  
![Web-Queue-Worker](https://docs.microsoft.com/en-us/azure/architecture/guide/architecture-styles/images/web-queue-worker-sketch.svg)
* Microservices - Good for containers  
![Microservices](https://docs.microsoft.com/en-us/azure/architecture/guide/architecture-styles/images/microservices-sketch.svg)
* CQRS - good for scaling data  
![CQRS](https://docs.microsoft.com/en-us/azure/architecture/guide/architecture-styles/images/cqrs-sketch.svg)
* Event-driven - good for scaling services  
![Event-driven](https://docs.microsoft.com/en-us/azure/architecture/guide/architecture-styles/images/event-driven-sketch.svg)
* [Serverless functions](https://martinfowler.com/articles/serverless.html) - FaaS  
![Serverless functions](https://martinfowler.com/articles/serverless/sps.svg)

#### Cloud Design Patterns

[Cloud Design Patterns](https://docs.microsoft.com/en-us/azure/architecture/patterns/) is a long list of patterns you can use to finetune your design of SW, Infrascructure, CI/CD pipline, Monitoring and Operations.  

### Samples With implementation

If you want code to look at here is a list of samples with code.

* N-tier: [Architect modern web applications with ASP.NET Core and Azure](https://docs.microsoft.com/en-us/dotnet/standard/modern-web-apps-azure-architecture/)  
How to select appropriate frontend and backend
    * eBook (2017, 115 pages): [Architecting Modern Web Applications with ASP.NET Core and Azure](https://aka.ms/webappebook)
    * Code: [eShopOnWeb](https://github.com/dotnet-architecture/eShopOnWeb)  
    MVC and Razor Pages frontend, EF Code first
* eBook (11-2017, 542 pages): [ASP.NET Core 2 and Angular 5](https://www.packtpub.com/application-development/aspnet-core-2-and-angular-5?utm_source=GitHub&utm_medium=repository&utm_campaign=9781788293600)
    * Code: [PacktPublishing/ASP.NET-Core-2-and-Angular-5](https://github.com/PacktPublishing/ASP.NET-Core-2-and-Angular-5)  
    Angular frontend, WebAPI, EF Code first, OIDConnect
* [.NET Microservices. Architecture for Containerized .NET Applications](https://docs.microsoft.com/en-us/dotnet/standard/microservices-architecture/index)
    * eBook(2018, 331 pages): [.NET Microservices Architecture](https://aka.ms/microservicesebook)  
    Using CQRS
    * Code: [eShopOnContainers](https://github.com/dotnet-architecture/eShopOnContainers)
    * Code: [eShopOnAzure](https://github.com/dotnet-architecture/eShopOnAzure)
    * Code: [eShopOnContainersAI](https://github.com/dotnet-architecture/eShopOnContainersAI)  
    ![eShopOnContainers](https://user-images.githubusercontent.com/1712635/38758862-d4b42498-3f27-11e8-8dad-db60b0fa05d3.png)
* [Designing, building, and operating microservices on Azure with Kubernetes](https://docs.microsoft.com/en-us/azure/architecture/microservices/)
    * Code: https://github.com/mspnp/microservices-reference-implementation  
* [More Code](https://github.com/dotnet-architecture/)

### Samples Without implementation

If you just want the architecture design samples here is a list.

* [Basic web application](https://docs.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app)
* [Scalable web application](https://docs.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/scalable-web-app)  
using WebApp, ApiApp, Queue, WebJob, Redis, SQL, Cosmos, Search, Blob, CDN
* [Multi-region web application](https://docs.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/multi-region)  
as above, but extend with standby region and replication
* [Serverless apps: Architecture, patterns, and Azure implementation](https://docs.microsoft.com/en-us/dotnet/standard/serverless-architecture/index)
    * eBook (2018, 54 pages): [Serverless apps](https://aka.ms/serverless-ebook) 

### Azure Tutorials

* [Azure Web Apps - Tutorials](https://docs.microsoft.com/en-us/azure/app-service/#step-by-step-tutorials)  
WebApp with Secure access to SQL DB
* [Create your first function in Azure using Visual Studio](https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-your-first-function-visual-studio)
* [Get started guide for developers on Azure](https://docs.microsoft.com/en-us/azure/guides/developer/azure-developer-guide)
* eBook (33 pages): [Azure Quick Start Guide for .NET Developers](https://www.microsoft.com/net/download/thank-you/azure-quick-start-ebook)

# Transistion to cloud

If you need help to get started in cloud.

* eBook (2017, 156 pages): [Enterprise Cloud Strategy](https://azure.microsoft.com/en-us/resources/enterprise-cloud-strategy/)  
Why go to cloud?
* eBook (2018, 120 pages): [Azure Strategy and Implementation Guide](https://azure.microsoft.com/en-us/resources/azure-strategy-and-implementation-guide/en-us/)  
Governance, Architecture, Operations, Service Management
* [Cloud Adoption Guide](https://docs.microsoft.com/en-us/azure/architecture/cloud-adoption-guide/)
* [Modernize Existing .NET Applications With Azure Cloud and Windows Containers (2nd edition)](https://docs.microsoft.com/en-us/dotnet/standard/modernize-with-azure-and-containers/index)
    * eBook (2018, 72 pages): [Modernizing Existing .NET Applications](https://www.microsoft.com/net/download/thank-you/modernizing-existing-net-apps-ebook)
    * Code: [eShopModernizing](https://github.com/dotnet-architecture/eShopModernizing)
* [Azure Essentials](https://www.microsoft.com/en-us/azureessentials/Pivot/AzureEssentials/AzureInfrastructure/Watch) - Intro to Azure

## Infrastructure

* eBook (10-2017, 346 pages): [Azure for Architects](https://azure.microsoft.com/en-us/resources/azure-for-architects/en-us/)
* Video course (2017): [Architecting Distributed Cloud Applications](https://www.youtube.com/watch?v=xJMbkZvuVO0&list=PL9XzOCngAkqs0Q8ZRdafnSYExKQurZrBY)
* Architecture for providing [Azure services for on-premise and the Internet](https://github.com/mspnp/reference-architectures/tree/master/dmz/secure-vnet-dmz)  
![Azure services](https://camo.githubusercontent.com/f48de024cb1b395a4727b20e18fb14dc33d1bb53/68747470733a2f2f646f63732e6d6963726f736f66742e636f6d2f617a7572652f6172636869746563747572652f7265666572656e63652d617263686974656374757265732f646d7a2f696d616765732f646d7a2d7075626c69632e706e67)
* ARM [Quickstart Templates](https://azure.microsoft.com/en-us/resources/templates/)
    * Git repo for [quickstart-templates](https://github.com/Azure/azure-quickstart-templates)

### AzureStack - Cloud on-premise

If you want to deploy to Azure-on-premise, then AzureStack is the Microsoft answer to OpenStack

* eBook (2017, 54 pages): [Azure Stack: Building an end-to-end validation environment](https://azure.microsoft.com/en-us/resources/azure-stack-building-end-to-end-validation-environment/en-us/)
* [Azure Stack Operator - Tutorials](https://docs.microsoft.com/en-us/azure/azure-stack/)

# More resources

* [Microsoft Virtual Academy eBooks](https://mva.microsoft.com/ebooks)
* [Rasor - eBooks](https://github.com/rasor/awesome-tables/blob/master/awesome-ebooks-training.md#ebooks)

# The past

Up until 2017 you could find guidance on

* [CodePlex Archive](https://archive.codeplex.com/?s=patterns%20practices) - Pattern & Practices

The End