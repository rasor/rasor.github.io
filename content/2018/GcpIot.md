Title: GCP IoT
Date: 2099-01-01 00:00
Tags: #gcp

# A journey to IoT in GCP  

First you'll need an account. There is a free trial you get via [GCP Free Tier](https://cloud.google.com/free/).  
If your trial has expired, then sign up with another email.  
If you sign up outside EU, then you can change your account type from Business to Individual.  
You'll have to enter a credit card, but if you delete your resources after use and use smallest size, then you probably can't exceed your $300 credit for free in that trial year.  
If you want to get a cost estimate then use [GCP Pricing Calculator](https://cloud.google.com/products/calculator/).  
  
When signed up you'll enter the [GCP Getting Started](https://console.cloud.google.com/getting-started) page.  
  
Ok, I'm in - I want to install the CLI [Cloud SDK](https://cloud.google.com/sdk/#download).  
On Windows it wants to install it here: `C:\Program Files (x86)\Google\Cloud SDK`.  
I already have Python installed, so I deselected "Bundled Python".  
After install it runs `gcloud init`, which wants you to login and connect to the initial created project (a resource pool).  
  
Some of the initial info I gat was:  
```text
Not setting default zone/region (this feature makes it easier to use
[gcloud compute] by setting an appropriate default value for the
--zone and --region flag).
See https://cloud.google.com/compute/docs/gcloud-compute section on how to set
default compute region and zone manually. If you would like [gcloud init] to be
able to do this for you the next time you run it, make sure the
Compute Engine API is enabled for your project on the
https://console.developers.google.com/apis page.

Created a default .boto configuration file at [C:\Users\userid\.boto]. See this file and
[https://cloud.google.com/storage/docs/gsutil/commands/config] for more
information about configuring Google Cloud Storage.

Run `gcloud help config` to learn how to change individual settings

This gcloud configuration is called [default]. You can create additional configurations if you work with multiple accounts and/or projects.
Run `gcloud topic configurations` to learn more.

Some things to try next:

* Run `gcloud --help` to see the Cloud Platform services you can interact with. And run `gcloud help COMMAND` to get help on any gcloud command.
* Run `gcloud topic -h` to learn about advanced features of the SDK like arg files and output formatting
```
  
You will also be be greeted with this page: [You are now authenticated with the Google Cloud SDK!](https://cloud.google.com/sdk/auth_success).  
  
Here is what I have now:  
```bash
gcloud -v
# Google Cloud SDK 222.0.0
# beta 2018.07.16
# bq 2.0.36 - BigQuery
# core 2018.10.19
# gsutil 4.34

gcloud config list
# [core]
# account = your@email.xx
# disable_usage_reporting = False
# project = central-run-123456
# Your active configuration is: [default]

# https://console.cloud.google.com/cloud-resource-manager
gcloud projects list
# PROJECT_ID          NAME              PROJECT_NUMBER
# central-run-123456  My First Project  1091175999999
```

* More help with gcloud: [Scripting gcloud commands](https://cloud.google.com/sdk/docs/scripting-gcloud)

# Functions

* [Quickstart:  Cloud Functions](https://cloud.google.com/functions/docs/quickstart#functions-prepare-environment-nodejs)

## PreReq

```bash
gcloud components update
gcloud components install beta # Node v8 and Python code
```

* Npm devDependencies for Express apps: [google-cloud](https://www.npmjs.com/package/google-cloud)

```bash
# You need `Google Cloud Functions` enabled.  
gcloud services enable cloudfunctions.googleapis.com
# Default region
gcloud config set functions/region europe-west1
gcloud config get-value functions/region
# europe-west1

# Sample code:
git clone https://github.com/GoogleCloudPlatform/nodejs-docs-samples.git
# git clone https://github.com/GoogleCloudPlatform/python-docs-samples.git
cd nodejs-docs-samples/functions/helloworld/

# gcloud SDK: https://cloud.google.com/sdk/gcloud/reference/beta/functions/

# Deploy:
gcloud functions deploy helloGET --runtime nodejs8 --trigger-http #--region=europe-west1
# Print:
gcloud functions describe helloGET
# httpsTrigger:
#  url: https://us-central1-central-run-220517.cloudfunctions.net/helloGET

start https://us-central1-central-run-220517.cloudfunctions.net/helloGET
# Hello World

# O&M:
gcloud functions -h
# Usage: gcloud functions [optional flags] <group | command>
#   group may be           event-types | logs | regions
#   command may be         call | delete | deploy | describe | list

gcloud functions list
# NAME      STATUS  TRIGGER       REGION
# helloGET  ACTIVE  HTTP Trigger  us-central1

# Delete:
gcloud functions delete helloGET # takes minutes...

```

# IoT

I want to connect some IoT devices to GCP. Here is an overview of the GCP services  
[![iot.svg](https://cloud.google.com/images/solutions/iot/iot.svg)](https://cloud.google.com/solutions/iot/)

You need `Cloud IoT API` enabled.  
```bash
gcloud services enable cloudiot.googleapis.com
# Operation "operations/acf.f93e2f75-fe30-4b85-8253-4458ba5fffff" finished successfully.

# https://console.cloud.google.com/apis/dashboard
gcloud services list
# NAME                              TITLE
# bigquery-json.googleapis.com      BigQuery API
# cloudapis.googleapis.com          Google Cloud APIs
# clouddebugger.googleapis.com      Stackdriver Debugger API
# cloudiot.googleapis.com           Cloud IoT API
# cloudtrace.googleapis.com         Stackdriver Trace API
# datastore.googleapis.com          Cloud Datastore API
# logging.googleapis.com            Stackdriver Logging API
# monitoring.googleapis.com         Stackdriver Monitoring API
# servicemanagement.googleapis.com  Service Management API
# serviceusage.googleapis.com       Service Usage API
# sql-component.googleapis.com      Cloud SQL
# storage-api.googleapis.com        Google Cloud Storage JSON API
# storage-component.googleapis.com  Google Cloud Storage
```

Here are commands for the IoT API:  
[Google APIs Explorer - Cloud IoT API v1](https://developers.google.com/apis-explorer/#p/cloudiot/v1/)

Here are IoT tutorials: 
[Google Cloud IoT - Solutions](https://cloud.google.com/solutions/iot/)

From an ESP32 (and ESP8266?) device here is how you connect it to  [Mongoose OS - Reporting state to Google IoT Core](https://mongoose-os.com/docs/mos/cloud/google.md#setup-google-iot-core)  

And here are Mongoose supported HW + firmware [Mongoose OS Documentation](https://mongoose-os.com/docs/mos/userguide/devboards.md)  

# Links

* Pricing
    * [GCP Free Tier](https://cloud.google.com/free/)
    * [GCP Pricing Calculator](https://cloud.google.com/products/calculator/)
* Community
    * [Google Events](https://developers.google.com/events/)
    * [Google Developers Experts](https://developers.google.com/experts/)
* Develop
    * [gcloud CLI (SDK) Quickstart for Windows](https://cloud.google.com/sdk/docs/quickstart-windows)
    * StackOverflow: [Newest gcloud Questions](https://stackoverflow.com/questions/tagged/gcloud)

* My blog I did not prepare for publish: [Google Onboard Cph 2017](https://github.com/rasor/rasor.github.io/blob/pelican/content/2017/GoogleOnboardCph2017.md)
* .NET
    * [Quickstart - Cloud Tools for Visual Studio](https://cloud.google.com/tools/visual-studio/docs/quickstart)
    * [How to run Hello World with .NET](https://cloud.google.com/dotnet/docs/getting-started/hello-world)

The End.
