Title: Using TFS from VSCode
Status: published
Category: Develop
Date: 2018-09-02 14:00
Tags: #vscode, #tfs, #git

You might continue a while working with TFS before you jump to GIT.  
At least we do that at my work. For frontend projects like Ionic, Angular, etc using a CLI for generation code templates it makes most sense to to stay in VSCode (opposed to Visual Studio).  
So howto use TFS from VSCode?

* Make sure you are already connected to TFS from normal Visual Studio
* From the normal Visual Studio you need to change your workspace from `server` to `local`
    * Goto Source Control Explorer and edit workspaces
    * Change Location from `server` to `local`
    * Map the root of your npm project (in level with package.json) to where you want it (or where it already is) in TFS 

[![edit workspaces](https://raw.githubusercontent.com/Microsoft/vsts-vscode/master/assets/tf-workspace-dialog.png)](https://github.com/Microsoft/vsts-vscode/blob/master/TFVC_README.md#what-is-the-difference-between-a-local-and-server-workspace-how-can-i-tell-which-one-im-working-with)

* Install into VSCode [Visual Studio Team Services](https://marketplace.visualstudio.com/items?itemName=ms-vsts.team) plugin
* In the root of your npm project (in level with package.json) create a [.tfignore](https://docs.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2013/jj155786(v=vs.120)#tfignore-file-example) file.  
Here is a sample:

```bash
# .tfignore
# When using VSCode plugin Visual Studio Team Services
# https://marketplace.visualstudio.com/items?itemName=ms-vsts.team
# .. then you need this .tfignore file

# https://docs.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2013/jj155786(v=vs.120)#tfignore-file-example

# Ignore all files in the sub-folders
\node_modules
\.sourcemaps
\www
\platforms
```

* In VSCode you can now login to TFS with command team - signin, where you´ll enter your corporate password
* So now you can checkin (incl see diffs, undo and exclude) to TFS from the Source Control tab

[![Source Control Tab in VSCode](https://raw.githubusercontent.com/Microsoft/vsts-vscode/master/assets/tfvc-viewlet.png)](https://github.com/Microsoft/vsts-vscode/blob/master/TFVC_README.md#the-tfvc-source-control-viewlet)

The End