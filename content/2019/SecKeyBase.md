Title:  KeyBase
Date: 2099-01-01 00:00
Category: Biz
Tags: #keybase

## KeyBase

Keybase makes a web of trust by trusing users on social networks. It enables filesharing and chat based on the trust, but also private sharing among devices.

* [Keybase - Wikipedia](https://en.wikipedia.org/wiki/Keybase)
* [Files - KBFS | Keybase Docs](https://keybase.io/docs/kbfs):
    * Public unencrypted files: [Keybase.pub – Browse public files in KBFS](https://keybase.pub/) - in `k:\public\yourname`
    * Private encrypted files: - in `k:\private\yourname`
    * Coming: Private shared encrypted files: - in `k:\private\yourname,yourfriend@twitter`
    * Qoute: We're giving everyone 250 gigabytes.
    * Qoute: If you throw away all your devices, you will _lose your private data_. Your _encrypted data_ is _ONLY encrypted for your device & paper keys_, not any PGP keys you have.
        * So **devices** and **paper key** gives access - the proofs - PGP and Twitter don't (I assume).
        * Though ![keybase login](https://keybase.io/images/getting-started/provision.png)
          suggest that **keybase passphrase** and **GPG** can be used for signing new devices.
    * Also be aware - Qoute: _We could, hypothetically, lose your data at any time. Or push a bug that makes you throw away your private keys._
* [It's Time to Encrypt Your Email: Using Keybase](https://code.tutsplus.com/tutorials/its-time-to-encrypt-your-email-using-keybase--cms-23724)
* Q&A:
    * Should you use it for private stuff?
        * No - there is not auto-logoff, so both on desktop and on mobile your apps are vulnerable.
        * No - missing 2FA for web/desktop - missing fingerprint login on mobile.
    * Should I use the Stellar wallet to be able to send money to other keybasers?
        * Only if that wallet is for pocket money - and does not transact to your larger accounts. 
    * Can you use it in China?
        * No - you have to go through VPN
* Tips:
    * You can encrypt public github repos - and share them with teams
    * You should only put proofs on accounts you have 2fA control over e.g. Twitter. Thus nobody can change the proof you put there.
    * You should set web in lockdown mode: [Lockdown - Index | Keybase Docs](https://keybase.io/docs/lockdown/index)
    * Use Teams to create a slack channel: [Keybase: Import your Slack Team](https://keybase.io/slack-importer)

The End
