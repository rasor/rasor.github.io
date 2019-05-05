Title: Neo4j Desktop Graph DB
Date: 2099-01-01 00:00
Category: Develop
Tags: #graphdb, #cypher, #neo4j, #tinkerpop, #python

# Neo4j - editions

On the [Neo4j Download](https://neo4j.com/download-center/) page you have options to download 
* two server versions, 
    * **Enterprise** or 
    * **Community**. You also have option of downloading 
* a **Desktop** version with a **GUI** included.
* A Cypher **CLI** is a separate install.

[Neo4j KB article](https://neo4j.com/developer/kb/using-neo4j-shell-neo4j-ce-3x/) talks about **CLIs**. There you find a handy script for a Neo4j **docker container**. 

I rather want to run Neo4j as container and have a GUI. I think I'll get that option by running the container in interactive mode. Also I want a desktop CLI.  
I also want a SDK for JavaScript and possibly some plugins. You also find the SDK's (called drivers) on the Download page.

# Windows Desktop edition



## Guides

* [2.5. Windows installation](https://neo4j.com/docs/operations-manual/current/installation/windows/)
* [Neo4j Desktop](https://neo4j.com/download-thanks-desktop/?edition=desktop&flavour=windows&release=1.1.21&offline=true)

# Docker Container edition

* [Docker hub](https://neo4j.com/developer/kb/using-neo4j-shell-neo4j-ce-3x/) script

From CMD: (Run as admin)

```bash
# set envir for Neo4j database files - notice folder format is not Linux, though it will be used from GIT BASH
setx NEO_DATA "C:\Users\user\ItData\neodata" /M
# SUCCESS: Specified value was saved.
```

From Git Bash:

```bash
# Download image from docker hub
docker pull neo4j
# ...
# Status: Downloaded newer image for neo4j:latest

# Verify envir
printenv | grep NEO
# NEO_DATA_BASH=C:\Users\user\ItData\neodata

# Create folder for CYPHER CSV imports
cd $NEO_DATA
mkdir import

# Start Docker

# Map a DB data folder and an CSV import folder on your PC for a Neo4j container and start it
# https://neo4j.com/docs/operations-manual/current/docker/introduction/#docker-volumes
CONTAINER=$(docker run -d --name neo4j -p 7474:7474 -v $NEO_DATA:/data -v $NEO_DATA/import:/var/lib/neo4j/import neo4j)
echo "Running Neo4j as $CONTAINER, waiting for startup"
sleep 10

# 
docker ps
# CONTAINER ID        IMAGE                         COMMAND                  CREATED              STATUS              PORTS                                        NAMES
# 95f89a2b0956        neo4j                         "/sbin/tini -g -- /d…"   About a minute ago   Up About a minute   7473/tcp, 7687/tcp, 0.0.0.0:7474->7474/tcp   neo4j

# to import a file from `$NEO_DATA_BASH/import/import.cypher`
# docker exec $CONTAINER /var/lib/neo4j/bin/neo4j-shell -f /var/lib/neo4j/import/import.cypher

# or for interactive mode
docker exec -ti $CONTAINER /var/lib/neo4j/bin/neo4j-shell
# the input device is not a TTY.  If you are using mintty, try prefixing the command with 'winpty'

# Annoying could not connect - the one fix I know is to repeat the command from the PS1 Docker CLI, which you can start from Kitematic or directly from Kitematic
```

From Kitematic:

* Select the **neo4j** container
* Press EXEC icon
    * This will open a PS1 prompt

```ps1
# where are we?
pwd
# /var/lib/neo4j

# What is the version?
./bin/neo4j --version
# neo4j 3.5.5

# now run the shell from here - neo4j-shell is now cypher-shell
./bin/cypher-shell
# enter username+password
```

When you are done with using the DB, you can stop it from GIT BASH

```bash
docker stop neo4j
```

* More info on [Docker Hub](https://hub.docker.com/_/neo4j?tab=description)
* Even more on [Docker - The Neo4j Operations Manual v3.5](https://neo4j.com/docs/operations-manual/current/docker/)
* Tutorial: [Neo4j Data Import: Moving Data from RDBMS to Graph](https://neo4j.com/developer/guide-importing-data-and-etl/)

### Links

* [Neo4j Graph Platform – The Leader in Graph Databases](https://neo4j.com/)

eBooks:

* [Neo4j Books: Free Graph Database Ebooks](https://neo4j.com/books/)
    * [Graph Databases for Beginners - Neo4j Graph Database Platform](https://neo4j.com/whitepapers/graph-databases-beginners-ebook/?ref=home)
    * [O'Reilly Graph Algorithms Book - Neo4j Graph Database Platform](https://neo4j.com/graph-algorithms-book/)


The End