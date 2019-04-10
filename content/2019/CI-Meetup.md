Title:  CI meetup-2019
Date: 2099-01-01 00:00
Category: DevOp
Tags: #ci, 

## CI meetup 2019

* Meetup: [Next-gen CI night](https://www.meetup.com/Cloud-Native-Copenhagen/events/258922126/)

## 17:30 Gitlab CI intro by Markus Suonto

Working @Eficode ROOT - currently @Tryg

* [Markus Suonto (@marextw) | Twitter](https://twitter.com/marextw)
* [suonto - Overview](https://github.com/suonto)
* PuTTY to get VNCViewer
* VNCViewer to enter workstation

### .gitlab-ci.yaml

```yaml
stages:
    - build
    - test
build:
    services:
        - docker:dind # docker in docker 
    script:
        - docker build ...
        - docker login ...
        - docker push ...
    only:
        changes:
            - Dockerfile
            - src/*
            - html/*
test:
    image: docker:stable
    stage: test
    services:
        - docker:dind # docker in docker 
    script:
        - docker login
        - xxx
    coverage: 'xxxx'
```

* Stages can be set to run in parallel!

```bash
workon demo
```

* Gitlab pipelines don't break like in Jenkins

Tips:

* [GitLab CI/CD Pipeline Configuration Reference | GitLab](https://docs.gitlab.com/ee/ci/yaml/#onlychangesexceptchanges)
* Marcus Blog: [The Fab 5 for GitLab CI](https://www.eficode.com/blog/gitlab-ci)

## 17:50 Spinakker.io intro by Hans Duedal

Works @Visma

* [Hans Duedal (@hansduedal) | Twitter](https://twitter.com/hansduedal)
* Get slides: [Spinnaker Intro](https://docs.google.com/presentation/d/165NTYXDW2cfdw8E5HGz_Y2jkRy9zPogSlE3Srb7M9cM/edit)
* Is not a CI tool..
* Blue/green deployments (called red/black)
* eBook: [Continuous Delivery With Spinnaker](https://www.spinnaker.io/publications/ebook/)

### Pipelines Stages

36 different pipeline stages...

* Stage: Bake
* Stage: Deployment
* Stage: Jenkins
* Stage: Webhook
* Stage: Canary - Analyse - roll back

### Infrastructure

* Can see multi cloud
* Load Balancers / k8s: services, ingresses

### Architecture

* Runs on microservices

### Caveats

* CPU hungry - timeouts happens
* Consider use armory.io

## 18:10 Drone CI intro by Laszlo Fogas

* [Laszlo Fogas (@laszlocph) | Twitter](https://twitter.com/laszlocph)
* Slides: [Drone CI intro](https://docs.google.com/presentation/d/12cZ0B9axdQ-EWs4SJMC28-MB2bOHhRV0rErx863sLiE/edit#slide=id.p)

```yaml
pipeline:
    npm-install:
        image: xxx
        commands: - npm install
    test:
        image: xxx
    buld:
        image: xxx
        secrets: [ docler_username, docker_psw]
        when: master #condition
        event: push

```

* Each step run in a container
* Plugin support - they are only bash scripts you copy into..
* Used by falcon.io
* Drone 1.0 just released
    * Multi machine pipeline
    * Jsonnet based yaml generation
    * No native k8s backen
* Licensing
    * Enterprise
    * OSS - too little features....
* cloud.drone.io SaaS

Laszlo forked 0.8 !!! So you don't have the License problems :-)

* [laszlocph/tsdbinfo](https://github.com/laszlocph/tsdbinfo)
    * [laszlocph/tsdbinfo](https://github.com/laszlocph/tsdbinfo/blob/master/.drone.yml)

## 18:30 Circle CI intro by Christian Palmhøj Nielsen

* [Christian Palmhøj Nielsen (@cpnielsen) | Twitter](https://twitter.com/cpnielsen)
* Slides: [CircleCI-intro.pdf](https://drive.google.com/file/d/1yK08uE7o9pW6B6MMnOnLpxve1RJv9-SZ/view)

The End