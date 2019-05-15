Title: Blockchain hackathons
Date: 2099-01-01 00:00
Category: Dev
Tags: #blockchain, #ethereum, #dai, #0x, #nucypher, #python

# Ethereum

* Truffle Quick Start Guide
    * Book: [Truffle Quick Start Guide | PACKT Books](https://www.packtpub.com/web-development/truffle-quick-start-guide)
    * Code: [PacktPublishing/Truffle-Quick-Start-Guide](https://github.com/PacktPublishing/Truffle-Quick-Start-Guide)
* Code: Create tokens. [ConsenSys/Tokens](https://github.com/ConsenSys/Tokens)
* kEth for test: [kovan-testnet/faucet](https://github.com/kovan-testnet/faucet#kovan-faucet)

### The Graph 

Using [GraphQL](GraphQlApollo.md) for querying Blockchains.  
Tool - GraphiQL: [Filling in the GraphQL pipeline: Ready-to-use code generation ·](https://www.onegraph.com/blog/2019/05/03_Filling_in_the_GraphQL_Pipeline_Ready_to_use_code_generation.html)


The Graph:  

* Invite: [The Graph Hackathon on CoinList Build - CoinList](https://coinlist.co/build/the-graph)
* Services: [Graph Explorer - Find all the data being indexed on The Graph](https://thegraph.com/explorer/)
* [The Graph (@graphprotocol) | Twitter](https://twitter.com/graphprotocol)
* Code: [graphprotocol](https://github.com/graphprotocol)

Blogs:  
* [Mohamed ElSeidy on Twitter](https://twitter.com/Drmelseidy/status/1124363757344436224)
    * [On The Value of Decentralized Querying - Token Daily](https://www.tokendaily.co/blog/on-the-value-of-decentralized-querying-)



#### Alternative querying techs

* [Chromapolis | Where Dapps Thrive (@chromapolis) | Twitter](https://twitter.com/chromapolis)
* VulcanizeDB by [Rick Dudley (@AFDudley0) | Twitter](https://twitter.com/AFDudley0/status/1093804937098788865)
* [Introducing Faster Ethereum Logs and Events](https://blog.infura.io/faster-logs-and-events-e43e2fa13773)
    * [QuickBlocks.io (@quickblocks) | Twitter](https://twitter.com/quickblocks/status/1119040622181199872) - Run your own node (for your DApps) so queries becomes fast.
* [POA Network (@poanetwork) | Twitter](https://twitter.com/poanetwork)
* [Scanners](BlockchainTokens.md)

#### Other articles

* [Private Keys + Websites = 💀](https://medium.com/mycrypto/private-keys-websites-aa85b42113a0)

### NuCypher  + CoinList hackathon 2019-03

* [rasor/nuc-openfaas](https://github.com/rasor/nuc-openfaas)

#### Other tech

* [Contracts, Swarm, Whisper](https://ethereum.stackexchange.com/a/388/50076)
    * [building the decentralized web 3.0](https://blog.ethereum.org/2014/08/18/building-decentralized-web/)
    * Ethereum Contracts - Decentralized Logic
    * Swarm - Distributed p2p storage and msg routing: [1. Introduction Swarm 0.3 documentation](https://swarm-guide.readthedocs.io/en/latest/introduction.html)
    * Whisper - Decentralized messaging
* StateMachine Replication: [Blockchain Consensus - Tendermint](https://tendermint.com/)
* IPFS
    * [Portia Burton, Community Engineer, Protocol Labs / IPFS «Getting started with IPFS»](https://www.youtube.com/watch?v=N76-HcQDuhQ&t=2250s)
* [Fluence network — decentralized data processing that works.](https://fluence.network/)
    * [Dmitry Kurinskiy, Co-founder & CTO, Fluence Labs «Building scalable decentralized backend for your Dapp»](https://www.youtube.com/watch?v=N76-HcQDuhQ&t=183s)

# 0x

* Home: [0x](https://0x.org/) - 0x is an open protocol that enables the P2P exchange of assets on the Ethereum
    * Twitter: [0x (@0xProject)](https://twitter.com/0xProject)
    * Medium: [0x](https://blog.0xproject.com/)
    * Dev: [0x](https://0x.org/docs)
* Intro
    * [Learn 0x. Earn 0x.](https://www.coinbase.com/earn/0x)
    * [Hackathon Workshops](https://www.youtube.com/playlist?list=PLZYHxOo6wufiK_mK71CaudyWpJHCJW1Yk)
    * [0x Acceleration Program](https://0x.org/eap)
        * [Announcing the 0x Ecosystem Acceleration Program](https://blog.0xproject.com/announcing-the-0x-ecosystem-acceleration-program-89d1cb89d565)
    * [0x Price Chart (ZRX) | Coinbase](https://www.coinbase.com/price/0x)
    * [A beginner’s guide to 0x](https://blog.0xproject.com/a-beginners-guide-to-0x-81d30298a5e0)
    * [What is 0x? (ZRX) Beginners Guide, Information & Review](https://blockonomi.com/0x-guide/)
    * [What is 0x? A Beginner’s Guide](https://coincentral.com/0x-beginner-guide/)
    * [Building self-sustaining ecosystems through governance by Will Warren & Peter Zeitz (Devcon4)](https://www.youtube.com/watch?v=-Fnwi5Tvtl0&feature=youtu.be)
    * How to get test Ether/test tokens?  
    See the [Codesandbox](https://codesandbox.io/s/github/0xproject/0x-codesandbox) or [0x Portal](https://0x.org/portal) for an Ether faucet and test token mint. There are other faucets available online.
    * What is asset data?  
    This is a common source of errors, asset data is more than just the contract address. It also contains the Asset Proxy ID to the Proxy it is routed to. For more information on how asset data is encoded, see here (https://github.com/0xProject/0x-protocol-specification/blob/master/v2/v2-specification.md#erc20proxy). To properly encode asset data see [Asset Data utils](https://0x.org/docs/0x.js#assetDataUtils-encodeERC20AssetData).
* 0x Instant
    * [一分鐘做出自己的代幣購買App – Taipei Ethereum Meetup – Medium](https://medium.com/taipei-ethereum-meetup/%E4%B8%80%E5%88%86%E9%90%98%E5%81%9A%E5%87%BA%E8%87%AA%E5%B7%B1%E7%9A%84%E4%BB%A3%E5%B9%A3%E8%B3%BC%E8%B2%B7app-47bacffc4c65)
* Marketplaces - called (order) Relayers
    * A Relayer: [The Complete Beginner’s Guide to Radar Relay Review 2019 - Is it Safe?](https://blockonomi.com/radar-relay-review/)
    * [Radar Relay](https://radarrelay.com/)
        * API
            * [Wallet Manager](https://developers.radarrelay.com/wallet-manager#lightwallet-usage)
    * 0x's own Trade portal (Shop): [0x](https://0x.org/portal) - integrates with MetaMAsk
    * Buid your own shop with [AssetBuyer js](https://0x.org/docs/asset-buyer#usage) - using own or existing relayer
    * Build a relayer: [Introducing the 0x Launch Kit](https://blog.0xproject.com/introducing-the-0x-launch-kit-4acdc3453585)
    * [CollexMarketplace/0x-launch-kit](https://github.com/CollexMarketplace/0x-launch-kit/)

## Shorts

* Short trading: [shorttokens](https://shorttokens.io/)
* [expo](https://expotrading.com/)
* 2019-01-10: [Bitcoin Price Analysis Jan.10: BTC Breaks Down to $3800 Following a Long Squeeze](https://cryptopotato.com/bitcoin-price-analysis-jan-10-btc-breaks-down-to-3800-following-a-long-squeeze/)
    * Quote: _The shorts reached their closest point (22K) to the low of November 14 (19.5K). We all remember that horrible day, the last day we’ve seen Bitcoin above $6000._
* 2018-11-14: [Bitcoin Short Positions Record Their All-Time High on Bitfinex](https://cryptopotato.com/bitcoin-short-positions-record-their-all-time-high-on-bitfinex/)
    * Quote: _the leading margin trading exchange Bitfinex had broken its all-time a high number of open short positions on Bitcoin. This has happened as the short positions just crossed 41,000 BTC._
* [Bitfinex - Rates on Margin Funding](https://www.bitfinex.com/stats#rates) - See "TOTAL AMOUNT USED IN MARGIN POSITIONS" - BTC
* Chart: [Bitcoin shorts vs Longs - Click for BTC margin charts - Datamish](https://datamish.com/d/000000004/btcusd?refresh=20s&orgId=1&from=now-6M&to=now)

## 0x hackathon 2019-01

* [0x + CoinList Hackathon](https://blog.0xproject.com/0x-coinlist-hackathon-3b48ddbfd21c)
    * [0x + Coinlist Hackathon FAQ](https://quip.com/KRs3A5rKbFrN)
    * [0x Hackathon on CoinList Build - CoinList](https://coinlist.co/build/0x)
    * [Your application](https://coinlist.co/build/0x/application)
    * Links: [0x Hackathon, Truffle Framework &amp; the new  Solidity ^0.5.0](https://www.meetup.com/Programmable-Money/events/257888677/)
    * Chat: [Discord](https://discordapp.com/channels/435912040142602260/524673671311130643)
    * Ideas: [22 Ideas to Explore with 0x](https://blog.0xproject.com/22-ideas-to-explore-with-0x-4d551c10dd4e)
    * Cases: [0x Use Cases](https://0x.org/why#cases)
    * Ideas: [ETHSingapore Wishlist and Bounty – bZxNetwork – Medium](https://medium.com/bzxnetwork/ethsingapore-wishlist-and-bounty-6d0b1b1d3ad2)

### 0x Winners

[0x + CoinList Hackathon Recap](https://blog.0xproject.com/0x-coinlist-hackathon-recap-e453b1195533)

* Workshop vids: [CoinList](https://www.youtube.com/channel/UCLSUauF82CnpumnbfwWpKww/videos)
* [Tokenary P2P Exchange - CoinList](https://coinlist.co/build/0x/projects/2e9e7ecb-4c1d-4f2d-a08b-6ff977435f75)
    * Github: [Tokenary/Tokenary-P2P-Exchange](https://github.com/Tokenary/Tokenary-P2P-Exchange)
    * Vid: [YouTube](https://www.youtube.com/watch?v=fS9pqt4jIwM&feature=youtu.be)
* [CashflowRelay - CoinList](https://coinlist.co/build/0x/projects/c84ee1bb-0db6-40b5-a811-29a32d96d8b6)
    * Web: https://www.cashflowrelay.com/
    * Github: [akropolisio/cashflowrelay-testnet](https://github.com/akropolisio/cashflowrelay-testnet)
    * Vid: [VimeUhOh](https://vimeo.com/316377730)
* [Alice - CoinList](https://coinlist.co/build/0x/projects/595631c5-411b-42a0-8083-0df91dfabef2)
    * Github: [markspereira/alice](https://github.com/markspereira/alice)
    * Vid: [Alice - 0x hackathon submission](https://vimeo.com/316001373)
* [Disclose - CoinList](https://coinlist.co/build/0x/projects/1080535c-0e62-4ea8-a2f8-a80e05ecf2b0)
    * Web: [Disclose](https://disclose-authority-client.herokuapp.com/)
    * Github: [stanislasdrg/disclose](https://github.com/stanislasdrg/disclose)
    * Vid1: [YouTube](https://www.youtube.com/watch?v=_pMUf6ox3vY&feature=youtu.be)
    * Vid2: [YouTube](https://www.youtube.com/watch?v=vghPIw6t_JU)
* [Cold Crypto - CoinList](https://coinlist.co/build/0x/projects/1ad38c3e-5b9a-4c75-aef8-d576635e49c4)
    * Web: [Cold Crypto · Secure Crypto Wallet for ETH and EOS](https://duxi.io/cold/0xinstant)
    * Github: [zlumer/qr-packets-demo](https://github.com/zlumer/qr-packets-demo)
    * Vid: [YouTube](https://www.youtube.com/watch?v=dOb4ahfesLU)
* [Mars Nation Land Selector - CoinList](https://coinlist.co/build/0x/projects/4052ca4c-8f54-4d9f-a1e6-b6d985f93547)
    * Web: [Mars Nation Harberger Marketplace](http://harberger-marketplace.s3-website-eu-west-1.amazonaws.com/)
    * Github: [marsnation/area-picker](https://github.com/marsnation/area-picker)
    * Vid: [YouTube](https://www.youtube.com/watch?v=hgOTm_N1B6k&feature=youtu.be)
* [VegaRelay - CoinList](https://coinlist.co/build/0x/projects/9d596d96-c914-4b2c-b2ec-10d269467e8c)
    * Web: [React App](https://serene-brushlands-11501.herokuapp.com/)
    * Github: [michaelhly/vegarelay](https://github.com/michaelhly/vegarelay)
    * Wiki: [michaelhly/vegarelay](https://github.com/michaelhly/vegarelay/wiki)
* [Obvy - CoinList](https://coinlist.co/build/0x/projects/b89130ff-cbe4-4ce8-8818-df3eee027e03)
    * Web: [Obvy](https://www.obvy.io/requests/new)
    * Github: [tqd2ax/obvy](https://github.com/tqd2ax/obvy)
    * Slides: [demo.pdf](https://drive.google.com/file/d/1mKY1F9jFRxXsp7H6T8tCReZ-tNOK_BHv/view)
* [ETHOptions  - CoinList](https://coinlist.co/build/0x/projects/54758bd0-4f06-4e1f-82a3-8cd302d2695c)
    * Github: [parinaA/0x-hack](https://github.com/parinaA/0x-hack)
* [DEFTY - CoinList](https://coinlist.co/build/0x/projects/9d11938a-5c5b-4243-9a34-e3506472d7ca) - Web wallet using Metamask, Ledger and Trezor - Trade loans 
    * Web: [React App](https://defty.netlify.com/)
    * Github: [Defty](https://github.com/DeftyHQ)
    * Vid: [YouTube](https://www.youtube.com/watch?v=SkCBC9eLg4Q&feature=youtu.be)

# Kyber

* Home: [Kyber Network | The On-Chain Liquidity Protocol](https://kyber.network/)
    * [Guide to Kyber Network (KNC) Information, Review & How to Buy KNC](https://blockonomi.com/kybernetwork-guide/)

# Dai hackathons 2018

A Medium article [Dai and CDP Hackathon Projects](https://medium.com/makerdao/dai-and-cdp-hackathon-projects-46a73f7133d2) 
listed several Dai projects

* [WyoHackathon 2018](https://www.wyohackathon.io/)
    * [Token Subscription](https://devpost.com/software/token-subscription)
        * Github: [tokensubscription.com](https://github.com/austintgriffith/tokensubscription.com)
        * Demo: [Token Subscription](https://tokensubscription.com/)
    * [Peregrine](https://devpost.com/software/peregrine-85qdna)
        * Github: [peregrine](https://github.com/opolis/peregrine)
            * [dapphub/ds-group](https://github.com/dapphub/ds-group)
            * [dapphub/ds-token](https://github.com/dapphub/ds-token)
        * Slides: [WyoHackathon - The Bufficorns Presentation](https://docs.google.com/presentation/d/1HLxy8w1b5SaM8Qnaw1-P1hCBI2XZMZxIf0LZ-PJESWg/edit#slide=id.g4179679fd9_1_4)
    * [WyoFlow](https://devpost.com/software/wyoflow)
        * Demo: [Home](http://wyoflow.org/)
    * [Rawhide](https://devpost.com/software/rawhide)
        * Github: [Rawhide](https://github.com/rawhideio)
        * [Rawhide - Fractional Livestock Platform](http://rawhide.io/)
    * [Topicless](https://devpost.com/software/topicless)
        * Github: [shemnon/wyohackathon](https://github.com/shemnon/wyohackathon)
        * Slides: [Topicless](https://docs.google.com/presentation/d/1OkUWPSFAPkFS-_2svyt8FKcOF78VtgL2U7_UW12RZ2g/edit#slide=id.g417b0eb1ef_0_577)
    * [Electronic Corporate Formation Portal](https://devpost.com/software/electronic-corporate-formation-portal)
        * Github: [DigitalCurrencyCompliance](https://github.com/DigitalCurrencyCompliance)
        * Slides: [WyoHackathon 2018.09.09.v1](https://docs.google.com/presentation/d/1vgTG7cBc9RacRNXxDje_ny8jw5Cq62RNT39942zmP4o/edit#slide=id.g4178e62811_0_24)
    * [Trustin.Me](https://devpost.com/software/trustin-me)
        * Github: [dewpey/Trusting.Me-Repo](https://github.com/dewpey/Trusting.Me-Repo)
        * Demo: [https://trustingme.surge.sh/](https://trustingme.surge.sh/)
    * [Undertaker & Petrix](https://devpost.com/software/shenanigans)
* [ETHBerlin Hackathon & Workshops - ETHBerlin](https://ethberlin.com/)
    * [CDP Liquidator](https://devpost.com/software/cdp-liquidator)
        * Github: [xwvvvvwx/liquidator-contracts](https://github.com/xwvvvvwx/liquidator-contracts)
        * Github: [xwvvvvwx/liquidator-frontend](https://github.com/xwvvvvwx/liquidator-frontend)
        * Demo: [CDP Liquidator](http://cdp-liquidator.surge.sh/)
        * Other from the team: [Oasis.direct](https://oasis.direct/)
    * [MakerDAO SuperDashboard](https://devpost.com/software/makerdao-superdashboard)
        * Github: [frostiq/makerdao-superdashboard](https://github.com/frostiq/makerdao-superdashboard)
        * [IPFS is the Distributed Web](https://ipfs.io/)
    * [SplitETH](https://devpost.com/software/spliteth)
        * Github: [SplitETH/SplitETH](https://github.com/SplitETH/SplitETH)
        * Etherscan: [Kovan Accounts, Address And Contracts](https://kovan.etherscan.io/address/0xf478bf1ac8c337474c21f713e874d753c28c4c48#code)
        * Demo: [React App](http://spliteth.s3-website-us-east-1.amazonaws.com/#/)
        * Slides: [ETHBerlin - SplitETH](https://docs.google.com/presentation/d/19Elr5nVLWM9SJH3j_RB69a8eT45zsNH1L-JpOu38uTI/edit#slide=id.g40e6f26bf5_0_77)
    * [SendSomeDai](https://devpost.com/software/sendsomedai)
        * Github: [amhed/send-some-dai-dapp](https://github.com/amhed/send-some-dai-dapp)
        * Demo: [React App](http://www.sendsomedai.com/)
        * Demo: [React App](https://send-some-dai.herokuapp.com/)
    * [Meme Lordz](https://devpost.com/software/meme-lordz)
        * Github: [relevant-community/memelordz-frontend](https://github.com/relevant-community/memelordz-frontend)
        * Slides: [Meme Lordz](https://docs.google.com/presentation/d/1D3drCDtPYKpPAJGv25BisYeXApSyHIoFpMDc9viWjk8/edit#slide=id.g3f1fc4cf36_0_152)
        * Demo: [Meme Lordz: The First Decentralized Meme Market!](https://www.memelordz.com/#/)
* [Whacked Blocks Hackathon](https://www.whackedblocks.com/)
    * Github: [akwodkiewicz/dai-bite-keeper](https://github.com/akwodkiewicz/dai-bite-keeper/)
* December 7 – 9, 2018 [ETHSingapore](https://ethsingapore.devpost.com/)
    * [ZkDAI](https://devpost.com/software/ethsingapore-zk-dai)
        * Medium: [ZkDai — Private DAI transactions on Ethereum using Zk-SNARKs](https://medium.com/@atvanguard/zkdai-private-dai-transactions-on-ethereum-using-zk-snarks-9e3ef4676e22)
        * Github: [atvanguard/ethsingapore-zk-dai](https://github.com/atvanguard/ethsingapore-zk-dai)
    * A lot more projects - [ETHSingapore](https://ethsingapore.devpost.com/submissions)

# Other projects

* Projs: [Blockchain Technology Solutions | Ethereum Solutions | ConsenSys](https://consensys.net/)
* Apps: [40 Ethereum Apps You Can Use Right Now](https://media.consensys.net/40-ethereum-apps-you-can-use-right-now-d643333769f7)
* Projs: [Coinbase | Ventures](https://ventures.coinbase.com/)

# Jobs

* [CTO at Weswap.io - Weswap Jobs on AngelList](https://angel.co/weswap-1/jobs/478609-cto-at-weswap-io)

The End