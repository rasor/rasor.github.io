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

# longer command - table gives header and fixed witdh, jaon gives values in quotes
docker container ls --format="table {{json .Image}}\t{{json .Status}}"
# IMAGE                           STATUS
# "openfaas/queue-worker:0.7.1"   "Up About an hour"
# "openfaas/gateway:0.11.1"       "Up About an hour"
# "nats-streaming:0.11.2"         "Up About an hour"
# "prom/alertmanager:v0.16.1"     "Up About an hour"
# "prom/prometheus:v2.7.1"        "Up About an hour"
# "openfaas/faas-swarm:0.6.1"     "Up About an hour"

# Convert all to json and select only some of the fields
docker container ls --format " {{json .}}" | jq '{ID, Image, Status}'
# {
#   "ID": "f56f6b94ab0f",
#   "Image": "prom/alertmanager:v0.16.1",
#   "Status": "Up 3 hours"
# }
# {
#   "ID": "b5a0f2cb0301",
#   "Image": "openfaas/queue-worker:0.7.1",
#   "Status": "Up 3 hours"
# }
# {
#   "ID": "7ec750aaa815",
#   "Image": "openfaas/faas-swarm:0.6.1",
#   "Status": "Up 3 hours"
# }
# {
#   "ID": "b58c1c59baad",
#   "Image": "prom/prometheus:v2.7.1",
#   "Status": "Up 3 hours"
# }
# {
#   "ID": "086e253e4e68",
#   "Image": "nats-streaming:0.11.2",
#   "Status": "Up 3 hours"
# }
# {
#   "ID": "a1a3381a45cf",
#   "Image": "openfaas/gateway:0.11.1",
#   "Status": "Up 3 hours"
# }
```

# Links

* [Awesome CLI - on Windows - Tools](https://github.com/rasor/awesome-tables/blob/master/awesome-cli-on-windows.md#tools)
* [jq Manual](https://stedolan.github.io/jq/manual/#TypesandValues)

The End