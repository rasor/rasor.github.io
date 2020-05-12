Title:  IPFS Pinning summit 2020-05-07
Date: 2099-01-01 00:00
Category: Develop
Tags: #blockchain, #p2p, #ipfs, #filecoin, #textile

* Agenda [IPFS Pinning Summit (May 7th - 8th) (2020)](https://ipfspinningsummit.com/)
    * Organizers:
        * [IPFS Powers the Distributed Web](https://ipfs.io/)
            * [The IPFS Team](https://ipfs.io/team/)
        * [FileCoin](https://filecoin.io/)
            * [Filecoin Documentation](https://docs.filecoin.io/)
            * [Making Storage Deals](https://docs.filecoin.io/how-to/store-making-storage-deals/)
            * [Filecoin Value Proposition](https://discuss.filecoin.io/t/filecoin-value-proposition/788/2)
            * [Technical Barriers to Blockchain](https://protocol.ai/blog/technical-barriers-to-blockchain/)
            * [Filecoin Testnet Mining](https://filecoin.io/blog/filecoin-testnet-mining/)
                * [porepgraphicv2-watermark.png](https://filecoin.io/images/blog/porepgraphicv2-watermark.png)
            * [Filecoin: Proof-of-Replication, Power-Fault-Tolerance and Research Roadmap](https://protocol.ai/blog/filecoin-proof-of-replication-power-fault-tolerance-research-roadmap/)
            * [Skycoin/CXO vs FileCoin/IPFS](https://www.skycoin.com/blog/posts/skycoin-vs-ipfs/)
    * Sponsor: [Protocol Labs](https://protocol.ai/)
    * New Meet: [Join our Cloud HD Video Meeting now](https://protocol.zoom.us/j/97465931409)
* [ipfs/awesome-ipfs](https://github.com/ipfs/awesome-ipfs)
* Chat / Links
    * [oduwsdl/ipwb](https://github.com/oduwsdl/ipwb)
    * [T&#xf5;nu Samuel](https://www.facebook.com/photo.php?fbid=10221054727735964&set=a.1128009638538&type=3&theater)
* 10:00 AM PT   Introduction 
    * 00 Molly Mackinlay [@momack28](https://twitter.com/momack28)
    * Welcome to the IPFS Pinning Summit! The IPFS ecosystem has grown significantly in the last year, creating new opportunities for services and applications. In this talk, we discuss ecosystem growth, the 2020 project roadmap, and what we hope to accomplish from the inaugural IPFS Pinning Summit.
    * Is P2P network
    * Opera has default support, Brave some
    * Use own node or gw to access IPFS network
        * [Public IPFS Gateways](https://ipfs.github.io/public-gateway-checker/)
    * Use Pinning to let data remain on network, when your node is offline
* 10:40 AM PT IPFS 0.5
    * 20 Steven Allen
        * [Stebalien](https://github.com/Stebalien)
    * A presentation on IPFS 0.5, and the features and metrics relevant for pinning services and other infrastructure and service providers.
    * Slides: [go-ipfs 0.5](https://docs.google.com/presentation/d/1a7TtjAxVL9_za1HNdiQmScKz31eQRAM_XzBv2aD7eEs/edit#slide=id.p1)
    * The Code: [ipfs/go-ipfs](https://github.com/ipfs/go-ipfs/releases/tag/v0.5.0)
* 11:15 AM PT Pinning advanced data structures — Thread and Bucket pinning at Textile
    * 40 Andrew Hill [@andrewxhill](https://twitter.com/andrewxhill)
    * **Textile**’s latest releases of **ThreadsDB** and **Buckets** come with new pinning capabilities that support dynamic datasets and IPNS addresses. In this talk, we will highlight how Threads, Buckets, and IPFS can enable new forms of pinning services.
    * Slides: [Future of Pinning - storing Threads and Buckets at Textile](https://speakerdeck.com/andrewxhill/future-of-pinning-storing-threads-and-buckets-at-textile)
    * About owning data
    * Buckets are build on ThreadsDB
    * Hubs are hosted hosted Theads services
* 11:45 AM PT Infura
    * 60 Mike Godsey [@godofthesey](https://twitter.com/godofthesey?lang=en)
    * Overview of the past, present, and a brief glimpse of the future for IPFS at Infura. IPFS is an essential part of the Infura Web3 development suite and we will talk about why we started to support it, how developers use it today, and what's to come.
    * [Ethereum API | IPFS API Gateway | ETH Nodes as a Service | Infura](https://infura.io/)
        * [Building Dapp Frontends with React &amp; Network.js](https://blog.infura.io/dapp-frontend-network/)
        * [Infura Documentation | Infura Documentation](https://infura.io/docs)
        * [IPFS Documentation - HTTP API](https://docs.ipfs.io/reference/api/http/)
        * [Infura News | New Tools for Running IPFS Nodes](https://blog.infura.io/new-tools-for-running-ipfs-nodes-196de636f079/)
* 12:15 PM PT Super Pinning with Fleek's New IPFS/S3 Product
    * 80 Brett Shear [@brettshear](https://twitter.com/brettshear?lang=en)
    * Learn how to use Fleek's new IPFS/S3 product to upload, pin & fetch files to/from IPFS at lightning speed thanks to built in compression, image resizing, CDN, & more!
    * Easy IPFS deployments
    * Pinning Host with cloudflare as CDN
    * [Fleek](https://fleek.co/)
    * [How to deploy a Next.js app onto IPFS using Fleek](https://blog.fleek.co/posts/fleek-nextJS)
        * [Next.js by Vercel - The React Framework](https://nextjs.org/)
* 12:45 PM PT Is Da Vinci Responsible for Maintaining the Mona Lisa?
    * 100 Kyle Tut [@kyletut](https://twitter.com/kyletut?lang=en)
    * When data is created on IPFS, who is responsible for maintaining that data? In this talk, Kyle dives into data permanence and discusses how to keep the data behind a CID alive.
    * [Pinata - Add Files To IPFS Effortlessly](https://pinata.cloud/)
        * Is a Pinning service
        * OffChain storage of NFTs
            * Instead of storing on web2 (urls data can change) then use IPFS (CIDs can't change)
            * Who's paying for offchain data? Buyer (Mona Lisa)? Creator (Warrenties/tombstone)? (Game) Platform?
        * OpenSea - eBay for NFTs
        * https://openbazaar.org/
* ??? 1:15 PM PT Web3 products for the web2 mind
    * 120 Greg Markou [@gregthegreek](https://twitter.com/gregthegreek?lang=en)
    * Offering users new and innovative products without disrupting their daily routine is a challenge for most blockchain projects. Our goal is to offer users a real alternative to storage without users having to think twice about how it works. The goal is to build products for real users, not subject matter experts, and this talk aims to guide us to that path with Filecoin.
    * [ChainSafe Systems](https://chainsafe.io/)
* 1:45 PM PT Using Ceramic to control pinsets with DIDs
    * 140 Joel Thorstensson [@oedth](https://twitter.com/oedth)
    * Ceramic combines merkle linked data with decentralized identifiers to create a public network of mutable documents. In this talk we will explore how this can be used to let any DID control data pinsets.
    * [Shared backend for Web3 | 3Box](https://3box.io/)
    * DID - Decentralized ID e.g. for creds.
        * DID foundation: [DIF - Decentralized Identity Foundation](https://identity.foundation/)
        * Verifialble Credentials
    * Ceramic Document 
        * Versions - must be signed by owner DID
        * Owned by DID
        * [Ceramic Network | A web without silos](https://www.ceramic.network/)
        * Example: [ceramicnetwork/js-ceramic](https://github.com/ceramicnetwork/js-ceramic)
* 2:30 PM PT Blockchain domains + IPFS = Decentralized Websites
    * 160 Bradley Kam [bradley-kam-444aa228](https://www.linkedin.com/in/bradley-kam-444aa228/)
    * Traditional DNS has two points of failure - domain names require centralized custodians and content is stored on servers controlled by one company, meaning websites can be taken down. Unstoppable Domains builds domain registries on blockchains. These domains are not part of DNS and are stored in users’ Ethereum wallets. The user signs a message with their private key and writes their IPFS hash to the blockchain, giving them the power to put up or take down their website. Domains work in apps like MyEtherWallet, Trust Wallet, and Opera Browser.
    * [Slides](https://docs.google.com/presentation/d/1-MXS7VdcB_vqCLTIef4pVIccWRynNh6cjeMbYt0zoTg/edit#slide=id.g6ef81f88c1_0_28)
    * [Unstoppable Domains](https://unstoppabledomains.com/about)
* 3:00 PM PT Sending, Receiving, and Validating Filecoin Payments
    * 180 Jonathan Schwartz [@j_schwartzz](https://twitter.com/j_schwartzz) - Open Work Labs
        * [Aragon](https://preview.autark.xyz/#/autarklabs/profile/0xA780b7eE456d6054f4ae77C6798FD0599464f740)
    * If you're an IPFS pinning service, infrastructure provider, or just interested in learning about accepting Filecoin as a form of payment without running your own Filecoin node, this talk is for you! First, we'll construct and send a Filecoin transaction together. Next, we'll locate the transaction on the network in a couple different ways, which might be useful for confirming a customer's payment. We'll wrap up by comparing the different wallet options to expect by Mainnet launch.
    * [Open Work Labs](https://www.openworklabs.com/)
        * [openworklabs/react-native-ipfs-http-client](https://github.com/openworklabs/react-native-ipfs-http-client)
    * [filecoin-project/lotus](https://github.com/filecoin-project/lotus/blob/master/api/api_full.go#L57)
    * [openworklabs/filecoin-web-wallet](https://github.com/openworklabs/filecoin-web-wallet)
    * [Jonathan Schwartz, Open Work Labs](https://filecoin.io/blog/community-jonathan-schwartz-owl/)
* 3:30 PM PT Make Your Home Not Spy On You - Ucam: Indoor Camera with Full Data Sovereignty
    * 200 Raullen Chai [@Raullen](https://twitter.com/Raullen)
    * We're surrounded by billions of Internet-connected and intelligent devices, which are observing and recording us all the time. The dream of a smart, safe, and efficient future is threatened by intrusive surveillance. Ucam, powered by IoTeX, is the next-gen indoor camera that is user-centric, feature-packed, and fully private. By shifting data ownership from corporations to consumers, Ucam ensures value extracted from data is delivered to their rightful owner. This presentation introduces Ucam’s technology including blockchain identity, decentralized storage (IPFS), and e2e encryption.
    * [Slides](https://docsend.com/view/5fyz9wk)
    * [IoTeX Offical](https://www.iotex.io/)
    * [Home - Ucam](http://ucam.iotex.io/)
* 4:00 PM PT Day 1 Close
    * 220 Juan Benet [@juanbenet](https://twitter.com/juanbenet)
        * [juan.benet.ai](https://juan.benet.ai/)
* 10:00 AM PT Day 2 Keynote
    * 220 Juan Benet
* 10:40 AM PT Pinning APIs & Use Cases
    * 240 Juan Benet
    * In this presentation, we discuss current and potential pinning use cases and a pinning API to meet these envisioned needs.
    * Slides: [https://ipfs.io/ipfs/QmUQjFpjZYJYNTbpubBHwwgC12iup1ogQv3d8dBXxzjCq6/ipfs-pinning-api.compressed.pdf](https://ipfs.io/ipfs/QmUQjFpjZYJYNTbpubBHwwgC12iup1ogQv3d8dBXxzjCq6/ipfs-pinning-api.compressed.pdf)
    * API: [Build, Collaborate & Integrate APIs | SwaggerHub](https://app.swaggerhub.com/apis/lanzafame/ipfs-pinning-service/0.0.1#/)
* 11:10 AM PT Pinning Service Integrations in IPFS Applications
    * 260 Molly Mackinlay
    * [IPFS-Applications-Diagram](https://www.figma.com/file/2bVNnjoOmxh4TtID9kzqEG/IPFS-Applications-Diagram)
* 12:00 PM PT Exploring Filecoin Integrations
    * 280 Pooja Shah [@poojaks_](https://twitter.com/poojaks_) - [linkedin](https://www.linkedin.com/in/pooja01/) - [Digital Money Forum](https://thedigitalmoneyforum.com/speakers/pooja-shah/)
    * Retrieval minors becomes CDN
    * Pinning Service is like pinning into memory
    * Minors batch for storage
    * [Prototype 0.0.1 : home](https://filecoin.onrender.com/)
* 12:40 PM PT A Tour of Powergate
    * 320 Andrew Hill
    * The Powergate is an API driven solution for deploying multitiered storage across Filecoin and IPFS. Persistent storage on Filecoin allows rich storage configuration for data such as replication factor, miner selection, deal renewal, and repair. Network available storage is configurable and provided through a connected IPFS peer or pinning network.
    * Aron
* 1:30 PM PT Interactive Sessions
* 3:30 PM PT Summit Close
* https://docs.google.com/document/d/1t5oAN92wtZ1_A2R8y1CEILEGi5OpRQ4f-Sdah03XqCU/edit
    * See the slides of the IPFS Pinning API talk https://ipfs.io/ipfs/QmUQjFpjZYJYNTbpubBHwwgC12iup1ogQv3d8dBXxzjCq6/ipfs-pinning-api.compressed.pdf
    * A previous proposal for the Pin RPC API https://app.swaggerhub.com/apis/lanzafame/ipfs-pinning-service/0.0.1#/
    * Textile Threads Docs  https://docs.textile.io/threads/introduction/
    * and the Paper https://docsend.com/view/gu3ywqi
* Discussion Room Q&A Breakout Session: https://protocol.zoom.us/j/94443651912
    * https://rl1-lotus-workshop.glitch.me/
* (@jbenet) Pinning API Workshop 1hr (1:30pm) https://protocol.zoom.us/j/91027000462

The End
