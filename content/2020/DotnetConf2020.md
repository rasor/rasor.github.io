Title: .NET Conf 2020, Nov 10-12
Date: 2099-01-01 00:00
Category: Develop
Tags: #csharp, #netcore5

* Home: [.NET Conf 2020](https://www.dotnetconf.net/agenda)
    * [Learn TV](https://docs.microsoft.com/en-us/learn/tv/)
    * [.NET Conf 2020 - Day 1](https://www.youtube.com/watch?v=mS6ykjdOVRg)
    * [.NET Conf Day 2/3](https://www.youtube.com/watch?v=Uq4qyHi3sYM)
    * [.NET Live TV | Live developer streams every day](https://dotnet.microsoft.com/live)
* Slides: [dotnet-presentations/dotNETConf](https://github.com/dotnet-presentations/dotNETConf/tree/master/2020/MainEvent)
* Blog: [.NET 5.0 Launches at .NET Conf, November 10-12 | .NET Blog](https://devblogs.microsoft.com/dotnet/net-5-0-launches-at-net-conf-november-10-12/)
    * [Twitch](https://www.twitch.tv/visualstudio)

Today Microsoft released .NET core 5 and C# 9.  
The conference is about what´s new in it.  

Here is what you get when installing [.NET 5.0](https://dotnet.microsoft.com/download/dotnet/5.0):
```text
The installation was successful.

The following were installed at: 'C:\Program Files\dotnet'
    • .NET SDK 5.0.100
    • .NET Runtime 5.0.0
    • ASP.NET Core Runtime 5.0.0
    • .NET Windows Desktop Runtime 5.0.0

This product collects usage data
    • More information and opt-out https://aka.ms/dotnet-cli-telemetry

Resources
    • .NET Documentation https://aka.ms/dotnet-docs
    • SDK Documentation https://aka.ms/dotnet-sdk-docs
    • Release Notes https://aka.ms/dotnet5-release-notes
    • Tutorials https://aka.ms/dotnet-tutorials
```
```bash
dotnet --version
# 5.0.100
```

--- ------------------------------------------------------------------
# Day #1
## 01 Keynote - Welcome to .NET 5  -  Scott Hunter  
08:00 (PT) | 16:00 (UTC) | 17:00 (Local)

Scott Hunter, Director of Program Management for .NET, will kick off the day with loads of new demos and some very special guests.

* [@coolcsh](https://twitter.com/coolcsh)
    * [Download .NET 5.0 (Linux, macOS, and Windows)](https://dotnet.microsoft.com/download/dotnet/5.0)
* [@scottgu](https://twitter.com/scottgu)
* [@shanselman](https://twitter.com/shanselman)
    * record
* [@maddyleger1](https://twitter.com/maddyleger1)
    * Xamarin
* [@gotheap](https://twitter.com/gotheap)
    * GitHub actions
    * Run tests in a Linux container
* Daniel Roth
* [@bradygaster](https://twitter.com/bradygaster)
    * WebApi
    * httpRepl.exe
* David Fowler
    * Tye - k8s dashboard 
    * > tye run

## 02 .NET Foundation "State of the Foundation"  -  Claire Novotny   Layla Porter  
09:00 (PT) | 17:00 (UTC) | 18:00 (Local)

Take a look at what the .NET Foundation has been up to and how to get involved.

## 03 What’s New in C#?  -  Mads Torgersen   Dustin Campbell  
09:30 (PT) | 17:30 (UTC) | 18:30 (Local)

Dustin and Mads take you on a tour of the new features in C# 9.0: Top-level programs remove clutter. Init-only properties and records improve support for immutable and value-based programming. New patterns take pattern matching to the next level. Can Dustin type as fast as Mads can speak, and vice versa? Only one way to find out!

* [@madstorgersen](https://twitter.com/madstorgersen)
* [@csharpfritz](https://twitter.com/csharpfritz)
* C# 9
    * record, with, deconstruct
    * when, switch
    * [Download .NET 5.0 (Linux, macOS, and Windows)](https://dotnet.microsoft.com/download/dotnet/5.0)

## 04 A talk for trailblazers: Blazor in .NET 5  -  Steve Sanderson   Safia Abdalla  
10:00 (PT) | 18:00 (UTC) | 19:00 (Local)

Wondering what’s in store for Blazor in .NET 5? Wonder no more! This talk features the latest and greatest features to arrive in Blazor as part of .NET 5. From improved APIs for working with the browser to CSS isolation to a variety of performance improvements, you’ll leave this presentation with rundown of everything you’ll be able to do in the latest version of Blazor.

* [https://twitter.com/csharpfritz](https://twitter.com/csharpfritz)
* [https://twitter.com/captainsafia](https://twitter.com/captainsafia)
* Blazor
    * > dotnet watch run
    * VSCode Debug: Attach to Blazor
    * `<InputFile>, <Virtualize>`
    * ![captainsafia/blazoract](https://user-images.githubusercontent.com/1857993/98490947-18f87f00-21e8-11eb-889f-db78c79b5a9b.png)
    * Code: [captainsafia/blazoract](https://github.com/captainsafia/blazoract)
    * Lazy-loading

## 05 Porting Projects to .NET 5  -  Immo Landwerth   Phillip Carter  
10:30 (PT) | 18:30 (UTC) | 19:30 (Local)

Want to move to .NET 5? In this session you'll see how to approach porting projects from .NET Framework, .NET Core, and .NET Standard to .NET 5 and the tools you can use to get there.

## 06 Entity Framework Core 5.0: The Next Generation for Data Access  -  Jeremy Likness   Shay Rojansky  
11:00 (PT) | 19:00 (UTC) | 20:00 (Local)

Use C#, .NET classes, and LINQ to interact with databases like Sqlite, Azure SQL Server and even Azure Cosmos DB from .NET 5 apps with Entity Framework Core. See the latest features in action like many-to-many, table-per-type and new diagnostics features.

* [@jeremylikness](https://twitter.com/jeremylikness)
* [@shayrojansky](https://twitter.com/shayrojansky)
* [Entity Framework documentation](https://docs.microsoft.com/en-us/ef/)
* Can scaffold DB into code

## 07 Modern Web Development with Blazor & .NET 5  -  Dan Roth   Javier Calvarro Nelson  
11:30 (PT) | 19:30 (UTC) | 20:30 (Local)

Blazor isn’t just for new apps! Blazor in .NET 5 is integrated seamlessly with ASP.NET Core to enable modern full stack web development with .NET. In this session we’ll show you how you can use Blazor and ASP.NET Core together to add rich client-side interactivity to both new and existing apps. You’ll learn how to use Blazor components from your existing MVC views and Razor Pages, handle server-side prerendering, setup authentication & authorization, improve load time performance, and then deploy your app into production.

* [@danroth27](https://twitter.com/danroth27)
* Blazor Server components running in MVC :-)
* Blazor webassembly components running in MVC :-)
    * Needs create API, too.
    * And needs API auth.
* [Blazor](https://dotnet.microsoft.com/apps/aspnet/web-apps/blazor)

## 08 Xamarin.Forms 5: Beautiful and Fast Apps with Less Code  -  Maddy Leger   David Ortinau  
12:00 (PT) | 20:00 (UTC) | 21:00 (Local)

Xamarin.Forms 5 is jam-packed with new features to make it easier than ever to develop fast, beautiful, cross-platform apps. Come see what new features are in Xamarin.Forms 5, and learn more about how our Xamarin Community Toolkit is getting more features than ever into your hands!

* [@davidortinau](https://twitter.com/davidortinau)
* [@maddyleger1](https://twitter.com/maddyleger1)
* `Reflector` for mirror IPhone connected via usb


## 09 Developing and Deploying Microservices with 'Tye'   -  David Fowler   Glenn Condron  
12:30 (PT) | 20:30 (UTC) | 21:30 (Local)

Learn about new tooling the .NET team is working on to help you build, debug and deploy microservices faster.

* [@davidfowl](https://twitter.com/davidfowl)
* [@condrong](https://twitter.com/condrong)
* Survey: https://www.surveymonkey.com/r/RWHQYL7
* [dotnet/tye](https://github.com/dotnet/tye)
* [sample](https://github.com/dotnet/tye/tree/master/samples/frontend-backend)
* VSCode ext: Tye Explorer - not ready, yet
```bash
tye init # creates tye.yaml
tye run
```

## 10 Get to know the .NET 5.0 SDK  -  Kathleen Dollard   Rainer Sigwald  
13:00 (PT) | 21:00 (UTC) | 22:00 (Local)

.NET 5 is the next version of .NET Core. The .NET SDK incudes the language compilers for C#, Visual Basic and F#. It also includes NuGet to manage packages, MSBuild to build and publish projects, and miscellaneous things like the templating engine. The .NET CLI and the community .NET tools enhance your command line experience and integrate with Visual Studio. Get a big picture of the .NET SDK and see what's new in 5.0.

* [@tashkant](https://twitter.com/tashkant)
* [@kathleendollard](https://twitter.com/kathleendollard)
* dotnet
* msbuild
* [.NET Core scripts](https://dotnet.microsoft.com/download/dotnet-core/scripts)

## 11 Introducing F# 5  -  Phillip Carter  
13:30 (PT) | 21:30 (UTC) | 22:30 (Local)

For the past five years, we've been working to make F# as good as it can on .NET Core. With the release of .NET 5, we're also introducing F# 5 - the culmination of this work. F# 5 makes interactive programming a joy, and introduces the building blocks for the next era of F#. Come see how!

## 12 .NET 5 Runtime Deep Dive with Rich Lander and the Architects  -  Rich Lander   Stephen Toub   Jan Kotas  
14:00 (PT) | 22:00 (UTC) | 23:00 (Local)

Go deep into some of the .NET 5 runtime features like performance improvements, how single-file applications work, ARM64 support, and more.

## 13 ML.NET in the Real World  -  Bri Achtman   Kundan Karma   Brett Parker   Chris Felstead  
14:30 (PT) | 22:30 (UTC) | 23:30 (Local)

Hear from real life .NET developers about the problems they decided to solve with Machine Learning and why they chose ML.NET to add ML to their apps.

## 14 What's new for desktop developers building WPF, UWP & WinForms  -  Dmitry Lyalin  
15:00 (PT) | 23:00 (UTC) | 00:00 (Local)

In this session we'll be taking you on a tour of what's new for desktop developers building applications using WPF, UWP and Windows Forms. We'll cover improvements in tooling such as what's new in XAML data binding diagnostic, XAML designer and Hot Reload. We'll also dive into WinForms topics such as designer and new features, explore .NET 5 support for ClickOnce and more!

## 15 High-performance Services with gRPC: What's new in .NET 5  -  James Newton-King  
15:30 (PT) | 23:30 (UTC) | 00:30 (Local)

gRPC is a high-performance RPC framework used by developers around the world to build fast apps. In this talk you will learn about what's new in gRPC for .NET 5, like performance improvements, gRPC-Web, Blazor WebAssembly support, Hosting on Http.sys and IIS, and OpenTelemetry.

## 16 Developer Fun with Scott Hanselman  -  Scott Hanselman  
16:00 (PT) | 00:00 (UTC) | 01:00 (Local)

Wind down a little from the day's sessions and learn some fun new things.

## 17 Virtual Attendee Party!  -  DeeDee Walsh   Sara Faatz   Jeff Fritz  
16:30 (PT) | 00:30 (UTC) | 01:30 (Local)

Have some fun, laugh, relax, answer triva questions, and win prizes from our sponsors.

--- ------------------------------------------------------------------
# Day #2
## 20 GitHub + Visual Studio ❤ .NET  -  Vix Rian   Andy Sterland  
09:00 (PT) | 17:00 (UTC) | 18:00 (Local)

GitHub and Visual Studio technologies have evolved and provide unique productivity enhancements to all .NET developers. Join this demo-filled session to see how it benefits you.

* [@vixgrows](https://twitter.com/vixgrows)
* [@andysterland](https://twitter.com/andysterland)
* Github Codespaces
    * VS: Connect to a codespace
    * Connect to a repo
    * [github.com/codespaces](https://github.com/codespaces)
    * VS: Ctrl-q to search
    * VS: Web - Publish as Github action
    * postCreate
    * devinit CLI executes tools in devinit.json
    * [Getting Started with devinit - Visual Studio](https://docs.microsoft.com/en-us/visualstudio/devinit/getting-started-with-devinit?view=vs-2019)
    * Feedback: [Developer Environment Customization](https://www.research.net/r/NP3MD76)
    * [GitHub Codespaces using Visual Studio or browser](https://visualstudio.microsoft.com/services/github-codespaces/)
    * [Quickstart for GitHub Actions - GitHub Docs](https://docs.github.com/en/free-pro-team@latest/actions/quickstart)
    * [actions/starter-workflows](https://github.com/actions/starter-workflows)

## 21 Effectively Diagnose and Debug .NET Apps in Visual Studio  -  Mark Downie  
10:00 (PT) | 18:00 (UTC) | 19:00 (Local)

Debug .NET Core running on Linux, master async debugging, and squeeze the last bit of performance out of your apps with the new features in Visual Studio.

* [@poppastring](https://twitter.com/poppastring)

## 22 What’s New in Visual Studio 2019 and beyond  -  Caty Caldwell  
10:30 (PT) | 18:30 (UTC) | 19:30 (Local)

Learn what’s new in latest Visual Studio 2019 as well as features the team is currently working on - including some that we’ve never shown to the public before.

* [@catycaldwell](https://twitter.com/catycaldwell)
* VS: Bundle in Template
    * Export Template
    * New project - select template
* Open proj - Do not load projects
    * Select projs - RC - load
    * Hide (unloaded) projs
    * Save as sln filter (slnf)
* Custom File nesting rules
* Web Live Preview
* Edit twice - then 3rd time intellicode knows and can repeat the action other/all places

## 23 Improve Your Productivity with Roslyn Analyzers  -  Mika Dumont   Kendra Havens  
11:00 (PT) | 19:00 (UTC) | 20:00 (Local)

Learn about Roslyn Analyzers and how it can supercharge your developer productivity. This session includes tips on how to leverage smart code focused tools, such as code fixes and refactorings and an introduction to write your own customized code fix and refactoring using Roslyn's open source API.

* [@mika_dumont](https://twitter.com/mika_dumont)
* [@gotheap](https://twitter.com/gotheap)
* squiggels, screwdriver, lightbulb are Roslyn analyzers
* [Refactoring - Visual Studio](https://docs.microsoft.com/en-us/visualstudio/ide/refactoring-in-visual-studio?view=vs-2019)
* [Code analysis in .NET](https://docs.microsoft.com/en-us/dotnet/fundamentals/code-analysis/overview)

## 24 HTTP API Development with .NET, Azure, and OpenAPI: Paper Cuts Begone!  -  Brady Gaster  
11:30 (PT) | 19:30 (UTC) | 20:30 (Local)

If you build HTTP APIs in .NET you probably have ceremonies you iterate through because the construction and testing of HTTP APIs hasn't *ever* been easy. Teams all over Microsoft have been working together to make the API development a joyful experience, as you'll see in this end-to-end tour.

* [@bradygaster](https://twitter.com/bradygaster)
* swagger in webapi 5
* nuget ms dotnet-httprepl
* Deploy API to Az and then use from PowerApps

## 25 Accelerate .NET to Azure with GitHub Actions  -  Isaac Levin  
12:00 (PT) | 20:00 (UTC) | 21:00 (Local)

GitHub Actions makes it easy to automate all your software workflows, now with world-class CI/CD. Easily deploy your .NET Core application to Azure with just one tool, GitHub.

* [@isaacrlevin](https://twitter.com/isaacrlevin)
* [isaacrlevin/.NET-Conf-Demos](https://github.com/isaacrlevin/.NET-Conf-Demos)
* [Building My Blog with GitHub Actions](https://www.isaaclevin.com/post/blog-on-actions/)
* [GitHub Actions Documentation - GitHub Docs](https://docs.github.com/en/free-pro-team@latest/actions)

## 26 Real-time 3D Games with .NET and Unity  -  John Miller   Abdullah Hamed  
12:30 (PT) | 20:30 (UTC) | 21:30 (Local)

Are you curious how to take your .NET skills to 25+ platforms like VR, AR, Xbox, and Switch to make amazing games and apps? Join this session to learn more about the Unity real-time 3D development platform and how your .NET skills can give you a head start towards that next big idea.

## 27 Introducing the New and Improved Azure SDK for .NET  -  Jeffrey Richter  
13:00 (PT) | 21:00 (UTC) | 22:00 (Local)

Come learn about the new Azure SDK for .NET and the improvements to performance, authentication and configuration that we have been working on in the last couple of years.

* [@jeffrichter](https://twitter.com/jeffrichter)
* [@azuresdk](https://twitter.com/azuresdk)
* [Azure SDK Latest Releases | Azure SDKs](https://azure.github.io/azure-sdk/)
* [Azure/azure-sdk](https://github.com/azure/azure-sdk)
    * [Azure/azure-sdk-for-net](https://github.com/azure/azure-sdk-for-net)
* [Azure SDKs - Blogs](https://devblogs.microsoft.com/azure-sdk/)
    * [AutoRest and OpenAPI: The backbone of Azure SDK | Azure SDK Blog](https://devblogs.microsoft.com/azure-sdk/code-generation-with-autorest/)
* [Welcome to the 'Architecting Distributed Cloud Applications' video series](https://www.youtube.com/watch?v=xJMbkZvuVO0&list=PL9XzOCngAkqs0Q8ZRdafnSYExKQurZrBY)
* [General Guidelines: Introduction | Azure SDKs](https://azure.github.io/azure-sdk/general_introduction.html)

## 28 The Missing Piece - Diving into the World of Big Data with .NET for Apache Spark  -  Rahul Potharaju   Jeremy Likness  
13:30 (PT) | 21:30 (UTC) | 22:30 (Local)

Data is growing at an unprecedented amount with both human generated and machine generated data. Come, learn about the open-source, .NET for Apache Spark project, the same technology that teams such as Office, Dynamics and Azure use widely to process 100s of Terabytes of data inside Microsoft.

## 29 Collecting ASP.NET Core Performance Traces in a Kubernetes Cluster  -  Mike Rousos  
14:00 (PT) | 22:00 (UTC) | 23:00 (Local)

Do you need to gather data on CPU usage, memory usage, or other potential performance issues for a containerized ASP.NET Core app? This talk will cover what you need to know to collect performance traces from ASP.NET Core apps running in a Kubernetes cluster.

* [mike-rousos-4983736/](https://www.linkedin.com/in/mike-rousos-4983736/)
* [@mjRousos](https://twitter.com/mjRousos) ??
* [Debug Linux dumps](https://docs.microsoft.com/en-us/dotnet/core/diagnostics/debug-linux-dumps)
    * [dotnet-trace tool - .NET Core](https://docs.microsoft.com/en-us/dotnet/core/diagnostics/dotnet-trace)
* [Cross Platform Managed Memory Dump Debugging | Visual Studio Blog](https://devblogs.microsoft.com/visualstudio/linux-managed-memory-dump-debugging/)

```bash
dotnet-trace
# use PerfView to view log
dotnet-dump
dotnet-gcdump
dotnet-counters
dotnet-monitor
```

* perfcollect  
* createdump  
    * complus_dbgenableminidump

## 30 Secretless Development from Local to Cloud with the New Azure SDKs, Project Tye, and Kubernetes  -  Jon Gallant  
14:30 (PT) | 22:30 (UTC) | 23:30 (Local)

Are you tired of managing secrets for local and cloud development? With the new Azure SDKs you can rid your applications of secrets with the new Azure Identity library. Come see how we implemented a secretless solution from local development with Project Tye to Azure Kubernetes Service.

* [@jongallant](https://twitter.com/jongallant)
* [jongio/memealyzer](https://github.com/jongio/memealyzer)
* [dotnet/tye](https://github.com/dotnet/tye)

## 31 Bringing .NET Interactive to Azure Data Studio Notebooks  -  Alan Yu   Jon Sequeira  
15:00 (PT) | 23:00 (UTC) | 00:00 (Local)

Azure SQL customers love Jupyter notebooks, especially having dedicated SQL, PowerShell, and C# kernels. This was a perfect opportunity to partner with the .NET interactive team to provide a consistent notebook experience. Come listen to our open source collaboration journey to make this possible.

## 32 Secure DevOps with the Microsoft Identity Platform  -  Christos Matskas   John Dandison  
15:30 (PT) | 23:30 (UTC) | 00:30 (Local)

Supercharge your devops skills and learn how to deploy and run your solutions securely in Azure using the Microsoft Identity Platform, ARM, service principals and Managed Identities. In this demo-rich session, you'll find out how to leverage the right tools and elevate DevOps to the next level!

## 33 Get Your JAM On  -  Aaron Powell  
16:00 (PT) | 00:00 (UTC) | 01:00 (Local)

You are embarking on a new project and have decided to go full Serverless and try out that JAMStack. After all, our application is a Blazor WASM app and some APIs, so Serverless is the perfect fit. But how do we design this solution, tackle local development and most importantly deploy to the cloud? In this session, you'll see how.

## 34 Migrate & Modernize ASP.NET Applications with Azure App Service and .NET 5  -  Gaurav Seth   Byron Tardif  
16:30 (PT) | 00:30 (UTC) | 01:30 (Local)

Learn how to modernize .NET Framework Apps, by migrating to App Service and 5 ways to get started with .NET 5 on App Service.

## 35 Blazor: Client Side vs. Server Side: Hands on Development and Deployment  -  Dr. Otto Dobretsberger  
17:00 (PT) | 01:00 (UTC) | 02:00 (Local)

We will look at the main differences between Client Side Blazor, and Server Side Blazor. We will discuss situations and scenarios in which one should be favored over the other. We will develop a small app & deploy it twice on Azure: As a Client Side Blazor App, and as a Server Side Blazor App.

## 36 Setting Up Feature Flags with .NET  -  Talia Nassi  
17:30 (PT) | 01:30 (UTC) | 02:30 (Local)

Let's set up feature flags with .NET! We will walk through how to create a feature flag in the UI, install dependencies, and implement your feature flag in your .NET app.

## 37 Level-up Your DevOps with GitHub Actions and Kubernetes  -  Rob Richardson  
18:00 (PT) | 02:00 (UTC) | 03:00 (Local)

Are you looking to rapidly deploy your content? Are Docker containers in your future? Come for this demo-only presentation where we start from scratch, build up a DevOps pipeline with GitHub Actions, and deploy to Kubernetes. Once setup, commit, and watch the magic flow into place.

* -----

## 38 Migrating a Windows Forms App to Blazor: The Amazing and True Story of GIFBot  -  Georgia Nelson  
18:30 (PT) | 02:30 (UTC) | 03:30 (Local)

In this talk, I will discuss the migration steps undertaken to go from a complex Desktop application to a robust ASP.NET-backed website with a Blazor front-end. The talk will highlight the ease at which I was able to translate functionality as a developer with very outdated web development skills.

## 39 Create a Text Parser in C# with ANTLR  -  Robin Reynolds-Haertle  
19:00 (PT) | 03:00 (UTC) | 04:00 (Local)

Caught with an unusual data format and want to convert it to something more friendly? Instead of writing buckets of string manipulation code, use ANTLR and C# to parse and make sense of that data. This talk will cover interesting uses of ANTLR and demonstrate parsing a unique data format.

* ---

## 40 Asynchronous Courotines with C#  -  Andrew Nosenko  
19:30 (PT) | 03:30 (UTC) | 04:30 (Local)

Coroutines are state-machine-style functions that can be suspended, resumed and executed cooperatively by yielding. In C# they are traditionally implemented as IEnumerable. With C# 8+, it's possible to combine "await" and "yield" within the same method, so we can have asynchrony inside coroutines. Come see how.

## 41 Bring Intelligence to the Edge with Custom Vision  -  Stefano Tempesta  
20:00 (PT) | 04:00 (UTC) | 05:00 (Local)

Get familiar with with Custom Vision, its API and ML algorithms for image classification, and explore an app for image capturing that uses a trained model with Custom Vision based on a custom image dataset.

## 42 C# Source Generators - Write Code that Writes Code  -  David Wengier  
20:30 (PT) | 04:30 (UTC) | 05:30 (Local)

With C# 9 there is finally an officially supported mechanism for generating source code into your .NET projects as part of the compiler pipeline. Lets run through how they work, some of the pros and cons, and play around with ideas to get your mind racing with the possibilities.

* [@davidwengier](https://twitter.com/davidwengier)
* [David Wengier](https://wengier.com/)
* Other generators: 
    * T4 - runs in runtime
    * RoslunSyntaxTree
* This runs in the compiler
* Starter Template: [davidwengier/SourceGeneratorTemplate](https://github.com/davidwengier/SourceGeneratorTemplate)
* SVG2Cs: [wieslawsoltes/SourceGenerators](https://github.com/wieslawsoltes/SourceGenerators)
    * SVG2PNG-PDF: [wieslawsoltes/Svg.Skia](https://github.com/wieslawsoltes/Svg.Skia)
* Sample validator: [davidwengier/EnumValidatorGenerator](https://github.com/davidwengier/EnumValidatorGenerator)
* Adv sample: [chsienki/Kittitas](https://github.com/chsienki/kittitas)
* Davids online generator: [sourcegen.dev - Source Generator Playground - @davidwengier](https://sourcegen.dev/)
    * [davidwengier/SourceGeneratorPlayground](https://github.com/davidwengier/SourceGeneratorPlayground)

## 43 Setting up Health Checks for an ASP.NET Core application and its Dependencies  -  Clyde D'Souza  
21:00 (PT) | 05:00 (UTC) | 06:00 (Local)

Site availability is crucial for the reputation and revenue of a business. In this session, we're going to look at setting up health checks for our ASP.NET Core application, its dependencies, and what your end-to-end transparent site uptime monitoring and reporting system might look like.

## 44 Maximising Algorithm Performance in .NET: Levenshtein Distance  -  James Turner  
21:30 (PT) | 05:30 (UTC) | 06:30 (Local)

With performance tricks you may not know on an algorithm you may never have heard of before, be prepared to learn about my journey from different array structures to pointers, SIMD to threading, as we take the journey to maximum performance together.

## 45 Enterprise Search Engine with Azure Cognitive Search and Unsupervised Machine Learning  -  Priyanka Shah  
22:00 (PT) | 06:00 (UTC) | 07:00 (Local)

Is your search engine missing word semantics? What if I want my search for "electric cars" to give me results for "green energy", or a search for "lithium" give results about "dry cells". Experience the power of cognitive search, topic modelling, neural word embedding with unsupervised ML to achieve this.

## 46 Building Reusable Rich UI controls using PowerApps Component Framework (PCF)  -  Dharanidharan Balasubramaniam   Jeevarajan Kumar  
22:30 (PT) | 06:30 (UTC) | 07:30 (Local)

The Power Apps component framework empowers professional developers and app makers to create code components for model-driven and canvas apps and provides enhanced user experiences for users working with data on forms, views, and dashboards. In this session, I am going to explain how we can build reusable rich UI controls using the PowerApps Component framework(PCF).

* [@crmindian](https://twitter.com/crmindian)

## 47 Architecting Cloud Native Application in Azure using .NET Core  -  Menaka Baskar  
23:00 (PT) | 07:00 (UTC) | 08:00 (Local)

In this session we will discuss about why .NET is a perfect blend to deliver Cloud Native applications.

* [@MenakaBasker](https://twitter.com/MenakaBasker)
* DevOps starter
    * [DevOps Starter documentation](https://docs.microsoft.com/en-us/azure/devops-project/)
    * [Overview of DevOps Starter for Azure](https://docs.microsoft.com/en-us/azure/devops-project/overview)

## 48 Controlling My Home Sauna Using .NET 5  -  Johnny Hooyberghs  
23:30 (PT) | 07:30 (UTC) | 08:30 (Local)

Today, .NET can really run everywhere. Come see how I was able to completely modernize my sauna controller by using .NET on a Raspberry Pi with Gpio support, .NET on Xamarin Forms, and .NET in a Docker container on a Linux host.

* [@djohnnieke](https://twitter.com/djohnnieke)
* [Johnny Hooyberghs Blog](https://blog.djohnnie.be/)
* [Djohnnie/MySauna-DotNetConf-2020](https://github.com/Djohnnie/MySauna-DotNetConf-2020)
* Raspberry Pi workers
    * System.Device.Gpio # Raspberry Pi GPIO interface
* Xamarin App
    * `adb connect <ip>` # connect and build to android
    * XAML hot reload
* Deploy containers to NAS in home
* [Modern Infrastructure as Code for Microsoft Azure | Pulumi](https://www.pulumi.com/azure/)
* [.NET Core (C#, VB, F#)](https://www.pulumi.com/docs/intro/languages/dotnet/)
* [pi-top [4]](https://www.pi-top.com/products/pi-top-4)

--- ------------------------------------------------------------------
# Day #3
## 50 Azure Management Superpowers with Pulumi  -  Mikhail Shilkov  
00:00 (PT) | 08:00 (UTC) | 09:00 (Local)

Managing infrastructure as code is a vital skill in today's cloud-first world. Learn how you can use C# or TypeScript to define and deploy Azure infrastructure and applications, including serverless functions, Kubernetes clusters, Cosmos DB, and much more.

* [@MikhailShilkov](https://twitter.com/MikhailShilkov)
* [Mikhail Shilkov](https://mikhail.io/)
* [mikhailshilkov - Overview](https://github.com/mikhailshilkov?tab=repositories)
* Pulumi - IaC
* [pulumi/examples](https://github.com/pulumi/examples)
    * [azure-nextgen-cs-aks](https://github.com/pulumi/examples/tree/master/azure-nextgen-cs-aks)
    ```bash
    # Create isolated deployment target
    pulumi stack init dev
    # Login to Azure CLI
    az login
    # azure location in which to run
    pulumi config set location westus2
    # Create infra from your cs code
    pulumi up
    # wait for up - then grap kubeconfig
    pulumi stack output KubeConfig > kubeconfig.yaml
    # work with your cluster - e.g. deploy something
    KUBECONFIG=./kubeconfig.yaml kubectl get nodes
    # tear down infra
    pulumi destroy --yes
    pulumi stack rm --yes
    ```
* [Announcing Next Generation Pulumi Azure Provider](https://mikhail.io/2020/09/announcing-nextgen-azure-provider/)
* Tool convert ARM to C#

## 51 Cross-platform Applications with Xamarin.Forms  -  Codrina Merigo  
00:30 (PT) | 08:30 (UTC) | 09:30 (Local)

You are a .NET developer and want to explore mobile apps? You struggle between Java, Swift, Objective C, React, Angular and so on? Don't give up, you can do it using your C# knowledge and have a working Android and iOS app in just a few minutes!

## 52 Get a Head Start with Entity Framework Core 5.0 with EF Core Power Tools  -  Erik Ejlskov Jensen  
01:00 (PT) | 09:00 (UTC) | 10:00 (Local)

You would really like to take advantage of Entitly Framewrk Core 5.0, but you are not familiar with the dotnet command line and the EF Core commands. See how the "EF Core Power Tools" for Visual Studio 2019 comes to your rescue!

* [@erikej](https://twitter.com/erikej)
* [ErikEJs blog](https://erikej.github.io/)
* EF core power tools
* [ErikEJ/EFCorePowerTools](https://github.com/ErikEJ/EFCorePowerTools)
* [EF Core Power Tools database reverse engineering: renaming of entities and properties](https://erikej.github.io/efcore/2020/09/07/ef-core-power-tools-renaming-advanced.html)
* Reverse eng from DB proj
* Reverse eng from existing DB
* [ErikEJ/SqlCeToolbox](https://github.com/ErikEJ/SqlCeToolbox)

## 53 Microfrontends with Blazor: Welcome to the Party!  -  Florian Rappl  
01:30 (PT) | 09:30 (UTC) | 10:30 (Local)

In this talk, microfrontends expert Florian Rappl introduces an established architecture for a creating modular frontend applications. He will show how this architecture can be implemented together with Blazor to create dynamic user experiences.

## 54 Introducing the MVVM Toolkit, a .NET Standard Library in the Windows Community Toolkit  -  Michael A. Hawker   Sergio Pedri  
02:00 (PT) | 10:00 (UTC) | 11:00 (Local)

We'll show you how to use this new light-weight .NET Standard MVVM library wherever you are building your application be it with Windows UWP, WPF, Xamarin, Uno, and even Blazor! We'll show you best practices in getting started with MVVM and how to hit the ground running when creating an new app!

## 55 AI Enrichment with Azure Cognitive Search  -  Luis Beltran  
02:30 (PT) | 10:30 (UTC) | 11:30 (Local)

Documents and images are great information sources. But when it comes to search, a database is often used. How would you feel if I told you that you can actually look for information contained in images, or find organizations mentioned in documents. Learn how to do it in this Azure Search session!

## 56 Getting Real-time Insights from your Serverless Solution  -  Eduard Keilholz  
03:00 (PT) | 11:00 (UTC) | 12:00 (Local)

The SignalR real-time framework has been there for ages, but how do you connect to services like Azure Functions? In my session, I will show you how to create a SignalR service, send messages to the SignalR service and handle events on a connected SPA application.

* [@ed_dotnet](https://twitter.com/ed_dotnet)
* [nikneem/serverless-realtime-import](https://github.com/nikneem/serverless-realtime-import)

## 57 Building React Applications in F#  -  Zaid Ajaj  
03:30 (PT) | 11:30 (UTC) | 12:30 (Local)

In this talk, I will show you how to build modern and type-safe frontend applications in React with F# as well as showcase the mature ecosystem of tools around it.

* [@zaid_ajaj](https://twitter.com/zaid_ajaj)
* F#
* [Zaid-Ajaj/dotnetconf-react-with-fsharp](https://github.com/Zaid-Ajaj/dotnetconf-react-with-fsharp)
* `Fable` - F# to Js compiler
    * Feliz
    * React fast-refresh
    * Webpack dev server
    * `[<ReactComponent>]`
* React
    * [Pigeon Maps - ReactJS with OpenStreetMap Tile Layers](https://pigeon-maps.js.org/)
    * [mariusandra/pigeon-maps](https://github.com/mariusandra/pigeon-maps)


## 58 Building Real-time Applications with Blazor and GraphQL  -  Michael Staib  
04:00 (PT) | 12:00 (UTC) | 13:00 (Local)

Come see how Blazor and GraphQL combined will revolutionize how we build rich SPA applications with .NET.

* [@michael_staib](https://twitter.com/michael_staib)
* [michaelstaib/PublicSpeaking](https://github.com/michaelstaib/PublicSpeaking)
* [chillicream](https://chillicream.com/)
    * [ChilliCream/hotchocolate](https://github.com/ChilliCream/hotchocolate)
    * [HotChocolate](https://twitter.com/Chilli_Cream/status/1324384158060322823)
* Banana Cake Pop
* [ChilliCream/graphql-workshop](https://github.com/ChilliCream/graphql-workshop)

## 59 A Piece of Cake - C# Powered Cross-platform Build Automation  -  Gary Ewan Park  
04:30 (PT) | 12:30 (UTC) | 13:30 (Local)

In this session we will start with a standard .NET Solution and incrementally add a build and orchestration script to compile the application, run unit tests, perform static analysis, package the application, and more, with the C# skills that you already have, using the Cake Build Automation System.

* [@gep13](https://twitter.com/gep13)
* [gep13 - Overview](https://github.com/gep13)
* Cake
    * [@cakebuildnet](https://twitter.com/cakebuildnet)
    * [Cake](https://github.com/cake-build/)
    * [cake-build/cake](https://github.com/cake-build/cake)
    * [cake-build/example](https://github.com/cake-build/example)
    * Cake won't make you vendor locked-in e.g. ADO
    * [Gary Ewan Park - Getting started with GitHub Actions](https://www.gep13.co.uk/blog/getting-started-with-github-actions)
    * [Gary Ewan Park - Using Cake GitHub Action](https://www.gep13.co.uk/blog/using-cake-github-action)
    * AddIns: [cake-contrib/Home](https://github.com/cake-contrib/Home/blob/master/Audit_for_Cake_0.33.0.md)
* PSake
    * [@devblackops](https://twitter.com/devblackops)
    * [psake/psake](https://github.com/psake/psake)
    * [devblackops/psake-github-action](https://github.com/devblackops/psake-github-action)
    * [GitHub Actions Tweet](https://twitter.com/devblackops/status/1072036355855671297)
* Github Actions:
    * [GitHub Actions Documentation - GitHub Docs](https://docs.github.com/en/free-pro-team@latest/actions)

## 60 Language Server Protocol and .NET  -  David Driscoll  
05:00 (PT) | 13:00 (UTC) | 14:00 (Local)

OmniSharp powers the C# experience in Visual Studio Code. It also inspired the Language Server Protocol that is used to make it such a great editor for your languag
* e of choice. Learn about how OmniSharp and the Language Server Protocol are helping build better experiences for Visual Studio and Visual Studio Code!

* [@david_dotnet](https://twitter.com/david_dotnet)
* OmniSharp
* [Language Server Protocol](https://microsoft.github.io/language-server-protocol/)

## 61 Getting Started With Blazor  -  Carole Rennie Logan  
05:30 (PT) | 13:30 (UTC) | 14:30 (Local)

In this session, we will introduce the core concepts for Blazor development, both client and server side. Then we will dive in to a Blazor Web Assembly example and look at how we can build rich client side apps in C#!

## 62 Overview of Single File Applications in .NET 5  -  Harishchandra Ukirade  
06:00 (PT) | 14:00 (UTC) | 15:00 (Local)

Single file applications is the part of exiting journey of unifying the .NET platform, with a single framework that extends from desktop, mobile, cloud and beyond. Get an overview of what this means and how you can leverage single file apps in .NET 5.

## 63 Components in Blazor  -  Poornima Nayar  
06:30 (PT) | 14:30 (UTC) | 15:30 (Local)

Blazor is the blazing word in the Microsoft Tech stack at the moment because you can run C# on the client. In this session, I will talk about what Razor components are, talk about their lifecycle, event handling, and how to pass information between Blazor Components.

## 64 3D Printed Bionic Hand - a Little IoT and a Xamarin Mobile App  -  Clifford Agius  
07:00 (PT) | 15:00 (UTC) | 16:00 (Local)

Meet Kayden, a local 16yr old young man and close family friend, who was born with no left forearm and hand. This talk is about the last 2 years open source work on 3D printing a prosthetic Hand and adding some IoT for control and a Xamarin mobile app for set-up and configuration.

## 65 Remote Computer Science with pi-top, .NET and Microsoft Teams  -  Mark Hardwick   Mike Roberts   Diego Colombo   Paul Meyer   Jon Sequeira  
07:30 (PT) | 15:30 (UTC) | 16:30 (Local)

Come see how we're using .NET, pi-top's smart rover, and Microsoft Teams to showcase the remote computer science class of the future. A Covid-19 resistant remote first approach that allows collaboration, coding, testing debugging and rich interactions involving data, video and Azure cloud services.

## 66 .NET for Infrastructure Automation  -  Nenne Adaora (Adora) Nwodo  
08:00 (PT) | 16:00 (UTC) | 17:00 (Local)

Are you a Software Engineer looking to learn about infrastructure as code? Today, with only .NET, you can now automate your infrastructure deployments. No need to worry about languages you don't know. This session will explain how to build, test and deploy our infrastructure by writing C# code.

## 67 Building Native Android Apps with .NET  -  Shadrack Inusah  
08:30 (PT) | 16:30 (UTC) | 17:30 (Local)

I'll show you the steps to build your first Android application in Visual Studio 2019 with .NET. We will see how to build a basic app and then compile and deploy using Android emulators.

## 68 Analyzing Memory Dumps of .NET Applications  -  Giovanni Bassi  
09:00 (PT) | 17:00 (UTC) | 18:00 (Local)

When an application does not work as expected in production, few options are available. Often it is not possible to debug, and bugs are not reproducible on dev machines. When that happens it is not easy to fix the problem, and a memory dump analysis is an excellent tool to help find the bug.

## 69 Enhancing Test Readability with Extension Methods and Fluent Interfaces  -  Nico Paez  
09:30 (PT) | 17:30 (UTC) | 18:30 (Local)

Automated tests are a key enabler for Continuous Delivery and in such context is very important to keep test code clean and readable. In this session we will explore a set of techniques that combined with some C# specific features can help you to enhance your test code in a considerable way.

## 70 Application State in Blazor Apps  -  Carl Franklin  
10:00 (PT) | 18:00 (UTC) | 19:00 (Local)

Carl shows you the benefits of keeping application data outside components and pages, how to do cross-component change notifications, and how to persist that AppState to localstorage.

## 71 2 years, 200 applications: A .NET Core Migration at Enterprise Scale  -  Lizzy Gallagher  
10:30 (PT) | 18:30 (UTC) | 19:30 (Local)

Does migrating your organization's codebase to .NET Core feel unattainable? Come be encouraged with the war stories from a massive migration!

## 72 Blazor Stability Testing Tools for Bullet Proof Applications  -  Ed Charbeneau  
11:00 (PT) | 19:00 (UTC) | 20:00 (Local)

.NET in the browser may sound like Blazor's strength, however the story of Blazor testing may just be its biggest potential upside. In this session we'll discuss what makes Blazor an ideal candidate for: Unit Testing, Integration Testing, and Automated System Testing.

## 73 Robust Connected Applications with Polly, the .NET Resilience Framework  -  Bryan Hogan  
11:30 (PT) | 19:30 (UTC) | 20:30 (Local)

Want to see how to make your applications much more resilient and reliable with just a few lines of code? With Polly, the .NET resilience framework (a .NET Foundation project), your application can easily tolerate transient faults and longer outages in remote systems or infrastructure. Come see how Polly can make your application a rock solid piece of work.

## 74 From Web Forms to Blazor - Introducing the Blazor Web Forms Components  -  Jeff Fritz  
12:00 (PT) | 20:00 (UTC) | 21:00 (Local)

There are millions of ASP.NET Web Forms applications out there. How do you migrate them to .NET Core? With Blazor of course! In this talk, learn about the easy steps you can take to successfully migrate your application to Blazor with the BlazorWebFormComponents.

## 75 ML.NET, Azure and Xamarin: Best Friends Forever  -  Veronika Kolesnikova  
12:30 (PT) | 20:30 (UTC) | 21:30 (Local)

Machine Learning is a hot topic now. It's used in all kinds of applications: web, desktop, mobile. If you are a .NET developer you already have all the knowledge to create a smart cloud cross-platform mobile application with the help of ML.NET, Xamarin and Azure. Come see how.

## 76 Trailblazor: Building Dynamic Applications with Blazor  -  Shaun Walker  
13:00 (PT) | 21:00 (UTC) | 22:00 (Local)

Underpinning Blazor's ability to create interactive web UIs using C# instead of JavaScript is a robust component model which offers exciting new opportunities for developers to create dynamic web applications. In this session we will explore a modular application framework for Blazor called Oqtane.

## 77 Validation Rules for Xamarin  -  Luis Matos  
13:30 (PT) | 21:30 (UTC) | 22:30 (Local)

Learn how to spend less time validating users' input and improve the experience offered to users by using validations rules.

## 78 Building Cross-Platform Desktop Apps with Electron.NET  -  John Juback  
14:00 (PT) | 22:00 (UTC) | 23:00 (Local)

Leverage your ASP.NET skills to deliver native applications for Windows, Mac, and Linux environments using Electron.NET.

* [@jjuback](https://twitter.com/jjuback)
* [ElectronNET/Electron.NET](https://github.com/ElectronNET/Electron.NET)
* [jjuback/NETConf2020](https://github.com/jjuback/NETConf2020)
* debug:
    * dotnet core attach
        * electron proc
* VSCode Excel Viewer to view csv and xsl
* [.NET UI Controls | Tools for WinForms, WPF, UWP, ASP.NET MVC | ComponentOne](https://www.grapecity.com/componentone)
* Electron Alternative: [Chromely](http://chromely.org/)

## 79 Running an Azure Static Web App with an API  -  Vaibhav Gujral  
14:30 (PT) | 22:30 (UTC) | 23:30 (Local)

Heard of Azure Static Web Apps? Come join this session to learn how to build and publish an Azure Static Web app in minutes with a backend API.

* [@vabgujral](https://twitter.com/vabgujral)
* [Vaibhav Gujrals Blog](https://vaibhavgujral.com/)
* [vabgujral - Overview](https://github.com/vabgujral)
* [vabgujral/MyBlazorDemo](https://github.com/vabgujral/MyBlazorDemo)
* [staticwebdev/blazor-starter](https://github.com/staticwebdev/blazor-starter)

## 80 Writing Event Based Microservices using Steeltoe  -  David Tillman  
15:00 (PT) | 23:00 (UTC) | 00:00 (Local)

Steeltoe has become a popular .NET framework used in building enterprise grade microservices. Recently Steeltoe added support for building event based microservices using common off the shelf message brokers. In this session see how to create message based microservices using the framework.

* [dtillman - Overview](https://github.com/dtillman)
* [SteeltoeOSS/Steeltoe](https://github.com/SteeltoeOSS/Steeltoe)
* [Enabling .NET Apps with Monitoring and Management Using Steeltoe](https://tanzu.vmware.com/content/slides/enabling-net-apps-with-monitoring-and-management-using-steeltoe-2)

## 81 Build native and hybrid mobile apps with Mobile Blazor Bindings  -  Eilon Lipton  
15:30 (PT) | 23:30 (UTC) | 00:30 (Local)

Extend your Blazor skills from the web to mobile apps with `Mobile Blazor Bindings`. This experimental project enables using Blazor to build native and `hybrid apps` for mobile and desktop platforms using a single code base and single skill set. Build your app and it will run on the most popular platforms, while getting all the native advantages that each platform has to offer.

* [@original_ejl](https://twitter.com/original_ejl)
* pInvoke into native
* [Eilon/CatTrackerDemo](https://github.com/Eilon/CatTrackerDemo)
* [Unified Blazor UI in the Mobile Blazor Bindings Preview 5 | ASP.NET Blog](https://devblogs.microsoft.com/aspnet/unified-ui-mobile-blazor-bindings-preview-5/)
* [xamarin/MobileBlazorBindings](https://github.com/xamarin/MobileBlazorBindings)

## 82 Build Real Embedded IoT with C# using Meadow  -  Adrian Stevens  
16:00 (PT) | 00:00 (UTC) | 01:00 (Local)

Use the `Meadow IoT platform` to build enterprise-grade hardware solutions that run full .NET on embeddable microcontrollers. We'll deploy C# apps to real hardware with Visual Studio. Learn how to control hardware using software patterns and techniques you already use for cloud, desktop and mobile!

* [@adrian_stevens](https://twitter.com/adrian_stevens)
* [adrianstevens - Overview](https://github.com/adrianstevens)
* [Home page](https://www.wildernesslabs.co/)
* [Wilderness Labs Developer Portal](http://developer.wildernesslabs.co/)
* [Meadow.Foundation API Reference Documentation | Meadow.Foundation API website](http://developer.wildernesslabs.co/docs/api/Meadow.Foundation/)
* [WildernessLabs/Clima](https://github.com/WildernessLabs/Clima)
* [Meadow F7 Micro Development kit w/Hack Kit Pro.](https://store.wildernesslabs.co/collections/frontpage/products/meadow-f7-micro-development-board-w-hack-kit-pro)
* [Hackster.io - The community dedicated to learning hardware.](https://www.hackster.io/WildernessLabs)

## 83 Lessons Learned from Building the YARP Proxy on .NET  -  Sam Spencer  
16:30 (PT) | 00:30 (UTC) | 01:30 (Local)

YARP is an open source reverse proxy being built on top of .NET, to provide an extensible proxy for use by 1P and 3P customers. Its being built on top of .NET and we have used it as forcing function to ensure that the platform has sufficient infrastructure and has been the driver for a number of improvements to ASP.NET and System.Net.Http libraries. We’ll walk through YARP and some of the lessons we learned building it.

* [@samsp](https://twitter.com/samsp)
* [YARP Documentation](https://microsoft.github.io/reverse-proxy/)
* [Getting Started with YARP](https://microsoft.github.io/reverse-proxy/articles/getting_started.html)
* [microsoft/reverse-proxy](https://github.com/microsoft/reverse-proxy)
* route
* load-balance
* handle some part self
* terminate ssl
* http/2 e.g. for gRPC
* async callbacks
* Alternatives
    * [HAProxy](https://www.haproxy.org/)
    * NginX

--- 
# Takeaways

* Inner loop
    * 09, 30 `Tye` as inner loop
    * 10 Include `.NET runtime` with `.NET core scripts`
* IaC:
    * 50 `Pulumi` as IaC deploy
* CI/CD:
    * 47 `DevOps Starter` using `Github Actions` or `ADO` as CI/CD
    * 25, 59 `github actions`
    * 48 Deploy to NAS via ADO (+ IoT)
    * 59 `Cake` - Cs build
* Debug
    * 29 `dotnet-trace`
    * 23 Dev using `Roslyn Analyzers`
* Other
    * 42 CodeGen in .NET
    * 27 Using `Azure SDK`
    * 24 `Swagger` included in 5.0
    * 20 Remote dev in `github codespaces`
    * 52 EF reverse eng with `EF core Power Tools`
    * 58 `Blazor` and `GraphQl`
* IoT: 
    * 48 Raspberry Pi
    * 82 Meadow


The End