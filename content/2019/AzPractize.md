Title: Azure Practize
Date: 2099-01-01 00:00
Category: DevOps
Tags: #azure, #cli, #ps1, #snapstore, #linux, #ssh, #azdevops, #git

# Azure Practize

## Intro

In this blog I am training for Azure certifications by going through howto deploy the basic resources in Azure through CLI (BASH and PS1) and through ARM templates.

I setup devops envir on an **Ubuntu Linux** and create scripts for deploy ARM templates, so it becomes easy to build and tear-down training environments.

Credits: Much of the learning comes from these sources
* Online Course: [Azure Academy Dashboard](https://training.azure-academy.com/dashboard) 
    * [AZ-103.1 | Azure Administrator](https://training.azure-academy.com/courses/course-v1:FP+AZ-103.1+2019_T3/course/)
    * [AZ-400.3 | Implementing Continuous Delivery](https://training.azure-academy.com/courses/course-v1:FP+AZ-400.3+2019_T1/course/)
* Lab instructions: [Microsoft Learning](https://github.com/MicrosoftLearning)
    * [AZ-103-MicrosoftAzureAdministrator](https://github.com/MicrosoftLearning/AZ-103-MicrosoftAzureAdministrator)
* Live Action:
    * The Cloud: [Microsoft Azure Portal](https://portal.azure.com/#home)
    * The CI/CD tool: [Azure DevOps Portal](https://dev.azure.com/)
        * [ARM Outputs](https://marketplace.visualstudio.com/items?itemName=keesschollaart.arm-outputs)
    * Visual Studio Code
        * [Azure Pipelines](https://marketplace.visualstudio.com/items?itemName=ms-azure-devops.azure-pipelines)
        * [GitHub Pull Requests](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github)
* Content templates:
    * ARM template repo: [azure-quickstart-templates](https://github.com/Azure/azure-quickstart-templates)
    * [Azure DevOps Demo Generator](https://azuredevopsdemogenerator.azurewebsites.net/)
        * [microsoft/TailwindTraders](https://github.com/microsoft/TailwindTraders)
            * ---> [Integrating Azure DevOps](https://github.com/microsoft/TailwindTraders/tree/master/Documents/DemoScripts/Integrating%20Azure%20DevOps%2C%20Microsoft%20Teams%20and%20GitHub)
            * Setup environments with Deployment Slots: [Walkthrough: Azure App Service Features](https://github.com/microsoft/TailwindTraders/tree/master/Documents/DemoScripts/Modernizing%20.NET%20Apps#walkthrough-azure-app-service-features)
        * [microsoft/PartsUnlimited](https://github.com/microsoft/PartsUnlimited)
        * NodeJs: [microsoft/ContosoAir](https://github.com/microsoft/ContosoAir)
 * Read:
    * Learn: [Microsoft Learn Azure](https://docs.microsoft.com/en-us/learn/browse/?products=azure)
        * [Azure Portal - Learn](https://docs.microsoft.com/en-us/learn/browse/?products=azure-portal)
        * [Azure DevOps - Learn](https://docs.microsoft.com/en-us/learn/browse/?products=azure-devops)
    * Docs: 
        * [Microsoft Azure Documentation](https://docs.microsoft.com/en-us/azure/index#pivot=products&panel=all)
        * [Azure DevOps documentation](https://docs.microsoft.com/en-us/azure/devops/?view=azure-devops)

# Azure Portal Home

In the Azure Portal I can quickly create a resource into an existing (or new) resource group, so I can export the ARM template and add it to my Infra-As-Code (IaC) git repo for easy reuse.

* [Microsoft Azure](https://portal.azure.com/#home)
    * [Learn Azure](https://docs.microsoft.com/en-us/learn/browse/?products=azure&resource_type=learning%20path)
    * [Monitor](https://portal.azure.com/#blade/Microsoft_Azure_Monitoring/AzureMonitoringBrowseBlade/overview)
    * [Security Center](https://portal.azure.com/#blade/Microsoft_Azure_Security/SecurityMenuBlade/0)
    * [Cost Management](https://portal.azure.com/#blade/Microsoft_Azure_CostManagement/Menu/overview)

# Azure Cloud Shell and Local CLIs

Sometimes you want to run a shell from a **browser** to avoid installing an azure shell locally.  

When you want to use the cloud shell you need to create:
* Resource Group
    * Storage Account
        * File Share

## Local CLIs - Install on Linux

### BASH 

On Ubuntu Linux you by default have a BASH CLI called terminal installed, but you need to install the [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-apt?view=azure-cli-latest).  
You can install it via `Snap Store`, but it did not work for me.  Instead you can use curl:
```bash
# BASH
# Install Azure CLI
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
# check if zure CLI is installed
az -v
```

### PS1

On Ubuntu Linux you don't have a PowerShell CLI. You can install it via the [Snap Store](https://snapcraft.io/snap-store)
```bash
# BASH
# Install snap store if you don't have it
sudo apt update
sudo apt install snapd # snapcraft daemon
sudo snap install snap-store # GUI for above
```

Now open `snapstore` app, search for `PowerShell` and install it.  
Info: This will install `/snap/powershell/39/opt/powershell/pwsh`. We will later use it from within Visual Studio Code.  
  
Up untill 2019 Azure was managed with module `AzureRM`. Now it is managed with module `az`. So now you can get the same features both in BASH and in PS1 (short for PowerShell).  

Now open the `PowerShell` CLI (hiding in the Administration group of apps) and install the `az` module:
```ps1
# PS1
# Install Azure module
Install-Module -Name Az -AllowClobber -Scope CurrentUser
```

## Other tools

From snap store do also install 
* `Visual Studio Code` # PS1 Script editor and CLI
    * Install plugins
        * [PowerShell](https://marketplace.visualstudio.com/items?itemName=ms-vscode.PowerShell) - Replaces `Powershell ISE`, which was suppurted before Powershell 6
            * Installs:
                * Powershell integrated Console. 
                    * Open it with `Ctrl+shift+p "pow show"`. Opposed to other terminal windows there is only one instance of this running.
                    * `$host` reveals it is called Visual Studio code host. 
                * Powershell command explorer A list under Extensions in the left side.
        * [Azure Tools](https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-node-azure-pack) - a collection of azure extensions - including `Azure CLI Tools`
        * [Shell launcher](https://marketplace.visualstudio.com/items?itemName=Tyriar.shell-launcher)
            * Configure the launcher, so you can open PS1 shells within VS Code
                * Create or open `~/.config/Code/User/keybindings.json`:  
                (Ctrl+Shift+P) Preferences: Open Keyboard Shortcuts (JSON) 
                * Add json in keybindings.json: `{"key": "ctrl+shift+t","command": "shellLauncher.launch"}`
                * Create or open `~/.config/Code/User/settings.json`:  
                (Ctrl+Shift+P) Preferences: Open Settings (JSON)
                * Add json in settings.json:  
                ```json
                "shellLauncher.shells.linux": [
                    {
                    "shell": "pwsh",
                    "label": "ps1 shell"
                    },
                    {
                    "shell": "bash",
                    "args": ["-l"],
                    "label": "bash shell"
                    }
                ],
                "terminal.explorerKind": "external"            
                ```
            * Test the terminal:
                * Open the CLI: `(ctrl+shift+t) ps1`. There can be multiple of this terminal
                * Issue a cmd: `$host`. Reveals it is called ConsoleHost.
    * Ref: [keyboard-shortcuts-linux](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-linux.pdf)
* `Microsoft Azure Storage Explorer`

## Docs and References
* BASH: [az](https://docs.microsoft.com/en-us/cli/azure/reference-index?view=azure-cli-latest)
    * Source: [Azure/azure-cli](https://github.com/Azure/azure-cli)
* PS1: [Az modules](hhttps://docs.microsoft.com/en-us/powershell/module/?view=azps-2.7.0)
    * [All az powershell modules](https://github.com/Azure/azure-powershell/blob/master/documentation/azure-powershell-modules.md)
    * Source: [Azure/azure-powershell](https://github.com/Azure/azure-powershell)
    * [Other PS1 Modules](https://docs.microsoft.com/en-us/powershell/module/)
    * [PowerShellGet installs new modules](https://docs.microsoft.com/en-us/powershell/module/powershellget/?view=powershell-6)
    ```ps1
    # Print installed modules
    get-module
    # You might need to allow to fetch official modules
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
    # Install module (e.g. Azure Stack)
    install-module -name azs -allowclobber
    # load module
    Import-Module -Name azs
    ```

## Login and Select Subscription

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

## Get help from CLI

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

## Resource Groups and ARM templates

Study:
* [Learn](https://docs.microsoft.com/en-us/learn/browse/?products=azure-resource-manager)
* [Docs](https://docs.microsoft.com/en-us/azure/azure-resource-manager/)
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
    * Link or nest templates for only having one place to change a set of resources using [linked or nested templates](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-linked-templates)
        * Nested templates are within parent
        * Linked templates are external templates outside parent
    * Link resources between groups, so a group can contain shared resources (e.g. infrastructure spanning systems) having **dependent resources** using [dependsOn](https://docs.microsoft.com/en-us/azure/azure-resource-manager/templates/define-resource-dependency)
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

### Creating Resource Groups

Guide: [Deploy resources with Azure CLI and template](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-template-deploy-cli)
```bash
# BASH
# Create Resource Group
az group create --name ExampleGroup --location "Central US"
# Deploy resources via ARM template
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
# Cleanup - careful - there might be dependent resources in the group
az group delete -n ExampleGroup 
```

Guide: [Deploy resources with PowerShell and template](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-template-deploy)
```ps1
# PS1
$resourceGroupName = Read-Host -Prompt "Enter the Resource Group name (i.e 'rg-envirname-infracontainer-or-systemname')" 
$location = Read-Host -Prompt "Enter the location (i.e. centralus or westeurope)"
# Create Resource Group
New-AzResourceGroup -Name $resourceGroupName -Location $location
# Deploy resources via ARM template
New-AzResourceGroupDeployment -ResourceGroupName $resourceGroupName `
  -TemplateFile c:\MyTemplates\azuredeploy.json
# print
Get-AzResourceGroup # all yours
Get-AzResourceGroup $resourceGroupName
# Cleanup - careful - there might be dependent resources in the group
Remove-AzResourceGroup $resourceGroupName
```

### Creating ARM templates

References:
* [ARM template structure and syntax](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-authoring-templates)
* [Azure Quickstart Templates](https://azure.microsoft.com/en-us/resources/templates/)

You create some PS1 or BASH scripts in [Azure DevOps](#Using-Azure-DevOps) together with your ARM templates and deploy your resources from them.

### Lock Resources

Guide: [Lock Azure resources to prevent changes](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-lock-resources)

```bash
# BASH
# Lock resource and print
az lock create --name LockSite --lock-type CanNotDelete --resource-group exampleresourcegroup --resource-name examplesite --resource-type Microsoft.Web/sites
az lock list --resource-group exampleresourcegroup --resource-name examplesite --namespace Microsoft.Web --resource-type sites --parent ""
# Lock resource group and print
az lock create --name LockGroup --lock-type CanNotDelete --resource-group exampleresourcegroup
az lock list --resource-group exampleresourcegroup
# Print all
az lock list
# Remove
lockid=$(az lock show --name LockSite --resource-group exampleresourcegroup --resource-type Microsoft.Web/sites --resource-name examplesite --output tsv --query id)
az lock delete --ids $lockid
```
```ps1
# PS1
# Lock resource and print
New-AzResourceLock -LockLevel CanNotDelete -LockName LockSite -ResourceName examplesite -ResourceType Microsoft.Web/sites -ResourceGroupName exampleresourcegroup
Get-AzResourceLock -ResourceName examplesite -ResourceType Microsoft.Web/sites -ResourceGroupName exampleresourcegroup
# Lock resource group and print
New-AzResourceLock -LockName LockGroup -LockLevel CanNotDelete -ResourceGroupName exampleresourcegroup
Get-AzResourceLock -ResourceGroupName exampleresourcegroup
# Print all
Get-AzResourceLock
# Remove
$lockId = (Get-AzResourceLock -ResourceGroupName exampleresourcegroup -ResourceName examplesite -ResourceType Microsoft.Web/sites).LockId
Remove-AzResourceLock -LockId $lockId
```

### Move Resources

[Guide](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-move-resources#services-that-can-be-moved)

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

Dependent resources must be moved together, when moving across subscriptions  
![Move in 3 steps](https://docs.microsoft.com/en-us/azure/azure-resource-manager/media/resource-group-move-resources/cross-subscription-move-scenario.png)  
(Image @Microsoft)

## Azure networks

Study:
* [Learn](https://docs.microsoft.com/en-us/learn/browse/?products=azure-virtual-network)
* Docs: [Azure networking](https://docs.microsoft.com/en-us/azure/networking/networking-overview)
* Docs: [VNets](https://docs.microsoft.com/en-us/azure/virtual-network/)
* [Course | AZ-103.1 | AzureAcademy - Virtual Networks](https://training.azure-academy.com/courses/course-v1:FP+AZ-103.1+2019_T3/course/#block-v1:FP+AZ-103.1+2019_T3+type@sequential+block@d74bdc62-11d1-d8bc-8ec0-b20f1110b85e)

Tips:
* VNets:
    * Create **public subnet** for your DMZ in Azure and a **private subnet** for your intranet. Put both in one **VNet**.
        * You can also create a subnet for a VPN Gateway to your onprem network
    * Subnet **ranges** are defined in [CIDR blocks](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing).  
    Example: 10.10.1.64/27 (32-27=5 bits = 32 IPs for a subnet starting with IP 10.10.1.64)  
        * [CIDR to IPv4 Address Range Utility Tool | IPAddressGuide](https://www.ipaddressguide.com/cidr)
        * **4 IPs are reserved** by Azure in **each subnet** (3 in beginning + 1 in end)
        * Don't reuse a range (both onprem and VNet), that is already used by your organization.
    * Default Max 50 VNets / subscription / region. Can be increased to 500.
    * Use [Bastion server](https://docs.microsoft.com/en-us/azure/networking/networking-overview#bastion) if you need RDP to VMs without public IP
    * Use [Service endpoints](https://docs.microsoft.com/en-us/azure/networking/networking-overview#serviceendpoints) for connection your subnet to SaaS resources like Azure SQL and storage. This limits access to the resources.
    * Optional: Protect each subnet with a firewall called **NSG** (Network Security Group)

Bastion server:  
![Bastion server](https://docs.microsoft.com/en-us/azure/networking/media/networking-overview/architecture.png)  
(Image @Microsoft)

Service endpoint:  
![Service endpoint](https://docs.microsoft.com/en-us/azure/networking/media/networking-overview/vnet-service-endpoints-overview.png)  
(Image @Microsoft)

VPN to OnPrem:  
![VPN to OnPrem](https://docs.microsoft.com/en-us/azure/networking/media/networking-overview/vpngateway-multisite-connection-diagram.png)  
(Image @Microsoft)

-------------------------------
# Using Azure DevOps

Refs:
* Portal: [Azure DevOps](https://dev.azure.com/)

## Intro

It was previously called VSTS and Visual Studio online before that.  
In relation to Azure Resources we want to use DevOps for storing version controlled ARM templates and their deployment pipeline as well.

Starting out simple we can have a PS1 script called `create-envir.ps1` for deployment.  
It takes a parameter (-envir:t) for telling whether we want to deploy to test (t) or to prod (p).  
The script will be stored in a git-repo called `IaC`.  
It will 
* Select subscription
* Create resource group 
* Deploy ARM template(s)

It also takes a parameter (-delete:$false), so you can use the script to delete the resource group, when done.  

## Enable connect from VSCode to AzDevOps repo

I prefer to use SSH keys for authetication from editor (VSCode) to git-repo (Azure DevOps).  
You need to create a SSH public key and upload it to Azure DevOps - Guide: [Connect to your Git repos with SSH - Azure Repos](https://docs.microsoft.com/en-us/azure/devops/repos/git/use-ssh-keys-to-authenticate?view=azure-devops)

After you have created a SSH key pair into `~/.ssh/` (or you might want to reuse an existing pair)  
then upload the SSH public key to your AzDevOps account:
```bash
# Using Linux:
# Copy the contents of the id_rsa_youruserid_github.pub file to your clipboard
xclip -sel clip < ~/.ssh/id_rsa_youruserid_github.pub
```

* Goto [https://dev.azure.com/ryouruserid/_usersSettings/keys](https://dev.azure.com/youruserid/_usersSettings/keys)
* Add SSH key
* Paste key: Ctrl-V
* Title: vscode_youruserid_github
* Save key

You also need to save AzDevOps url to [~/.ssh/known_hosts](https://stackoverflow.com/questions/52711525/cant-clone-git-repo-and-getting-error-ssh-askpass-exec-usr-bin-ssh-askpass):
`ssh-keyscan -t rsa ssh.dev.azure.com >> ~/.ssh/known_hosts`

## First push to AzDevOps repo

Now create a repo at AzDevOps - mine is called `iac-01`.  
Then clone the repo to your local PC: 
```bash
# BASH
cd ~/some-project-dir
git clone git@ssh.dev.azure.com:v3/ryouruserid/iac-01/iac-01
cd iac-01
# Print remote url
git remote -v
# create a file
touch README.md
# start VSCode
code .
```

Now add some text into README.md and use VSCode for commit and push the code to AzDevOps.  

Later: Create the PS1 script....

-------------------------------
# Azure DevOps Demo Generator

## Intro

To get a head start with **Azure DevOps**, then we in this section will use **Azure DevOps Demo Generator** to fork a Github demo web project which we can create a full CI/CD pipeline towards **Azure**

I was evaluating two projects, which both can be created using **Azure DevOps Demo Generator**:

Code Projects including deploy scripts:
* Modern: 
    * Guide: [microsoft/TailwindTraders](https://github.com/microsoft/TailwindTraders/tree/master/Documents/DemoScripts/Integrating%20Azure%20DevOps%2C%20Microsoft%20Teams%20and%20GitHub)
        * MS Teams integration
            * Connector: Azure DevOps:
                * Guide: [Integrating Microsoft Teams with Azure DevOps Services](https://azuredevopslabs.com/labs/vstsextend/teams/#integrating-microsoft-teams-with-azure-devops-services)
                * Guide: [Create a service hook for Azure DevOps Services and TFS with Microsoft Teams](https://docs.microsoft.com/en-us/azure/devops/service-hooks/services/teams?view=azure-devops)
                * Azure DevOps connector not available in Teams Free edistion! [DevOps Connector and Visual Studio app is missing. - Developer Community](https://developercommunity.visualstudio.com/content/problem/420390/devops-connector-and-visual-studio-app-is-missing.html)
            * App: Azure Boards
                * [Azure Boards with Microsoft Teams - Azure Boards](https://docs.microsoft.com/en-us/azure/devops/boards/integrations/boards-teams?view=azure-devops)
                * [Microsoft Teams with Azure DevOps Services (Collaborate, Communicate and Celebrate)](https://azuredevopslabs.com/labs/vstsextend/teams/#azure-devops-kanban-board--dashboards-in-teams)
            * App: Azure Repos
                * [Azure Repos with Microsoft Teams - Azure Repos](https://docs.microsoft.com/en-us/azure/devops/repos/integrations/repos-teams?view=azure-devops)
            * App: Azure Pipelines
                * [Azure Pipelines with Microsoft Teams - Azure Pipelines](https://docs.microsoft.com/en-us/azure/devops/pipelines/integrations/microsoft-teams?view=azure-devops)
                * [Microsoft Teams with Azure DevOps Services (Collaborate, Communicate and Celebrate)](https://azuredevopslabs.com/labs/vstsextend/teams/#azure-pipelines-with-microsoft-teams)
    * Frontend Code [TailwindTraders-Website](https://github.com/microsoft/TailwindTraders-Website/blob/master/Deploy/DeployWebAKS.ps1)
    * Backend Code [TailwindTraders-Backend](https://github.com/microsoft/TailwindTraders-Backend/tree/master/Deploy)
* 3y old: 
    * Guide: [Introduction to Auto-assembly usage - Lab](https://training.azure-academy.com/courses/course-v1:FP+AZ-400.3+2019_T1/courseware/083e1ae3-93c7-1f72-6306-1765a78799e4/649fcbb5-9ffd-8340-28fb-ffd7acdf7aa2/1?activate_block_id=block-v1%3AFP%2BAZ-400.3%2B2019_T1%2Btype%40vertical%2Bblock%40cc9d8629-1a01-32f3-c599-647e806bdf90)
    * Code: [microsoft/PartsUnlimited](https://github.com/microsoft/PartsUnlimited/tree/master/env)

Needless to say that I continued with the modern one - TailwindTraders.  

## Implement TailwindTraders DevOps integration

The integration process is described in guide: [Integrating Azure DevOps, Microsoft Teams and GitHub](https://github.com/microsoft/TailwindTraders/tree/master/Documents/DemoScripts/Integrating%20Azure%20DevOps%2C%20Microsoft%20Teams%20and%20GitHub).  
I have used a **personal (MSDN) account**, since with my enterprise account I don't have permissions to create DevOps projects, which is needed by the Demo Generator.  
But using pesonal account means you cannot connect to MS Teams, since **Azure DevOps connector** (in MS Teams) requires
* Non-free MS Teams (O365) account
* DevOps and MS Teams accounts must be in same AAD tenant (same org)

Prerequisites:
* Accounts
    * Github account
    * Azure account
    * Azure Devops account
* SW
    * VS Code
        * [Azure Pipelines](https://marketplace.visualstudio.com/items?itemName=ms-azure-devops.azure-pipelines)
        * [GitHub Pull Requests](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github)
    * Git

### Prefill an Azure DevOps project

Using Azure DevOps Demo Generator you can prefill an Azure DevOps project, so you can get to know what you get OOTB (out of the box).  

Steps:
* Open the [Azure DevOps Demo Generator webapp](https://azuredevopsdemogenerator.azurewebsites.net/?name=tailwindtraders)
* Login to Azure Devops and select an organization
* Give this new project a name. I gave mine the name `TailwindForkedMsDemo`.
* Select the template `Tailwind Traders`
* Select option `Yes, I want to fork`. With this option the webapp will fork the two github repos for Tailwind Traders to your own github account. This enables you to make changes to the code, which will trigger a build in Azure DevOps
    * [TailwindTraders-Website](https://github.com/microsoft/TailwindTraders-Website) and
    * [TailwindTraders-Backend](https://github.com/microsoft/TailwindTraders-Backend) 
* Go ahead and press `Create Project`

You should now have personal forks of the Github repos and an Azure DevOps projects, that 

-------------------------------

```bash
# BASH
```
```ps1
# PS1
```
-------------------------------

# Links

* My old blogs
    * [Azure Fundamentals Course 107979F](https://rasor.github.io/azure-fundamentals-course-107979f.html)
    * [Microsoft Architecture and Implementations](https://rasor.github.io/microsoft-architecture-and-implementations.html)

The End
