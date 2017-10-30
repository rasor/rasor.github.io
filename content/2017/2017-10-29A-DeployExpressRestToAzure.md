Title: Deploying Express REST API to Azure
Date: 2017-10-29 21:00
Modified: 2017-10-30 17:00
Category: DevOp
Tags: #npm, #git, #express, #nodejs, #azure

This blog is part of a series.

1. [Deploying Ionic to Azure]({filename}/2017/2017-10-09A-DeployIonicToAzure.md)
2. [Deploying Express REST API to Azure]({filename}/2017/2017-10-29A-DeployExpressRestToAzure.md)
3. Add Facebook Authentication to your Express REST API - Planned

In this blog I will deploy an Express REST API to Azure Mobile Apps.

The exercise is almost identical to Part 1 - Deploy Ionic to Azure, so in this blog I'll leave out the pictures.

# Here is how to do

## The Build server (VSTS)

Currently the build server (VSTS) is running  
`user-agent = "npm/3.10.10 node/v6.10.0 win32 x64"`.

So you should also build your API with `node v6` or perhaps a bit lower. It is a bit like in .NET you would also want to build with a framework e.g. `.NET 4.5.2` when the build server has `.NET 4.7` - at least you don't get too big surprises when your code is build on the build server.

It should be possible to specify another node version with `WEBSITE_NODE_DEFAULT_VERSION`, though I haven't tried. Look for more info [here](http://blog.stevensanderson.com/2016/10/04/angular2-template-for-visual-studio/).

## Your local repo

So before you start deploy you should verify that your code can build for prod on `node v6`.

```bash
# If you got nvm switch to v6
nvm list
nvm use 6.11.4
# or just check that you have v6
node -v
# If you don't have v6 you might get surprises when you build in VSTS, but purhaps you won't.
```

If no errors then we can continue.

## Your remote origin

