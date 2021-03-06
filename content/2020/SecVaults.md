Title: Vaults
Date: 2099-01-01 00:00
Category: Devops
Tags: #

HowTo setup your own vault?

* Deploye an I-drive using [ownCloud - share files and folders, easy and secure](https://owncloud.com/)
    * Code: [ownCloud](https://github.com/owncloud)
    * [Features](https://owncloud.com/find-the-right-edition/)
        * OAuth2
        * 2-Factor Authentication - TOTP
        * Optional End-to-End Encryption with key service. # User devices based encryption
        * Encryption of Primary Storage (AES-256), key management. # Admin can't read any files.
        * Storage Encryption with HSM support. # Key stored in HW.
        * Secure View. # Shared content can only be viewed.
        * Optional Native Brute Force Protection
    * [Installation](https://doc.owncloud.org/server/10.5/admin_manual/installation/)
    * eBook: [Nginx HTTP Server - Fourth Edition](https://www.packtpub.com/product/nginx-http-server-fourth-edition/9781788623551) Cpt 10 - Creating your ownCloud drive.
* [Vault by HashiCorp](https://www.vaultproject.io/)
    * Code: [hashicorp/vault](https://github.com/hashicorp/vault)
    * Learn: [Getting Started | Vault - HashiCorp Learn](https://learn.hashicorp.com/collections/vault/getting-started)
        * [Getting Started with Vault UI | Vault - HashiCorp Learn](https://learn.hashicorp.com/collections/vault/getting-started-ui)
        * [Kubernetes | Vault - HashiCorp Learn](https://learn.hashicorp.com/collections/vault/kubernetes)
    * Guide: [The HashiCorp Vault Adoption Guide](https://www.hashicorp.com/resources/adopting-hashicorp-vault)
    * Doc: [Architecture | Vault by HashiCorp](https://www.vaultproject.io/docs/internals/architecture.html)
        * [Key Rotation | Vault by HashiCorp](https://www.vaultproject.io/docs/internals/rotation)
    * eBook: [Learning DevOps](https://www.packtpub.com/product/learning-devops/9781838642730) Cpt 12 - Page 366 - Installing Vault locally.
    * Pros:
        * Can be installed as a k8s app
* HSM and Cold Storage 
    * [square/subzero](https://github.com/square/subzero)
    * [Ledger Vault - solution to scale your digital asset business](https://vaultplatform.ledger.com/why-vault)
    * CustodianS: [Leading US-based Crypto Custodian Providers for Institutional Clients](https://medium.com/blockchain4all/leading-us-based-crypto-custodian-providers-for-institutional-clients-3ba9b8683c6d)
* Bitwarden Secure Notes (can be Onprem installed)
    * Code: [Bitwarden](https://github.com/bitwarden)
    * [Host It Yourself](https://bitwarden.com/open-source/)
    * Automate with [bitwarden/cli](https://github.com/bitwarden/cli)
* Keybase Private files (in Cloud)
    
The End
