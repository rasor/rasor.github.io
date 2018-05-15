Title: Vue Storefront
Date: 2099-01-01 00:00
Tags: #vue, #magento, #webshop, #seo, #pwa, #openshift, #docker

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

* OLTP chain: [VueFront](https://github.com/DivanteLtd/vue-storefront) -> [ExpressApiBack](https://github.com/DivanteLtd/vue-storefront-api) -> ElasticSearch or MongoDB  
* Sync with Magento chain: [KueWorker](https://github.com/Automattic/kue) -> KueBack(Redis) ->  [Mage2VueFront](https://github.com/DivanteLtd/mage2vuestorefront) -> ElasticSearch or MongoDB <-> Magento DB  

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
* Optional Install [cUrl CLI on Windows](https://rasor.github.io/curl-cli-on-windows.html) - This will ensure that you can call a remote end over SSL
2. Install [Docker CE for Windows](https://store.docker.com/editions/community/docker-ce-desktop-windows).  
Moore info: [Running Docker containers on Bash on Windows](https://blog.jayway.com/2017/04/19/running-docker-on-bash-on-windows/)
I installed [Docker4Win here](2018-05-06-Docker4Win.md)  
3. Install [NVM for Windows, Node.js and Yarn](https://rasor.github.io/using-nvm-for-windows-and-yarn.html) 
4. Install [vue-cli](https://www.npmjs.com/package/vue-cli)  
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
vue create my-30project
```  
  * v2.9.3 [vue-cli](https://github.com/vuejs/vue-cli/tree/master) intro
  * v3.0. [@vue/cli](https://github.com/vuejs/vue-cli/blob/dev/docs/README.md#introduction) intro
5. If you use VS Code install: [Vetur](https://marketplace.visualstudio.com/items?itemName=octref.vetur) - Vue tooling for VS Code

### Vue Storefront

... InProgress

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

* [Vue Storefront - YouTube](https://www.youtube.com/channel/UCkm1F3Cglty3CE1QwKQUhhg)
* Blog: -> 2018.01.31 [Vue Storefront — how to install and integrate with Magento2](https://medium.com/@piotrkarwatka/vue-storefront-how-to-install-and-integrate-with-magento2-227767dd65b2)
* Blog: 2018.01.04 [How to connect 3rd party platform to Vue Storefront?](https://medium.com/@piotrkarwatka/how-to-connect-3rd-party-platform-to-vue-storefront-df9cb30779f6)
* Slides: 2018.02.26 [Vue Storefront Basics - Why we created Vue Storefront and how it works](https://www.slideshare.net/FilipRakowski/vue-storefront-basics)

* vue [shopping-carts](https://github.com/topics/shopping-cart?l=vue)
* vue: PWA front, Magento back [DivanteLtd/vue-storefront](https://github.com/DivanteLtd/vue-storefront)
  * Demo: [Home Page - Vue Storefront](https://demo.vuestorefront.io/)
* [Vue Storefront (@VueStorefront)](https://twitter.com/VueStorefront)
* [Installing on Windows](https://github.com/DivanteLtd/vue-storefront/blob/master/doc/Installing%20on%20Windows.md)
* [Installing on Linux and MacOS](https://github.com/DivanteLtd/vue-storefront/blob/master/doc/Installing%20on%20Linux%20and%20MacOS.md)
* [Magento2 - NoSQL database and PWA support](https://www.linkedin.com/pulse/magento2-nosql-database-pwa-support-piotr-karwatka/)
* [Config file format for vue storefront](https://github.com/DivanteLtd/vue-storefront/wiki/Config-file-format-for-vue-storefront)
* [FAQ and Receipes](https://github.com/DivanteLtd/vue-storefront/blob/master/doc/FAQ%20and%20Receipes.md)
* [More docs...](https://github.com/DivanteLtd/vue-storefront/tree/master/doc)

## Vue

### Vue Libs

* [vue-bulma/nprogress](https://github.com/vue-bulma/nprogress)
* [vue-tags](https://www.npmjs.com/package/vue-tags)

### Vue - Learn

* [Build Async Vue.js Apps with RxJS](https://egghead.io/courses/build-async-vue-js-apps-with-rxjs?utm_source=drip&utm_medium=email&utm_campaign=may2018&utm_term=vue&utm_content=build-async-vue-js-apps-with-rxjs)

## Other

* [front-end-performance-checklist-2018.pdf](https://www.dropbox.com/s/8h9lo8ee65oo9y1/front-end-performance-checklist-2018.pdf?dl=0)
* SEO and PWA: [2018 State of PWA](https://medium.com/progressive-web-apps/2018-state-of-progressive-web-apps-f7517d43ba70)
* [Other headless / API first apps](HeadlessApiFirst.md)
* [Other ecommerce projects on GitHub](https://github.com/topics/ecommerce)
* My [list of npm installs locally](https://github.com/rasor/awesome-tables/blob/master/awesome-angular-tables.md)

### OpenShift 

* [Installing OpenShift](https://rasor.github.io/developing-with-openshift.html)
* [Deploying](https://docs.openshift.org/latest/minishift/getting-started/quickstart.html#deploy-sample-app) to MiniShift

The End