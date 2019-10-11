Title: Azure Practize
Date: 2099-01-01 00:00
Category: DevOps
Tags: #azure

## Azure Portal Home

* [Microsoft Azure](https://portal.azure.com/#home)
    * [Learn Azure](https://docs.microsoft.com/en-us/learn/browse/?products=azure&resource_type=learning%20path)
    * [Monitor](https://portal.azure.com/#blade/Microsoft_Azure_Monitoring/AzureMonitoringBrowseBlade/overview)
    * [Security Center](https://portal.azure.com/#blade/Microsoft_Azure_Security/SecurityMenuBlade/0)
    * [Cost Management](https://portal.azure.com/#blade/Microsoft_Azure_CostManagement/Menu/overview)

## Azure Cloud Shell

When you want to use the cloud shell via browser you need to create:
* Resource Group
    * Storage Account
        * File Share
 
References
* BASH: [az](https://docs.microsoft.com/en-us/cli/azure/reference-index?view=azure-cli-latest)
    * Source: [Azure/azure-cli](https://github.com/Azure/azure-cli)
* PS1: [Az modules](hhttps://docs.microsoft.com/en-us/powershell/module/?view=azps-2.7.0)
    * Source: [Azure/azure-powershell](https://github.com/Azure/azure-powershell)
    * [Other PS1 Modules](https://docs.microsoft.com/en-us/powershell/module/)

### Select Subscription

When running from local CLI, then you'll have to select **current subscription**:
```bash
# BASH login
az login
# Change to wanted subscription
az account list
az account set -s "some subscription name"
az account show
```

```ps1
# PS1 login
connect-azaccount
# Change to wanted subscription
Get-AzContext -ListAvailable
set-azcontext -subscriptionname "some subscription name"
Get-AzContext
```

### Get help from CLI

```bash
# BASH
# Structure
# az [ group ] [ subgroup ] [ command ] {parameters}
# List all cmdlets
az -h
# View group help
az vm -h
# View command help
az vm create -h
```

```ps1
# PS1
# List all cmdlets in the Az.Accounts module
Get-Command -Module Az.Accounts
# List all cmdlets that contain VirtualNetwork
Get-Command -Name '*VirtualNetwork*'
# List all cmdlets that contain VM in the Az.Compute module
Get-Command -Module Az.Compute -Name '*VM*'
# View the basic help content for Get-AzSubscription
Get-Help -Name Get-AzSubscription
# View the examples for Get-AzSubscription
Get-Help -Name Get-AzSubscription -Examples
# View the full help content for Get-AzSubscription
Get-Help -Name Get-AzSubscription -Full
# View the help content for Get-AzSubscription on https://docs.microsoft.com
Get-Help -Name Get-AzSubscription -Online
```
 
The End
