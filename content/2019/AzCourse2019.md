Title:  Azure Foundations Course 2019
Date: 2099-01-01 00:00
Category: DevOp
Tags: #azure, 

## Notes from Azure Foundations Course

### Pre installing.

Before the course I updated to latest

* Visual Studio
* VsCode

#### Visual Studio

In VSInstaller I selected the Azure package to get Azure SDK installed. This enables [Visual Studio Azure resource group projects](https://docs.microsoft.com/en-us/azure/azure-resource-manager/vs-azure-tools-resource-groups-deployment-projects-create-deploy)

#### Azure CLI

Azure CLI give me convenient `az` commands to run from bash - very nice together with VSCode.  
HowTo: [Install the Azure CLI for Windows](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-windows?view=azure-cli-latest)

After install of MSI package:

* Open PowerShell

```bash
# Verify installation
az -v
# azure-cli                         2.0.58
# .. and a lot of other rows
# Python location 'C:\Program Files (x86)\Microsoft SDKs\Azure\CLI2\python.exe'
# Extensions directory 'C:\Users\<user>\.azure\cliextensions'
```

Notice the CLI is running on Python which it installed for itself.   
_You need to add some path to ENV to be able to run from Git Bash, too._

```bash
# Try login
az login
# Note, we have launched a browser for you to login. For old experience with device code, use "az login --use-device-code"
# You have logged in. Now let us find all the subscriptions to which you have access...
# [
#   {
#     "cloudName": "AzureCloud",
#     "id": "119643ba-5138-4a85-876c-aaaaaaaaaaaa",
#     "isDefault": true,
#     "name": "Visual Studio Enterprise",
#     "state": "Enabled",
#     "tenantId": "eef828d6-45f3-457f-a6e0-aaaaaaaaaaaa",
#     "user": {
#       "name": "someone@testing.az",
#       "type": "user"
#     }
#   }
# ]
```

#### Azure PowerShell

Azure PowerShell will be used for automation scripts together with container yaml files and json ARM templates.  
It replaces AzureRM, which you should uninstall first.  

Installation of [Azure PowerShell with PowerShellGet](https://docs.microsoft.com/en-us/powershell/azure/install-az-ps?view=azps-1.3.0):  

* Open PowerShell

```bash
# While running as admin:

# Allow to download 
Set-ExecutionPolicy RemoteSigned
# Enable remote install
Import-Module PowerShellGet
# Install Azure PowerShell
Install-Module -Name Az -AllowClobber
# Test by connecting to Az
Connect-AzAccount
```

The new tool runs also on Linux (via .NET Standard), so that is why MS made a new one. Read More: [Introducing the Azure PowerShell Az module](https://docs.microsoft.com/en-us/powershell/azure/new-azureps-module-az?view=azps-1.3.0).  
[Here is some Querys](https://docs.microsoft.com/en-us/powershell/azure/queries-azureps?view=azps-1.3.0) to get you started

The End
