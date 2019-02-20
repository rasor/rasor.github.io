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


## 15:15 Continuous Delivery to AWS using Azure DevOps

* [Morten Brix Pedersen](https://www.linkedin.com/in/mbrix/) - Queue-it
* [Morten Brix Pedersen (@mbrix) | Twitter](https://twitter.com/mbrix)
* [mbp - Overview](https://github.com/mbp)

Azure DevOps - Collection of tools from Kanban to 

* PreReq: Creted VPC in AWS
    * Installed AWS tools for VSTS [aws/aws-vsts-tools](https://github.com/aws/aws-vsts-tools)
* Publish to AWS EC Registry
* Deploy to AWS Fargate

```bash
# test we are running
dotnet run
```
build.yaml:
* Build 
* add docker file w igm
* push img to AWS ECR
* add cloudformation script - VSTS Task: AWS CloudFormation Update Stack

GiraffeApp.yaml
* Fetch Secrets and add as parms to yaml
* Deploy to AWS Fargate


## 16:00 Alexa Skill Development

* [Goran Vuksic (@gvuksic) | Twitter](https://twitter.com/gvuksic)
* [https://www.linkedin.com/in/goranvuksic/](https://www.linkedin.com/in/goranvuksic/)

Amazon Echo - wifi connected loudspeaker

* interacts with 
    * Echo button - enables play games
    * Echo Connect - to home phone
    * AWS Alexa in cloud - "Alexa - turn on kitchen light" - connects back to your IoT at home.

## 14:30 Bring ML awareness with DeepLens to the business by accessing the office with the face

* [Lezgin Bakircioglu](https://www.linkedin.com/in/lezgin-bakircioglu-2239b93/)

* DeepLens is a CP with cam. Only for Dev
    * [AWS DeepLens – Deep learning enabled video camera for developers - AWS](https://aws.amazon.com/deeplens/)
    * Problems:
        * Slow CPU
        * Only runs one model
        * State
        * Overheates in 2 days
        * Wifi disconnect
* Build
    * Hard way: SageMaker + Jupyter
    * Easy way: DeepLens as first filter - AWS for rest.
        * Use DoorMan [Doorman - Community Project](https://aws.amazon.com/deeplens/community-projects/Doorman/)
            * [YouTube](https://www.youtube.com/watch?v=UXVD22jDbu8)
        * Arduino
* Sln: [dwtechnologies/concierge](https://github.com/dwtechnologies/concierge)

## 13:45 Making Machine Learning social with SageMaker, Meeshkan and Slack

* [Mike Solomon](https://www.linkedin.com/in/michael-thomas-solomon/)
* CEO at [Meeshkan](https://www.meeshkan.com/)
    * [Meeshkan (@MeeshkanML) | Twitter](https://twitter.com/meeshkanml)
    * [Meeshkan | Slack](https://meeshkan-community.slack.com/join/shared_invite/enQtNTMyOTA5MTgwOTc5LTk5ZWYxMTE3MzgxZDNiNTFmOWMzOGE2MTNiMDhkODJmNDFjZTU3ODI1MDczMTYzOWRhZTdkNDBkY2E3YWYyM2E)

What:

* SagMakerML graphs are parsed into Slack

Tools:

* [Machine Learning Models & Algorithms | Amazon SageMaker on AWS](https://aws.amazon.com/sagemaker/)
    * Lots of getting startet...
    * Missing
        * No chat
        * No easy alerts
        * No serendipity - find by accident
        * No lurking - lust read - not do
        * No audit log of teams thaoughts process - the why

Dev:

* [Meeshkan/meeshkan-client](https://github.com/Meeshkan/meeshkan-client)
* [Meeshkan/udemy-tmnt-koopa](https://github.com/Meeshkan/udemy-tmnt-koopa)
* [Meeshkan/meeshkan-client](https://github.com/Meeshkan/meeshkan-client/blob/dev/examples/sagemaker/pytorch_rnn_meeshkan.ipynb)
* Dev Jupyter notebooks locally
* [Training with PyTorch on Amazon SageMaker – Julien Simon – Medium](https://medium.com/@julsimon/training-with-pytorch-on-amazon-sagemaker-58fca8c69987)
* [PyTorch](https://pytorch.org/)
    * Gradients easily exposed and tweakable

When training the model in SageMaker, then a notification is sent to Slack and same, when done a graph is sent to Slack, so it can be discussed.
Deeplearning often runs for days, so you have slack users for monitoring :-)

## 13:00 Running Devops at the Tradeshift rocketship

* [Jesper Terkelsen/](https://www.linkedin.com/in/jesperterkelsen/)
    * jnt(at)tradeshift.com

Tips:

* Run test envirs on spot
* Managed svc slow to spin up - not good for test, so can they run in containers, then do
* Photo of transaction problem solving graph

## 11:15 Let's build a serverless data stream on AWS

* Martin Larsen [https://www.linkedin.com/in/realvaluetalks/](https://www.linkedin.com/in/realvaluetalks/) - Queue-it
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

# Sponsor offers

* [A Gift from N2WS](http://get.n2ws.com/aws-summit-2019/)

The End