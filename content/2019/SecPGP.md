Title:  PGP
Date: 2099-01-01 00:00
Category: Biz
Tags: #pgp, #yubikey, #keybase, #ssh, #nfc

## PGP

PGP gives you a private and a public key. You can use them for encrypting and signing (SSH, S/MIME etc).  

* Theory - Assymmetric Encryption: [A Deep Dive on End-to-End Encryption: How Do Public Key Encryption Systems Work?](https://ssd.eff.org/en/module/deep-dive-end-end-encryption-how-do-public-key-encryption-systems-work)
* Theory - Encrypt emails: [It's Time to Encrypt Your Email](https://code.tutsplus.com/tutorials/its-time-to-encrypt-your-email--cms-23719)

### HW storage

Your PGP key kan be stored in a YubiKey:

* [How to use GPG with YubiKey (bonus: WSL)](https://codingnest.com/how-to-use-gpg-with-yubikey-wsl/)
    * YubiKey is also used as a HW 2FA device. The benefit of this is that you can use it for 2FA device both for Mobile and PC. If you loose it no one will know what email account it is tied to (oppesed to on a mobile Goggle Autehnticater will work with the apps on the device).  
    * In other words - YubiKey is a digital keyring
    * To GPG YubiKey is a (smart)card
    * Buy [YubiKey 5](https://www.yubico.com/product/yubikey-5-nfc/)
* [Using Your YubiKey with OpenPGP : Yubico Support](https://support.yubico.com/support/solutions/articles/15000006420-using-your-yubikey-with-openpgp)

Perhaps it is possible to store your PGP key on your NFC enabled credit card, as another (backup) media?

* [Credit Cards with Near Field Communication NFC Payment | finder.com.au](https://www.finder.com.au/nfc-credit-cards)

### Applications

So how would you have a great usage of a PGP key stored on a NFC HW device?  

* Are there any email apps where you could encrypt the mail with a tap of your creditcard?
* Are there any apps, where you can encrypt files on a disk with a tap of your creditcard? An decypt them in a similar way?
* In [KeyBase](SecKeyBase.md) one of the proves of you are who you are - is something signed with your PGP key. I think it will be stored in the app on the device (mobile or PC)

#### Webmail

* Mailclient tester: [Email Privacy Tester](https://www.emailprivacytester.com/)
    * Mikes public keys: [Mike Cardwell - Grepular](https://www.grepular.com/)
* Free [TutaNota](https://tutanota.com/security)
    * [Encrypt it all: How Tutanota secures your private key and your data with state-of-the-art encryption.](https://tutanota.com/blog/posts/innovative-encryption/)
    * DNSSEC and DANE: [DANE: How to install the DANE browser add-ons - updated](https://tutanota.com/blog/posts/dane-how-to-browser-plugins/) 
    * Validates from-mail via DMARC [How to Explain DMARC in Plain English | Return Path](https://blog.returnpath.com/how-to-explain-dmarc-in-plain-english/)
* Free or e2½/user/month - incl 12GB sharable encr disk: [Mailfence](https://mailfence.com/en/secure-email.jsp)
    * [The Mailfence Threat Model | Secure and private email](https://mailfence.com/en/threat-model.jsp)
* [ProtonMail - Security Features](https://protonmail.com/security-details)

## Hosting

* WebHosting: [Top Rated Web hosting Companies on Trustpilot](https://www.trustpilot.com/categories/web_hosting#)
    * Node.Js - $3/month: [FastComet](https://www.fastcomet.com/pricing)
    * VPS - uk - e5/month: [Deploys.io - Classic Virtual Servers](https://deploys.io/store/virtual-servers/classic)
* MailHosting: [Top Rated Email Service Provider Companies on Trustpilot](https://www.trustpilot.com/categories/email-service-provider)

The End