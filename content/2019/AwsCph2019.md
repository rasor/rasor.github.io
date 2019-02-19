Title:  AWS Community Day Cph 2019
Date: 2099-01-01 00:00
Category: DevOp
Tags: #aws

# AWS Community Day Cph 2019-02-19

* Home: [AWS Community Day](https://awscommunitynordics.org/communityday/)

## Persons and groups

* [Martin Buberl (@martinbuberl) | Twitter](https://twitter.com/martinbuberl)
* [User Groups](https://awscommunitynordics.org/usergroups/)
* [Copenhagen AWS User Group (Copenhagen, Denmark)](https://www.meetup.com/Copenhagen-AWS-User-Group/)

## 13:00 Running Devops at the Tradeshift rocketship

* [Jesper Terkelsen/](https://www.linkedin.com/in/jesperterkelsen/)




## 11:15 Let's build a serverless data stream on AWS

* Martin Larsen [https://www.linkedin.com/in/realvaluetalks/](https://www.linkedin.com/in/realvaluetalks/)
* [Martin Larsen: Technology talks with real value](http://realvaluetalks.com/)

Building:

A ticket system needs to remove bad actors from buying. Those are sending lots of requests fast.

* 1. Input: A ELB Log read by
* 2. Kinesis stream provider - having Shards
* Consumers:
    * 3b. Kinesis Data Analytics
    * Spark
    * Lambda 
* 4. Output: Kinesis Firehose - then dashboard via AWS Athena query counting bad actors
* 5. Lambda: Take action - block IPs from bad actors in Firewall

Lambda doing: Bad Actor filter

* Look at IP - is it from a proxy
* Model data. eventType, nodeType

Tools: 

* [Amazon Athena — Serverless Interactive Query Service - AWS](https://aws.amazon.com/athena/) (Query) - can deserialize json
* [Streaming Data Firehose - Amazon Kinesis - AWS](https://aws.amazon.com/kinesis/data-firehose/) (buffer streams while storing)
* [Amazon QuickSight](https://aws.amazon.com/quicksight/) (BI)

## 10:15 Efficiently exposing apps on Kubernetes at scale

* [Rasheed Amir (@rasheedwaraich) | Twitter](https://twitter.com/rasheedwaraich)
* Com: Stakater. k8s + OpenShift automation
    * Blog: [Stakater – Medium](https://medium.com/stakater)
* [stakater/Xposer](https://github.com/stakater/Xposer)
    * [Stakater](https://www.stakater.com/projects-overview.html)

Problem:  
Pod are not accessible outside cluster.  

For k8s You need to know: Servicees, Ports, Ingress.

* k8s service - has a stable IP, LB acrods pods. 
    * Svc types
        * ClusterIP: not accible from outside
        * NodePort: One service/port. Not good for prod.
        * LoadBalancer: 1 svc - 1 lb. Expensive - LB's are expensive.
* Ingress - The good solution :-)
    * nginx Ingress controller
        * Auto creates LB, e.g. ELB in AWS.
* Labels are used for routing

Learned:

* 2 Ingress ctrls + 2 AWS ELBs - see img
    * 1 for private
    * 1 for public
* 1 AWS ALB can replace 2 ELBs

DNS:

* [kubernetes-incubator/external-dns](https://github.com/kubernetes-incubator/external-dns) - autocreate routes

TLS/SSL:

* [jetstack/cert-manager](https://github.com/jetstack/cert-manager) - autoprovision certs
Using Lets Encrypt
* AWS ACM. Now using Terraform - later AWS ...?

Scaling:

* Node Autoscaling

Authentication: 

* Key club

Monitoring - from outside cluster:

* Could use: Pingdom, UptimeRobot, StatusCake
* [Ingress Monitor Controller — Uptime Alerts for Kubernetes Services](https://medium.com/stakater/ingress-monitor-controller-uptime-alerts-for-kubernetes-services-855a6bf48ac0)
    * [stakater/IngressMonitorController](https://github.com/stakater/IngressMonitorController)
* [stakater/Forecastle](https://github.com/stakater/Forecastle)

## Questions

Where to host clusters?  

* AWS spot instances
    * 8 Nodes cluster 11$/day
* DigitalOcean - Mgd k8s - $20/ month / 1 node. 2 node - just dougble. You don't pay for the manangement node.

## 9:15 Monitoring Serverless architectures on AWS Lambda

* [Serhat Can (@srhtcn) | Twitter](https://twitter.com/srhtcn)

### OpsGenie by Atlassain

* [Serhat Can on Twitter](https://twitter.com/srhtcn/status/1093524383971360771)
* Prod blog: [Automate Resource Adjustments for Amazon EC2 with Opsgenie Actions, A Use Case](https://www.opsgenie.com/blog/automate-resource-adjustments-in-amazon-ec2-with-opsgenie-actions-a-use-case)

### Monitoring

* CloudWatch metrics / Logs
* [AWS X-Ray – Distributed Tracing System](https://aws.amazon.com/xray/)
    * [Tracing serverless application with AWS X-Ray – Nordcloud Engineering – Medium](https://medium.com/nordcloud-engineering/tracing-serverless-application-with-aws-x-ray-2b5e1a9e9447)

Need for monitoring:

* Logs
* Metrics
* Traces
* Aggregates of all above

Problems of existing prods: 

* Only Sync data senders
    * Sln: Sync for dev envir
* Manual instrumentation
    * Sln: Automate trace with [] method plugin
* Distributed tracing
    * Sln: Using X-Ray

### Resources

* [AWS Serverless Application Repository - Amazon Web Services](https://aws.amazon.com/serverless/serverlessrepo/)
* [Thundra | Serverless Observability](https://thundra.io/)

Suggestions:

* Plugin for cold-starts
* Opentracing API and data model
* Aggreagate all
* Heatmaps

The End