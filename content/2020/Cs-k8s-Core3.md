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


The End
