Title: Vue Storefront
Date: 2099-01-01 00:00
Tags: #vue, #magento, #webshop, #seo, #pwa, #openshift, #docker

[Vue Storefront](https://medium.com/@piotrkarwatka/vue-storefront-1-0rc-3-has-arrived-5c770a338d4) will soon be out (june 2018).
It is a PWA frontend to the Magento webshop.  

I think I'll give it a testdrive.  
I am attending a online marketing seminar and workshop presented by [Thomas Zacchi (@tzacchi)](https://twitter.com/tzacchi) from [intoto digital](https://www.intoto.dk/), so it I could use a modern webshop to play with.  

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

1. Install [Docker CE for Windows](https://store.docker.com/editions/community/docker-ce-desktop-windows)  
I installed [Docker4Win here](2018-05-06-Docker4Win.md)  

... InProgress

## Links

### Vue Storefront

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

### Other

* SEO and PWA: [2018 State of PWA](https://medium.com/progressive-web-apps/2018-state-of-progressive-web-apps-f7517d43ba70)
* [Other headless / API first apps](HeadlessApiFirst.md)
* [Other ecommerce projects on GitHub](https://github.com/topics/ecommerce)

### OpenShift 

* [Installing OpenShift](https://rasor.github.io/developing-with-openshift.html)
* [Deploying](https://docs.openshift.org/latest/minishift/getting-started/quickstart.html#deploy-sample-app) to MiniShift

The End