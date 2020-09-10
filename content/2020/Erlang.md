Title: Erlang
Date: 2099-01-01 00:00
Category: Develop
Tags: #erlang, #elixir, #cli, #beam

* Download 
    * Erl REPL: [Erlang Programming Language](https://www.erlang.org/downloads)
        * Download a prebuild version e.g. http://erlang.org/download/otp_win64_23.0.1.exe
        * Put erl in your path - Run CMD as admin
        `SETX PATH "%PATH%;%ProgramFiles%\erl-23.0.1\bin" /M`
        * Verify install: 
        ```bash
        erl
        # Eshell V11.0.1
        # 1>
        ```
    * Erl Webserver: [Nine Nines: Cowboy User Guide](https://ninenines.eu/docs/en/cowboy/2.6/guide/)
        * Code: [ninenines/cowboy](https://github.com/ninenines/cowboy)
    * Erl Webserver: [Yaws](http://yaws.hyber.org/)
        * Linux: `apt-get install yaws`
        * Windows: [/download/windows/](http://yaws.hyber.org/download/windows/)
        * Verify install: 
        ```bash
        yaws --help
        yaws --version
        # Yaws 2.0.4
        ```
    * Erl WebFramework: [Chicago Boss: The Erlang Web Framework](http://chicagoboss.org/)
    * Erl WebFramework/AppServer: [N2O](https://synrc.com/apps/n2o/doc/web/)
        * Erlang JavaScript Parse Transform
        * SSR with Erl on cli and srv
        * Offline cli
        * Cowboy Rest API
        * Nitrogen DSL templates
    * Erl **AVZ** authorization library
    * Erl key-value storages access library **KVS**
    * Erl **MQS** Message Bus client library (gproc, emqttd)
    * Erl Webserver lib: [mochi/mochiweb](https://github.com/mochi/mochiweb)
    * Erl Package Manager: [Rebar3](https://www.rebar3.org/docs)
        * Code: [Getting Started](https://www.rebar3.org/docs)
    * Elixir WebFramework: [Phoenix Framework](https://www.phoenixframework.org/)
* QuickStarts
    * [Erlang/OTP 23.0](https://erlang.org/doc/index.html)
    * [Erlang Programming Language](https://www.erlang.org/docs)
    * [Erlang -- Getting Started With Erlang](https://erlang.org/doc/getting_started/users_guide.html)
    * [Erlang -- OTP Design Principles](https://erlang.org/doc/design_principles/users_guide.html)
    * [Erlang from behing the trenches by Francesco Cesarini](https://www.slideshare.net/nashjain/erlang-from-behing-the-trenches-by-francesco-cesarini)
    * [Learning Erlang - Easier than you think](https://www.youtube.com/watch?v=OCkL9z8IxOI)
    * Elixir [Processes](https://elixir-lang.org/getting-started/processes.html)
    * Elixir Build tool: [Introduction to Mix](https://elixir-lang.org/getting-started/mix-otp/introduction-to-mix.html)
* BEAM (Erlang VM)
    * [BEAM (Erlang virtual machine) - Wikipedia](https://en.wikipedia.org/wiki/BEAM_(Erlang_virtual_machine))
    * [Comparison of application virtualization software - Wikipedia](https://en.wikipedia.org/wiki/Comparison_of_application_virtualization_software)
    * [Erlang BEAM Instruction Set](http://www.cs-lab.org/historical_beam_instruction_set.html)
    * [Elixir and The Beam: How Concurrency Really Works](https://medium.com/flatiron-labs/elixir-and-the-beam-how-concurrency-really-works-3cc151cddd61)
    * Tooling Mix instead of Rebar
    * Ruby like syntax
    * [Elixir vs Erlang | Learn the Key Differences of Elxir vs Erlang](https://www.educba.com/elixir-vs-erlang/)
    * [Elixir vs Erlang 2020](https://medium.com/@devathon_/elixir-vs-erlang-2020-de0facb6cd92)
* OTP
    * Supervisors - branches
    * Workers - leaves
        * Managers
            * Starts other workers
* Monitoring
    * [Nagios Monitoring for Erlang](https://lethain.com/nagios-monitoring-for-erlang/)
    * [lethain/nagios_erlang](https://github.com/lethain/nagios_erlang)
    * [Monitoring and Preemptive Support The Road to Five Nines on the Beam - Francesco Cesarini](https://www.youtube.com/watch?v=EHqs_RrVMoE)
    * [Erlang & Elixir DevOps From The Trenches - Why we felt the need to formalize operational experience with the BEAM virtual machine](https://www.erlang-solutions.com/blog/erlang-elixir-devops-from-the-trenches-why-we-felt-the-need-to-formalize-operational-experience-with-the-beam-virtual-machine.html)
* Other Docs
    * Benchmarked all the existing modern web frameworks [N2O](https://synrc.com/framework/web/)
    * [Comparison of Erlang Web Frameworks](https://github.com/ChicagoBoss/ChicagoBoss/wiki/Comparison-of-Erlang-Web-Frameworks)
    * Webserver theory and tests
        * [Nine Nines: The modern Web](https://ninenines.eu/docs/en/cowboy/2.6/guide/modern_web/)
        * [A comparison between Misultin, Mochiweb, Cowboy, NodeJS and Tornadoweb](http://www.ostinelli.net/a-comparison-between-misultin-mochiweb-cowboy-nodejs-and-tornadoweb/)
    * [Wayback Machine](https://web.archive.org/web/20170615113350/https://esl-website-production.s3.amazonaws.com/uploads/document/file/77/The_route_to_the_successful_adoption_of_non-mainstream_programming_languages_-_Erlang_Solutions_Whitepaper_2017_.pdf)
* Events
    * [BEAM Virtual Meetup: Come listen to SAŠA JURIĆ, author of Elixir in Action](https://www.meetup.com/erlangusergroup/events/272331762/)
        * [@sasajuric](https://twitter.com/sasajuric)
        * [@FrancescoC](https://twitter.com/FrancescoC)
    * ClojErl: [Virtual BEAM Meetup GMT, July 29 - Clojerl on the BEAM!](https://www.youtube.com/watch?v=ooN3AiF8qPQ&feature=youtu.be)
* Plugin
    * [Remote&#32;-&#32;Containers&#32;-&#32;Visual&#32;Studio&#32;Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

### Yaws

Readme:

For just running yaws, it works pretty much the same as on UNIX.
Commands that don't work are --id, --heart and some more
Try yaws --help for available options.

Just starting

> yaws -i 

Starts a basic yaws system with a yaws.conf taken from
the install dir.

The End

### Blockchain

* [Blockchain 2018: Myths vs Reality | Erlang Solution blog](https://www.erlang-solutions.com/blog/blockchain-2018-myths-vs-reality.html)
* [Blockchain No Brainer Ownership in the Digital Era](https://www.erlang-solutions.com/blog/blockchain-no-brainer-ownership-in-the-digital-era.html)
* [æternity - a blockchain for scalable, secure and decentralized æpps](https://aeternity.com/)
    * [BLOCKCHAIN INNOVATOR ÆTERNITY CHOOSES ERLANG TO SCALE TO BILLIONS OF USERS](https://esl-web-static.s3.amazonaws.com/uploads/document/file/86/aeternity_Case_Study_-_blockchain_Erlang_scale_billions_users_2018___Erlang_Solutions.pdf)