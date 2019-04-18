Title:  OpenFaaS Cleanup
Date: 2099-01-01 00:00
Category: Develop
Tags: #openfaas, #docker

## OpenFaaS Cleanup

After having started [OpenFaaS on Windows Devbox](https://rasor.github.io/openfaas-on-windows-devbox.html) then Swarm will start new containers each time Docker On Windows (DoW) starts.  
This means you end up with a lot of containers which have been exited.  
So howto get rid of all the OpenFaaS exited images?

```bash
# Print images - tab delimted
docker container ls --format="{{ .Image}}\t{{ .Status}}"
# openfaas/queue-worker:0.7.1     Up About an hour
# openfaas/gateway:0.11.1 Up About an hour
# nats-streaming:0.11.2   Up About an hour
# prom/alertmanager:v0.16.1       Up About an hour
# prom/prometheus:v2.7.1  Up About an hour
# openfaas/faas-swarm:0.6.1       Up About an hour

# longer command - 
docker container ls --format="table {{json .Image}}\t{{json .Status}}"
```

The End