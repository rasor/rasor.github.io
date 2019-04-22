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

# where status=exited and Networks=func_functions
# select ID, Image, Status
docker container ls --filter "status=exited" --format " {{json .}}" | jq '.' --slurp | jq '.[] | select(.Networks == "func_functions")' | jq '{ID, Image, Status}'

# Convert to JSON array
# where status=exited and Networks contains func_functions
# select json objs containing Networks
# pick valus of Networks
docker container ls --filter "status=exited" --format " {{json .}}" | jq '.' --slurp | jq '.[] | select(.Networks | contains("func_functions"))' | jq '{Networks}'  | jq '.Networks'

# foreach object execute
# execute echo --someswitch <network> 
docker container ls --filter "status=exited" --format " {{json .}}" | jq '.' --slurp | jq '.[] | select(.Networks | contains("func_functions"))' | jq '.Networks' | xargs -L1 echo '--someswitch'

# remove exited containers - not working - why??
docker container ls --filter "status=exited" --format " {{json .}}" | jq '.' --slurp | jq '.[] | select(.Networks | contains("func_functions"))' | jq -r '.ID' | xargs -L1 docker container rm
# Error: No such container: e4e419c18314

# without jq
docker ps --filter "status=exited" | grep 'weeks ago' | awk '{print $1}' | xargs --no-run-if-empty docker rm

# Remove all stopped containers
docker container prune

# Remove orphaned volumes and stopped containers, images and networks
docker system prune

# what is left?
docker ps -a
```

# Links

* [How to remove old Docker containers](https://stackoverflow.com/a/17237701/750989)
* [How I filter and grep Docker](https://medium.freecodecamp.org/how-i-filter-and-grep-docker-containers-images-and-volumes-and-how-you-can-too-a60e52bf7784)
* [docker ps - Filtering](https://docs.docker.com/engine/reference/commandline/ps/#filtering)
* [Examples using grep](http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_04_02.html)
* [Awesome CLI - on Windows - Tools](https://github.com/rasor/awesome-tables/blob/master/awesome-cli-on-windows.md#tools)
* [jq Manual](https://stedolan.github.io/jq/manual/#TypesandValues)
* [Using jq with bash to run command for each object in array](https://stackoverflow.com/questions/43192556/using-jq-with-bash-to-run-command-for-each-object-in-array)
* [How to transform JSON to CSV using jq](https://medium.freecodecamp.org/how-to-transform-json-to-csv-using-jq-in-the-command-line-4fa7939558bf)
* [kislyuk/yq - jq wrapper for YAML and XML documents](https://github.com/kislyuk/yq)

The End
