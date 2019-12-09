Title:  Chain 2 API - Chainlink
Date: 2099-01-01 00:00
Category: Develop
Tags: #blockchain, #chainlink, #api, #hackathon, #honeycomb

* Hackathons
    * 2019-11: [Honeycomb Smart Contract Hackathon](https://honeycomb.devpost.com/)
        * Rules: [Honeycomb Smart Contract Hackathon](https://honeycomb.devpost.com/rules)
        * Hackathon Questions: [Honeycomb Marketplace Discord Discord](https://discordapp.com/invite/NgKdSv4)
        * Other Questions: [Honeycomb Telegram](https://t.me/clcgio)
    * Other Chainlink hackathons:
        * [Exploring the Wide Variety of Winning Chainlink Applications](https://blog.chain.link/exploring-the-wide-variety-of-winning-chainlink-applications-from-recent-hackathons/)
* About Chainlink and Hoenycomb:
    * Docs: 
        * What is Chainlink? [Welcome to Chainlink](https://docs.chain.link/docs)
        * [Architecture Overview](https://docs.chain.link/docs/architecture-overview)
        * [Chainlink External Adapters Explained](https://blog.chain.link/chainlink-external-adapters-explained/)
        * What is Hoenycomb? [Honeycomb Joins the Chainlink Reference Data Contract](https://medium.com/clc-group/honeycomb-joins-the-chainlink-reference-data-contract-45b873576010)
            * Honeycomb API Marketplace provides **per call priced premium API data** to smart contract developers **over the Chainlink network**. We **serve this data over a number of Chainlink nodes** connected to a large number of **external adapters** 
        * Why Chainlink? [Honeycomb Joins the Chainlink Reference Data Contract](https://medium.com/clc-group/honeycomb-joins-the-chainlink-reference-data-contract-45b873576010)  
            * Aggregation of multiple APIs into a single deterministic answer
            * Put trust on Oracles (e.g. Honeycomb) - not on API (transport)
                * Provides highly secure and reliable oracles to large enterprises (Google, Oracle and SWIFT)
    * Honeycomb Services: [Home - CLC Group](https://www.clcg.io/)
        * [Honeycomb - CLC Group](https://www.clcg.io/honeycomb/)
        * -> Login: [Honeycomb](https://honeycomb.market/)
            * [API Marketplace](https://developer.honeycomb.market/browse-apis)
            * [Dapp Store](https://honeycomb.market/dappstore)
* Dev:
    * Outgoing flow:
        * (ETH) **Blockchain DApp** calls 
        * **Chainlink Dapp** (on-chain Oracle - see [Honeycomb DApp store](https://honeycomb.market/dappstore)) which uses/aggregates  
        * **External Adapter** (see [API Marketplace](https://developer.honeycomb.market/browse-apis)) that calls
        * **External API** (off-chain)
    * Blockchain DApps
        * [Using Chainlink Reference Data Contracts](https://docs.chain.link/docs/using-chainlink-reference-contracts)
        * HowTo: [Consume Chainlinks](https://docs.chain.link/docs/contract-creators-overview)
        * Chainlinks to Consume
            * [Chainlinks (Ethereum Mainnet)](https://docs.chain.link/docs/chainlinks-ethereum-mainnet)
        * [Viewing Chainlink Transactions on the Ropsten Testnet](https://blog.chain.link/viewing-chainlink-transactions-on-the-ropsten-testnet/)
        * DApp code generator: [CONTRACTOR - CoinList](https://coinlist.co/build/chainlink/projects/4d7f84a3-8f93-4262-8281-5691257df35d)
    * Honeycomb (Partner nodes hosting Chainlink Oracle **jobs**/DApps)
        * [Honeycomb Marketplace 101 for Ethereum Developers](https://medium.com/clc-group/honeycomb-marketplace-101-for-ethereum-developers-c7c63c2d3049)
        * [Example Walkthrough](https://docs.chain.link/docs/example-walkthrough)
        * Blog: [CLC Group – Medium](https://medium.com/clc-group)
            * [Honeycomb Marketplace 101 for Ethereum Developers](https://medium.com/clc-group/honeycomb-marketplace-101-for-ethereum-developers-c7c63c2d3049)
        * Wiki + Starter: [honeycomb-wiki](https://github.com/clc-group/honeycomb-wiki/wiki)
        * HowTo create Oracle DApps: [Contract Creators](https://docs.chain.link/docs/contract-creators)
    * Chainlink network (Chainlink node hosting on-chain Oracle DApps/External Adapters)
        * Blog: [Development - Chainlink](https://blog.chain.link/tag/development/)
        * HowTo + Starter: [How to use Chainlink with Truffle](https://blog.chain.link/how-to-use-chainlink-with-truffle-2/)
            * [Using Truffle to interact with Chainlink Smart Contracts | Blog | Truffle Suite](https://www.trufflesuite.com/blog/using-truffle-to-interact-with-chainlink-smart-contracts)
        * HowTo: [Running a Chainlink Node for the First Time](https://blog.chain.link/running-a-chainlink-node-for-the-first-time/)
        * Wiki: [Chainlink Wiki](https://github.com/smartcontractkit/chainlink/wiki)
            * [Development Setup Guide](https://github.com/smartcontractkit/chainlink/wiki/Development-Setup-Guide)
        * API: [Chainlink](https://docs.chain.link/reference)
    * Chainlink Faucet
        * [Ropsten Chainlink Faucet](https://ropsten.chain.link/)
        * [Rinkeby Chainlink Faucet](https://rinkeby.chain.link/)
        * [Kovan Chainlink Faucet](https://kovan.chain.link/)
* APIs available for hackathon participants (on API Marketplace - see above): 
    * Aeris Weather - Weather data
    * Aviation Edge - Flight schedules 
    * Brave New Coin - Crypto market data
    * PeakMetrics - News data
    * Coinlayer - Crypto market rates
    * Crowdscores - Soccer scores
    * Currencylayer - Forex rates
    * Daneel - Blockchain news and market data 
    * Data Sports Group - Sports scores and statistics 
    * EOD Historical Data - Traditional market rates
    * Fixer - Forex rates
    * Geo DB Cities - Global City and Region Data
    * Ipstack - IP geolocation
    * NeutrinoAPI - Utility functions, inc. SMS and email outputs
    * Regulus - Company details database
    * Sports Open Data - Sports data
    * SteamAPIs - Steam marketplace data
    * Tatum Blockchain API - Blockchain data
    * TheRundown - Sports scores and odds
    * Twinword - Text analysis
    * World Weather Online - Weather data
* Other APIs: [API Marketplace - Free Public &amp; Open Rest APIs | RapidAPI](https://rapidapi.com/)
* Data scraping
    * [Kristjan Kirpu · PEPZ](https://pepzwee.com/)
* Chainlink Projects /Oracles
    * Inspiration: [44 Ways to Enhance Your Smart Contract With Chainlink](https://blog.chain.link/44-ways-to-enhance-your-smart-contract-with-chainlink/)
    * Upcoming
        * [Oracle selects first 20 startups for Chainlink blockchain project - Ledger Insights](https://www.ledgerinsights.com/oracle-selects-startups-chainlink-project/)
* Press
    * [What is the &#039;oracle problem&#039; &amp; how does Chainlink solve it? | Data Driven Investor](https://www.datadriveninvestor.com/2019/06/15/what-is-the-oracle-problem-how-does-chainlink-solve-it/) - including Google announcement
    * [Building hybrid blockchain/cloud applications with Ethereum and Google Cloud | Google Cloud Blog](https://cloud.google.com/blog/products/data-analytics/building-hybrid-blockchain-cloud-applications-with-ethereum-and-google-cloud)  
    ![Chainlink + Google](https://storage.googleapis.com/gweb-cloudblog-publish/images/Untitled_6.max-1600x1600.png)  
    _Image by Google_
    * 
* Other
    * TCF (Off-chain Trusted Compute Framework)
        * Hyperledger Avalon: [Introducing Hyperledger Avalon](https://www.hyperledger.org/blog/2019/10/03/introducing-hyperledger-avalon)
        * Chainlink and TCF/TEE: [Chainlink and the Trusted Compute Framework](https://medium.com/coinmonks/chainlinks-implications-in-the-trusted-compute-framework-7b7628c86b09)
    * TEE (Off-chain Trusted Execution Environments)
        * Intel SGX
        * ARM TrustZone
        * TEE Oracle [Town Crier](https://www.town-crier.org/what-is-tc.html) - using Intel SGX
            * [Getting Started](https://www.town-crier.org/get-started.html)
        * [IoTeX & Chainlink: Delivering Real World Data to the Blockchain](https://medium.com/iotex/iotex-chainlink-delivering-real-world-data-to-the-blockchain-17abb11981a7)

The End
