Title: Scaffolding DB layer from DB
Date: 2099-01-01 00:00
Modified: 2099-01-01 00:00
Category: Develop
Tags: #csharp, #ef, #db, #mvc

## Intro

ASP.NET MVC has build-in scaffolding enabling you to generate a frontend from a DB with a snap, so you can browse your DB. This has been a feature since around 2010.  

It is a great feature to use for PoCs and demos.  

In this blog I'll use Northwind DB and scaffold a master-detail view of `orders` and `order details`

## Install

### Prerequisites

* SMSS
* Visual Studio

### Install Northwind SQL DB

* Clone [Northwind DB](https://github.com/Microsoft/sql-server-samples/tree/master/samples/databases/northwind-pubs)
* or clone a [subset](https://github.com/microsoft/sql-server-samples#cloning-only-a-subset-of-the-repo-with-sparse-checkout)

```bash
# Bash:
# full clone
git clone https://github.com/microsoft/sql-server-samples.git
cd sql-server-samples/samples/databases/northwind-pubs
```

* Open SMSS
* Connect to the target SQL Server
    * In my case I connect to `localhost\SQLEXPRESS`
* Open `instnwnd.sql` in SMSS
* Execute `instnwnd.sql`

```sql
-- check if we got some data
SELECT * FROM orders
-- gives 830 rows
```

## Scaffold

### Create a webapp

```bash
# Bash:
mkdir CsScaffoldNorthwind
cd CsScaffoldNorthwind

# We need a c# web template - what is its name?
dotnet new -l
# dotnet gitignore file                             gitignore                                  Config
# ASP.NET Core Web App (Model-View-Controller)      mvc                      [C#], F#          Web/MVC
# Solution File                                     sln                                        Solution
dotnet new mvc
# We need a solution file
dotnet new sln
# We need a gitignore file
dotnet new gitignore

# Test build and run
dotnet build
dotnet run
```

Open the web in a browser on either  

* https://localhost:5001/ or
* http://localhost:5000/
* Press Ctrl-C to stop the webserver

#### Testing the webapp from VS  

* Open the sln file in VS
* In Sln Explorer right-click sln and add existing project - select CsScaffoldNorthwind.csproj
* In the Run-dropdown select `CsScaffoldNorthwind`
* Press F5. Now VS will run `dotnet run` in the background and start a browser for you.

Above code is [V.0.0.1](https://github.com/rasor/CsScaffoldNorthwind/releases/tag/0.0.1)

### 

## Links

* [Scaffolding ASP.NET Core MVC](https://www.c-sharpcorner.com/article/scaffolding-asp-net-core-mvc/)
* [ASP.NET MVC - Scaffolding - Tutorialspoint](https://www.tutorialspoint.com/asp.net_mvc/asp.net_mvc_scaffolding.htm)
* [Get the sample SQL Server databases for ADO.NET code samples - ADO.NET](https://docs.microsoft.com/en-us/dotnet/framework/data/adonet/sql/linq/downloading-sample-databases#get-the-northwind-sample-database-for-sql-server)

The End.