I have forked [dreamhouseapp/dreamhouse-rest-services](https://github.com/dreamhouseapp/dreamhouse-rest-services) by [Christophe Coenraets (@ccoenraets)](https://twitter.com/ccoenraets) to [rasor/dreamhouse-rest-services](https://github.com/rasor/dreamhouse-rest-services).  
Why? Because I need to give VSTS access to my GitHub account. I can't give it access to @ccoenraets's repo.  
You can fork [mine](https://github.com/rasor/dreamhouse-rest-services), since it is modified a bit with web.config, making it runable in Azure.  
BTW - You can read about @ccoenraets's code here: [DreamHouse: Sample Application with Ionic 3 and Angular 4](http://coenraets.org/blog/2017/04/dreamhouse-sample-application-ionic3-angular4/).

The `web.config` file you need for node.js projects running in IIS looks like this:

```xml
<?xml version="1.0" encoding="utf-8"?>
<!--
     This configuration file is required if iisnode is used to run node processes behind
     IIS or IIS Express.  For more information, visit:
     https://github.com/tjanczuk/iisnode/blob/master/src/samples/configuration/web.config
-->
<configuration>
  <system.webServer>
    <!-- Visit http://blogs.msdn.com/b/windowsazure/archive/2013/11/14/introduction-to-websockets-on-windows-azure-web-sites.aspx for more information on WebSocket support -->
    <webSocket enabled="false" />
    <handlers>
      <!-- Indicates that the server.js file is a node.js site to be handled by the iisnode module -->
      <add name="iisnode" path="server.js" verb="*" modules="iisnode"/>
    </handlers>
    <rewrite>
      <rules>
        <!-- Do not interfere with requests for node-inspector debugging -->
        <rule name="NodeInspector" patternSyntax="ECMAScript" stopProcessing="true">
          <match url="^server.js\/debug[\/]?" />
        </rule>

        <!-- First we consider whether the incoming URL matches a physical file in the /public folder -->
        <rule name="StaticContent">
          <action type="Rewrite" url="public{REQUEST_URI}"/>
        </rule>

        <!-- All other URLs are mapped to the node.js site entry point -->
        <rule name="DynamicContent">
          <conditions>
            <add input="{REQUEST_FILENAME}" matchType="IsFile" negate="True"/>
          </conditions>
          <action type="Rewrite" url="server.js"/>
        </rule>
      </rules>
    </rewrite>
    
    <!-- 'bin' directory has no special meaning in node.js and apps can be placed in it -->
    <security>
      <requestFiltering>
        <hiddenSegments>
          <remove segment="bin"/>
        </hiddenSegments>
      </requestFiltering>
    </security>

    <!-- Make sure error responses are left untouched -->
    <httpErrors existingResponse="PassThrough" />

    <!--
      You can control how Node is hosted within IIS using the following options:
        * watchedFiles: semi-colon separated list of files that will be watched for changes to restart the server
        * node_env: will be propagated to node as NODE_ENV environment variable
        * debuggingEnabled - controls whether the built-in debugger is enabled

      See https://github.com/tjanczuk/iisnode/blob/master/src/samples/configuration/web.config for a full list of options
    -->
    <!--<iisnode watchedFiles="web.config;*.js"/>-->
  </system.webServer>
</configuration>
```

It seems like the web.confog is generated for you, when you choose Node.js as target environment during Release Definition in VSTS.

## Your local repo

When you have forked a repo do:
```bash
git clone https://github.com/yourgithubusername/dreamhouse-rest-services
cd dreamhouse-rest-services
npm install # download node_modules
start "" "http://localhost:5000/properties" #start browser - this work in windows
node server # start webserver
# refresh browser (F5) if it timed out before the server was started
```

## Build to drop folder in VSTS

* When you have created a VSTS account via [Visual Studio VSTS](https://www.visualstudio.com/) browse to <https://yourvstsusername.visualstudio.com/_projects>
* Since you already have a build project from part 1, you can reuse that project and just create yet a build definion on:
<https://yourvstsusername.visualstudio.com/dreamhouse-mobile-ionic/_build?path=%5C&_a=allDefinitions>  
or you can browse to there: Press `Build and Release` then  `All Definitions`. There you see your Build Definition for building your Ionic project.
* press `+ New` to add a new Build Definition - more or less as you might be used to from TFS.  
* Choose an Empty process - meaning there are no build steps to start out with  
* Now you need to connect to GitHub. Select `Get sources` in left pane and select `Remote repo` in right pane. You need to authenticate towards GitHub - go through that process.  
Name: `yourgithubusername_dreamhouse-rest-services`
Repo: `https://github.com/yourgithubusername/dreamhouse-rest-services`
Set Clean to `true`, so the source files from the Ionic build will be removed - Set clean options to `Sources`  
Notice - this is like when you did git clone locally
* Just above `Get Sources` there is `Process` - select it.  
Name: dreamhouse-rest-services-Build  
Agent Queue: Hosted VS2017
* So what did you do after git clone? `npm install`. In Phase 1 press `+` and select npm task.
![Select npm task](img/2017-10-09-VSTS5.PNG "Select npm task")
* Configure npm task by pressing the dropdown list and select `install`  
![Configure npm install](img/2017-10-09-VSTS6.PNG "Configure npm install")
* After install you started the browser and did `node server`. But that was a development task - not a build task  
* So we ran out of steps locally, but on the build server we still need to package the build output and send it to Azure  
Next task is a zip-task. Press `+` and select `Archive Files`  
![Select zip task](img/2017-10-09-VSTS8.PNG "Select zip task")
* Root folder is the build code you want to deploy. It is located in the `.\` folder - just as when you work locally.  
Unselect "Prefix root folder ..."  
The name of the zipped package should be `$(Build.ArtifactStagingDirectory)/$(Build.BuildId).zip`  
* Final build step to do is to put the package in a drop folder  
Next task is a publish task. Press `+` and select `Publish Build Artifacts`  
Notice - you can create PowerShell, Shell Script and Batch Script tasks. So if you npm installed a nice utility, you could then do anything with it in a script which could be in your code e.g. `.\scripts\runkarmaandprotractortests.cmd
![Select publish task](img/2017-10-09-VSTS10.PNG "Select publish task")
* Path to publish is the zip file you created in last step  
Artifact Name is the name of the drop folder. Call it `drop-rest`, so it can't be confused with the Ionic drop.  
And location must be `TFS` (opposed to File Share)  
* Press `Save & queue`. In top of the screen you'll see `Build #<some-number> has been queued.`
* Click on `#<some-number>`. Now you can see the progress of the build.  
When the build has finished you'll see `Build Succeeded` and above that `dreamhouse-rest-services-Build / Build <some-number> / Phase 1`  
* Click on `Build <some-number>`. Now you get 5 tabs for that build: `Summary - Timeline - Artifacts - Code coverage* - Tests`  
* Click on `Artifacts`. Now you see the dropfolder. Check it out and see if it contains what you expected.  

Have you noticed that these Build Tasks correspond to the features in [TeamCity](https://www.jetbrains.com/teamcity/)? 

Next up is to deploy the package to Azure.

## Setup WebApp in Azure

* When you have created a free Azure account via [Microsoft Azure](https://azure.microsoft.com/en-in/free/) browse to [Azure Portal](https://portal.azure.com/)
* In Part 1 you created a Resource Group e.g. `ResGroupNorthEurope`. This is where all your stuff in Azure lives.
![Configure Resource Group](img/2017-10-09-Azure2.PNG "Configure Resource Group")
* This time you could also have chosen  webapp as before, but Azure has another option called Mobile App. This has the option of offering Notifications and other MBaaS (Mobile Backend) services.  
You find that under `App Services`. Click `+ Add` then `Filter`  
Enter `Mobile Apps`  
Then you see a small selection of mobile apps  
* Select `Mobile App`  
Since I have already taken subdomain dreamhouse-rest-services you have to choose another one - e.g.  `yourvstsusername-dreamhouse-rest-services`  
Resourse Group: Use the one you created before: ``Use Existing`  
App Service Plan is the Dyno in Heroku or EC2 in AWS - the size of your PaaS.  
Resuse the one you created in Part 1 e.g. `AppSvcPlanNorthEuropeWindows (Standard: 1 Small)`

You're done in Azure. Next up is to release to Azure from VSTS.

## Release to Azure from VSTS

* Go back to <https://yourvstsusername.visualstudio.com/dreamhouse-mobile-ionic/_build>
* You can deploy to many environments and services. This time we want to deploy to our Mobile App.  
First step is to select that target environment in a Release  
Click tab `Releases` then `+` - `Create Release Definition` - Select `Deploy Node.js App to App Service` and click Apply   
![Add Release Definition](img/2017-10-29-VSTSRelease1.PNG "Add Release Definition")
* Notice the ´!´ - something needs attention - click either of them  
![Tasks needs attention](img/2017-10-09-VSTSRelease2.PNG "Tasks needs attention")
* Hey - that looks familiar - a list of steps in a task list - just as under tab `Build`  
Yes, but heading is `Environment 1` - not `Phase 1`. And for the environmet you have to connect to Azure.
Azure subscription click on the drop down list to select the one you connected to in Part 1.  
When connected you can click the dropdown list to select your mobile app `yourvstsusername-dreamhouse-rest-services`  
![Connect to Azure](img/2017-10-29-VSTSRelease3.PNG "Connect to Azure")
* Head back to tab `Pipeline` - we need to fetch a source to deploy  
Select `Add Artifact` and select source type: `Build`, so we can fetch the zip file from drop.  
Notice: Source type can also be: `Git, GitHub, Jenkins and Team Foundation Version Control`.  
Project: Select `dreamhouse-mobile-ionic`  
Build Definition: Select `dreamhouse-rest-services-Build`.  
Notice that since you did a build before VSTS knows it created `drop-rest`
Accept default values and press Add.  
![Add Artifact](img/2017-10-29-VSTSRelease4.PNG "Add Artifact")
* Press the lightning icon on the Artifact. 
* Enable Continous deployment. Notice the trigger is whenever a new drop has been made.  
![Release Trigger](img/2017-10-09-VSTSRelease5.PNG "Release Trigger")
* Now that we have a source we can head back to `Tasks`, select `Deploy Azure App Service`
* App Service name: `yourvstsusername-dreamhouse-mobile-rest`  
Package: `$(System.DefaultWorkingDirectory)\**\*.zip`. You can browse to it by pressing `...`  
![Pick zip file](img/2017-10-09-VSTSRelease6.PNG "Pick zip file")
* Before we save the Release Definition head to `Pipeline` - and select the Lightning in the Environment  
Notice you have a possibility to select persons to approve deployment. This can be tester that approves one environment before a build is rolled out for the next environment.  
![Approvers](img/2017-10-09-VSTSRelease7.PNG "Approvers")
We don't want approvers - so go on and save as `dreamhouse-rest-Release`.

Have you noticed that these Release workflow correspond to the features in [Octopus Deploy](https://octopus.com/)? 

## Trig a build and a release to Azure

Now we are ready for the big show - deploy to Azure
(Notice - all the images are reused from Part 1)

* Head back to `Builds` - tab `All Definitions` - click on the `dreamhouse-rest-services-Build`  
![Prepare to build](img/2017-10-09-VSTSQueue1.PNG "Prepare to build")
* Click `Queue New Build...` - then click `Queue`   
![Queue build](img/2017-10-09-VSTSQueue2.PNG "Queue build")
* If the Build succeded head to `Releases` tab and verify that the build triggered a release  
![Triggered release](img/2017-10-09-VSTSQueue4.PNG "Triggered release")
* If the release succeeded, too head to `Azure App Services` in [Azure](https://portal.azure.com)  
Select your service and scroll down to `Continous Delivery`  
You should see the Release has been Deployed Successfully  
![Succeeded release](img/2017-10-09-VSTSQueue5.PNG "Succeeded release")
In my case the relese ended with this warning:  
`2017-10-29T19:44:36.5445296Z ##[warning]Failed to update App Service configuration details. Error: Error: connect ETIMEDOUT 157.56.31.170:443` That meant that the above image did not show a succeeded release. 
Instead I could browse in the App Service Console and the files were alse viewable from App Service Editor.

So to verify that browse to you service on  
<http://yourvstsusername-dreamhouse-mobile-rest.azurewebsites.net/properties>

If you are just reading along you can also find my site [here](http://dreamhouse-mobile-rest.azurewebsites.net/properties)

The End.
