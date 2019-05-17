Title: VPN or Tor?
Date: 2099-01-01 00:00
Category: DevOps
Tags: #vpn, #tor, #duckduckgo, #tracker, #gpg

# VPN or Tor?

I wonder if Tor can be used for browsing sites that are normally barred within China?
Or can I get a the VPN in my Wifi router working as a gateway - It is using OpenVPN.

Link:

* [Tor or VPN - Which is Best for Security, Privacy & Anonymity? [2019]](https://blokt.com/guides/tor-vs-vpn)

## OpenVPN

Cons: 

* My Wifi VPN + client PC and Mobile is not exactly easy to configure. 

Pros:

* Does not give the cons from Tor.

### Installing OpenVPN

#### Wifi router

Router is Netgear Router R7000, which  [routerlogin.net](http://www.routerlogin.net/)  
Internally you reach it on http://192.168.1.1/OPENVPN.htm, where you will get this instruction (including my added comments and prints)

To install VPN client on your client devices:  
* Step 1: Select the **Enable VPN Service** check box and click the **Apply** button.
* Step 2: Download the **client utility** from [Community Downloads | OpenVPN](https://openvpn.net/community-downloads/) and install it on the devices where you want to run the **VPN client**. _Currently iOS and Android clients are not supported._  
    * [Verify setup-program signature](https://openvpn.net/community-resources/sig/)
        * Copy signing key from [security-key-2019.asc](https://swupdate.openvpn.net/community/keys/security-key-2019.asc)
        * Copy signature from [openvpn-install-2.4.7-I607-Win10.exe.asc](https://swupdate.openvpn.org/community/releases/openvpn-install-2.4.7-I607-Win10.exe.asc) to your download folder
```bash
cd <download folder>

# Import signing key into your keyring
gpg --import security-key-2019.asc
# gpg: keybox '/c/Users/user/.gnupg/pubring.kbx' created
# gpg: /c/Users/user/.gnupg/trustdb.gpg: trustdb created
# gpg: key 12F5F7B42F2B01E7: public key "OpenVPN - Security Mailing List <security@openvpn.net>" imported
# gpg: Total number processed: 1
# gpg:               imported: 1

# Verify that the downloaded program match the signature 
gpg -v --verify openvpn-install-2.4.7-I607-Win10.exe.asc openvpn-install-2.4.7-I607-Win10.exe
# gpg: Signature made 25 Apr 2019 09:20:09 RST
# gpg:                using RSA key 82175D35AA8D0E8BDE5F4F9E5DC351805ACFEAC6
# gpg: using subkey 5DC351805ACFEAC6 instead of primary key 12F5F7B42F2B01E7
# gpg: using subkey 5DC351805ACFEAC6 instead of primary key 12F5F7B42F2B01E7
# gpg: using pgp trust model
# gpg: Good signature from "OpenVPN - Security Mailing List <security@openvpn.net>" [unknown]
# gpg: using subkey 5DC351805ACFEAC6 instead of primary key 12F5F7B42F2B01E7
# gpg: WARNING: This key is not certified with a trusted signature!
# gpg:          There is no indication that the signature belongs to the owner.
# Primary key fingerprint: F554 A368 7412 CFFE BDEF  E0A3 12F5 F7B4 2F2B 01E7
#      Subkey fingerprint: 8217 5D35 AA8D 0E8B DE5F  4F9E 5DC3 5180 5ACF EAC6
# gpg: binary signature, digest algorithm SHA256, key algorithm rsa4096

# All good: "Good signature"

$ gpg --list-keys
# /c/Users/user/.gnupg/pubring.kbx
# ---------------------------------
# pub   rsa4096 2017-02-09 [SC] [expires: 2027-02-07]
#       F554A3687412CFFEBDEFE0A312F5F7B42F2B01E7
# uid           [ unknown] OpenVPN - Security Mailing List <security@openvpn.net>
# sub   rsa4096 2019-02-04 [S] [expires: 2020-03-09]
# sub   rsa4096 2019-02-04 [E] [expires: 2020-03-09]
```
* Step 2b: Run setup. Here is what is does:
    * Creates `C:\Program Files\OpenVPN` containing
        * OpenVpn CLI and GUI
        * A guide: `C:\Program Files\OpenVPN\doc\INSTALL-win32.txt`
        * A config folder where you will put the downloaded VPN server files from Step 3
    * Creates `C:\Program Files\TAP-Windows\`. This gives you virtual network funtionality needed by VPN.   
    [What are TAP-Windows adapters? Where do I download this Driver?](https://www.thewindowsclub.com/tap-windows-adapters-vpn-driver)
* Step 3: Click the proper button below to download the **configuration files** for your VPN clients.  
_For Windows          For non-Windows_  (the config files are downloaded from your wifi router)  
* Step 4:Unzip the **configuration files** you have just downloaded and copy them to the folder where the VPN client is installed on your device. For a client device with Windows64-bit system, the VPN client is installed at `C:\Program files\OpenVPN\config\` by default.
* Step 5: For a client device with Windows, you need to **modify the VPN interface name** to `NETGEAR-VPN`. The VPN interface usually has a Device Name as `TAP-Windows Adapter`. You can rename the interface via `Control Panel\Network and Internet\Network Connections`.   
![NETGEAR-VPN](img/2019/2019-04-27-OpenVpn01.jpg)
```bash
# After rename:
ipconfig /all
# Ethernet adapter NETGEAR-VPN:
#    Description . . . . . . . . . . . : TAP-Windows Adapter V9
```
* Step 6: **Client utility** must be installed and run by a user who has **administrative privileges**.  
```bash
cd C:\Program Files\OpenVPN\config
..\bin\openvpn client1.ovpn
# Fri Apr 26 23:40:08 2019 us=731074 WARNING: No server certificate verification method has been enabled.  See http://openvpn.net/howto.html#mitm for more info.
# Fri Apr 26 23:40:08 2019 us=731074 OpenSSL: error:140AB18E:SSL routines:SSL_CTX_use_certificate:ca md too weak
# Fri Apr 26 23:40:08 2019 us=731074 Cannot load certificate file client.crt
# Fri Apr 26 23:40:08 2019 us=731074 Exiting due to fatal error

# Yak - can I configure my OpenVPN client to weaken on the requirement on the certificate?
# Or can I configure my Wifi VPN server to generate a stronger certificate?
# Fix: https://forums.openvpn.net/viewtopic.php?t=23979

# You can check that the certificate is using MD5:
 ../bin/openssl x509 -in ca.crt -noout -text | grep "Signature Algorithm"
#    Signature Algorithm: md5WithRSAEncryption

# By the way - the certificate will expire in 2014:
../bin/openssl x509 -in ca.crt -noout -text | grep "After"
#            Not After : Nov 23 02:40:28 2024 GMT

```
* Step 6b: Above did not work. The best solution would have been to upload a stronger certificate to the VPN server (Wifi router) and use corresponding client config.  
Here is a guide for doing that: [Changing the VPN keys on R7000 v1.0.1.pdf](https://community.netgear.com/ejquo23388/attachments/ejquo23388/home-wifi-routers-nighthawk/89120/1/Changing%20the%20VPN%20keys%20on%20R7000%20v1.0.1.pdf).  
This seems to be too experimental and risky (for doing something wrong on the server), so instead I'll try another option
* Step 6c: Install an older OpenVPN.
    * I assume I can reuse the TAP adapter, so I'll just uninstall `openvpn-install-2.4.7-I607-Win10` (via `Control Panel\Programs\Programs and Features`).
    * No such luck - Uninstall OpenVPN also uninstalled the TAP adapter (which is also the one you renamed in `Network Connections`).
    * Older releases available at [/downloads/releases/](https://build.openvpn.net/downloads/releases/).
    * Testing 
        * openvpn-install-2.4.7-I604-Win10
        * openvpn-install-2.4.7-I602
        * openvpn-install-2.4.6-I602
        * Same problem: `ca md too weak`.
* Step 6d: Install an older OpenVPN - Testing openvpn-install-2.4.3-I602  
Log: (stored in `C:\Users\user\OpenVPN\log`)  
```bash
# Sat Apr 27 12:44:02 2019 OpenVPN 2.4.3 x86_64-w64-mingw32 [SSL (OpenSSL)] [LZO] [LZ4] [PKCS11] [AEAD] built on Jul 14 2017
# Sat Apr 27 12:44:02 2019 Windows version 6.2 (Windows 8 or greater) 64bit
# Sat Apr 27 12:44:02 2019 library versions: OpenSSL 1.0.2l  25 May 2017, LZO 2.10
# Sat Apr 27 12:44:02 2019 MANAGEMENT: TCP Socket listening on [AF_INET]127.0.0.1:25340
# Sat Apr 27 12:44:02 2019 Need hold release from management interface, waiting...
# Sat Apr 27 12:44:02 2019 MANAGEMENT: Client connected from [AF_INET]127.0.0.1:25340
# Sat Apr 27 12:44:02 2019 MANAGEMENT: CMD 'state on'
# Sat Apr 27 12:44:02 2019 MANAGEMENT: CMD 'log all on'
# Sat Apr 27 12:44:03 2019 MANAGEMENT: CMD 'echo all on'
# Sat Apr 27 12:44:03 2019 MANAGEMENT: CMD 'hold off'
# Sat Apr 27 12:44:03 2019 MANAGEMENT: CMD 'hold release'
# Sat Apr 27 12:44:03 2019 WARNING: No server certificate verification method has been enabled.  See http://openvpn.net/howto.html#mitm for more info.
# Sat Apr 27 12:44:03 2019 LZO compression initializing
# Sat Apr 27 12:44:03 2019 Control Channel MTU parms [ L:1654 D:1212 EF:38 EB:0 ET:0 EL:3 ]
# Sat Apr 27 12:44:03 2019 Data Channel MTU parms [ L:1654 D:1450 EF:122 EB:411 ET:32 EL:3 ]
# Sat Apr 27 12:44:03 2019 Local Options String (VER=V4): 'V4,dev-type tap,link-mtu 1590,tun-mtu 1532,proto UDPv4,comp-lzo,cipher AES-128-CBC,auth SHA1,keysize 128,key-method 2,tls-client'
# Sat Apr 27 12:44:03 2019 Expected Remote Options String (VER=V4): 'V4,dev-type tap,link-mtu 1590,tun-mtu 1532,proto UDPv4,comp-lzo,cipher AES-128-CBC,auth SHA1,keysize 128,key-method 2,tls-server'
# Sat Apr 27 12:44:03 2019 TCP/UDP: Preserving recently used remote address: [AF_INET]100.xxx.xxx.xxx:12974
# Sat Apr 27 12:44:03 2019 Socket Buffers: R=[65536->65536] S=[65536->65536]
# Sat Apr 27 12:44:03 2019 UDP link local: (not bound)
# Sat Apr 27 12:44:03 2019 UDP link remote: [AF_INET]100.xxx.xxx.xxx:12974
# Sat Apr 27 12:44:03 2019 MANAGEMENT: >STATE:1556361843,WAIT,,,,,,

# Sat Apr 27 12:45:03 2019 TLS Error: TLS key negotiation failed to occur within 60 seconds (check your network connectivity)
# Sat Apr 27 12:45:03 2019 TLS Error: TLS handshake failed
# Sat Apr 27 12:45:03 2019 TCP/UDP: Closing socket
# Sat Apr 27 12:45:03 2019 SIGUSR1[soft,tls-error] received, process restarting
# Sat Apr 27 12:45:03 2019 MANAGEMENT: >STATE:1556361903,RECONNECTING,tls-error,,,,,
# Sat Apr 27 12:45:03 2019 Restart pause, 5 second(s)
# Sat Apr 27 12:45:08 2019 WARNING: No server certificate verification method has been enabled.  See http://openvpn.net/howto.html#mitm for more info.
# Sat Apr 27 12:45:08 2019 Re-using SSL/TLS context
# Sat Apr 27 12:45:08 2019 LZO compression initializing
# .... repeat from 44:03
```
* Now we are further. Error `TLS Error: TLS key negotiation failed to occur`
    * [OpenVPN issue - TLS key negotiation failed to occur within 60 seconds](https://serverfault.com/questions/765521/openvpn-issue-tls-key-negotiation-failed-to-occur-within-60-seconds#765562)
    * It seems like there is hole missing for port TCP/UDP 1194.
    But the Router (VPN serer) has no firewall. Meaning the port cannot be blocked - unless it is the client PC that has to open up in its internal firewall for outgoing VPN tunnel setup.
    * OK in Windows Firewall open up for openvpn-gui.exe and openvpn.exe on private and public networks
![Firewall - public + private networks](img/2019/2019-04-27-OpenVpn02.PNG)
![Firewall - select apps](img/2019/2019-04-27-OpenVpn03.PNG)
* Testing after opening in firewall in Windows. Testing from the inside network:  
Log:  
```bash
# Sat Apr 27 16:35:45 2019 TCP/UDP: Incoming packet rejected from [AF_INET]192.168.1.1:12974[2], expected peer address: [AF_INET]100.xxx.xxx.xxx:12974 (allow this incoming source address/port by removing --remote or adding --float)
```
* Now the VPN client complains that the VPN server demands the client to come from outside. So next step is to disconnect PC from home Wifi and connect it to mobile wifi (personal hotspot).  
Log:  
```bash
# Sat Apr 27 16:45:41 2019 MANAGEMENT: >STATE:1556376341,WAIT,,,,,,
# Sat Apr 27 16:46:41 2019 TLS Error: TLS key negotiation failed to occur within 60 seconds (check your network connectivity)
# Sat Apr 27 16:46:41 2019 TLS Error: TLS handshake failed
# Sat Apr 27 16:46:41 2019 TCP/UDP: Closing socket
```
* Back to Firewall problem - Seems like incoming port 12974 was allowed while being inside network. 
Next I added OpenVpn-Gui.exe as an outgoing FW rule. Still no connection!  
Perhaps the IPhone has a firewall, too that needs to be opened? Nope - No FW in the phone.  
So next I'll try adding `--float` to the config file (as propoesed above) internally - to see if I can get hole through internally.  
client1float.ovpn:  
```bash
# ...
dev-node NETGEAR-VPN
remote 100.xxx.xxx.xxx 12974
float 
resolv-retry infinite
# ...
```
Log:  
```bash
# Sat Apr 27 18:16:47 2019 us=215884 MANAGEMENT: >STATE:1556381807,WAIT,,,,,,
# Sat Apr 27 18:16:47 2019 us=218876 MANAGEMENT: >STATE:1556381807,AUTH,,,,,,
# Sat Apr 27 18:16:47 2019 us=219876 TLS: Initial packet from [AF_INET]192.168.1.1:12974, sid=6ece84e3 ac73ca4a
# Sat Apr 27 18:16:47 2019 us=595553 VERIFY OK: depth=1, C=TW, ST=TW, L=Taipei, O=netgear, OU=netgear, CN=netgear, emailAddress=mail@netgear.com
# Sat Apr 27 18:16:47 2019 us=595553 VERIFY OK: depth=0, C=TW, ST=TW, O=netgear, OU=netgear, CN=netgear, emailAddress=mail@netgear.com
# Sat Apr 27 18:16:47 2019 us=731459 Control Channel: TLSv1, cipher TLSv1/SSLv3 DHE-RSA-AES256-SHA, 1024 bit RSA
# Sat Apr 27 18:16:47 2019 us=731459 [netgear] Peer Connection Initiated with [AF_INET]192.168.1.1:12974
# Sat Apr 27 18:16:48 2019 us=881304 MANAGEMENT: >STATE:1556381808,GET_CONFIG,,,,,,
# Sat Apr 27 18:16:48 2019 us=881304 SENT CONTROL [netgear]: 'PUSH_REQUEST' (status=1)
# Sat Apr 27 18:16:48 2019 us=884223 PUSH: Received control message: 'PUSH_REPLY,route 192.168.1.1 255.255.255.0,redirect-gateway,route-gateway dhcp,ping 10,ping-restart 120'
# Sat Apr 27 18:16:48 2019 us=884223 Flag 'def1' added to --redirect-gateway (iservice is in use)
# Sat Apr 27 18:16:48 2019 us=885223 OPTIONS IMPORT: timers and/or timeouts modified
# Sat Apr 27 18:16:48 2019 us=885223 OPTIONS IMPORT: route options modified
# Sat Apr 27 18:16:48 2019 us=885223 OPTIONS IMPORT: route-related options modified
# Sat Apr 27 18:16:48 2019 us=885223 Data Channel MTU parms [ L:1590 D:1450 EF:58 EB:411 ET:32 EL:3 ]
# Sat Apr 27 18:16:48 2019 us=885223 Data Channel Encrypt: Cipher 'AES-128-CBC' initialized with 128 bit key
# Sat Apr 27 18:16:48 2019 us=885223 Data Channel Encrypt: Using 160 bit message hash 'SHA1' for HMAC authentication
# Sat Apr 27 18:16:48 2019 us=885223 Data Channel Decrypt: Cipher 'AES-128-CBC' initialized with 128 bit key
# Sat Apr 27 18:16:48 2019 us=885223 Data Channel Decrypt: Using 160 bit message hash 'SHA1' for HMAC authentication
# Sat Apr 27 18:16:48 2019 us=885223 interactive service msg_channel=596
# Sat Apr 27 18:16:48 2019 us=904231 ROUTE_GATEWAY 192.168.1.1/255.255.255.0 I=23 HWADDR=60:6c:66:a8:53:5e
# Sat Apr 27 18:16:48 2019 us=951225 OpenVPN ROUTE: OpenVPN needs a gateway parameter for a --route option and no default was specified by either --route-gateway or --ifconfig options
# Sat Apr 27 18:16:48 2019 us=951225 OpenVPN ROUTE: failed to parse/resolve route for host/network: 192.168.1.1
# Sat Apr 27 18:16:48 2019 us=951225 open_tun
# Sat Apr 27 18:16:48 2019 us=955226 TAP-WIN32 device [NETGEAR-VPN] opened: \\.\Global\{8226EE13-989D-495D-8290-ABEE9BD555EB}.tap
# Sat Apr 27 18:16:48 2019 us=956226 TAP-Windows Driver Version 9.21 
# Sat Apr 27 18:16:48 2019 us=956226 TAP-Windows MTU=1500
# Sat Apr 27 18:16:48 2019 us=957204 Successful ARP Flush on interface [63] {8226EE13-989D-495D-8290-ABEE9BD555EB}
# Sat Apr 27 18:16:49 2019 us=363748 Extracted DHCP router address: 192.168.1.1
# Sat Apr 27 18:16:52 2019 us=451714 Recursive routing detected, drop tun packet to [AF_INET]192.168.1.1:12974
# ...
# Sat Apr 27 18:16:52 2019 us=991617 Recursive routing detected, drop tun packet to [AF_INET]192.168.1.1:12974
# Sat Apr 27 18:16:53 2019 us=14633 TEST ROUTES: 1/1 succeeded len=0 ret=1 a=1 u/d=up
# Sat Apr 27 18:16:53 2019 us=15597 C:\WINDOWS\system32\route.exe ADD 192.168.1.1 MASK 255.255.255.255 192.168.1.1 IF 23
# Sat Apr 27 18:16:53 2019 us=29609 Route addition via service succeeded
# Sat Apr 27 18:16:53 2019 us=29609 C:\WINDOWS\system32\route.exe ADD 0.0.0.0 MASK 128.0.0.0 192.168.1.1
# Sat Apr 27 18:16:53 2019 us=42003 Route addition via service succeeded
# Sat Apr 27 18:16:53 2019 us=42003 C:\WINDOWS\system32\route.exe ADD 128.0.0.0 MASK 128.0.0.0 192.168.1.1
# Sat Apr 27 18:16:53 2019 us=49074 Route addition via service succeeded
# Sat Apr 27 18:16:53 2019 us=49074 WARNING: this configuration may cache passwords in memory -- use the auth-nocache option to prevent this
# Sat Apr 27 18:16:53 2019 us=49074 Initialization Sequence Completed
# Sat Apr 27 18:16:53 2019 us=49074 MANAGEMENT: >STATE:1556381813,CONNECTED,SUCCESS,,192.168.1.1,12974,,
```
* Success - internally :-).  
Does it also work via phone wifi? Nope!  
PPTP passthrough Removed from IOS10: [VPN using hotspot with ios 10 not working - Apple Community](https://discussions.apple.com/thread/7673183).
But OpenVPN does not use PPTP - it uses OpenSSL ([Which is the Best VPN Protocol? PPTP vs. OpenVPN vs. L2TP/IPsec vs. SSTP](https://www.howtogeek.com/211329/which-is-the-best-vpn-protocol-pptp-vs.-openvpn-vs.-l2tpipsec-vs.-sstp/)).  
Apparently IOS10 barred more then that.   

* Step 7: For help connecting using OpenVPN clients, please refer to [2x HOW TO | OpenVPN](https://openvpn.net/community-resources/how-to/#quick)
* Step 8: Deactivate/Remove outgoing FW rule to see if it is needed.
    * VPN still worked - but now I realized it took a long time to respond from external web sites. Some website wrote that the all those build-in home VPN's are slow. A better option is to set up a PC with a VPN server installed - and have the Wifi router do port forwarding to the PC.
* Step 9: Enable Dynamic DNS and download new client profile. Currently, when the ISP gives my WiFi router a new IP, then VPN will stop working.  
Netgear provides one free DDNS account, when you have the HW. Here is a guide: [How to Setup a NETGEAR Dynamic DNS account?](https://kb.netgear.com/23860/How-to-Setup-a-NETGEAR-Dynamic-DNS-account)
* Goto [New Product Registration](https://www.netgear.com/mynetgear/register/register.aspx) and register you router. There are **password limitations**. Reuse the password for your DDNS registration later.
* Goto [Dynamic DNS service](http://192.168.1.1/DNS_ddns.htm)
    * Enter `NETGEAR` as service Provider. They give you one registration for free (through No IP).
    * Enter a subdoamin name
    * Enter email and password and register
![Dynamic DNS](https://www.downloads.netgear.com/files/answer_media/images/23860/1.jpg)  
_Image on Netgears web_

Reply:
The NETGEAR DDNS on this router is currently configured to:  
Host Name: aaaaaaa.mynetgear.com  
Email: bbbbb@ccccc.dd  

Pressing **Show Status** pops up [DDNS status page](http://www.routerlogin.net/DNS_ddns_st.htm).  
_Tip from [Registering a Netgear DDNS](https://community.netgear.com/t5/Nighthawk-WiFi-Routers/Registering-a-Netgear-DDNS/td-p/451771)_

You will receive a mail from https://www.noip.com/, where you will have confirm your new account.

You can edit the IP address on [Manage DNS Records](https://www.noip.com/members/dns/). Change it to 100.xxx.xxx.xxx. You find it as `IP Address` on [Internet Setup](http://192.168.1.1/BAS_ether.htm)

Now you can lookup the IP address:  

```bash
nslookup aaaaaaa.mynetgear.com
# Server:  UnKnown
# Address:  192.168.1.1

# Non-authoritative answer:
# Name:    aaaaaaa.mynetgear.com
# Address:  100.xxx.xxx.xxx
```

You can now replace you IP in the `C:\Program files\OpenVPN\config\client1.ovpn` file  
```bash
# from
remote 100.xxx.xxx.xxx 12974
# to
remote aaaaaaa.mynetgear.com 12974
```

You can now test your VPN again.

Now somehow Netgear should notify NOIP, when its IP is changed by the ISP.  

You also have the option to install a client on your, that can be notified by NOIP, when it gets a signal from Netgear.    
[Dynamic Update Client (DUC)](https://my.noip.com/#!/dynamic-dns/duc).  
But that should not be needed, when we reach the VPN by DNS `aaaaaaa.mynetgear.com`.

* Next steps:
    * Change from UDP port 12974 to TCP 443 - which will be open everywhere.
    * Create client profiles for several IPhones.

Notes: 
* If you want to make any change in Advanced Configurations section, please make the changes before you download the configuration files in Step 3.
* Step 3 migth popup with this message: _"Currently your Dynamic DNS service is not enabled, and the IP address for your Internet connection will be used for client configurations. When the IP address for your Internet connection is changed, you will have to download and install the configuration files again."_

Links

* [How do I enable the VPN feature on my NETGEAR router using a Windows computer?](https://kb.netgear.com/23854/How-do-I-use-the-VPN-service-on-my-Nighthawk-router-with-my-Windows-client)
* [OpenVPN Support Forum](https://forums.openvpn.net/)
* Guide for building new certs for R7000: [Re: Netgear R7000 and OpenVPN for Android App](https://community.netgear.com/t5/Nighthawk-WiFi-Routers/Netgear-R7000-and-OpenVPN-for-Android-App/m-p/1515771/highlight/true#M89120)
    * [Changing the VPN keys on R7000 v1.0.1.pdf](https://community.netgear.com/ejquo23388/attachments/ejquo23388/home-wifi-routers-nighthawk/89120/1/Changing%20the%20VPN%20keys%20on%20R7000%20v1.0.1.pdf)
* Building Certificates and Keys: [Easy_Windows_Guide – OpenVPN Community](https://community.openvpn.net/openvpn/wiki/Easy_Windows_Guide)
* Building Certificates and Keys: [2x HOW TO | OpenVPN](https://openvpn.net/community-resources/how-to/#quick)
* [Netgear R7000 and OpenVPN for Android App](https://community.netgear.com/t5/Nighthawk-WiFi-Routers/Netgear-R7000-and-OpenVPN-for-Android-App/td-p/1310857)
* [Which is the Best VPN Protocol? PPTP vs. OpenVPN vs. L2TP/IPsec vs. SSTP](https://www.howtogeek.com/211329/which-is-the-best-vpn-protocol-pptp-vs.-openvpn-vs.-l2tpipsec-vs.-sstp/)
* No Firewall on R7000: [Firewall settings](https://community.netgear.com/t5/Nighthawk-WiFi-Routers/Firewall-settings/td-p/510090)
* [OpenVPN issue - TLS key negotiation failed to occur within 60 seconds](https://serverfault.com/questions/765521/openvpn-issue-tls-key-negotiation-failed-to-occur-within-60-seconds#765562)
* Sample client and server configs: [Windows Firewall issue with OpenVPN - OpenVPN Support Forum](https://forums.openvpn.net/viewtopic.php?t=20115)
* [How to setup Inbound/Outbound firewall rules on NETGEAR Modem router/gateways | Answer | NETGEAR Support](https://kb.netgear.com/8219/How-to-setup-Inbound-Outbound-firewall-rules-on-NETGEAR-Modem-router-gateways)
* [Re: R7000 - does this router have a firewall?](https://community.netgear.com/t5/Nighthawk-WiFi-Routers/R7000-does-this-router-have-a-firewall/m-p/1491643/highlight/true#M80416)
    * [Is UPnP a Security Risk?](https://www.howtogeek.com/122487/htg-explains-is-upnp-a-security-risk/)
* [How-To: Import/Export GPG key pair](https://www.debuntu.org/how-to-importexport-gpg-key-pair/)

#### IPhone

To make your IPhone a VPN client you need to  

* Prepare client config files for IPhone
* Upload the client config files to your IPhone
* Import the client config files to app and phone

##### Prepare client config files for IPhone

EarthVPN provides a sample [configuration .ovpm file for ios7+](http://www.earthvpn.com/images/configurationios7.txt). You can download it and modify it.  
Save it as e.g. `client1-ios.ovpn`.  
You can remove all the xml tags like <ca>, since you have the content of these files in separate files in the `C:\Program files\OpenVPN\config\` folder. Instead you replace them by ca, cert and key.  

```bash
client
dev tun
proto udp
remote aaaaaaa.mynetgear.com 12974
float
resolv-retry infinite
nobind
persist-key
persist-tun
ca ca.crt
cert client.crt
key client.key
# auth-user-pass
# reneg-sec 0
# auth SHA1
cipher AES-128-CBC
comp-lzo
verb 5
```

Links:

* [How to Configure OpenVPN on Iphone Ipad IOS - VPN PPTP, SSTP, L2TP and OpenVPN Anonymous VPN Access to 32 Countries](http://www.earthvpn.com/how-to-configure-openvpn-on-iphone-ipad-ios/)

##### Upload the client config files to your IPhone

You can use iTunes for transferring files to OpenVPN on your phone

* In IPhone Install [‎OpenVPN Connect](https://itunes.apple.com/us/app/openvpn-connect/id590379981) app
* On PC Start iTunes
* Connect your phone via USB cable to your PC and login
* In iTunes a **phone icon** appears. Press it an select your phone 
![Connect to iPhone](img/2019/2019-04-27-OpenVpn05.PNG)
* Select **File Sharing** in left menu and scroll down to **OpenVPN** in the list of apps
![Connect iPhone to PC](img/2019/2019-04-27-OpenVpn04.PNG)
* Drag and drop the config files into the folder in iTunes
![Upload file to iPhone](img/2019/2019-04-27-OpenVpn05.PNG)
* Done - the files are now uploaded

##### Import the client config files to app and phone

* In IPhone start OpenVPN

Links:

* [FAQ regarding OpenVPN Connect iOS | OpenVPN](https://openvpn.net/vpn-server-resources/faq-regarding-openvpn-connect-ios/)
* Install: [‎OpenVPN Connect](https://itunes.apple.com/us/app/openvpn-connect/id590379981)
* Guide for iVPN service: [VPN Setup guide for OpenVPN Connect on iPhone devices](https://www.ivpn.net/setup/iphone-openvpn-connect.html)
* Guide for Linux VPN service: [Setup a VPN on your iPhone with OpenVPN and Linux](https://louwrentius.com/setup-a-vpn-on-your-iphone-with-openvpn-and-linux.html)

#### PC

* [Quick Start Guide | OpenVPN](https://openvpn.net/quick-start-guide/)
* Download: [Community Downloads | OpenVPN](https://openvpn.net/community-downloads/)
    * PGP signature - Win10: [https://swupdate.openvpn.org/community/releases/openvpn-install-2.4.7-I607-Win10.exe.asc](https://swupdate.openvpn.org/community/releases/openvpn-install-2.4.7-I607-Win10.exe.asc)
    * HowTo verify signature [GnuPG Public Key | OpenVPN](https://openvpn.net/community-resources/sig/)
* Guide: [Linux Connectiion Guide For OpenVPN Access Server | OpenVPN](https://openvpn.net/vpn-server-resources/connecting-to-access-server-with-linux/)

.....

## Tor

Questions:

* Can you browse normal websites at all from Tor? Yes - this is called the Surface web.
* Does China block the Tor Relays? I guess they block as many as they know of, which probably means all.

Cons: 

* Even though the aim of using Tor would just be to reach normal websites like Google, then it will probably attract unwanted attention from e.g. agencies.
* I assume you can't download Tor browser, If you are inside China.

Links:

* [How to Use the Tor Browser for Privacy Online [Guide + Review]](https://blokt.com/guides/how-to-use-the-tor-browser)
* [It's Time to Encrypt Your Email: Using Keybase](https://code.tutsplus.com/tutorials/its-time-to-encrypt-your-email-using-keybase--cms-23724)

### DuckDuckGo

DuckDuckGo is good for removing trackers.

* Chrome plugin: [DuckDuckGo Privacy Essentials](https://chrome.google.com/webstore/detail/duckduckgo-privacy-essent/bkdgflcldnnnapblkhphbgpggdiikppg)
* [Mobile App](https://duckduckgo.com/app?natb=v166-2__&cp=atbaoct)

But DuckDuckGo also provides an Onion service, which is Google Search for the Tor browser.

The End