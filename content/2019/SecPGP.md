Title:  PGP
Date: 2099-01-01 00:00
Category: Biz
Tags: #pgp, #yubikey, #keybase, #ssh, #nfc

## PGP

PGP gives you a private and a public key. You can use them for encrypting and signing (SSH, S/MIME etc).  

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

The End
