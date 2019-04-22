Title:  Graph DBs
Date: 2099-01-01 00:00
Category: Develop
Tags: #graphdb, #gremlin, #neo4j, #tinkerpop

## Graph DBs

* Language: [Gremlin (programming language) - Wikipedia](https://en.wikipedia.org/wiki/Gremlin_(programming_language))
* Framework: [Apache TinkerPop](http://tinkerpop.apache.org/)
    * Community: [Google Grupper](https://groups.google.com/forum/#!forum/gremlin-users)
* [DB-Engines Ranking](https://db-engines.com/en/ranking/graph+dbms)

### Neo4j

* [Neo4j Graph Platform – The Leader in Graph Databases](https://neo4j.com/)
    * eBook: [Neo4j Graph Platform – The Leader in Graph Databases](https://neo4j.com/)
    * eBook: [Graph Databases for Beginners - Neo4j Graph Database Platform](https://neo4j.com/whitepapers/graph-databases-beginners-ebook/?ref=home)

### Azure Cosmos DB

* [Introduction to Azure Cosmos DB Gremlin API](https://docs.microsoft.com/en-us/azure/cosmos-db/graph-introduction)
    * Gremlin.NET on GitHub [apache/tinkerpop](https://github.com/apache/tinkerpop/tree/master/gremlin-dotnet)
        * [Build an Azure Cosmos DB .NET Framework or Core application using the Gremlin API](https://docs.microsoft.com/en-us/azure/cosmos-db/create-graph-dotnet)
    * Gremlin-JavaScript on GitHub [jbmusso/gremlin-javascript](https://github.com/jbmusso/gremlin-javascript)
        * [Build an Azure Cosmos DB Node.js application by using Gremlin API](https://docs.microsoft.com/en-us/azure/cosmos-db/create-graph-nodejs)
    * Gremlin-Python on GitHub [apache/tinkerpop](https://github.com/apache/tinkerpop/tree/master/gremlin-python)
        * [Quickstart: Gremlin API with Python - Azure Cosmos DB](https://docs.microsoft.com/en-us/azure/cosmos-db/create-graph-python)
    * Gremlin console [TinkerPop Documentation](https://tinkerpop.apache.org/docs/current/reference/#gremlin-console)
* [Azure Cosmos DB tutorial: Create, query, and traverse in Apache TinkerPops Gremlin Console](https://docs.microsoft.com/en-us/azure/cosmos-db/create-graph-gremlin-console)

### Local

* [bricaud/gremlin-server](https://github.com/bricaud/gremlin-server)

```bash
git clone https://github.com/bricaud/gremlin-server
cd gremlin-server

# Build gremlin container
# docker build -t gremlin-container .
# or pull it from https://hub.docker.com/r/bricaud/gremlin-server/
docker pull bricaud/gremlin-server

# Start container -  graphson file will be saved in the home directory ~/
# If you build then run
docker run -p 8182:8182 -v ~/:/graph_file -it --name gremlin gremlin-container
# If you pulled then run
docker images | grep gremlin
# bricaud/gremlin-server         latest              50bf58cf4261        2 months ago        431MB
docker run -p 8182:8182 -v ~/:/graph_file -it --name gremlin bricaud/gremlin-server
# the input device is not a TTY.  If you are using mintty, try prefixing the command with 'winpty'
```

To avoid above error use instead docker powershell cli, which you can start from inside Kitematic
```ps1
docker run -p 8182:8182 -v ~/:/graph_file -it --name gremlin bricaud/gremlin-server
# LANG=C.UTF-8
# HOSTNAME=4a20ddaeb14a
# JAVA_HOME=/usr/lib/jvm/java-1.8-openjdk
# JAVA_VERSION=8u191
# PWD=/gremlin/apache-tinkerpop-gremlin-server-3.4.0
# HOME=/root
# TERM=xterm
# SHLVL=1
# PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin
# JAVA_ALPINE_VERSION=8.191.12-r0
# _=/usr/bin/env
# starting gremlin-server
# [INFO] GremlinServer - 3.4.0
#          \,,,/
#          (o o)
# -----oOOo-(3)-oOOo-----

# [INFO] GremlinServer - Configuring Gremlin Server from gremlin-conf.yaml
# [INFO] MetricManager - Configured Metrics Slf4jReporter configured with interval=180000ms and loggerName=org.apache.tinkerpop.gremlin.server.Settings$Slf4jReporterMetrics
# [INFO] DefaultGraphManager - Graph [graph1] was successfully configured via [gremlin-graph-main.properties].
# [INFO] ServerGremlinExecutor - Initialized Gremlin thread pool.  Threads in pool named with pattern gremlin-*
# [INFO] ServerGremlinExecutor - Initialized GremlinExecutor and preparing GremlinScriptEngines instances.
# [INFO] ServerGremlinExecutor - Initialized gremlin-groovy GremlinScriptEngine and registered metrics
# [INFO] ServerGremlinExecutor - A GraphTraversalSource is now bound to [g] with graphtraversalsource[tinkergraph[vertices:0 edges:0], standard]
# [INFO] ServerGremlinExecutor - A GraphTraversalSource is now bound to [g1] with graphtraversalsource[tinkergraph[vertices:0 edges:0], standard]
# [INFO] OpLoader - Adding the standard OpProcessor.
# [INFO] OpLoader - Adding the session OpProcessor.
# [INFO] OpLoader - Adding the traversal OpProcessor.
# [INFO] TraversalOpProcessor - Initialized cache for TraversalOpProcessor with size 1000 and expiration time of 600000 ms
# [INFO] GremlinServer - idleConnectionTimeout was set to 0 which resolves to 0 seconds when configuring this value - this feature will be disabled
# [INFO] GremlinServer - keepAliveInterval was set to 0 which resolves to 0 seconds when configuring this value - this feature will be disabled
# [INFO] AbstractChannelizer - Configured application/vnd.gremlin-v3.0+gryo with org.apache.tinkerpop.gremlin.driver.ser.GryoMessageSerializerV3d0
# [INFO] AbstractChannelizer - Configured application/vnd.gremlin-v3.0+gryo-stringd with org.apache.tinkerpop.gremlin.driver.ser.GryoMessageSerializerV3d0
# [INFO] AbstractChannelizer - Configured application/vnd.gremlin-v3.0+json with org.apache.tinkerpop.gremlin.driver.ser.GraphSONMessageSerializerV3d0
# [INFO] AbstractChannelizer - Configured application/json with org.apache.tinkerpop.gremlin.driver.ser.GraphSONMessageSerializerV3d0
# [INFO] GremlinServer$1 - Gremlin Server configured with worker thread pool of 1, gremlin pool of 8 and boss thread pool of 1.
# [INFO] GremlinServer$1 - Channel started at port 8182.
# [INFO] MarkerIgnoringBase - type=GAUGE, name=org.apache.tinkerpop.gremlin.server.GremlinServer.gremlin-groovy.sessionless.class-cache.average-load-penalty, value=1.1320263E9
# [INFO] MarkerIgnoringBase - type=GAUGE, name=org.apache.tinkerpop.gremlin.server.GremlinServer.gremlin-groovy.sessionless.class-cache.estimated-size, value=2
# [INFO] MarkerIgnoringBase - type=GAUGE, name=org.apache.tinkerpop.gremlin.server.GremlinServer.gremlin-groovy.sessionless.class-cache.eviction-count, value=0
# [INFO] MarkerIgnoringBase - type=GAUGE, name=org.apache.tinkerpop.gremlin.server.GremlinServer.gremlin-groovy.sessionless.class-cache.eviction-weight, value=0
# [INFO] MarkerIgnoringBase - type=GAUGE, name=org.apache.tinkerpop.gremlin.server.GremlinServer.gremlin-groovy.sessionless.class-cache.hit-count, value=0
# [INFO] MarkerIgnoringBase - type=GAUGE, name=org.apache.tinkerpop.gremlin.server.GremlinServer.gremlin-groovy.sessionless.class-cache.hit-rate, value=0.0
# [INFO] MarkerIgnoringBase - type=GAUGE, name=org.apache.tinkerpop.gremlin.server.GremlinServer.gremlin-groovy.sessionless.class-cache.load-count, value=2
# [INFO] MarkerIgnoringBase - type=GAUGE, name=org.apache.tinkerpop.gremlin.server.GremlinServer.gremlin-groovy.sessionless.class-cache.load-failure-count, value=0
# [INFO] MarkerIgnoringBase - type=GAUGE, name=org.apache.tinkerpop.gremlin.server.GremlinServer.gremlin-groovy.sessionless.class-cache.load-failure-rate, value=0.0
# [INFO] MarkerIgnoringBase - type=GAUGE, name=org.apache.tinkerpop.gremlin.server.GremlinServer.gremlin-groovy.sessionless.class-cache.load-success-count, value=2
# [INFO] MarkerIgnoringBase - type=GAUGE, name=org.apache.tinkerpop.gremlin.server.GremlinServer.gremlin-groovy.sessionless.class-cache.long-run-compilation-count, value=0
# [INFO] MarkerIgnoringBase - type=GAUGE, name=org.apache.tinkerpop.gremlin.server.GremlinServer.gremlin-groovy.sessionless.class-cache.miss-count, value=2
# [INFO] MarkerIgnoringBase - type=GAUGE, name=org.apache.tinkerpop.gremlin.server.GremlinServer.gremlin-groovy.sessionless.class-cache.miss-rate, value=1.0
# [INFO] MarkerIgnoringBase - type=GAUGE, name=org.apache.tinkerpop.gremlin.server.GremlinServer.gremlin-groovy.sessionless.class-cache.request-count, value=2
# [INFO] MarkerIgnoringBase - type=GAUGE, name=org.apache.tinkerpop.gremlin.server.GremlinServer.gremlin-groovy.sessionless.class-cache.total-load-time, value=2264052600
# [INFO] MarkerIgnoringBase - type=GAUGE, name=org.apache.tinkerpop.gremlin.server.GremlinServer.sessions, value=0
# [INFO] MarkerIgnoringBase - type=METER, name=org.apache.tinkerpop.gremlin.server.GremlinServer.errors, count=0, mean_rate=0.0, m1=0.0, m5=0.0, m15=0.0, rate_unit=events/second
# [INFO] MarkerIgnoringBase - type=TIMER, name=org.apache.tinkerpop.gremlin.server.GremlinServer.op.eval, count=0, min=0.0, max=0.0, mean=0.0, stddev=0.0, median=0.0, p75=0.0, p95=0.0, p98=0.0, p99=0.0, p999=0.0, mean_rate=0.0, m1=0.0, m5=0.0, m15=0.0, rate_unit=events/second, duration_unit=milliseconds
# [INFO] MarkerIgnoringBase - type=TIMER, name=org.apache.tinkerpop.gremlin.server.GremlinServer.op.traversal, count=0, min=0.0, max=0.0, mean=0.0, stddev=0.0, median=0.0, p75=0.0, p95=0.0, p98=0.0, p99=0.0, p999=0.0, mean_rate=0.0, m1=0.0, m5=0.0, m15=0.0, rate_unit=events/second, duration_unit=milliseconds
```

OK, the server is now running in the ps1 shell.  

Now you need a shell **running as admin** to install a python module

```bash
# Install python gremlin module
pip3 install gremlinpython==3.4.0
# ...
# Installing collected packages: aenum, tornado, gremlinpython
# Successfully installed aenum-2.1.2 gremlinpython-3.4.0 tornado-4.5.3

# Verify install
pip3 show gremlinpython
# Name: gremlinpython
# Version: 3.4.0
# Summary: Gremlin-Python for Apache TinkerPop
# Home-page: http://tinkerpop.apache.org
# Author: UNKNOWN
# Author-email: UNKNOWN
# License: Apache 2
# Location: c:\program files (x86)\python36-32\lib\site-packages
# Requires: six, tornado, aenum
```

You can kill above shell again.  

So go back to the first bash shell and run a test

```bash
# Test
py -3 test_graph.py
# Number of nodes 0, number of edges 0.
# Writing nodes...
# writing edge...
# Number of nodes 2, number of edges 1.
# Nodes and the data associated:
# [{'name': ['Node1'], 'description': ['First node'], 'Node number': [1]}, {'name': ['Node2'], 'description': ['Second node'], 'Node number': [2]}]
# Property associated to "name" on Node1:
# {'Created': 'Today'}
# Edge and the data associated:
# [{}]
# Removing the nodes...
```

Nice - we can see that the script added nodes and edges, printed them and then removed them :-)  

Now lets stop the server  

```bash
# Stop gremlin server
docker container stop gremlin

# Check it is status Exited
docker ps -a
# CONTAINER ID        IMAGE                         COMMAND                  CREATED             STATUS                     PORTS                NAMES
# 2d81aa9510d7        bricaud/gremlin-server        "/usr/bin/dumb-init …"   39 minutes ago      Exited (0) 3 minutes ago                        gremlin

# Try re-start it
docker container start 
# Check its logs
docker logs -f 2d81aa9510d7
# ....
# [INFO] GremlinServer$1 - Channel started at port 8182
# Ctrl-C to exit logs
```

### Meetup 2019-04-15

* pedro@dataverz.net
    * @parraguezr
    * [Pedro Parraguez Ruiz](https://www.parraguezr.net/)
* [Global Graph Celebration Day - Copenhagen](https://www.meetup.com/Copenhagen-Graph-Databases-Meetup/events/259549580/)
    * [Global Graph Celebration Day](https://globalgraphcelebrationday.com/)
    * [Neo4j Browser](https://88f0bc82.databases.neo4j.io/browser/)
* eBooks: [Neo4j Books: Free Graph Database Ebooks &amp; Other Resources](https://neo4j.com/books/)
    * [O&#039;Reilly Graph Algorithms Book - Neo4j Graph Database Platform](https://neo4j.com/graph-algorithms-book/)
* Cool sites
    * [WikiGalaxy: Explore Wikipedia in 3D](http://wiki.polyfra.me/)
    * Use for navigation API between docs
* [Graph Database Use Cases and Solutions](https://neo4j.com/use-cases/)
* [netsights](http://www.netsights.dk/)
* Tools
    * gephi - Metrics about how important are nodes. What position in the network do I have?
        * load with node.csv and edges.csv
        * Layout can organize network
        * you can color by properties - e.g. male/female
    * 


The End