Title: Install LinuxLite on Laptop
Date: 2099-01-01 00:00
Category: DevOps
Tags: #linux , #etcher, #usb, #rufus, #iso

I want to have a small Linux running on a small old laptop.

Currently it is running [Fedora and Windows](https://rasor.wordpress.com/2012/12/12/xen-hypervisor/) on different partitions. I haven't used the PC for many years, so now it is time for it to get a fresh install.  
This time I don't want the larger Fedora, but a more easy and small one.  
The disk also needs a wipe. For that I flashed [Gnome Partition Editor](https://gparted.sourceforge.io/livecd.php) to USB (see using Etcher below).  

I [installed DamnedSmallLinux](https://rasor.wordpress.com/2013/07/02/linux-on-usb/) (DSL) back in 2013.  
But [DSL apparently hasn't been updated since 2008](https://en.wikipedia.org/wiki/Damn_Small_Linux).  

So what are [the choises?](https://en.wikipedia.org/wiki/Template:Linux_distributions). Here you can see some [more details](https://en.wikipedia.org/wiki/Comparison_of_Linux_distributions)
I think I'll try [Linux Lite](https://en.wikipedia.org/wiki/Linux_Lite) - a Ubuntu/Debian fork.  
Lite is recommended on [9 Best Linux Distros For Beginner Users — 2019 Edition](https://fossbytes.com/best-linux-distro-beginners/) for slow/old/small machines and for Linux dummies comming from Windows.   
It uses a simmple Desktop Xfce without animations and fancy design.  
Check out other desktops on [10 Best Linux Desktop Environments And Their Comparison | 2018 Edition](https://fossbytes.com/best-linux-desktop-environments/)

Also interestion is [Android-x86](https://en.wikipedia.org/wiki/Android-x86) - of course an Android fork.  
You can download from [Android-x86 - OSDN](https://osdn.net/projects/android-x86/releases).  

For a development PC I would to use CentOS, which is the community edition of RedHat - a Fedoroa fork.  
You can download [CentOS here](https://centos.org/download/). A DVD version is 4.5 GB, whereas a minimal version is only 1 GB.  
But after reading [11 Best Linux Distros For Programming & Developers [2019 Edition]](https://fossbytes.com/best-linux-distros-for-programming-developers/) it seems like [Pop!_OS](https://system76.com/pop) is the choise for me. All developer tools already installed. Drivers installed. Pop!_OS is a Debian/Ubuntu fork.

Also interesting is the [10 Most Secure Linux Distros For Complete Privacy & Anonymity | 2017 Edition](https://fossbytes.com/secure-linux-distros-privacy-anonymity/) list.

## Install LinuxLite

You can download [LinuxLite here](https://www.linuxliteos.com/download.php). The .iso file is 1.3 GB, so not exactly small. Perhaps not that fast after all. The Andoid .iso is only 0.88 GB.  
After download you can drag'n'drop the .iso back to the page to MD5sum checker to see if the file is uncorrupt.  

Now you need to burn the .iso to a bootable USB stick. [Here is HowTo On Windows](https://www.linuxliteos.com/manual/install.html#llusbwin).  
* Download a burner like [balena Etcher](https://www.balena.io/etcher/)
* Install and execute Etcher.
* Select source (.iso), target (USB) and burn.
* Info: balena also offers a Raspberri PI - [balenaFin](https://www.balena.io/fin/) to host the OS.
* If problems: If the flash is not formatted and Windows refuses to format it, then Use [Rufus](https://rufus.ie/) either just to format or also for burning .iso

### Testing Lite

Lite was really easy to use - just as a user without cmd line needs - the tools are just where you are used to in Windows.  
I didn't have to install any driver on my old PC.

The End