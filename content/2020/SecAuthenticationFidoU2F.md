Title:  Authentication with FIDO
Date: 2099-01-01 00:00
Category: Develop
Tags: #authentication, #fido, #2fa, #usb, #nfc, #bluetooth, #yubikey, #iot

# Intro

FIDO **UAF** uses **shared keys** using e.g. **HOTP or TOTP** meaning you can copy that key and loose it to fishing.  
FIDO **U2F** uses **public keys**. The private key stays in your device, which can be a USB Key, embedded in phone, watch or anything else.  
[FIDO2](https://fidoalliance.org/fido2/) introduced **WebAuthn**

* [https://paulstamatiou.com/getting-started-with-security-keys/](https://paulstamatiou.com/getting-started-with-security-keys/)
* Functions covered by [Yubico](https://www.yubico.com/products/compare-products-series/)

## Authentication with FIDO U2F - Universal 2nd Factor

* [Download Specifications - FIDO Alliance](https://fidoalliance.org/specifications/download/)
    * [Universal 2nd Factor (U2F) Overview](https://fidoalliance.org/specs/fido-u2f-v1.2-ps-20170411/fido-u2f-overview-v1.2-ps-20170411.html)
    * [FIDO U2F JavaScript API](https://fidoalliance.org/specs/fido-u2f-v1.2-ps-20170411/fido-u2f-javascript-api-v1.2-ps-20170411.html)
    * [FIDO Bluetooth® Specification v1.0](https://fidoalliance.org/specs/fido-u2f-v1.2-ps-20170411/fido-u2f-bt-protocol-v1.2-ps-20170411.html)
    * [FIDO NFC Protocol Specification v1.0](https://fidoalliance.org/specs/fido-u2f-v1.2-ps-20170411/fido-u2f-nfc-protocol-v1.2-ps-20170411.html)
    * [U2F Security Key - Buy Guide - FIDO & YubiKey](https://u2f-key.tech/)
* [FIDO® Certified products](https://fidoalliance.org/certification/fido-certified-products/)

### FIDO2, WebAuthn & CTAP

* [FIDO2: Moving the World Beyond Passwords using WebAuthn & CTAP](https://fidoalliance.org/fido2/)
* [FIDO2: Web Authentication (WebAuthn) - FIDO Alliance](https://fidoalliance.org/fido2/fido2-web-authentication-webauthn/)
* [Web Authentication: An API for accessing Public Key Credentials Level 1](https://www.w3.org/TR/webauthn/)

## Applications

### Yubikey

* [Yubico Reveals First Biometric YubiKey at Microsoft Ignite | Yubico](https://www.yubico.com/blog/yubico-reveals-first-biometric-yubikey-at-microsoft-ignite/)
* [YubiKeys | Strong Two-Factor Authentication for Secure Login | Yubico](https://www.yubico.com/products/yubikey-hardware/) - supports U2F and NFC (for mobile) and USB (for PC)
* Features: [Compare Products | Yubico](https://www.yubico.com/products/yubikey-hardware/compare-products-series/)
* Review 2018-09: [Yubico YubiKey 5 NFC](https://www.pcmag.com/review/363889/yubico-yubikey-5-nfc)
* [Yubico Authenticator - Apps on Google Play](https://play.google.com/store/apps/details?id=com.yubico.yubioath&hl=en) - Uses OTP - not U2F
* Manage: [Downloads | Yubico](https://www.yubico.com/products/services-software/download/)
* Yubikey 5:
    * Limit [32 OATH-TOTP credentials](https://support.yubico.com/support/solutions/articles/15000014174--yubikey-5-nfc) via Yubico Authenticator

Guides:

* [Using Your YubiKey with Authenticator Codes : Yubico Support](https://support.yubico.com/support/solutions/articles/15000006419-using-your-yubikey-with-authenticator-codes)
* [YubiKey 5 Series Technical Manual : Yubico Support](https://support.yubico.com/support/solutions/articles/15000014219-yubikey-5-series-technical-manual)
* [YubiKey - ArchWiki](https://wiki.archlinux.org/index.php/YubiKey)
* [Using GnuPG for Custom Configuration Secrets : Yubico Support](https://support.yubico.com/support/solutions/articles/15000006454-using-gnupg-for-custom-configuration-secrets)
* [YubiKey for SSH, Login, 2FA, GPG and Git Signing](https://ocramius.github.io/blog/yubikey-for-ssh-gpg-git-and-local-login/)
* 2019-02: [Use A YubiKey For PGP Signing, Encryption, And Authentication](https://www.thepolyglotdeveloper.com/2019/02/use-yubikey-pgp-signing-encryption-authentication/)
* [OpenPGP - Export Secret Keys to a Yubikey](https://blog.eleven-labs.com/en/openpgp-secret-keys-yubikey-part-2/)
* 2017-09: [Configuring an offline GnuPG master key and subkeys on YubiKey](https://www.andreagrandi.it/2017/09/30/configuring-offline-gnupg-masterkey-subkeys-on-yubikey/)
* Keyboard bot: [How to Weaponize the Yubikey - Black Hills Information Security](https://www.blackhillsinfosec.com/how-to-weaponize-the-yubikey/)
* [Yubico Get API Key](https://upgrade.yubico.com/getapikey/)

News:

* [Yubico Authenticator App for iOS Now Supports NFC | Yubico](https://www.yubico.com/blog/yubico-authenticator-app-for-ios-now-supports-nfc/)
    * [Yubico iOS Authentication Expands to Include NFC | Yubico](https://www.yubico.com/blog/yubico-ios-authentication-expands-to-include-nfc/)
* Lots of adds! [YubiKey 5 Series Arrives With Passwordless Authentication](https://www.tomshardware.com/news/yubikey-5-series-passwordless-authentication,37834.html)

### Duo Authenticator (now Cisco)

* [Duo Authenticator](https://duo.com/pricing)
    * [Duo Mobile: Secure Two-Factor Authentication App](https://duo.com/product/trusted-users/two-factor-authentication/duo-mobile)
    * [Authentication Methods](https://duo.com/product/trusted-users/two-factor-authentication/authentication-methods)
    * Cons:
        * [The Free version](https://duo.com/pricing/duo-free) is [only a 30d trail](https://duo.com/trial)
        * You have to sign up. This enables Google Drive to backup you 2FA codes (thus sharing your 2FA codes with Google). You don't have to enable the backup feature.

### Other HW keys

* [FIDO ®-NFC | FEITIAN](https://www.ftsafe.com/Products/FIDO/NFC)
* Review 2018-09: [Google Titan Security Key Bundle](https://www.pcmag.com/review/363644/google-titan-security-key-bundle)
* Mobile as HW key: [Google Offers Built-In Security Key Feature for Android Phones](https://www.pcmag.com/news/367713/google-offers-built-in-security-key-feature-for-android-phon)
* Mobile as HW key: [How to Use Android Smartphone as a Security Key | Mashtips](https://mashtips.com/use-android-smartphone-as-security-key/)
* [U2FReviews](https://github.com/hillbrad/U2FReviews)
* [USB Dongle Authentication](https://www.dongleauth.info/dongles/)
* [Google open-sources the firmware needed to build hardware security keys | ZDNet](https://www.zdnet.com/article/google-open-sources-the-firmware-needed-to-build-hardware-security-keys/)
    * [google/OpenSK](https://github.com/google/OpenSK)
    * [Tock Embedded Operating System](https://www.tockos.org/)
    * Case: [OpenSK Key Enclosure by RightBrainElectronics](https://www.thingiverse.com/thing:4132768)

| [Dongle](https://www.dongleauth.info/dongles/) | OTP credentials | Comment |
|------------------------------------------------|-----------------|---------|
|[Bluink](https://bluink.ca/buy) key ($30)|[Unlimited TOTP (in app)](https://bluink.ca/files/BluinkKeyUserGuide.pdf)|App not in eu|
|[Feitian](https://www.ftsafe.com/Products/FIDO/Single_Button_FIDO) ePass FIDO2|[]()|3 keys: USB-A/NFC, USB-C, BlueTooth|
|[Google](https://store.google.com/us/config/titan_security_key?hl=en-US) Titan|[]()|3 keys: USB-A/NFC ($25), USB-C ($40), BlueTooth ($35) - no OTP|
|HyperSecu|[]()|
|[Nitrokey](https://www.nitrokey.com/#comparison) PRO 2 ($49)|[5 TOTP](https://www.nitrokey.com/files/doc/Nitrokey_Pro_factsheet.pdf)|
|[Nitrokey](https://www.nitrokey.com/#comparison) Storage 2 ($109)|[15 TOTP](https://www.nitrokey.com/files/doc/Nitrokey_Storage_factsheet.pdf)|
|OnlyKey|[]()|
|Secalot|[]()|
|[SoloKeys](https://solokeys.com/)|[]()|No OTP|
|VASCO|[]()|
|WWPass|[]()|
|Yubikey 5|[32 OATH-TOTP](https://support.yubico.com/support/solutions/articles/15000014174--yubikey-5-nfc)|

### Who else supports U2F?

* List: [USB Dongle Authentication](https://www.dongleauth.info/)
* List: [YubiKey Catalog](https://www.yubico.com/works-with-yubikey/catalog/)
* List: [Comparison of webmail providers - Wikipedia](https://en.wikipedia.org/wiki/Comparison_of_webmail_providers)
* Github, Twitter, Google, AWS, Microsoft, Facebook ...
* WebMail Review: [Best Secure Email: Top 10 Services for 2019 | Restore Privacy](https://restoreprivacy.com/secure-email/)
    * WebMail - De: [TutaNota](https://tutanota.com/security)
    * WebMail - De (No U2F - only TOTP): [posteo.de](https://posteo.de/en/site/features)
        * [Help - How can I use a YubiKey for two-factor authentication with Posteo?  - posteo.de](https://posteo.de/en/help/how-can-i-use-a-yubikey-for-two-factor-authentication-with-posteo)
    * WebMail - No - $20/user/year: [Runbox](https://runbox.com/)
    * WebMail - Au/Us - $30/user/year : [FastMail](https://www.fastmail.com/pricing/)
    * WebMail - Ca: [Thexyz](https://www.thexyz.com/)
    * WebMail - Ch - Free: [ProtonMail](https://protonmail.com/security-details)
    * WebMail $12/user/year: [101Domain](https://www.101domain.com/email_services.htm) - Poor on Trustpilot
    * WebMail: [Gandi Email](https://www.gandi.net/en/domain/email) - Poor on Trustpilot
    * WebMail: [Yubikey Hardware Authentication Plugin - SquirrelMail - Webmail for Nuts](http://squirrelmail.org/plugin_view.php?id=273)
* Domain - Uk: [GoDaddy UK](https://uk.godaddy.com/)
* Domain - De: [Hetzner Online GmbH](https://www.hetzner.com/domainregistration) - Poor on Trustpilot
* PswMgr: [Keeper](SecPasswordMgrs.md)
* PswMgr - OSS: [Home](https://psono.com/)
* [Get YubiKey for Windows Hello - Microsoft Store](https://www.microsoft.com/en-us/p/yubikey-for-windows-hello/9nblggh511m5?SilentAuth=1&wa=wsignin1.0&activetab=pivot:overviewtab)

|Who|RecoveryEmail|Yubi|Free|Payed|iCloud|
|---|---|---|---|---|---|
|--- Free ---|
|MailFence|Y|N|Y ½G|e2½/m||
|TutaNota|N|PC|Y 1G|e2½/m||
|ProtonMail|Y|Android|Y ½G|e4/m|| Also 2FA TOTP
|--- Payed ---|
|Mailbox.org|Y|Y|N|e1/m|100M| Deleted after 60d
|Posteo|Y|Y|N|e1/m|| Also sync IOS Notes
|RunBox||Y|N|||
|FastMail||Y|N|||
|TheXYZ||Y|N|||
|101Domain||?|N|||
|Gandi||?|2mailbox/domain|||

## 2FA

* [Authenticator - Wikipedia](https://en.wikipedia.org/wiki/Authenticator)
* [Two-Factor Authentication (2FA) – John Gallias](https://johngallias.com/two-factor-auth/)

## SW 2FA

* [Krypton U2F Authenticator](https://krypt.co/)
    * [krypt.co](https://github.com/kryptco)
    * Good for Google since Google don't support Yubikey NFC login via IPhone
* [Yubico Authenticator | Yubico](https://www.yubico.com/products/services-software/download/yubico-authenticator/)
* [Duo Trusted Access](https://duo.com/)

## Keys

Guides:

* [getting-started-with-security-keys/](https://paulstamatiou.com/getting-started-with-security-keys/)

## Other FIDO protocols

* FIDO UAF - Universal Authentication Framework - see specs above
* [A YubiKey for iOS Will Soon Free Your iPhone From Passwords](https://www.wired.com/story/yubikey-lightning-ios-authentication-passwords/)

## Recover from 2FA loss

If you loose your **authenticator app** and you have recovery keys then you need to  

* Install the authenticator app on a new device
* For each app 
    * Use recovery code to regain access to the app
    * Enter the app - goto security settings - Remove Authenticator 2FA  
    Then your lost device is not possible to use
    * Recreate Authenticator 2FA
    * Backup the new recover code
* If your authenticator was on IOS:
    * Reset lost device to factory settings via Find My IPhone: [iCloud: Erase your device with Find My iPhone](https://support.apple.com/kb/PH2701?locale=en_US)
    * You can choose between **Lost Mode** and **Erase iPhone**
* If your authenticator was on Android:
    * [[How To] Remotely Ring/Lock/Erase/Factory Reset your Android Phone | TechToLead.com](https://www.techtolead.com/how-to-remotely-ringlockerasefactory-reset-your-android-phone/442/)
    * You can choose between **Lock** and **Erase**

If you loose your **2FA HW key** like YubiKey you need to 

* Go to each app trusing on that key
    * Log in using alternative 2FA method / device / key
    * Remove the lost key
    * Add a new key
    * You also have the option of adding several keys, but you should be ready to follow this procedure if any of the keys are lost.  
    So you need to know the ID of the one which was lost

This means you should have two 2FA devices / keys for every app. Optimally this should be two HW devices like Yubikey.  
With a lot of apps supporting 2FA you would also need a list of what app is using what 2FA device / key.  

If you uses a HW key as 2FA for a password manager, then you risk all your accounts has been compromized.  
Tip: You could use two separeate 2FA devices for password manager and for the apps.

* Use Key-M to protect your email (to avoid password reset) - If you loose it ...
* Use Key-A to protect your apps (including password manager) with 2FA

App Precautions:

* Don't use email as recovery option
* Don't use mobile phone number as recovery option
* Do Use 2 HW keys as login - keep the backup key safe
* Do protect cloud account with HW keys
* If you can't use keys then use authenticator apps on two different phones - keep the backup authenticator app safe
    * If you use phone backup to cloud then your cloud account must be protected by HW key
    * Use authenticator apps with finger print login - e.g. Microsoft authenticator

More:

* [Losing Your YubiKey : Yubico Support](https://support.yubico.com/support/solutions/articles/15000006444-losing-your-yubikey)
* [What happens if you lose your phone with Google Authenticator](https://www.reddit.com/r/ethtrader/comments/6vwk7p/what_happens_if_you_lose_your_phone_with_google/)

## Other Links

* [MyCrypto’s Security Guide For Dummies And Smart People Too](https://medium.com/mycrypto/mycryptos-security-guide-for-dummies-and-smart-people-too-ab178299c82e)
* [You're Probably Doing 2FA Wrong: Here's the Right Way](https://www.tomsguide.com/us/2fa-right-way,news-29824.html)
* [Google: Phishing Attacks That Can Beat Two-Factor Are on the Rise](https://www.pcmag.com/news/367026/google-phishing-attacks-that-can-beat-two-factor-are-on-the)
* [FBI Issues Surprise New Cyber Attack Warning: Multi-Factor Authentication Is Being Defeated](https://www.forbes.com/sites/zakdoffman/2019/10/07/fbi-issues-surprise-cyber-attack-warningurges-new-precautions/#636eccfa7efb)
* [How to Protect Your Bitcoin from $5 Wrench Attacks](https://blog.keys.casa/how-to-protect-your-bitcoin-from-5-wrench-attacks/)
* [The Dos and Don'ts of Bitcoin Key Management](https://blog.keys.casa/the-dos-and-donts-of-bitcoin-key-management/)
    * [Metal Bitcoin Seed Storage Reviews](https://jlopp.github.io/metal-bitcoin-storage-reviews/)

The End