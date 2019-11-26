Title: Application Lifecycle Management (ALM) Processes
Date: 2099-01-01 00:00
Category: DevOps
Tags: #alm, #codereview

# ALM Processeses

## Code Review

### Git as process-rule handler?

In the **(1) Fork and Pull** git model code review should be done [after a Pull Request (PR)](https://guides.github.com/introduction/flow/) in a feature branch.  
Likewise in the **(2) Shared Repository** git model.

In (1) you have 
* **Contributers** to send PRs.
* **Maintainers** to do code-review and merge changes.

In (2) the repo is the same (no fork) and our enterprise team wants to have both roles for all.  
Can we live without branching in our small team?  
Or is merging so easy with Git, that we want the benefits from branching?  

### Setting the code standards

Which rules should the code be validated against?

* Should there exist a **design review** or should it be allowed to **trash the whole change** due to **badly chosen design**?
* Does a code change oppinion mean that the code **must** be changed or is it only **nice-to-have** or should the change be done at **next change** ?
* Must Design Patterns or links to examples have to added in oppinions?
* Should there exist **automated code / performance check** that must be applied to?
* Maybes: How can we check for **Bad Complexity** - does the code add any value? _(Ref: The Developer's Code)_
    * When not to use review - doesn't HotDog-code needs review?
    * When not to use Entities and Services (Classes)?
    * When not to use Generics?
    * When not to use Inheritance?
    * When not to use DI/UnitTests?
    * When not to use Layers?
    * When not to use Trace?
    * When not to use ORMs?
    * When not to use CI/CD?
    * When not to use Authentication/Authorization?
    * Avoid BUFD (Big upfront Design) - YAGNI (You ain't gonna need it) - KISS (Keep it simple, Stupid)
* Do's:
    * Use correct data types ( don't use strings everywhere)
    * Use names - not abbreviations (e.g. not CLX32)
* Dont's:
    * Don't put logic in dto's (data tranfer objects)
* How can we check for the best level of doing **workflow / deviance** coding?
    * When not to use Azure Logic Flow?
    * When not to use Events brokers / Service Busses?
    * When not to use Finite State Machines?
    * When not to use Switch?
    * When not to use If?

### Finding the Maintainer

* Can the Contributer **choose** his wanted Maintainer?
* Or are the Maintainers **fixed** for per system, per tech or per something else?
* Should Contributers and Maintainer work in teams with someone they have the **best relation** with?

# Links

* My old blogs
    * TFS as AGile tool: [TFS 2008 test drive](https://rasor.wordpress.com/2008/11/08/tfs-2008-test-drive/)
        * [TFS 2008 inst: Errors](https://rasor.wordpress.com/2008/11/07/tfs-inst-errors/)
    * HowTo working Agile: [Agile Project managent](https://rasor.wordpress.com/2013/02/10/agile-project-managent/)
    * Git processes: [Contributing to Open Source](https://rasor.github.io/contributing-to-open-source.html)
    * Creating SW designs: [System SW Architecture](https://rasor.wordpress.com/2017/01/18/system-sw-architecture/)

The End
