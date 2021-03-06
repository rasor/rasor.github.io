Title: Google Onboard CPH
Date: 2099-01-01 00:00

Visiting [Cloud OnBoard - Copenhagen](https://lp.google-mkto.com/2017-OnBoard-Copenhagen)

* Tweets: #GoogleCloudOnboard
* Presenter: Jerry Javala jerry@qvik.fi
* [Slides](http://go.google-mkto.com/gz024AC0l109PC02T304FH9)
* [Slides - recent?](https://docs.google.com/presentation/d/1QKqBMBDjStbnerGXyNrhd2nw3nPYdNHGfSs3T70kfHU/edit?usp=sharing_eip&ts=59faf77d)
* [Questions](Goo.gl/J79Jqx)
* $3000 [startup discount](Goo.gl/MmNLGG)

I want to follow [Quickstart for Node.js in the App Engine- GCP](https://cloud.google.com/nodejs/getting-started/hello-world)
Code: <https://github.com/GoogleCloudPlatform/nodejs-docs-samples> - [my fork](https://github.com/rasor/nodejs-docs-samples)

* gcloud ref: https://cloud.google.com/sdk/gcloud/reference/  
* GCP console: https://console.cloud.google.com  

So what is needed for a NodeJs webapp to be deployed to GCP?

app.yaml

```yaml
runtime: nodejs
env: flex
```

package.json

```yaml
  "cloud": {
    "msg": "Hello, world!"
  },
  "engines": {
    "node": ">=4.3.2"
  },
  "scripts": {
    "deploy": "gcloud app deploy", 
    "start": "node app.js",
    "lint": "samples lint",
    "pretest": "npm run lint",
    "system-test": "samples test app",
    "test": "npm run system-test",
    "e2e-test": "samples test deploy"
  },
  "dependencies": {
    "express": "4.15.2"
  },
  "devDependencies": {
    "@google-cloud/nodejs-repo-tools": "1.3.1"
  }
 ```

Create a project via App Engine Dashboard
https://console.cloud.google.com/projectselector/appengine/create?lang=nodejs&st=true
You could call it nodeappengdore, which also gives you the url
<https://nodeappengdore.appspot.com>

```bash
gcloud config set compute/zone europe-west3
gcloud config set project nodeappengdore # name-of--your-GCP-proj
```

```bash
git clone https://github.com/rasor/nodejs-docs-samples
cd nodejs-docs-samples/appengine/hello-world
yarn install
start "" "http://localhost:8080"
yarn start
#gcloud app create --region=europe-west3 - already done in browser
gcloud app deploy # takes time ...
# --version=v2 --no-stop-previous-version # Deploy a v2 to serve e.g. 50%
gcloud app browse # as start "" "https://nodeappengdore.appspot.com"
```

You can see your deployed project in the App Engine here 
https://console.cloud.google.com/appengine?project=nodeappengdore
- and projecct here
https://console.cloud.google.com/home/dashboard?project=nodeappengdore
- which shows you also have gotten 5 buckets of storage
https://console.cloud.google.com/storage/browser?project=nodeappengdore
- of which 1 is enabled
https://console.cloud.google.com/storage/browser/staging.nodeappengdore.appspot.com
It seems like the definition of the AppEng is stored in there:
Pushing eu.gcr.io/nodeappengdore/appengine/default.20171102t091459:latest

--------------

So we deployed from local to cloud
HowTo deploy from fork to cloud after this initial setup?
- Container Registry - Build Trigger - Create Trigger - GitHub
https://console.cloud.google.com/gcr/triggers?project=nodeappengdore
You need a cloudbuild.yaml
* [Build Steps - Cloud Container Builder](https://cloud.google.com/container-builder/docs/concepts/build-steps)
* [Writing Build Requests - Cloud Container Builder](https://cloud.google.com/container-builder/docs/how-to/writing-build-requests)
* [Build Steps - Cloud Container Builder](https://cloud.google.com/container-builder/docs/concepts/build-steps)
Guide: https://wildfish.com/blog/2017/03/29/google-cloud-container-builder-introduction/
Example for Guide: https://github.com/wildfish/google-cloud-container-builder-example
Example: https://github.com/GoogleCloudPlatform/cloud-builders/blob/master/nodejs/yarn/cloudbuild.yaml
Example: https://github.com/GoogleCloudPlatform/cloud-builders/blob/master/npm/cloudbuild.yaml
Custom steps: https://cloud.google.com/container-builder/docs/tutorials/creating-a-custom-build-step

https://github.com/GoogleCloudPlatform/cloud-builders

Import from GitHub to internal Repo:
- Source Repos

/*
Seems like you have to import an API via  
https://console.developers.google.com/apis/dashboard?project=nodeappengdore
What to import
https://cloud.google.com/container-registry/docs/continuous-delivery
https://cloudplatform.googleblog.com/2014/09/using-bitbucket-for-push-to-deploy.html
*/


Next they recommend tutorial [Node.js Bookshelf App](https://cloud.google.com/nodejs/getting-started/tutorial-app)

--------------

# Notes

* REST is called Cloud Endpoints. They can be deployed to everywhere in GCP
* Storage
** GC Storage is CDN, when changed to be public available.
** GC Bigtable is NoSQL - HBase API, Streaming or Batch. Use Dev version for play.
** GC SQL - Is MySQL - Machine Size and Storage Size affects throughput heavily
** GC Spanner - Good for distributed DB - also blockchain?
** See quizlet compare
** FireBase or Cloud FireStore
-------------

** kubernetes
*** images from DockerHub
** mesos
** Docker Swarm
** OpenShift

* Container Eng (GKE) is GCK's implementation of Kubernetes
** Guide GKE: https://wildfish.com/blog/2017/03/14/django-google-container-engine-gke/
* Container Builder build images in cloud (instead of locally)
** Guide CB: https://wildfish.com/blog/2017/03/29/google-cloud-container-builder-introduction/
* Container Registry stores project images

Use instead GitLab for builder - can also push to container registry
https://docs.gitlab.com/omnibus/build/prepare-build-environment.html

--------------

* Snapshots for App VM backups. 

* Network
* Use loadbalancer for SSH access to private VM
* VM can have set RDP for access

* Cloud Launcher - ready apps in VMs
- Using Deployment Manager via yaml files.


--------------

* Qwik labs

Links:

* [Google Developer Days](https://developers.google.com/events/gdd-europe/)
* [CodeLab](https://codelabs.developers.google.com/)
* [Training](https://cloud.google.com/training/)
* [GCP Calculator](https://cloud.google.com/products/calculator/)
* Latency from where you are: <http://www.gcping.com/>
* APIs: <https://developers.google.com/apis-explorer/#p/>
* [GCP Free Tier - Google Cloud Platform](https://cloud.google.com/free/?utm_term=outbound-team)
* [Node JS on GCP](https://cloud.google.com/nodejs/)
* [Node.js docs on GCP](https://cloud.google.com/nodejs/docs/)
* [Firebase](https://firebase.google.com/)
* [Running the Node.js Bookshelf on Container Engine - GCP](https://cloud.google.com/nodejs/tutorials/bookshelf-on-container-engine)
* https://github.com/rasor/awesome-tables/blob/master/awesome-cli-js.md
* [GDG Meetups](https://www.meetup.com/pro/gdg/)

The End