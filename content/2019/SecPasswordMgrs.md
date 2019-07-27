Title:  Password Managers
Date: 2099-01-01 00:00
Category: DevOps
Tags: #keeper, #yubikey, #2fa, #nfc

## Password Managers

* List $: [The Best Password Managers for 2019](https://www.pcmag.com/roundup/300318/the-best-password-managers#)
* List free: [The Best Free Password Managers for 2019](https://www.pcmag.com/roundup/331555/the-best-free-password-managers)
* List: [Privacy Tools - How to Restore Your Online Privacy in 2019](https://restoreprivacy.com/privacy-tools/) - see "Password manager"
* List: [Works With YubiKey Catalog | Yubico](https://www.yubico.com/works-with-yubikey/catalog/#protocol=all&usecase=password-management&key=all)

Password Managers are browser plugins that capture form data. The data is stored on encrypted cloud drive (vault). The privatekey is your master password.

Some Extra features:

* App psws
* Cloud Vault
    * Share in vault
* Pwned check
* Inherit - who take over your data
* Android [Autofill](https://www.addictivetips.com/android/google-autofill-settings-for-apps-android/)
* Beware: [Thinking outside of the password manager box](https://labs.detectify.com/2019/02/28/thinking-outside-of-the-password-manager-box/)

### LessPass

LessPass calculates passwords

* [LessPass How Does It Works?](https://blog.lesspass.com/lesspass-how-it-works-dde742dd18a4)

### Bitwarden

* [Open Source Password Management Solutions | Bitwarden](https://bitwarden.com/#organizations)
    * [Bitwarden](https://github.com/bitwarden)
* [Security | Bitwarden Help](https://help.bitwarden.com/security/)
* Pros:
    * [Family](https://bitwarden.com/#organizations) version gives 5 users, 1GB storage for 1$/mo
    * Supports [YubiKey](https://help.bitwarden.com/article/setup-two-step-login-yubikey/) with NFC on IOS.
    * Is OSS: [Installing and deploying | Bitwarden Help](https://help.bitwarden.com/article/install-on-premise/)
    * Fingerprint or pin protection after login
    * Server can be self-hosted
* Cons:
    * Not U2F in free version, but TOTP

### Keeper

* Keeper: [Keeper Password Manager & Digital Vault](https://www.pcmag.com/review/326390/keeper-password-manager-digital-vault)
    * Buying family package gives you 5 persons
    * 10G Encrypted cloud drive (vault) included in family package - folders can be shared
    * Zero knowledge - loose your master psw or security question - then your data is lost
    * Guess: With 2FA you will need to 
        * login to Keeper
        * 2FA to Keeper
        * 2FA to the site you are visiting
        * 2FA with [YubiKey](SecAuthenticationFidoU2F.md) - NFC on Mobiles, USB on PC's
    * Guess: Loose your device will loose your psws, if not using Keeper 2FA
    * Self destruct devise after 5 wrong logins
    * OneClick generator creates a 16 char psw, but default/auto is only 12 char

### LastPass

* [LastPass](https://www.lastpass.com/)
* Review: [LastPass Premium](https://www.pcmag.com/review/317692/lastpass-4-0-premium)
* Pros:
    * Does both have [IPhone Authenticator](https://lastpass.com/auth/) and IPhone PswMgr - both with backup to cloud
    * You can convert any USB drive into an authenticator. Just install LastPass's Sesame utility on it and you're done. Plug it in to authenticate.
    * Family edition gives you Shared folder / Vault
    * Recommended in Free version: [LastPass](https://www.pcmag.com/review/317662/lastpass)
* Cons: 
    * Premium does support Yubikey OTP, but not U2F  
    [Using Your YubiKey with LastPass on iPhone : Yubico Support](https://support.yubico.com/support/solutions/articles/15000006425-using-your-yubikey-with-lastpass-on-iphone)  
    [Introducing YubiKey MFA for iOS on Your LastPass Account - The LastPass Blog](https://blog.lastpass.com/2018/05/introducing-yubikey-mfa-for-ios-on-your-lastpass-account.html/)

### Firefox Lockwise

* [‎Firefox Lockwise](https://apps.apple.com/us/app/firefox-lockwise/id1314000270)

### iCloud KeyChain

* [Set up iCloud Keychain](https://support.apple.com/en-us/HT204085)
    * Notes: 
        * Does not update to Windows / Linux.
        * Create a private MasterKey:  
        Quote: "Skip the step to create an iCloud Security Code. Your keychain data is then stored locally on the device, and updates across only your approved devices"
        * You can choose extra long PassCode. [What is Apples iCloud Keychain and how do I use it?](https://newatlas.com/apple-icloud-keychain-ios7/30301/)
        * Does now include Vault for files
        * 2FA only can you your IPhone as device.

### Google Password Manager (Android Smart Lock for Passwords)

* [Password Manager](https://passwords.google.com/)
    * 2018-05 [How to Use Google’s Password Manager to Sync Your Passwords Everywhere](https://www.howtogeek.com/231237/how-to-use-google%E2%80%99s-password-manager-to-sync-your-passwords-everywhere/)
    * Notes:
        * Only works with Android and Chrome.
        * Create a private MasterKey:  
        Quote: "Choose to encrypt your passwords with “your own sync passphrase”, you won’t be able to access your passwords on the web. Smart Lock for Passwords on Android won’t function, either.)"
        * Autogenerate passwords
        * 2FA can be any method that Google supports - e.g. U2F using YubiKey. See 2015-10 [Googles New Smart Lock Is the Password Manager for the Rest of Us](https://lifehacker.com/googles-new-smart-lock-is-the-password-manager-for-the-1710352668)
        * Android Smart Lock is supported by a few apps - see link above.
        * Implement Smart Lock in your Android app: [Smart Lock for Passwords on Android &nbsp;|&nbsp; Google Developers](https://developers.google.com/identity/smartlock-passwords/android/)
        * [How to Disable Google Smart Lock on Android and Chrome](https://www.guidingtech.com/disable-google-smart-lock-android-chrome/)
        * Set Chrome as default on IOS:
            * [Change default browser? - Apple Community](https://discussions.apple.com/thread/8317628)
            * [How to make Chrome your default browser on iOS](https://www.idownloadblog.com/2014/02/02/make-chrome-default-browser-ios/)

### G Suite Password Sync (GSPS)

For companies

* [About GSuite Password Sync](https://support.google.com/a/answer/2611859?hl=en)
    * Features: [Compare G Suite editions](https://gsuite.google.com/compare-editions/?feature=product_suite)
        * No vault in Basic edition


## Pwned check

* [Have I Been Pwned: Check if your email has been compromised in a data breach](https://haveibeenpwned.com/)

## Other

* [Simple Tricks to Remember Insanely Secure Passwords](https://www.pcmag.com/article/359862/simple-tricks-to-remember-insanely-secure-passwords)

## Vaults

* OSS [Nextcloud](https://nextcloud.com/)

## Notes

* List: [6 Best Cross Platform Note Apps for Windows, Mac, iOS &amp; Android | Mashtips](https://mashtips.com/crossplatform-note-apps-windows-mac-ios-android/)
* Encrypted: [StandardNotes - What happens to my data if Standard Notes disappears?](https://standardnotes.org/help/4/what-happens-to-my-data-if-standard-notes-disappears)



The End
