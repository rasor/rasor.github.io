Title: Vue Storefront installation on Windows Dev box
Status: published
Date: 2018-05-15 23:00
Modified: 2018-08-18 19:00
Category: DevOp
Tags: #vue, #magento, #webshop, #seo, #pwa, #docker, #git, #yarn, #npm, #nvm

[Vue Storefront](https://medium.com/@piotrkarwatka/vue-storefront-1-0rc-3-has-arrived-5c770a338d4) will soon be out (june 2018).
It is a PWA frontend to the Magento webshop.  

I think I'll give it a testdrive.  
I am attending a online marketing seminar and workshop presented by [Thomas Zacchi (@tzacchi)](https://twitter.com/tzacchi) from [intoto digital](https://www.intoto.dk/), so I could use a modern webshop to play with.  

## Initial thoughts about installation

I think I'll deploy Magento to a cheap PHP webhotel I have and then at another time roll it out as a Docker container.  
[bitnami/magento/](https://hub.docker.com/r/bitnami/magento/) looks good for test - it proposes a data volume with MariaDB.  
Vue Storefront could just as well be served from the same container as Magento.  

But hey - I won't need it neither front nor back deployed - I only want to play. Then instead I'll serve it in MiniShift from my PC.  

## Got a little wiser

In the article  ["Magento2 - NoSQL database and PWA support"](https://www.linkedin.com/pulse/magento2-nosql-database-pwa-support-piotr-karwatka/) [Piotr Karwatka (@piotrkarwatka)](https://twitter.com/piotrkarwatka) explains there is a little more the setup than a Vue frontend and a Magento backend.  
There seems to be two chains that works something like  

* OLTP chain: [VueFront](https://github.com/DivanteLtd/vue-storefront) -> [ExpressApiBack](https://github.com/DivanteLtd/vue-storefront-api) -> ElasticSearch or MongoDB container 
* Sync with Magento chain: [KueWorker](https://github.com/Automattic/kue) -> KueBack(Redis) container ->  [Mage2VueFront](https://github.com/DivanteLtd/mage2vuestorefront) -> ElasticSearch or MongoDB <-> Magento DB  

The model of VueFront the data apparently is great for NoSQL storage and querying, which supposedly scales better than the models used in SQL (which the Magento DB uses).  
So I guess we for the dev envir again are down to three containers:  

* Vue apps: VueFront, ExpressApiBack, KueWorker, Mage2VueFront
* Vue storage: Redis, ElasticSearch or MongoDB
* Magento app, Magento DB

If we for a quick start skip the sync chain, then [data can be fetched](https://github.com/DivanteLtd/vue-storefront/blob/master/doc/Installing%20on%20Linux%20and%20MacOS.md#install-the-vue-storefront-api) from [magento2-sample-data](https://github.com/magento/magento2-sample-data)  
Let's see if that is doable.

## [Installing on Windows](https://github.com/DivanteLtd/vue-storefront/blob/master/doc/Installing%20on%20Windows.md)

### Prerequisites

1. Install [Git for Windows](https://git-scm.com/downloads) - This will install `Git Bash`
    1. Optional Install [cUrl CLI on Windows](https://rasor.github.io/curl-cli-on-windows.html) - This will ensure that you can call a remote end over SSL
2. Install [Docker CE for Windows](https://store.docker.com/editions/community/docker-ce-desktop-windows). 
    1. I installed [Docker4Win here](2018-05-06-Docker4Win.md)  
    2. Moore info: [Running Docker containers on Bash on Windows](https://blog.jayway.com/2017/04/19/running-docker-on-bash-on-windows/)
3. If you use VS Code you could install [Docker Support for VSCode](https://marketplace.visualstudio.com/items?itemName=PeterJausovec.vscode-docker) 
4. Install [NVM for Windows, Node.js and Yarn](https://rasor.github.io/using-nvm-for-windows-and-yarn.html) 
5. Install [vue-cli](https://www.npmjs.com/package/vue-cli)  
```bash
# print installed node versions
nvm list

# At time of writing vue-cli 3 is still in beta, so I choose an old one
#nvm install 8.11.1
nvm use 8.11.1 
npm install -g vue-cli@2.9.3
vue --version
# Test drive
vue list
cd .\your-vue-root\
vue init webpack-simple my-29project
cd my-29project
code . #if you are using VS Code editor
npm install
npm run dev # Opens http://localhost:8080/

# When vue-cli 3 comes out I want to have that cli together with another node version - notice - the cli changed name @npm
#nvm install 10.1.0
nvm use 10.1.0
npm install -g @vue/cli@3.0.0-beta.10
vue --version
# Test drive
cd .\your-vue-root\
vue create my-30project
```  
    1. v2.9.3 [vue-cli](https://github.com/vuejs/vue-cli/tree/master) intro
    2. v3.0. [@vue/cli](https://github.com/vuejs/vue-cli/blob/dev/docs/README.md#introduction) intro
6. If you use VSCode you could install [Vetur](https://marketplace.visualstudio.com/items?itemName=octref.vetur) - Vue tooling for VSCode for syntax highlight and snippets
7. If you use Chrome you need [Vue.js devtools](https://chrome.google.com/webstore/detail/vuejs-devtools/nhdogjmejiglipccpnnnanhbledajbpd?hl=en) for debugging
    1. The devtools has **Open in editor** button to bring you back to the code. check out [What’s new in Vue Devtools 4.0](https://medium.com/the-vue-point/whats-new-in-vue-devtools-4-0-9361e75e05d0), which also points you to this [setup guide](https://github.com/vuejs/vue-devtools/blob/master/docs/open-in-editor.md)


### Install Vue Storefront

There are two parts

* the Express API including a Docker container for the data
* the Vue frontend

#### VS API

1. Start Docker VM by double-click on the desktop icon. This takes a while
2. Install VS API  
From GitBash:
```bash
cd .\your-vue-root\
git clone https://github.com/DivanteLtd/vue-storefront-api.git vue-storefront-api
cd vue-storefront-api
# Fetch dependencies
yarn
```
3. Load you docker VM with containers from docker-compose.yaml  
From CMD prompt:
```bash
# login to docker - this did not work from GitBash, but did from CMD
docker login -u yourUseridNotYourEmail -p yourPassword
# Run Docker containers required by vue-storefront-api. This can take a while ...
docker-compose up
# this CMD promt won't return the promt. It is probably a Daemon now, so switch back to GitBash
```
4. Load the Docker data containers with data  
From GitBash:
```bash
# Verify that the containers are running
docker network ls
# Open browser for Elastic Search (es1) container
start http://localhost:9200/
# Restore products database (yarn restore) and run latest migrations (yarn migrate)
yarn restore
yarn migrate
```
5. Copy `config/default.json` to `config/local.json`
6. Add [.\.vscode\launch.json](https://gist.github.com/rasor/6eb9293a025ae919d66a31a8f8bdcb3d) to the project
7. Edit package.json - change:  
```yaml
  "scripts": {
    "dev": "nodemon -w src --exec \"babel-node src --presets es2015,stage-0\"",
```  
to (add --inspect)  
```yaml
  "scripts": {
    "dev": "nodemon --inspect -w src --exec \"babel-node src --presets es2015,stage-0\"",
```
8. Run API using `yarn dev`
9. Verify API is running  
start http://localhost:8080/api/  
Response:  `{"version":"0.1.0"}`
10. Debug the API from VSCode by setting breakpoints and press `play Attach` on the Debug tab.

#### VS Frontend

1. Install VS API  
From GitBash 2:
```bash
cd .\your-vue-root\
git clone https://github.com/DivanteLtd/vue-storefront.git vue-storefront
cd vue-storefront
# Fetch dependencies
yarn install
```
2. Copy `config/default.json` to `config/local.json`
3. Images: because vue-storefront-api uses `imagemagick` and some nodejs cmdline bindings it can be dificult to run the image proxy on localhost/windows machine. Please point out the vue-storefront to image proxy provided by changing `config/local.json` images.baseUrl:

```js
export default {
  elasticsearch: {
    httpAuth: '',
    host: 'localhost:8080/api/catalog',
    index: 'vue_storefront_catalog'
  },
  // we have vue-storefront-api (https://github.com/DivanteLtd/vue-storefront-api) endpoints below:
  orders: {
    endpoint: 'localhost:8080/api/order/create'
  },
  images: {
    baseUrl: 'https://demo.vuestorefront.io/img/'
  }
}
```
5. Run Vue Storefront Server using `yarn dev`
6. Verify Fronteend is running  
start http://localhost:3000/  

You will see a [PWA](https://medium.com/@deepusnath/4-points-to-keep-in-mind-before-introducing-progressive-web-apps-pwa-to-your-team-8dc66bcf6011) webshop
[![Vue Storefront](img/2018/2018-05-15-VueStore1.PNG)](https://demo.vuestorefront.io/)  

The shop is reponsive  
[![Vue Storefront](img/2018/2018-05-15-VueStore2.PNG)](https://demo.vuestorefront.io/)

And images resizes to small, when devices are very small  
[![Vue Storefront](img/2018/2018-05-15-VueStore3.PNG)](https://demo.vuestorefront.io/)

## Turn off Vue Storefront

1. Frontend - in GitBash-2 is just a PWA server - there is nothing to save - just `X` it
2. API - in GitBash-1 is just an API server - there is nothing to save - just `X` it
3. Now what about the CMD and the VM? You need to tell the containers in the VM to close down and then close down the VM.
    * Start a new GitBash-3  
```bash
# Verify containers are there
docker container ls
```

Output: 
```
CONTAINER ID   IMAGE               COMMAND                  CREATED       STATUS       PORTS                              NAMES
fcd38fe4910e   kibana:5.5          "/docker-entrypoint.…"   2 hours ago   Up 2 hours   0.0.0.0:5601->5601/tcp             vue-storefront-api_kibana_1
070f93cc3a08   redis               "docker-entrypoint.s…"   2 hours ago   Up 2 hours   0.0.0.0:6379->6379/tcp             vue-storefront-api_redis_1
a3fec0cc4f2b   elasticsearch:5.5   "/docker-entrypoint.…"   2 hours ago   Up 2 hours   9200/tcp, 9300/tcp                 vue-storefront-api_es2_1
56caf26862c4   elasticsearch:5.5   "/docker-entrypoint.…"   2 hours ago   Up 2 hours   0.0.0.0:9200->9200/tcp, 9300/tcp   es1
```

Hmm - this is part of the [ELK Stack: Elasticsearch, Logstash, Kibana](https://www.elastic.co/elk-stack) and the Redis needed for sync with Magento is also there, so perhaps it is ready to connect to a real Magento installation.

```bash
cd .\your-vue-root\
cd vue-storefront-api
# Turn off the containers
docker-compose stop
```

Output:
```
Stopping vue-storefront-api_kibana_1 ... done
Stopping vue-storefront-api_redis_1  ... done
Stopping vue-storefront-api_es2_1    ... done
Stopping es1                         ... done
```

The CMD promt will display this, so you can close it.
```
redis_1   | 1:signal-handler (1526416098) Received SIGTERM scheduling shutdown...
redis_1   | 1:M 15 May 20:28:18.957 # User requested shutdown...
redis_1   | 1:M 15 May 20:28:19.142 * Saving the final RDB snapshot before exiting.
es2_1     | [2018-05-15T20:28:19,274][INFO ][o.e.n.Node               ] [J8Lto-u] stopping ...
es1       | [2018-05-15T20:28:19,271][INFO ][o.e.n.Node               ] [sH31WJW] stopping ...
redis_1   | 1:M 15 May 20:28:19.306 * DB saved on disk
redis_1   | 1:M 15 May 20:28:19.306 # Redis is now ready to exit, bye bye...
es1       | [2018-05-15T20:28:19,444][INFO ][o.e.n.Node               ] [sH31WJW] stopped
es1       | [2018-05-15T20:28:19,444][INFO ][o.e.n.Node               ] [sH31WJW] closing ...
es2_1     | [2018-05-15T20:28:19,473][INFO ][o.e.n.Node               ] [J8Lto-u] stopped
es2_1     | [2018-05-15T20:28:19,473][INFO ][o.e.n.Node               ] [J8Lto-u] closing ...
es1       | [2018-05-15T20:28:19,509][INFO ][o.e.n.Node               ] [sH31WJW] closed
es2_1     | [2018-05-15T20:28:19,509][INFO ][o.e.n.Node               ] [J8Lto-u] closed
vue-storefront-api_es2_1 exited with code 143
vue-storefront-api_redis_1 exited with code 0
vue-storefront-api_kibana_1 exited with code 143
es1 exited with code 143
```

4. Optionally Close Docker from the taskbar-notification-icon: Select `Quit`

## Startup scripts

I've created [three scripts](https://gist.github.com/rasor/a3e6e6d6fd824685956d922a3de55b63) that does the above startup.  
You can put them in `\your-vue-root\` and just double-click on them to start up VueStorefront. They are:

* vsapi1.bat
* vsapi2.sh
* vs3.sh

Note: 

* You must set Git Bash to open extension .sh for this to work
* You must start them in above order and wait patiently for each part to start before you continue with the next script

## Whats next?

* You can customize your frontend theme and change the behavior (code)
* You can install Magento at some host and configure your shop to go towards it
* You can deploy your shop

----------------

# Links

## Vue Storefront

### 4 - Vue Storefront - People

* [vuestorefront.slack.com](https://vuestorefront.slack.com/messages/DAP34PT8U/)
* [Vue Storefront (@VueStorefront) | Twitter](https://twitter.com/VueStorefront)
* [Piotr Karwatka (@piotrkarwatka) | Twitter](https://twitter.com/piotrkarwatka)
* [Filip Rakowski (@filrakowski) | Twitter](https://twitter.com/filrakowski)

### 1 - Vue Storefront - Events

* 2018 May [Vue Storefront Hackathon, 1.0 STABLE, case studies – Piotr Karwatka – Medium](https://medium.com/@piotrkarwatka/vue-storefront-hackathon-1-0-stable-case-studies-29406050727a)
* 2018 May [Wro Open Source 2018](http://go.divante.co/wro-open-source/#lp-pom-block-1029)

### 2 - Vue Storefront - Github issues

* [vue-storefront issues](https://github.com/DivanteLtd/vue-storefront/issues?q=is%3Aopen+is%3Aissue+label%3Avs-hackathon)

### 3 - Vue Storefront - Learn 

* eBook (2018, 122 pages): [Microservices Architecture for eCommerce](http://go.divante.co/microservices-architecture-ecommerce/)  
* [Vue Storefront - YouTube](https://www.youtube.com/channel/UCkm1F3Cglty3CE1QwKQUhhg)
* Blog: -> 2018.01.31 [Vue Storefront — how to install and integrate with Magento2](https://medium.com/@piotrkarwatka/vue-storefront-how-to-install-and-integrate-with-magento2-227767dd65b2)
* Blog: 2018.01.04 [How to connect 3rd party platform to Vue Storefront?](https://medium.com/@piotrkarwatka/how-to-connect-3rd-party-platform-to-vue-storefront-df9cb30779f6)
* Slides: 2018.02.26 [Vue Storefront Basics - Why we created Vue Storefront and how it works](https://www.slideshare.net/FilipRakowski/vue-storefront-basics)

* vue: PWA front, Magento back [DivanteLtd/vue-storefront](https://github.com/DivanteLtd/vue-storefront)
    * Demo: [Home Page - Vue Storefront](https://demo.vuestorefront.io/)
* [Installing on Windows](https://github.com/DivanteLtd/vue-storefront/blob/master/doc/Installing%20on%20Windows.md)
* [Installing on Linux and MacOS](https://github.com/DivanteLtd/vue-storefront/blob/master/doc/Installing%20on%20Linux%20and%20MacOS.md)
* [Magento2 - NoSQL database and PWA support](https://www.linkedin.com/pulse/magento2-nosql-database-pwa-support-piotr-karwatka/)
* [FAQ and Receipes](https://github.com/DivanteLtd/vue-storefront/blob/master/doc/FAQ%20and%20Receipes.md)
* [Project structure](https://github.com/DivanteLtd/vue-storefront/blob/master/doc/Project%20structure.md)
* [Config file format for vue storefront](https://github.com/DivanteLtd/vue-storefront/wiki/Config-file-format-for-vue-storefront)
* [More docs...](https://github.com/DivanteLtd/vue-storefront/tree/master/doc)

## Vue

### Vue Libs

* vue [shopping-carts](https://github.com/topics/shopping-cart?l=vue)
* [vue-bulma/nprogress](https://github.com/vue-bulma/nprogress)
* [vue-tags](https://www.npmjs.com/package/vue-tags)

### Vue - Learn

* [Installation — Vue.js](https://vuejs.org/v2/guide/installation.html)
* [Build Async Vue.js Apps with RxJS](https://egghead.io/courses/build-async-vue-js-apps-with-rxjs?utm_source=drip&utm_medium=email&utm_campaign=may2018&utm_term=vue&utm_content=build-async-vue-js-apps-with-rxjs)

## Other

* [front-end-performance-checklist-2018.pdf](https://www.dropbox.com/s/8h9lo8ee65oo9y1/front-end-performance-checklist-2018.pdf?dl=0)
* SEO and PWA: [2018 State of PWA](https://medium.com/progressive-web-apps/2018-state-of-progressive-web-apps-f7517d43ba70)
* [Other headless / API first apps](HeadlessApiFirst.md)
* [Other ecommerce projects on GitHub](https://github.com/topics/ecommerce)
* My [list of npm installs locally](https://github.com/rasor/awesome-tables/blob/master/awesome-cli-js.md#nvm-sets-of-tools---avoiding-version-conficts)

### OpenShift 

* [Installing OpenShift](https://rasor.github.io/developing-with-openshift.html)
* [Deploying](https://docs.openshift.org/latest/minishift/getting-started/quickstart.html#deploy-sample-app) to MiniShift

The End
