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
    * [All az powershell modules](https://github.com/Azure/azure-powershell/blob/master/documentation/azure-powershell-modules.md)
    * Source: [Azure/azure-powershell](https://github.com/Azure/azure-powershell)
    * [Other PS1 Modules](https://docs.microsoft.com/en-us/powershell/module/)
        * Print installed: `get-module`
        * Install (e.g. Azure Stack): `install-module -name azs -allowclobber`

### Select Subscription

When running from local CLI, then you'll have to select **current subscription**:
```bash
# BASH
az -v
# azure-cli                         2.0.74

# login
az login
# Change to wanted subscription
az account list
az account set -s "some subscription name"
# show current
az account show
az logout
```

```ps1
# PS1 login
connect-azaccount
# Change to wanted subscription
Get-AzSubscription
Get-AzContext -ListAvailable #subset of above
set-azcontext -subscriptionname "some subscription name"
# show current
Get-AzContext
disconnect-azaccount
```

### Get help from CLI

[Tips for using Azure CLI effectively](https://github.com/Azure/azure-cli/blob/dev/doc/use_cli_effectively.md)

```bash
# BASH
# Structure
# az [ group ] [ subgroup ] [ command ] {parameters}
# List all commands
az -h
# find a command
az find blob
# View group help
az vm -h
# View command help
az vm create -h
# looking up resource group and name
az vm show -g [tab][tab]
# AccountingGroup   RGOne  WebPropertiesRG
az vm show -g WebPropertiesRG -n [tab][tab]
# StoreVM  Bizlogic
az vm show -g WebPropertiesRG -n Bizlogic
az vm list --output table # {json,jsonc,table,tsv,yaml,none}
# Using jq
az vm list --output jsonc | jpterm
# filter with http://jmespath.org/
az vm list --query "[?provisioningState=='Succeeded'].{ name: name, os: storageProfile.osDisk.osType }"
# Name                    Os
# ----------------------  -------
# storevm                 Linux
# bizlogic                Linux
```

```ps1
# PS1
# List all az commands in currently installed az. modules
Get-Help '-az'
# List all cmdlets containing account in name
Get-Help account
# List currently installed modules
Get-Module
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

### Resource Group and ARM

Study:
* [Learn](https://docs.microsoft.com/en-us/learn/browse/?products=azure-resource-manager)
* [Course | AZ-103.1 | AzureAcademy - Resource Manager](https://training.azure-academy.com/courses/course-v1:FP+AZ-103.1+2019_T3/course/#block-v1:FP+AZ-103.1+2019_T3+type@sequential+block@d14c5e7b-2617-7a76-c09d-cde3c1584c9d)

Resource Group Tips:
* Administrate via **Portal, BASH, PS1, SDK or REST API**
    * New features: Max **180 days** from API to Portal
    * API is provided by **resource provider**s - i.e. Microsoft.Storage providing storage accounts
        * A resource **provider** delivers many resource **types**
        * Format: {resource-provider}/{resource-type}
        * Example: Microsoft.KeyVault/vaults
        * A resource-type needs valid API version and locations
* Use **ARM** templates for **deploy**
    * Use **same ARM template** for different **environments**
    * Link groups, so a group can be a shared group (e.g. infrastructure spanning systems)
* Use **CLI** terminals (**BASH or PS1**) for **manage** (start, stop, delete, etc)
    * Delete group, when not used
* **Deploy, upgrade, manage, delete, apply-RBAC-to, tag, monitor** resources as a **single entity**
    * View **billing** based on resourses with same **tag**
    * View **systems** based on resourses with same **tag**
    * View **infra** based on resourses with same **tag**
    * Create **resource groups** based on these (tag-)groupings, which also separates **lifecycle**s
* Resource **Groups**:
    * cannot share same resource
    * cannot be renamed
    * can span regions
    * can scope RBAC
    * needs a location (region) for storing their metadata - though its resources can be in different regions
    * can **move** its **resources** to other **groups** - even in other **subscriptions**
        * [Guide](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-move-resources#services-that-can-be-moved)
        * Some [services can't be moved](https://docs.microsoft.com/en-us/azure/azure-resource-manager/move-support-resources)
        * Both **groups** will be **locked** until move completes, but resources will not be down
        * Both **subscriptions** 
            * must be **active**
            * must have **same Azure AD tenant ID**
        * Target **subscription** 
            * must have the **provider registered**
            * must be within [limits and quotas](https://docs.microsoft.com/en-us/azure/azure-subscription-service-limits)
        * Minimum **permissions** needed: **RG write** and **RG mmoveResources**
        * When moving across subscriptions:  
        **Dependent resources** must be moved together with wanted resource to move   
* **Resources**
    * can interact with resources in other groups
* Resource Manager **Settings**:
    * **Locks**:
        * To avoid accidental deletion
        * Apply on level
            * Subscription
                * Resource Group or
                    * Resource
        * Are inherited by child resources
        * Apply by **Owner**s or **User Access Admin**s
    * Tags
    * Users
    * Automation scripts

[Deploy resources with Azure CLI and template](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-template-deploy-cli)
```bash
# BASH
az group create --name ExampleGroup --location "Central US"
az group deployment create \
  --name ExampleDeployment \
  --resource-group ExampleGroup \
  --template-file storage.json \
  --parameters storageAccountType=Standard_GRS
# print
az group list # all yours - default: json format
az group list --output table # {json,jsonc,table,tsv,yaml,none}
az group list --output yaml # cool - converting json to yaml
# filter with http://jmespath.org/
az group list --query "[?location == 'westeurope']"
az group list --query "[].name[?contains(@,'Exa')=='true']" # hmm - contains not working on my pc - am I missing a pip install or npm install?
az group show -n ExampleGroup
# Cleanup
az group delete -n ExampleGroup 
```

[Deploy resources with PowerShell and template](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-template-deploy)
```ps1
# PS1
$resourceGroupName = Read-Host -Prompt "Enter the Resource Group name (i.e 'rg-envirname-infracontainer-or-systemname')" 
$location = Read-Host -Prompt "Enter the location (i.e. centralus or westeurope)"

New-AzResourceGroup -Name $resourceGroupName -Location $location
New-AzResourceGroupDeployment -ResourceGroupName $resourceGroupName `
  -TemplateFile c:\MyTemplates\azuredeploy.json
# print
Get-AzResourceGroup # all yours
Get-AzResourceGroup $resourceGroupName
# Cleanup
Remove-AzResourceGroup $resourceGroupName
```

#### Move Resources

* [Guide](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-move-resources#services-that-can-be-moved)

![Move in 3 steps](https://docs.microsoft.com/en-us/azure/azure-resource-manager/media/resource-group-move-resources/cross-subscription-move-scenario.png)  
(Image by Microsoft)

```bash
# BASH
# AAD Tenant in both subscriptions must match
az account show --subscription <your-source-subscription> --query tenantId
# Register provider in target subscription
az provider list --query "[].{Provider:namespace, Status:registrationState}" --out table
az provider register --namespace Microsoft.Batch
# Move
webapp=$(az resource show -g OldRG -n ExampleSite --resource-type "Microsoft.Web/sites" --query id --output tsv)
plan=$(az resource show -g OldRG -n ExamplePlan --resource-type "Microsoft.Web/serverfarms" --query id --output tsv)
az resource move --destination-group newgroup --ids $webapp $plan
```
```ps1
# PS1
# AAD Tenant in both subscriptions must match
(Get-AzSubscription -SubscriptionName <your-source-subscription>).TenantId
# Register provider in target subscription
Get-AzResourceProvider -ListAvailable | Select-Object ProviderNamespace, RegistrationState
Register-AzResourceProvider -ProviderNamespace Microsoft.Batch
# Move
$webapp = Get-AzResource -ResourceGroupName OldRG -ResourceName ExampleSite
$plan = Get-AzResource -ResourceGroupName OldRG -ResourceName ExamplePlan
Move-AzResource -DestinationResourceGroupName NewRG -ResourceId $webapp.ResourceId, $plan.ResourceId
```

-------------------------------

```bash
# BASH
```
```ps1
# PS1
```

The End
