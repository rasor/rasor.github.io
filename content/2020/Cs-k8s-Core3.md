Title: ASP.NET Core with k8s hosting
Date: 2099-01-01 00:00
Category: Develop
Tags: #csharp, #netcore3, #docker, #k8s

# Intro

This is an extract of content from an eBook into small, reusable snippets.

Source is:
* eBook (2019): [Syncfusion Free Ebooks | Using .NET Core, Docker, and Kubernetes Succinctly](https://www.syncfusion.com/ebooks/using-netcore-docker-and-kubernetes-succinctly)
    * By [@apomic80](https://twitter.com/apomic80)        
        * Github: [apomic80](https://github.com/apomic80)

## Chapter 1 ASP.NET and Docker Together
### Execute .NET Core application with Docker

Install and start Docker.  
Then open a shell.  

```bash
# Verify docker CLI is installed
docker --version
# Docker version 19.03.13, build 4484c46d9d

# View docker images cached on your machine
docker image ls
# or
docker images
# REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
```

Now we'll run a console app.
```bash
# pull specific images into your cache
docker pull microsoft/dotnet-samples # this is a console app
docker images
# REPOSITORY                 TAG                 IMAGE ID            CREATED             SIZE
# microsoft/dotnet-samples   latest              70e25069fca7        20 months ago       181MB

# start an image
docker run --name consoleapp 70e25069fca7
#    Hello from .NET Core!

# Which containers are running?
docker ps
# CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
# none - the above one fineshed and exited

# show all containers
docker ps -a
# CONTAINER ID        IMAGE                  COMMAND                  CREATED             STATUS                     PORTS                       NAMES
# a51691a1650f        70e25069fca7           "dotnet dotnetapp.dll"   3 minutes ago       Exited (0) 3 minutes ago                               consoleapp

# run again - to avoid creating more images
docker start consoleapp # runs in background by default, so you won't see print here - instead do
docker start consoleapp -i # interactive mode

# remove the image
docker rm consoleapp # by name
# or
docker rm a51691a1650f # by id
```

Next we'll run a web app.  
```bash
# Terminal 1:
# pull a web app
docker pull microsoft/dotnet-samples:aspnetapp # this is a web app
docker images
# REPOSITORY                 TAG                 IMAGE ID            CREATED             SIZE
# microsoft/dotnet-samples   aspnetapp           575d85b4a69b        20 months ago       263MB
# microsoft/dotnet-samples   latest              70e25069fca7        20 months ago       181MB

# start a new image
docker run --name mvcapp 575d85b4a69b # you can add -d to run in damon/background mode, which gives you the prompt back, but you then won't see its outputs
# Hosting environment: Production
# Content root path: /app
# Now listening on: http://[::]:80
# Application started. Press Ctrl+C to shut down.
```
```bash
# Terminal 2:
docker ps
# CONTAINER ID        IMAGE                  COMMAND                  CREATED             STATUS                   PORTS                       NAMES
# 82225a6f9672        575d85b4a69b           "dotnet aspnetapp.dll"   36 seconds ago      Up 34 seconds                                        mvcapp
```

But you can't access it on http://[::]:80 ... You have to redirect an outer port into its port 80.
```bash
# Terminal 1:
# stop the image
docker stop mvcapp # notice - stopping by name
# remove image
docker rm mvcapp

# start the image with access from port 8080 
docker run -p 8080:80 --name mvcapp 575d85b4a69b  # notice - starting by name, so we don't add yet an image
#or
docker create -p 8080:80 --name mvcapp 575d85b4a69b
docker start mvcapp # runs in background by default - use -i to see its outputs
```
```bash
# Terminal 2:
# open browser
start http://localhost:8080
docker ps
# CONTAINER ID        IMAGE                  COMMAND                  CREATED             STATUS                   PORTS                       NAMES
# bab98369a976        575d85b4a69b           "dotnet aspnetapp.dll"   45 seconds ago      Up 43 seconds            0.0.0.0:8080->80/tcp        mvcapp
```
```bash
# Terminal 1:
# stop the image
docker stop mvcapp # notice - stopping by name
# remove image
docker rm mvcapp
```

## Chapter 2 Create Your Application with Docker
### Develop your ASP.NET Core application using Docker

Dotnet core commands:

* dotnet new: Creates a new project from the specified template. If you want to create an MVC application, you can use dotnet new mvc.
* dotnet restore: Restores all the NuGet dependencies of our application.
* dotnet build: Builds our project.
* dotnet run: Executes our project.
* dotnet watch run: Runs our project and watches for file changes to rebuild and re-run it.
* dotnet publish: Creates a deployable build (the .dll) of our project.

Install VSCode plugin [Docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)

```bash
# Terminal 1:
# Create a C# gitignore file in the root
dotnet new gitignore

# create a folder for MVC frontend
mkdir -p cpt2/frontend
cd cpt2/frontend
# Create mvc web
dotnet new mvc

# Build an run a webserver
dotnet build
dotnet run
```
```bash
# Terminal 2:
# open a browser
start https://localhost:5001/
```
Stop the webserver in Teminal 1 with ctrl-c.  

Now create `.vscode` files `launch.json` and `tasks.json`:  
* Ctrl-shft-p # to open cmd palette
* `.NET: Generate Assets for Build and Debug`
    * Choose `ASPNET Core`, `linux` container and ports `5000, 5001`

You can now goto runner with `ctrl-shft-d` and press run. You can hit breakpoints.  

Now create a `Dockerfile`, `.dockerignore` and `docker-compose.yml`:  
* In explorer put cursor on cpt2\frontend
* Ctrl-shft-p # to open cmd palette
* `Docker: Add Docker files to workspace`
    * Choose `ASPNET Core`, `linux` container and ports `5000, 5001`, `yes` to create compose file

```dockerfile
# Generated Dockerfile
# 1. Target img to deploy to
FROM mcr.microsoft.com/dotnet/core/aspnet:3.1 AS base
WORKDIR /app
EXPOSE 5000
EXPOSE 5001

# 5. Source img to build on
FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build
WORKDIR /src
# 7. Copy project file from local pc into Source img
COPY ["cpt2/frontend/frontend.csproj", "cpt2/frontend/"]
RUN dotnet restore "cpt2/frontend/frontend.csproj"
COPY . .
WORKDIR "/src/cpt2/frontend"
# 11. Build .dll
RUN dotnet build "frontend.csproj" -c Release -o /app/build

FROM build AS publish
# 13. Create a deployable package
RUN dotnet publish "frontend.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
# 16. Copy from Source img to Target img
COPY --from=publish /app/publish .
# 17. Define start command
ENTRYPOINT ["dotnet", "frontend.dll"]
```

Change cmd 7 to 10, so you'll be able to `docker build` from inside folder `cpt2/frontend`

```dockerfile
# 7. Copy project file from local pc into Source img
COPY ./frontend.csproj .
RUN dotnet restore frontend.csproj
COPY . .
WORKDIR /src
```

* [Dockerfile reference](https://docs.docker.com/engine/reference/builder/)

Let's build our docker img

```bash
# verify docker is running
docker images
# goto folder with Dockerfile
cd cpt2/frontend
docker build --help
# build img and tag it frontend2
docker build -t frontend2 .

# System.InvalidOperationException: Unable to configure HTTPS endpoint. No server certificate was specified, and the default developer certificate could not be found or is out of date.


# Sending build context to Docker daemon  6.432MB
# Step 1/17 : FROM mcr.microsoft.com/dotnet/core/aspnet:3.1 AS base
# 3.1: Pulling from dotnet/core/aspnet
# bb79b6b2107f: Pull complete
# fd6f53cfcb35: Pull complete
# 29b35ed07a14: Pull complete
# fd068c4127c7: Pull complete
# dc51486f316e: Pull complete
# Digest: sha256:4030ec40f9b5c1e8cac5d550639b7b05d1d6af0c89b4b47d66bad7f93379c9eb
# Status: Downloaded newer image for mcr.microsoft.com/dotnet/core/aspnet:3.1
#  ---> e3559b2d50bb
# Step 2/17 : WORKDIR /app
#  ---> Running in 14fd02991c3d
# Removing intermediate container 14fd02991c3d
#  ---> df46b5f3b46a
# Step 3/17 : EXPOSE 5000
#  ---> Running in 5adf5a71198d
# Removing intermediate container 5adf5a71198d
#  ---> 817df2c51839
# Step 4/17 : EXPOSE 5001
#  ---> Running in 1815541a6c6a
# Removing intermediate container 1815541a6c6a
#  ---> 02891abd8059
# Step 5/17 : FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build
# 3.1: Pulling from dotnet/core/sdk
# e4c3d3e4f7b0: Pull complete
# 101c41d0463b: Pull complete
# 8275efcd805f: Pull complete
# 751620502a7a: Pull complete
# 8e306865fd07: Pull complete
# 9d2f53e752c2: Pull complete
# 143a93e01eba: Pull complete
# Digest: sha256:d09eefeaad2129f0a0ac047095792afc6792e7aae4b8bb1c1fa5b6650caae240
# Status: Downloaded newer image for mcr.microsoft.com/dotnet/core/sdk:3.1
#  ---> 5fe503d51830
# Step 6/17 : WORKDIR /src
#  ---> Running in 143a136929b6
# Removing intermediate container 143a136929b6
#  ---> 0e5a8185b7a2
# Step 7/17 : COPY ./frontend.csproj .
#  ---> 203c96e3d357
# Step 8/17 : RUN dotnet restore frontend.csproj
#  ---> Running in cd917bface5b
#   Determining projects to restore...
#   Restored /src/frontend.csproj (in 170 ms).
# Removing intermediate container cd917bface5b
#  ---> 866543516985
# Step 9/17 : COPY . .
#  ---> 6ac6636b092c
# Step 10/17 : WORKDIR /src
#  ---> Running in 40c27a3098f1
# Removing intermediate container 40c27a3098f1
#  ---> d3f07b018611
# Step 11/17 : RUN dotnet build "frontend.csproj" -c Release -o /app/build
#  ---> Running in 56cc1964bf83
# Microsoft (R) Build Engine version 16.7.0+7fb82e5b2 for .NET
# Copyright (C) Microsoft Corporation. All rights reserved.
#   Determining projects to restore...
#   Restored /src/frontend.csproj (in 185 ms).
#   frontend -> /app/build/frontend.dll
#   frontend -> /app/build/frontend.Views.dll
# Build succeeded.
#     0 Warning(s)
#     0 Error(s)
# Time Elapsed 00:00:05.03
# Removing intermediate container 56cc1964bf83
#  ---> 7ccf08805a5b
# Step 12/17 : FROM build AS publish
#  ---> 7ccf08805a5b
# Step 13/17 : RUN dotnet publish "frontend.csproj" -c Release -o /app/publish
#  ---> Running in 27507652111d
# Microsoft (R) Build Engine version 16.7.0+7fb82e5b2 for .NET
# Copyright (C) Microsoft Corporation. All rights reserved.
#   Determining projects to restore...
#   All projects are up-to-date for restore.
#   frontend -> /src/bin/Release/netcoreapp3.1/frontend.dll
#   frontend -> /src/bin/Release/netcoreapp3.1/frontend.Views.dll
#   frontend -> /app/publish/
# Removing intermediate container 27507652111d
#  ---> c08c7122d789
# Step 14/17 : FROM base AS final
#  ---> 02891abd8059
# Step 15/17 : WORKDIR /app
#  ---> Running in b52e89be9e92
# Removing intermediate container b52e89be9e92
#  ---> 97d3ac799145
# Step 16/17 : COPY --from=publish /app/publish .
#  ---> 2ac048ea1f90
# Step 17/17 : ENTRYPOINT ["dotnet", "frontend.dll"]
#  ---> Running in 7359a524012b
# Step 17/17 : ENTRYPOINT ["dotnet", "frontend.dll", "--urls", "'http://0.0.0.0:5000;https://0.0.0.0:5001'"]
#  ---> Running in ef35cfccc80f
# Step 17/17 : CMD dotnet watch run --urls "http://0.0.0.0:5000;https://0.0.0.0:5001"
#  ---> Running in 7bcf38a65540
# Removing intermediate container 7359a524012b
#  ---> f7828ef4f47e
# Successfully built f7828ef4f47e
# Successfully tagged frontend2:latest
# SECURITY WARNING: You are building a Docker image from Windows against a non-Windows Docker host. All files and directories added to build context will have 
# '-rwxr-xr-x' permissions. It is recommended to double check and reset permissions for sensitive files and directories.

# Print image
docker images
# REPOSITORY                             TAG                 IMAGE ID            CREATED             SIZE  
# frontend2                              latest              f7828ef4f47e        5 minutes ago       212MB 
# mcr.microsoft.com/dotnet/core/aspnet   3.1                 e3559b2d50bb        7 days ago          207MB 
# mcr.microsoft.com/dotnet/core/sdk      3.1                 5fe503d51830        7 days ago          708MB 

# Test run the img
docker run -p 5000:5000 --name nfrontend2 -t frontend2
#docker run -p 5000:5000 -p 5001:5001 --name nfrontend2 -t frontend2
#docker create -p 5000:5000 -p 5001:5001 --name nfrontend2 -t frontend2 --entrypoint 'dotnet dev-certs https && # warn: Microsoft.AspNetCore.DataProtection.Repositories.FileSystemXmlRepository[60]
#       Storing keys in a directory '/root/.aspnet/DataProtection-Keys' that may not be persisted outside of the container. Protected data will be unavailable 
# when container is destroyed.
#       No XML encryptor configured. Key {22010cbd-95fa-4543-9ae3-63ee61afff7f} may be persisted to storage in unencrypted form.
#       Now listening on: http://[::]:80
#       Application started. Press Ctrl+C to shut down.
#       Hosting environment: Production
#       Content root path: /app
```

```bash
# Terminal 2:
docker start nfrontend2
# Which containers are running?
docker ps
# CONTAINER ID        IMAGE               COMMAND                 CREATED             STATUS              PORTS                              NAMES
# 6fc16e63dbd5        frontend2           "dotnet frontend.dll"   18 seconds ago      Up 17 seconds       0.0.0.0:5000-5001->5000-5001/tcp   nfrontend2   

# Print entry point
docker ps -a --format "table {{.Image}}:\t {{.Command}}" --no-trunc
# IMAGE:                   COMMAND
# frontend2:               "dotnet frontend.dll…"

docker ps -a --output table

# Open browser
start https://localhost:5001
# --- Can't be reached using localhost .....

# Cleanup
docker stop nfrontend2
docker rm nfrontend2
# Cleanup done?
docker ps -a
```

To fix that the the webserver does not hear anything on localhost you would normally change
```jsonc
    <!-- Properties/launchSettings.json -->
    "frontend": {
      "applicationUrl": "https://localhost:5001;http://localhost:5000",
    }
```
to
```jsonc
    <!-- Properties/launchSettings.json -->
    "frontend": {
      "applicationUrl": "https://0.0.0.0:5001;http://0.0.0.0:5000",
    }
```

But apparently `launchSettings.json` is totally replaced by what Dockerfile, so you should replace
```dockerfile
# 17. Define start command
ENTRYPOINT ["dotnet", "frontend.dll"]
```
with
```dockerfile
# 17. Pass in UseUrls
#ENV MVCAPPURLS=https://0.0.0.0:5001;http://0.0.0.0:5000
ENV MVCAPPURLS=http://0.0.0.0:5000
# 18. Define start command
ENTRYPOINT ["dotnet", "frontend.dll"]
```
Notice that I am not sending in the https-part. For that to work you will also have to install a SSL certificate!  
If you had the SDK on the image you could have installed the certificate with `dotnet dev-certs https`.  

The ENV we defined we read in 

Before:
```csharp
// Program.cs
                    webBuilder
                        .UseStartup<Startup>();

```
After
```csharp
// Program.cs
                    webBuilder
                        .UseUrls(Environment.GetEnvironmentVariable("MVCAPPURLS"))
                        .UseStartup<Startup>();
```

After `docker build` and `docker run` you can `start http://localhost:5000/`.  

```yaml
# Generated docker-compose.debug.yml
# Please refer https://aka.ms/HTTPSinContainer on how to setup an https developer certificate for your ASP .NET Core service.

version: '3.4'

services:
  frontend:
    image: frontend
    build:
      context: .
      dockerfile: cpt2/frontend/Dockerfile
    ports:
      - 5000
      - 5001
    environment:
      - ASPNETCORE_ENVIRONMENT=Development
      - ASPNETCORE_URLS=http://+:5000
    volumes:
      - ~/.vsdbg:/remote_debugger:rw
```

Change frontend in both the .debug.yml and then non-debug yml to:

```yaml
  frontend:
    image: frontend2
    build:
      context: .
      dockerfile: Dockerfile
```


```bash
```
```bash
```
```bash
```
```bash
```
```bash
```
```bash
```
```bash
```
```bash
```

# REFs

* [Inner-loop development workflow for Docker apps](https://docs.microsoft.com/en-us/dotnet/architecture/containerized-lifecycle/design-develop-containerized-apps/docker-apps-inner-loop-workflow)
* [Development workflow for Docker apps](https://docs.microsoft.com/en-us/dotnet/architecture/microservices/docker-application-development-process/docker-app-development-workflow)
* [DevOps with Kubernetes and VSTS: Part 1](https://colinsalmcorner.com/devops-with-kubernetes-and-vsts-part-1/)
* [Generic Host Builder in ASP .NET Core 3.1](https://wakeupandcode.com/generic-host-builder-in-asp-net-core-3-1/)
* Change entry point: [Containerize an app with Docker tutorial - .NET Core](https://docs.microsoft.com/en-us/dotnet/core/docker/build-container?tabs=linux#change-the-entrypoint)
* [Setting Default Docker Environment Variables During Image Build](https://vsupalov.com/docker-build-time-env-values/)

The End
