Title: ASP.NET Core 3 and React
Date: 2099-01-01 00:00
Category: Develop
Tags: #csharp, #react, #netcore3

# Running code from eBook `ASP.NET Core 3 and React`

* eBook (2019-12): [ASP.NET Core 3 and React](https://www.packtpub.com/product/asp-net-core-3-and-react/9781789950229)
    * By [@carlrippon](https://twitter.com/carlrippon) 
    * on  github as [carlrip](https://github.com/carlrip)
    * home: [https://www.carlrippon.com/books/](https://www.carlrippon.com/books/)
* Code: 
    * https://github.com/PacktPublishing/ASP.NET-Core-3-and-React
    * Tested on Fork: https://github.com/rasor/ASP.NET-Core-3-and-React

## Install

### PreReqs

See list on [github](https://github.com/PacktPublishing/ASP.NET-Core-3-and-React):
* VS Code
* FrontEnd
    * [Node.js](https://nodejs.org/en/)
* Backend
    * VS Code plugins: 
        * [C# for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csharp)
        * [SQL Server (mssql)](https://marketplace.visualstudio.com/items?itemName=ms-mssql.mssql)
    * .NET Core SDK: [Download .NET Core 3.1 SDK (v3.1.402) - Windows x64 Installer](https://dotnet.microsoft.com/download/dotnet-core/thank-you/sdk-3.1.402-windows-x64-installer?journey=vs-code)
    * [SQL Express](https://www.microsoft.com/en-us/sql-server/sql-server-downloads)
        * Connection string: `Server=localhost\SQLEXPRESS;Database=master;Trusted_Connection=True;`
        * Verify:
        ```ps1
        # From CMD shell:
        sqlcmd -S localhost\SQLEXPRESS -E
        select @@Version
        go
        # Microsoft SQL Server 2019 (RTM) - 15.0.2000.5 (X64)
        ```
        * Optionally [Configure Windows Firewall](https://docs.microsoft.com/en-us/sql/sql-server/install/configure-the-windows-firewall-to-allow-sql-server-access?view=sql-server-ver15)
    * [SQL Server Management Studio (SSMS) - SQL Server Management Studio (SSMS)](https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver15)

## Run code

* Open VSCode in folder .\ASP.NET-Core-3-and-React\Chapter08
```bash
# Terminal for Backend:
cd Chapter08
cd backend
dotnet restore
dotnet run
# Master ConnectionString => Data Source=localhost\SQLEXPRESS;Initial Catalog=master;Integrated Security=True;Password=
# Created database QandA
# Beginning transaction
# Checking whether journal table exists..
# Journal table does not exist
# Beginning transaction     
# Beginning database upgrade
# Checking whether journal table exists..
# Journal table does not exist
# Executing Database Server script 'QandA.SQLScripts.01-Tables.sql'
# Checking whether journal table exists..
# Creating the [SchemaVersions] table
# The [SchemaVersions] table has been created
# Executing Database Server script 'QandA.SQLScripts.02-Sprocs.sql'
# Upgrade successful
# info: Microsoft.Hosting.Lifetime[0]
#       Now listening on: https://localhost:5001
# info: Microsoft.Hosting.Lifetime[0]
#       Now listening on: http://localhost:5000
# info: Microsoft.Hosting.Lifetime[0]
#       Application started. Press Ctrl+C to shut down.
# info: Microsoft.Hosting.Lifetime[0]
#       Hosting environment: Development
# info: Microsoft.Hosting.Lifetime[0]
#       Content root path: \ASP.NET-Core-3-and-React\Chapter15\backend
```

Test from SMSS:
```sql
  SELECT * FROM [QandA].[dbo].[Question]
```

Test from browser:
* [http://localhost:5000/api/questions/](http://localhost:5000/api/questions/)
* [http://localhost:5000/api/questions/?search=type](http://localhost:5000/api/questions/?search=type)
* [https://localhost:5001/api/questions/](https://localhost:5001/api/questions/)

These will give you json responses.

* Press `ctrl-c` to stop the webserver.

The End
