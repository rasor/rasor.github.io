Title: Deploying Ionic to Azure
Date: 2017-10-10 21:00
Modified: 2017-10-13 22:00
Category: DevOp
Tags: #npm, #git, #ionic, #ngx, #azure, #pwa

This blog is based on [@sethreidnz](https://twitter.com/sethreidnz)'s 
article [Deploying an Angular CLI project using VSTS Build and Release](https://sethreid.co.nz/deploying-angular-cli-project-using-vsts-build-release/).  
This blog deploys a Ionic 3 / Angular 4 app to Azure.

# The final workflow

After your Ionic project has been connected with Azure through VSTS then you have this workflow:

1. From you editor: Add feature to you project and git push to origin
2. From VSTS: Queue a new build

That's it. Done. You have deployed your Ionic project to Azure as a webapp.

So why doesn't the pipeline just hook a webhook into your git origin and queue a build by itself (as you are used to from e.g. Heroku)?  
Well - if you use VSTS as Version Control, then it will work - I have used "Remote repo" option - apparently it is not ready yet.

And why would you want to deploy a Ionic app as a webapp, when it is supposed to be installed on phones?  
Ionic is born as PWA - you might want to use those features.  
Also you just might want to demo the app as webapp before sending it to the app store.  
So with Ionic you have only one codebase to maintain - checkout [MillionEyez](https://www.millioneyez.com) on the web and download their app. Same code.  

BTW - In the coming Ionic 4 Ionic will have moved to WebComponents, which enables layout components to be loaded before the content components giving a much better experience.  
You will also be able to use Ionic from any other webframework - e.g. React or VueJs.

# Here is how to do

## The Build server (VSTS)

Currently the build server (VSTS) is running  
`user-agent = "npm/3.10.10 node/v6.10.0 win32 x64"`.

So you should also build your app with `node v6` or perhaps a bit lower. It is a bit like in .NET you would also want to build with a framework e.g. `.NET 4.5.2` when the build server has `.NET 4.7` - at least you don't get too big surprises when your code is build on the build server.

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

# Build for prod
npm run build --prod --aot
```

If no errors then we can continue.

## Your remote origin

I have forked [dreamhouseapp/dreamhouse-mobile-ionic](https://github.com/dreamhouseapp/dreamhouse-mobile-ionic) by [Christophe Coenraets (@ccoenraets)](https://twitter.com/ccoenraets) to [rasor/dreamhouse-mobile-ionic](https://github.com/rasor/dreamhouse-mobile-ionic).  
Why? Because I need to give VSTS access to my GitHub account. I can't give it access to @ccoenraets's repo.  
You can fork mine, since it is modified a bit, making it runable in Azure.  
BTW - You can read about @ccoenraets's code here: [DreamHouse: Sample Application with Ionic 3 and Angular 4](http://coenraets.org/blog/2017/04/dreamhouse-sample-application-ionic3-angular4/).

## Your local repo

If you forked my repo do:
```bash
npm install -g cordova@7.0.1 ionic@3.12.0 # just in case you have not installed Ionic
git clone https://github.com/yourgithubusername/dreamhouse-mobile-ionic
cd dreamhouse-mobile-ionic
npm install # download node_modules
ionic serve # does code run without build?
npm run build --prod --aot # can you build?
```

## Build to drop folder in VSTS

* When you have created a VSTS account via [Visual Studio VSTS](https://www.visualstudio.com/) browse to <https://yourvstsusername.visualstudio.com/_projects>
* Create a project for dreamhouse-mobile-ionic - Press `New Project` and enter name `dreamhouse-mobile-ionic`.  
![New VSTS project](img/2017-10-09-VSTS1.PNG "New VSTS project")
* Since your code is in GitHub, you don't need to have it in VSTS, too. So no need to look in tab `Code`.
* Instead goto tab `Build and Release` and press `+ New` to add a new Build Definition - more or less as you might be used to from TFS.  
![New Build definition](img/2017-10-09-VSTS2.PNG "New Build definition")
* Choose an Empty template - meaning there are no build steps to start out with  
![Select Empty template](img/2017-10-09-VSTS3.PNG "Select Empty template")
* Now you need to connect to GitHub. Select `Get sources` in left pane and select `Remote repo` in right pane. You need to authenticate towards GitHub - go through that process. In the image below I have already connected  
Notice - this is like when you did git clone locally
![Connect to GitHub](img/2017-10-09-VSTS4.PNG "Connect to GitHub")
* So what did you do after git clone? `npm install`. In Phase 1 press `+` and select npm task.
![Select npm task](img/2017-10-09-VSTS5.PNG "Select npm task")
* Configure npm task by pressing the dropdown list and select `install`  
![Configure npm install](img/2017-10-09-VSTS6.PNG "Configure npm install")
* After install you did `Ionic serve`. But that was a development task - not a build task  
Next build task is `npm run build --prod --aot`. Go on - add yet a npm task as you did before
* Configure npm task by pressing the dropdown list and select `custom`, since you can't select run  
Add `run build --prod --aot` as Command and arguments  
You probably recognize `--aot` - [Ahead-of-Time](https://angular.io/guide/aot-compiler) from Angular 4. It gives faster load time, so it is quite important  
![Configure npm run](img/2017-10-09-VSTS7.PNG "Configure npm run")
* So we ran out of steps locally, but on the build server we still need to package the build output and send it to Azure  
Next task is a zip-task. Press `+` and select `Archive Files`  
![Select zip task](img/2017-10-09-VSTS8.PNG "Select zip task")
* Root folder is the build code you want to deploy. It is located in the www folder - just as when you work locally  
And the name of the zipped package should be `$(Build.ArtifactStagingDirectory)/$(Build.BuildId).zip`  
![Configure zip](img/2017-10-09-VSTS9.PNG "Configure zip")
* Final build step to do is to put the package in a drop folder  
Next task is a publish task. Press `+` and select `Publish Build Artifacts`  
Notice - you can create PowerShell, Shell Script and Batch Script tasks. So if you npm installed a nice utility, you could then do anything with it in a script which could be in your code e.g. `.\scripts\runkarmaandprotractortests.cmd
![Select publish task](img/2017-10-09-VSTS10.PNG "Select publish task")
* Path to publish is the zip file you created in last step  
Artifact Name is the name of the drop folder. It must be called `drop`  
And Type must be `Server` (opposed to File Share)  
![Configure publish](img/2017-10-09-VSTS11.PNG "Configure publish")

Have you noticed that these Build Tasks correspond to the features in TeamCity? 

Next up is to deploy the package to Azure.

## Setup WebApp in Azure

* When you have created a free Azure account via [Microsoft Azure](https://azure.microsoft.com/en-in/free/) browse to [Azure Portal](https://portal.azure.com/)
* The first thing you need is a place for all you stuff at Azure to live. That is called a `Resource Group`  
Click `Resource Groups` then `+ Add`  
![Add Resource Group](img/2017-10-09-Azure1.PNG "Add Resource Group")
* Name - I have called mine `ResGroupNorthEurope`  
Location - I live in area `North Europe`  
![Configure Resource Group](img/2017-10-09-Azure2.PNG "Configure Resource Group")
* So what do you want there? A webapp. You find that under `App Services`. Click `+ Add` then `Filter`  
Then you see a variaty of categories of webapps
![Add WebApp](img/2017-10-09-Azure3.PNG "Add WebApp")
* Select `Web App` 
Since I have already taken subdomain dreamhouse-mobile-ionic you have to choose another one - e.g.  `yourvstsusername-dreamhouse-mobile-ionic`  
Resourse Group: Use the one you created before: ``Use Existing`  
App Service Plan is the Dyno in Heroku or EC2 in AWS - the size of your PaaS. I have chosen the smallest: S1  
Tip: You can reuse the Resource Group and the App Service Plan for several resources e.g. webapps.
![Configure WebApp](img/2017-10-09-Azure4.PNG "Configure WebApp")

You're done in Azure. Next up is to release to Azure from VSTS.

## Release to Azure from VSTS

* Go back to <https://yourvstsusername.visualstudio.com/dreamhouse-mobile-ionic/_build>
* You can deploy to many environments and servivces. We just want to deploy to our App Service.  
First step is to select that target environment in a Release  
Click tab `Releases` then `+` - `Create Release Definition` - Select `Azure App Service Deployment` and click Apply   
![Add Release Definition](img/2017-10-09-VSTSRelease1.PNG "Add Release Definition")
* Notice the ´!´ - something needs attention - click either of them  
![Tasks needs attention](img/2017-10-09-VSTSRelease2.PNG "Tasks needs attention")
* Hey - that looks familiar - a list of steps in a task list - just as under tab `Build`  
Yes, but heading is `Environment 1` - not `Phase 1`. And for the environmet you have to connect to Azure.
Click on `Manage` subscribtion and go through an authentication process  
When connected you can click the dropdown list to select your website  
![Connect to Azure](img/2017-10-09-VSTSRelease3.PNG "Connect to Azure")
* Head back to tab `Pipeline` - we need to fetch a source to deploy  
Select `Add Artifact` and select source type: `Build`, so we can fetch the zip file from drop.  
Notice: Source type can also be: `Git, GitHub, Jenkins and Team Foundation Version Control`.  
Build Definition: Select the only one from the list.  
Accept default values and press Add.  
![Add Artifact](img/2017-10-09-VSTSRelease4.PNG "Add Artifact")
* Press the lightning icon on the Artifact. Notice the trigger is whenever a new drop has been made.  
![Release Trigger](img/2017-10-09-VSTSRelease5.PNG "Release Trigger")
* Now that we have a source we can head back to `Tasks`, select `Deploy Azure App Service` and enter the missing zipfile: `$(System.DefaultWorkingDirectory)\**\*.zip`. You can browse to it by pressing `...`  
![Pick zip file](img/2017-10-09-VSTSRelease6.PNG "Pick zip file")
* Before we save the Release Definition head to `Pipeline` - and select the Lightning in the Environment  
Notice you have a possibility to select persons to approve deployment. This can be tester that approves one environment before a build is rolled out for the next environment.  
![Approvers](img/2017-10-09-VSTSRelease7.PNG "Approvers")
We don't want approvers - so go on and save.

Have you noticed that these Release workflow correspond to the features in Octopus Deploy? 

## Trig a build and a release to Azure

Now we are ready for the big show - deploy to Azure

* Head back to `Builds` - tab `All Definitions` - click on the only one `dreamhouse-mobile-ionic-Build`  
![Prepare to build](img/2017-10-09-VSTSQueue1.PNG "Prepare to build")
* Click `Queue New Build...`  
![Queue build](img/2017-10-09-VSTSQueue2.PNG "Queue build")
* Click `Queue`
![npm run build](img/2017-10-09-VSTSQueue3.PNG "npm run build")
* If the Build succeded head to `Releases` tab and verify that the build triggered a release  
![Triggered release](img/2017-10-09-VSTSQueue4.PNG "Triggered release")
* If the release succeeded, too head to `Azure App Services` in [Azure](https://portal.azure.com)  
Select your service and scroll down to `Continous Delivery`  
You should see the Release has been Deployed Successfully  
![Succeeded release](img/2017-10-09-VSTSQueue5.PNG "Succeeded release")

If that is true then you site should be live on  
<http://yourvstsusername-dreamhouse-mobile-ionic.azurewebsites.net>

If you are just reading along you can also find my site [here](http://dreamhouse-mobile-ionic.azurewebsites.net/)

----------------------------

# Links

* [Deploying Ionic1 to Heroku](https://rasor.wordpress.com/2017/06/29/deploying-ionic1-as-a-webapp-to-heroku/)
* [Deploy your .NET core app to an Azure web app](https://docs.microsoft.com/en-us/vsts/build-release/apps/cd/azure/aspnet-core-to-azure-webapp?tabs=vsts)
* [MSDN](https://my.visualstudio.com)
* [Yarn with Travis CI](https://yarnpkg.com/en/docs/install-ci#travis-tab)
* [Authentication and authorization in Azure App Service](https://docs.microsoft.com/en-us/azure/app-service/app-service-authentication-overview)
* [Add authentication on Cordova with Mobile Apps](https://docs.microsoft.com/en-us/azure/app-service-mobile/app-service-mobile-cordova-get-started-users)
* [SSR with .NET Core](https://docs.microsoft.com/en-us/aspnet/core/client-side/spa-services)
* [Azure Mobile Apps - MBaaS - C#](https://docs.microsoft.com/en-us/azure/app-service-mobile/app-service-mobile-dotnet-backend-how-to-use-server-sdk)
* [Azure Mobile Apps - MBaaS - NodeJs](https://docs.microsoft.com/en-us/azure/app-service-mobile/app-service-mobile-node-backend-how-to-use-server-sdk)
* [Azure CLI 2.0](https://docs.microsoft.com/en-us/cli/azure/overview?view=azure-cli-latest)
* [Azure CLI Samples - App Service](https://docs.microsoft.com/en-us/azure/app-service/app-service-cli-samples)

The End