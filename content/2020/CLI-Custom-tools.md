Title: Write CLI tools
Date: 2099-01-01 00:00
Category: Develop
Tags: #cli, #repl, #javascript, #featherjs, #csharp, #bash, #yeoman, #rest, #faas, #curl, #postman

CLI's are the heart of local automation using command scripts.  
API's are the heart of remote automation using curl scripts.  

Here I use the term 
* `CLI Tool` as a common synonym for
    * Console app
    * Command Line tool
    * Shell script
* `CLI` as a common synonym for
    * Shell
    * CMD
    * BASH
    * Powershell
* `API` as a common synonym for
    * A REST service

Sometimes you want to write your own command (CLI Tool) that can be used locally from a BASH CLI or remotely via REST.  
Here are some usecases:
```text
CLI             -  CLI Tool              - REST API
--------------------------------------------------------------
                   CLI Tool - write (1)
                   CLI Tool (2)         <- CLI Tool - download
                   CLI Tool (3)         -> REST API
                   CLI Tool             <- REST API (4)
                   CLI Tool (5)         -> Yeoman
CLI - write (6)
```

1) Write BASH CLI tools
* Awesome List: [sw-yx/cli-cheatsheet](https://github.com/sw-yx/cli-cheatsheet)
* [Vorpal](https://vorpal.js.org/)
    * [Feathers - Built on the Shoulders of Giants](https://github.com/gaearon/feathers-docs/blob/master/why/philosophy.md#built-on-the-shoulders-of-giants)
* [commander](https://www.npmjs.com/package/commander)
    * [commander examples](https://github.com/tj/commander.js/tree/master/examples)
    * 2015: [Building command line tools with Node.js - Atlassian Developer Blog](https://blog.developer.atlassian.com/scripting-with-node/)
* Using React or Stencil in your CLI via [Import-jsx](https://www.npmjs.com/package/import-jsx)

2) Run adhoc CLI tools
* npm runner: [Introducing npx: an npm package runner](https://blog.npmjs.org/post/162869356040/introducing-npx-an-npm-package-runner)
    * Exec js gist: [npx is cool](https://gist.github.com/zkat/4bc19503fe9e9309e2bfaa2c58074d32)

3) Call REST API from CLI
* curl
* [newman](https://www.npmjs.com/package/newman) - CLI for postman

4) Convert CLI to REST API (call cli remotely with curl)
* OpenFaaS: Call CLI from FaaS [Turn Any CLI into a Function with OpenFaaS](https://blog.alexellis.io/cli-functions-with-openfaas/)
* cmd.io: [Using the Run API - Cmd Documentation](https://www.cmd.io/guides/run-api/)

5) Write template generators.  
E.g. you make an angular CLI and want it to have a generate command
* Write Generators with [yeoman](http://yeoman.io/)

6) Write CLIs (REPLs)
* C# REPL: [Building a C# Interactive shell in a browser with Blazor (WebAssembly) and Roslyn](https://www.strathweb.com/2019/06/building-a-c-interactive-shell-in-a-browser-with-blazor-webassembly-and-roslyn/)

The End
